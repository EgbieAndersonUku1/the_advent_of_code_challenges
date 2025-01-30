from utils import get_problem_file

class Cache:
    def __init__(self):
        self.cache = []
    
    def get_cache(self):
        return self.cache
    
    def add_cache(self, value):
        if isinstance(value, list):
            self.cache.extend(value)
        else:
            self.cache.append(value)
    
    
def get_elves_calories_count(calories_list: list) -> dict:
    """Parses the input file and calculates total calories per elf."""
    calories_count    = 0
    num_of_elves_seen = 0
    
    elves = {}
    
    for calories in calories_list:
        calories = calories.strip("\n")
       
        if calories.isdigit():
            calories_count += int(calories)
        else:
            num_of_elves_seen += 1
            elves[num_of_elves_seen] = calories_count
                           
            calories_count = 0
            
    return elves
    

def sort_calories_by_highest(elves:dict) -> list:
    """Sorts elves' calorie counts in descending order."""

    if not isinstance(elves, dict):
        raise ValueError(f"Expected a dictionary but got type: {type(elves)}")
    
    calories = cache.get_cache()
    if calories:
        return calories
    
    calories = sorted(elves.values(), reverse=True)
    cache.add_cache(calories)
    return calories


def get_the_highest_medium_and_lowest_calories_total(calories_list: list) -> int:
    """
    Returns the sum of the top three calorie values.
    
    Args:
        calories_list: A list of integers contains calories
    
    :Returns:
        The total sum of the top three calorie values
    """
    if not isinstance(calories_list, list):
        raise ValueError("The list cannot be empty nor cannot be a list")
    if len(calories_list) < 3:
        raise ValueError("The list must have at least the three integers")
    
    return sum(calories_list[:3])


def main():
    """The main function that runs the file"""
    calories      = get_problem_file()
    elves         = get_elves_calories_count(calories)
    calories_list = sort_calories_by_highest(elves)

    highest_calories = calories_list[0]
    total            = get_the_highest_medium_and_lowest_calories_total(calories_list)

    print(f"The highest calorie count is: {highest_calories} ")
    print(f"The top three highest calorie count is:  {total}")

if __name__ == "__main__":
    
    cache = Cache()
    main()