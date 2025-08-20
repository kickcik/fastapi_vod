import string
from typing import Final


class Base62:
    BASE: Final[str] = string.ascii_letters + string.digits
    BASE_LEN: Final[int] = len(BASE)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(f"number has to be over 0 integer, but got {num}")

        if num == 0:
            return cls.BASE[0]
        result = []
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
        return "".join(result)
