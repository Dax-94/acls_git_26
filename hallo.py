"""A small sample script for a GitHub demo."""


def greet(name: str) -> str:
	"""Return a friendly greeting."""
	return f"Hello, {name}! Welcome to the GitHub demo."


if __name__ == "__main__":
	print(greet("world"))
