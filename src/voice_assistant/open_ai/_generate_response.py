import openai

from ._base import IGPTResponseGenerator


class GPTResponseGenerator(IGPTResponseGenerator):
    def __init__(self):
        pass

    def submit(self, query: str) -> str:
        pass
