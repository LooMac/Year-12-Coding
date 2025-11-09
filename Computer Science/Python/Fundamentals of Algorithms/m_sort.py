def merge_sort(items):

    # Base case for recursion:
    # The recursion will stop when the list has been divided into single items
    if len(items) <= 1:
        return items
    else:
        midpoint = (len(items)-1) // 2 # Calculate the midpoint index
        left_half = items[0:midpoint+1] # Create left half list
        right_half = items[midpoint+1:len(items)] # Create right half list

        left_half = merge_sort(left_half) # Recursive call on left half
        right_half = merge_sort(right_half) # Recursive call on right half
        
        print(left_half,right_half)

        # Call procedure to merge both halves
        merged_items = merge(left_half, right_half) # Call function to merge both halves

        return merged_items

def merge(left, right):

    merged = [] # New list for merging the items
    index_left = 0 # left current position
    index_right = 0 # right current position

    # While there are still items to merge
    while index_left < len(left) and index_right < len(right):

        # Find the lowest of the two items being compared 
        # and add it to the new list
        if left[index_left] < right[index_right]:
            merged.append(left[index_left])
            index_left += 1
        else:
            merged.append(right[index_right])
            index_right += 1

    # Add to the merged list any remaining data from left list
    while index_left < len(left):
        merged.append(left[index_left])
        index_left += 1

    # Add to the merged list any remaining data from right list
    while index_right < len(right):
        merged.append(right[index_right])
        index_right += 1

    return merged

print(merge_sort([0,4,6,6,7,8,1]))