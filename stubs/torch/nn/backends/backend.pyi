# Stubs for torch.nn.backends.backend (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class FunctionBackend:
    function_classes: Any = ...
    def __init__(self) -> None: ...
    def __getattr__(self, name: Any): ...
    def register_function(self, name: Any, function_class: Any) -> None: ...
