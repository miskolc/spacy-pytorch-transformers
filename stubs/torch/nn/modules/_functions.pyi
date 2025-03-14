# Stubs for torch.nn.modules._functions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.autograd.function import Function
from typing import Any

class SyncBatchNorm(Function):
    @staticmethod
    process_group: Any = ...
    world_size: Any = ...
    def forward(self, input: Any, weight: Any, bias: Any, running_mean: Any, running_var: Any, eps: Any, momentum: Any, process_group: Any, world_size: Any): ...
    @staticmethod
    def backward(self, grad_output: Any): ...
