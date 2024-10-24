def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    # Write your code here
    import math
    minutes = (seconds % 3600) // 60
    hours = seconds // 3600
    
    
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."

def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    # Write your code here
    import math
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.raidans(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."

def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    # Write your code here
    import math
    lots_of_heys = "hey" * n
    return lots_of_heys

def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    # Write your code here
    string_numbers = str(num_a) + str(num_b)
    return string_numbers
