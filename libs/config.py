"""Config"""

# pylint: disable=E1101, C0301

import dataclasses

__version__ = "1.0.0"


@dataclasses.dataclass
class Config:
    """Config"""

    n = 10000
    q_av = 3
    nav = 10
    dm = 0
    dsig = 5

    def __init__(
        self,
        n=n,
        pref_factor=q_av,
        num_percent=nav,
        norm_distrib_law=dsig,
    ) -> None:
        """
        n: кількість реалізацій
        pref_factor: коефіцієнт переваги
        num_percent: кількість \u0443 відсотках та абсолютних одиницях
        norm_distrib_law: параметри нормального закону розподілу середне
        """

        self.n = int(n)
        self.q_av = pref_factor
        self.nav = int(self.n * num_percent / 100)
        self.dsig = norm_distrib_law


if __name__ == "__main__":
    cfg = Config(10000, 3, 10, 5)

    print(cfg.__dict__)  # vars(cfg)
