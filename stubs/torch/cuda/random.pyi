# Stubs for torch.cuda.random (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def get_rng_state(device: Any = ...): ...
def get_rng_state_all(): ...
def set_rng_state(new_state: Any, device: Any = ...) -> None: ...
def set_rng_state_all(new_states: Any) -> None: ...
def manual_seed(seed: Any): ...
def manual_seed_all(seed: Any): ...
def seed(): ...
def seed_all(): ...
def initial_seed(): ...
