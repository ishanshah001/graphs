def findDuplicate(nums) -> int:
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    duplicate = nums[0]
    while slow != duplicate:
        slow = nums[slow]
        duplicate = nums[duplicate]

    return slow