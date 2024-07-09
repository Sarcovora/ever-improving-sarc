from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from improve.util.config import default


class Strategy(Enum):
    CLIP = "clip"
    DYNAMIC = "dynamic"
    NONE = None


@dataclass
class FoundationModel_CN:
    name: str
    ckpt: str
    task: str

    noact: list = default([-1, -2, -3, -4])  # no action dimensions
    strategy: Strategy = "clip" # residual scaling strategy
    residual_scale: float = 1.0  # residual scaling factor

    batch_size: int = 8  # number of parallel environments

    def __post_init__(self):
        self.policy = self.name
        if self.policy in ["octo-base", "octo-small"]:
            if self.ckpt in [None, "None"] or "rt_1_x" in self.ckpt:
                self.ckpt = self.policy


@dataclass
class OctoS_CN(FoundationModel_CN):
    name: str = "octo-small"
    ckpt: None = None
    task: str = "widowx_put_eggplant_in_basket"


class OctoB_CN(FoundationModel_CN):
    name: str = "octo-base"
    ckpt: None = None
    task: str = "widowx_put_eggplant_in_basket"


class RTX_CN(FoundationModel_CN):
    pass
