from typing import Optional


def greet(name: str, age: Optional[int] = None) -> str:
    if age is None:
        return f"Hello {name}"

    return f"Hello {name}, age {age}"


async def fetch_data() -> dict[str, str]:
    return {
        "status": "success",
        "message": "Data fetched"
    }