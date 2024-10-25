""" Cluster """

# pylint: disable=E0401, R0914

from dataclasses import dataclass
import os

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from keras.preprocessing import image

from rendering import Rendering as Render
from utils import Utils


@dataclass
class Cluster(Render, Utils):
    """Cluster"""

    def point(self, data, op_systems, colums, cluster_num):
        """point"""

        cluster_data = data[data[colums[0]].isin(op_systems)]
        kmeans = KMeans(n_clusters=cluster_num)
        kmeans.fit(cluster_data[[colums[1]]])
        cluster_data["Cluster"] = kmeans.labels_

        plt.figure(figsize=(8, 6))

        for item in range(cluster_num):
            cluster = cluster_data[cluster_data["Cluster"] == item]
            plt.scatter(
                cluster.index,
                cluster[colums[1]],
                label=f"Cluster {item}",
            )

        self.show(
            title="K-Means clustering",
            xlabel=colums[1],
            ylabel=colums[0],
        )

    def picture(self, files_dir, cluster_num, view_columns=5):
        """picture"""

        images_path = [
            os.path.join(files_dir, file_name) for file_name in os.listdir(files_dir)
        ]
        image_features = [
            self.get_average_color(image_path) for image_path in images_path
        ]

        kmeans = KMeans(n_clusters=cluster_num)
        kmeans.fit(image_features)
        labels = kmeans.labels_

        for cluster in range(cluster_num):
            cluster_images = [
                images_path[i] for i, label in enumerate(labels) if label == cluster
            ]
            view_rows = [
                cluster_images[i : i + view_columns]
                for i in range(0, len(cluster_images), view_columns)
            ]

            rows = len(view_rows)
            fig, axs = plt.subplots(len(view_rows), view_columns, figsize=(10, 10))
            fig.suptitle(f"Group {cluster + 1}")

            axs = axs.flatten()

            for idx, image_path in enumerate(cluster_images):
                img = image.load_img(image_path)
                axs[idx].imshow(img)
                axs[idx].axis("off")

            for ax in axs[rows:]:
                ax.axis("off")

            plt.show()
