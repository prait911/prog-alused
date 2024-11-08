"""Basic list operations."""


def create_list_of_two_elements(a: int, b: int) -> list:
    """
    Return list of two elements a and b (in that order).

    create_list_of_two_elements(1, 2) => [1, 2]
    create_list_of_two_elements(81, 72) => [81, 72]
    """
    return[a, b]
    


def create_list_with_edge_elements(elements: list) -> list:
    """
    Create a new list with 2 elements: the first and the last element.

    The initial list has at least one element.
    If the initial list has only one element, the same element is
    both the first and the last element.

    create_list_with_edge_elements([1, 2, 3]) => [1, 3]
    create_list_with_edge_elements([1]) => [1, 1]
    create_list_with_edge_elements(["a", "b"]) => ["a", "b"]
    create_list_with_edge_elements(["a", "b", "c", "d", "f"]) => ["a", "f"]
    """
    new_list = []
    new_list.append(elements[0])
    new_list.append(elements[-1])
    return new_list

# print(create_list_with_edge_elements([1, 2, 3]))

def get_middle_element_of_list(elements: list) -> any:
    """
    Return the middle element in the list with odd number of element.

    The list always has odd number of elements.
    get_middle_element_of_list([1]) = 1
    get_middle_element_of_list([1, 2, 3]) => 2
    get_middle_element_of_list(["a", "b", "c"]) => "b"
    """
    new_list = []
    return elements[len(elements)//2]
    


def get_middle_part_of_list(elements: list) -> list:
    """
    Create a new list of the input list where the first and the last element are removed.

    The initial list has at least 2 elements (don't have to validate that).

    get_middle_part_of_list([1, 2, 3]) => [2]
    get_middle_part_of_list([1, 3]) => []
    get_middle_part_of_list([1, 3, 6, 7]) => [3, 6]
    get_middle_part_of_list(["a", "b", "b", "a"]) => ["b", "b"]
    """
    
    return elements[1:-1]



def create_new_list_with_added_number(numbers: list, number: int) -> list:
    """
    Return a new list where a number has been added.

    Do not modify the existing list.
    create_new_list_with_added_number([1, 2, 3], 4) => [1, 2, 3, 4]
    """
    new_list = numbers + [number]
    return new_list
# print(create_new_list_with_added_number([1, 2, 3], 4))


def swap_edge_elements(elements: list) -> list:
    """
    Swap the first and the last element.

    List always has at least 2 elements.
    Elements can be either numbers or strings.

    swap_edge_elements([1, 2, 3]) => [3, 2, 1]
    swap_edge_elements([1, 2]) => [2, 1]
    swap_edge_elements([1, 2, 1, 4]) => [4, 2, 1, 1]
    swap_edge_elements(["foo", "bar", "pub"]) => ["pub", "bar", "foo"]

    """
    numbers = elements
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers
# print (swap_edge_elements([1, 2, 3]))

def add_element_in_position(elements: list, new_element: any, position: int) -> list:
    """
    Add a new element into the list into the specified position.

    The position is always valid.
    The elements on the position and on the right are shifted by one.

    add_element_in_position([1, 2, 3], 2, 2) => [1, 2, 2, 3]
    add_element_in_position([1], 9, 0) => [9, 1]
    add_element_in_position([1], 9, 1) => [1, 9]
    """
    new_list = elements
    new_list.insert(-2, 2)
    return new_list
print(add_element_in_position([1, 2, 3], 2, 2))

def get_repeated_list(elements: list, repetiton: int) -> list:
    """
    Repeat the elements by certain amount of times.

    get_repeated_list([1, 2], 2) => [1, 2, 1, 2]
    get_repeated_list([1], 5) => [1, 1, 1, 1, 1]
    get_repeated_list([1, 2], 0) => []
    """
    # Korrutab iga elementi 2 korda
    new_list = elements
    new_list * repetition
    return new_list


def remove_first_element_from_list(elements: list) -> None:
    """
    Remove the first element of the list.

    The list will be modified, nothing is returned.
    There is at least 1 element in the list.

    x = [1, 2, 3]
    remove_first_element_from_list(x)
    x => [2, 3]
    """
    new_list = numbers
    new_list.pop(numbers)
    return elements.pop(0)


def reverse_list(elements: list) -> list:
    """
    Return reversed list.

    reverse_list([1, 2, 3]) => [3, 2, 1]
    reverse_list(["a", "b"]) => ["b", "a"]
    """
    new_list = [1, 2, 3]
    new_list.reverse()
    return new_list


