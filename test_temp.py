from temp import add


def test_add() -> None:
    a, b = 1, 1

    result = add(a, b)

    assert result == 2


async def test_abc() -> None:
    print("abc")
