# Paulo Juarez


def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def twoSumDict(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def twoSumLoopsAll(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append([i, j])
    return pairs


def twoSumDictAll(nums, target):
    seen = {}
    pairs = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                pairs.append([j, i])
        if num in seen:
            seen[num].append(i)
        else:
            seen[num] = [i]
    return pairs


def main():
    nums = [2, 7, 11, 15, 1, 8, 3, 5]
    target = 10

    print("Two Sum using Loops:", twoSumLoops(nums, target))
    print("Two Sum using Dictionary:", twoSumDict(nums, target))
    print("All Two Sum Pairs using Loops:", twoSumLoopsAll(nums, target))
    print("All Two Sum Pairs using Dictionary:", twoSumDictAll(nums, target))


if __name__ == "__main__":
    main()
