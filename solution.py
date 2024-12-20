"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 18 <= time <= 24:
        return not coffee_needed
    elif 5 <= time <= 17:
        return coffee_needed
    elif 1 <= time <= 4:
        return not coffee_needed
    
    
   
    
    
def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c:
        return 10
    elif a == b != c:
        return 5
    elif a != b and b != c and a != c:
        return 1
    else:
        return 0
    
# print(lottery(2, 3, 1))

def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount % 5 == 0 and (ordered_amount // 5) <= big_baskets:
        return 0
    elif small_baskets >= ordered_amount and ordered_amount >= 0:
        return big_baskets
    elif small_baskets + (big_baskets * 5) == ordered_amount:
        return small_baskets
    else:
        for big in range(big_baskets):
            weight = (big + 1) * 5
            if weight == ordered_amount:
                return 0
            for small in range(small_baskets):
                weight += 1
                if weight == ordered_amount:
                    return small + 1
    return -1
    
    
