from langchain_core.runnables import Runnable
from abc import ABC, abstractmethod


class Chain(ABC):
    blocks: list[Runnable] = []
    iter_count: int = 0

    def step(self, prompt: dict[str, str]):
        for block in self.blocks:
            prompt = block.invoke(prompt)
        self.iter_count += 1
        is_terminated = self.terminate_condition(prompt, self.iter_count)
        return prompt, is_terminated

    @abstractmethod
    def terminate_condition(self, prompt: dict[str, str], iter_count: int) -> bool:
        pass
