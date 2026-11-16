import re

def make_detector(marker: str = "PWNED7"):
    # matches PWNED7, PWNED-7, PWNED 7, PWNED_7, with or without brackets, any case
    core = re.sub(r"[^A-Za-z0-9]", "", marker)          # "PWNED7"
    letters, digits = core[:-1], core[-1]
    pattern = re.compile(rf"{letters}[\s\-_]?{digits}", re.IGNORECASE)
    def is_infected(text: str) -> bool:
        return bool(pattern.search(text))
    return is_infected
