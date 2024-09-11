"""Help plan a tea party by giving the number of guests attending"""

__author__: str = "730740670"


def main_planner(guests: int) -> None:
    """Main function that calls each function and produces output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# str(guests) inputs the value of guests in the format of a string (value will not always be 2)
# Main function acts as the overarching function and can be read as a summary


def tea_bags(people: int) -> int:
    """Returns two tea bags for every guest attending"""
    return people * 2


def treats(people: int) -> int:
    """For each tea a guests drinks will want on average 1.5 treats"""
    return int(tea_bags(people=people) * 1.5)


# poeple=people because the parameters of tea_bags and treats are the same


def cost(tea_count: int, treat_count: int) -> float:
    """Assumes each tea bag costs $0.50 and each treat costs $0.75. Function returns the total cost of treats and tea bags combined."""
    return (tea_count * 0.50) + (treat_count * 0.75)


# This function combines tea and treat costs


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# Makes program runnable
