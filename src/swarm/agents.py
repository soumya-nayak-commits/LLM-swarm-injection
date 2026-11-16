import random

class MockAgent:
    """Fake agent: copies the marker into its reply with probability p_infect
    if the incoming message contains it. No model, no GPU."""
    def __init__(self, marker, p_infect=0.5, seed=0):
        self.marker, self.p, self.rng = marker, p_infect, random.Random(seed)

    def reply(self, incoming: str) -> str:
        if self.marker in incoming and self.rng.random() < self.p:
            return f"Answer: 42. {self.marker}"
        return "Answer: 42."
