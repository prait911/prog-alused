"""Function examples."""


# func()
def func() -> str:
    print("I´m inside the function")


# my_name_is(name)
def my_name_is(name: str) -> str:
    print(f"My name is {name}")


# sum_six(num)`
def sum_six(num: int) -> int:
    return 6 + num
print(sum_six(1))

# sum_numbers()
def sum_numbers(a: int, b: int) -> int:
    return a + b
print(sum_numbers(5, 5))

# usd_to_eur()
def usd_to_eur(a: int) -> int:
    return a * 0.8