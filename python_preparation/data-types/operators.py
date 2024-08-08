# partition a list of integers into two parts and check sums of both partitions are same
# nums = [1, 5, 11, 5]


def can_partition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, it's not possible to partition into two equal sums
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    possible_sums = set([0])
    
    for num in nums:
        current_sums = list(possible_sums)
        for s in current_sums:
            if s + num == target_sum:
                return True
            possible_sums.add(s + num)
    
    return target_sum in possible_sums

# Example usage
nums = [1, 5, 11, 5]
if can_partition(nums):
    print("The list can be partitioned into two parts with equal sum.")
else:
    print("The list cannot be partitioned into two parts with equal sum.")
