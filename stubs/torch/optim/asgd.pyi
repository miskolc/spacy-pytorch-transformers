# Stubs for torch.optim.asgd (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .optimizer import Optimizer
from typing import Any, Optional

class ASGD(Optimizer):
    def __init__(self, params: Any, lr: float = ..., lambd: float = ..., alpha: float = ..., t0: float = ..., weight_decay: int = ...) -> None: ...
    def step(self, closure: Optional[Any] = ...): ...
