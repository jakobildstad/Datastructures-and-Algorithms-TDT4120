def find_longest_subarray(nums: list[int], k: int) -> int:
    count_dict = {}
    left = 0
    longest_length = 0

    for right in range(len(nums)):
        if nums[right] in count_dict:
            count_dict[nums[right]] += 1
        else:
            count_dict[nums[right]] = 1

        while len(count_dict) > k:
            count_dict[nums[left]] -= 1

            if count_dict[nums[left]] == 0:
                del count_dict[nums[left]]

            left += 1

        longest_length = max(longest_length, right - left + 1)

    return longest_length