from abc import ABC, abstractmethod


class Block(ABC):
    def __init__(self, prompt, output_parser):
        self.prompt = prompt
        self.output_parser = output_parser

    @abstractmethod
    def invoke(self, options: dict[str, str]):
        pass


class GeneralBlock(Block):
    def invoke(self, model, options: dict[str, str]):
        chain = self.prompt | model | self.output_parser
        return chain.invoke(options)
