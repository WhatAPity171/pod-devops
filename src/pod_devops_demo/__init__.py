__all__ = ["__version__", "greet"]

__version__ = "0.1.0"


def greet(name: str) -> str:
    cleaned = name.strip() or "world"
    return f"Hello there, {cleaned}!"
