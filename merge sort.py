def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  
    left_half = merge_sort(arr[:mid]) 
    right_half = merge_sort(arr[mid:]) 

    return merge(left_half, right_half)  

def merge(left, right):
    """Merges two sorted arrays into one sorted array."""
    sorted_array = []
    i = j = 0

    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

   
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

def main():
    
    user_input = input("Enter a list of integers: ")
    
    input_list = list(map(int, user_input.split()))

    
    sorted_list = merge_sort(input_list)

    
    print("Sorted List:", sorted_list)

if __name__ == "__main__":
    main()