def find_unique(nums):
    seen = set()
    unique = set()
    for num in nums:
        if num in seen:
            unique.discard(num)
        else:
            seen.add(num)
            unique.add(num)
    return list(unique)