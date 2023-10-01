def shuffle(lst, random_nums):
    # Pair each string with a random number and sort by the random numbers
    paired_lists = list(zip(random_nums, lst))
    paired_lists.sort(key=lambda x: x[0])

    # Extract the shuffled strings
    return [x[1] for x in paired_lists]
