from pod_devops_demo import greet


def test_greet_name() -> None:
    assert greet("Ala") == "Hello, Ala!"


def test_greet_blank() -> None:
    assert greet("   ") == "Hello, world!"
