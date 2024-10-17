"""Rendering"""

import matplotlib.pyplot as plt


class Render:
    """Render data results"""

    def hist(self, data, **wargs):
        """Show results in plt"""

        bins = wargs.get("bins")
        facecolor = wargs.get("facecolor")
        alpha = wargs.get("alpha")

        # characteristics.all(data)

        plt.hist(
            data,
            bins=bins or 20,
            facecolor=facecolor or "#7eb253",
            alpha=alpha or 0.5,
        )
        plt.show()

    def plot(self, s0_l, sv_l, text):
        """Plot_AV"""

        plt.clf()  # Очищення холста
        plt.plot(sv_l)
        plt.plot(s0_l)
        plt.xlabel("Похибка")
        plt.ylabel("Ймовірність")
        plt.ylabel(text)
        plt.show()
