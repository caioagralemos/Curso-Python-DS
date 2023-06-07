def longest_consecutive_sequence(arr):
    my_set = set(arr)
    longest_sequence = 0

    for x in my_set:
        # Check if x-1 exists in the set, if it does, skip the current iteration
        if x - 1 in my_set:
            continue

        current_num = x
        current_sequence = 1

        # Increment current_num by 1 until the next number is not in the set
        while current_num + 1 in my_set:
            current_num += 1
            current_sequence += 1

        # Update the longest_sequence if the current sequence is longer
        longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""