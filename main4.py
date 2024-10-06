# Problem 1: Find Closest NFT Values

# Understand:
# - We need to find the two NFT values closest to a given budget.
# - The function should work with any list of NFT values and any budget.

# Match:
# - This problem can be solved using a max heap to keep track of the two closest values.

# Plan:
# 1. Create a max heap to store the two closest values.
# 2. Iterate through the NFT values, calculating the difference from the budget.
# 3. Push each value onto the heap, keeping only the two closest.
# 4. Return the two closest values.

# Implement:
def find_closest_nft_values(nft_values, budget):
    import heapq
    maxheap = []
    for num in nft_values:
        heapq.heappush(maxheap, ((-1 * abs(budget-num)), num ))
        if len(maxheap) > 2:
            heapq.heappop(maxheap)
    
    return [n[1] for n in maxheap]

# Review:
# - The function correctly finds the two closest NFT values to the given budget.
# - It uses a max heap to efficiently keep track of the two closest values.

# Evaluate:
# Time complexity: O(n log 2) ≈ O(n), where n is the number of NFT values.
# Space complexity: O(1), as we only keep a max heap of at most 2 elements.

# Test cases
nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))

# Problem 2: Find Trending Meme

# Understand:
# - We need to find the meme with the highest total reposts within a given time range.
# - The time range is inclusive of both start and end days.

# Match:
# - This problem can be solved by iterating through the memes and summing their reposts.

# Plan:
# 1. Initialize variables to keep track of the highest repost count and corresponding meme name.
# 2. Iterate through each meme.
# 3. Sum the reposts for the given time range.
# 4. Update the highest count and meme name if necessary.
# 5. Return the name of the trending meme.

# Implement:
def find_trending_meme(memes, start_day, end_day):
    res = 0
    w = ""
    for meme in memes:
        name = meme['name']
        count = 0

        for i in range(start_day, end_day+1):
            count += meme["reposts"][i]
        if count > res:
            w = meme["name"]
            res = count
    return w

# Review:
# - The function correctly finds the meme with the highest total reposts within the given range.
# - It handles multiple memes and different time ranges.

# Evaluate:
# Time complexity: O(m * n), where m is the number of memes and n is the range of days (end_day - start_day + 1).
# Space complexity: O(1), as we only use a constant amount of extra space.

# Test cases
memes = [
    {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
    {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
    {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
]

memes_2 = [
    {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
    {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
    {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
]

memes_3 = [
    {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
    {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
]

print(find_trending_meme(memes, 1, 3))
print(find_trending_meme(memes_2, 0, 2))
print(find_trending_meme(memes_3, 2, 4))

# Problem 3: Organize Fabric Rolls

# Understand:
# - We need to pair up fabric rolls, starting with the smallest.
# - If there's an odd number of rolls, the largest one is left unpaired.

# Match:
# - This problem can be solved by sorting the rolls and then pairing them.

# Plan:
# 1. Sort the fabric rolls in ascending order.
# 2. Iterate through the sorted list, pairing the first two rolls each time.
# 3. If there's an odd number of rolls, add the last one separately.

# Implement:
def organize_fabric_rolls(fabric_rolls):
    fabric_rolls.sort()  # Sort the fabric rolls by length
    pairs = []

    while len(fabric_rolls) > 1:
        smallest = fabric_rolls.pop(0)
        closest = fabric_rolls.pop(0)
        pairs.append((smallest, closest))

    if fabric_rolls:
        return pairs + [fabric_rolls[0]]
    else:
        return pairs

# Review:
# - The function correctly pairs up the fabric rolls, starting with the smallest.
# - It handles both even and odd numbers of rolls.

# Evaluate:
# Time complexity: O(n log n) due to the sorting step, where n is the number of fabric rolls.
# Space complexity: O(n) to store the pairs and the sorted list.

# Test cases
fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))

# Problem 4: Find Best Break Pair

# Understand:
# - We need to find a pair of break times that sum up closest to the target time.
# - If multiple pairs have the same difference, return the pair with the smaller break times.

# Match:
# - This problem can be solved using the two-pointer technique on a sorted array.

# Plan:
# 1. Sort the break times.
# 2. Use two pointers, one at the start and one at the end of the sorted array.
# 3. Move the pointers based on the sum comparison with the target.
# 4. Keep track of the closest pair found.

# Implement:
def find_best_break_pair(break_times, target):
    if len(break_times) < 2:
        return ()

    break_times.sort()
    
    left, right = 0, len(break_times) - 1
    closest_pair = ()
    closest_diff = float('inf')
    
    while left < right:
        current_sum = break_times[left] + break_times[right]
        current_diff = abs(target - current_sum)
        
        if current_diff < closest_diff or (current_diff == closest_diff and (break_times[left], break_times[right]) < closest_pair):
            closest_pair = (break_times[left], break_times[right])
            closest_diff = current_diff
        
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return closest_pair

    return closest_pair

# Review:
# - The function correctly finds the pair of break times closest to the target sum.
# - It handles edge cases like having fewer than 2 break times.
# - It returns the pair with smaller break times if multiple pairs have the same difference.

# Evaluate:
# Time complexity: O(n log n) due to the sorting step, where n is the number of break times.
# Space complexity: O(1) as we only use a constant amount of extra space.

# Test cases
break_times = [10, 20, 35, 40, 50]
break_times_2 = [5, 10, 25, 30, 45]
break_times_3 = [15, 25, 35, 45]
break_times_4 = [30]

print(find_best_break_pair(break_times, 60))
print(find_best_break_pair(break_times_2, 50))
print(find_best_break_pair(break_times_3, 70))
print(find_best_break_pair(break_times_4, 60))

# Problem 5: Most Popular Destination

# Understand:
# - We need to find the most visited city from a list of visits.
# - Each visit is represented by a tuple of (city, date).
# - We need to return both the city name and the number of visits.

# Match:
# - This problem can be solved using a hash map to count visits for each city.

# Plan:
# 1. Create a hash map to store the count of visits for each city.
# 2. Iterate through the visits, updating the count for each city.
# 3. Find the city with the maximum count.
# 4. Return the most visited city and its visit count.

# Implement:
from collections import defaultdict

def most_popular_destination(visits):
    res = ""
    count = 0
    hashmap = defaultdict(int)
    for city, date in visits:
        hashmap[city] += 1
    for city in hashmap:
        if hashmap[city] > count:
            res = city
            count = hashmap[city]
    return (res, count)

# Review:
# - The function correctly finds the most visited city and its visit count.
# - It uses a hash map for efficient counting of visits.

# Evaluate:
# Time complexity: O(n), where n is the number of visits.
# Space complexity: O(m), where m is the number of unique cities.

# Test cases
visits = [("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"), ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"), ("Paris", "2024-08-20")]
print(most_popular_destination(visits))

visits_2 = [("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"), ("Berlin", "2024-07-10"), ("London", "2024-07-15")]
print(most_popular_destination(visits_2))

visits_3 = [("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"), ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]
print(most_popular_destination(visits_3))

# Problem 6: Find Longest Gap

# Understand:
# - We need to find the longest time gap between consecutive timestamps.
# - Timestamps are given as integers.

# Match:
# - This problem can be solved by iterating through the sorted timestamps and calculating the differences.

# Plan:
# 1. Initialize the result to 0.
# 2. Iterate through the timestamps from index 0 to second-to-last.
# 3. Calculate the difference between each pair of consecutive timestamps.
# 4. Update the result if a larger gap is found.
# 5. Return the largest gap.

# Implement:
def find_longest_gap(timestamps):
    res = 0
    for i in range(len(timestamps)-1):
        diff = abs(timestamps[i] - timestamps[i+1])
        res = max(res, diff)
    return res

# Review:
# - The function correctly finds the longest gap between consecutive timestamps.
# - It handles both positive and negative differences by using the absolute value.

# Evaluate:
# Time complexity: O(n), where n is the number of timestamps.
# Space complexity: O(1), as we only use a constant amount of extra space.

# Test cases
timestamps1 = [30, 50, 70, 100, 120, 150]
print(find_longest_gap(timestamps1))

timestamps2 = [10, 20, 30, 50, 60, 90]
print(find_longest_gap(timestamps2))

timestamps3 = [5, 10, 15, 25, 35, 45]
print(find_longest_gap(timestamps3))

# Problem 7: Analyze Storyline Continuity

# Understand:
# - We need to check if the scenes in a storyline are in chronological order.
# - Each scene has a timestamp, and we need to ensure they're in ascending order.

# Match:
# - This problem can be solved by comparing consecutive timestamps.

# Plan:
# 1. Iterate through the scenes starting from the second scene.
# 2. Compare each scene's timestamp with the previous scene's timestamp.
# 3. If any timestamp is less than or equal to the previous one, return False.
# 4. If we complete the iteration without finding any issues, return True.

# Implement:
def analyze_storyline_continuity(scenes):
    for i in range(1, len(scenes)):
        if scenes[i]["timestamp"] <= scenes[i-1]["timestamp"]:
            return False
    return True

# Review:
# - The function correctly checks if the scenes are in chronological order.
# - It returns False as soon as it finds a discontinuity, which is efficient.

# Evaluate:
# Time complexity: O(n), where n is the number of scenes.
# Space complexity: O(1), as we only use a constant amount of extra space.

# Test cases
scenes = [
    {"scene": "The hero enters the dark forest.", "timestamp": 1},
    {"scene": "A mysterious figure appears.", "timestamp": 2},
    {"scene": "The hero faces his fears.", "timestamp": 3},
    {"scene": "The hero finds a hidden treasure.", "timestamp": 4},
    {"scene": "An eerie silence fills the air.", "timestamp": 5}
]

continuity = analyze_storyline_continuity(scenes)
print(continuity)

scenes = [
    {"scene": "The spaceship lands on an alien planet.", "timestamp": 3},
    {"scene": "A strange creature approaches.", "timestamp": 2},
    {"scene": "The crew explores the new world.", "timestamp": 4},
    {"scene": "The crew encounters hostile forces.", "timestamp": 5},
    {"scene": "The crew makes a narrow escape.", "timestamp": 6}
]

continuity = analyze_storyline_continuity(scenes)
print(continuity)

# Problem 8: Check Expiration Order

# Understand:
# - We need to check if a list of items with expiration dates is in order.
# - Dates are given in the format "YYYY-MM-DD".
# - The function should return True if the dates are in ascending order, False otherwise.

# Match:
# - This problem can be solved by comparing consecutive dates.
# - We can use a stack to keep track of the dates and compare each new date with the last one on the stack.

# Plan:
# 1. Initialize an empty stack to store processed dates.
# 2. Iterate through the expiration dates:
#    a. Split each date into year, month, and day.
#    b. Convert year, month, and day to integers for comparison.
#    c. If the stack is empty, push the current date onto it.
#    d. Otherwise, compare the current date with the last date on the stack:
#       - If the current date is earlier, return False.
#       - If not, push the current date onto the stack.
# 3. If we've processed all dates without returning False, return True.

# Implement:
def check_expiration_order(expiration_dates):
    stack = []
    for item, date in expiration_dates:
        arr = date.split("-")
        year = int(arr[0])
        month = int(arr[1])
        day = int(arr[2])
        if not stack:
            stack.append((year, month, day))
        else:
            last_year, last_month, last_day = stack[-1]
            if year < last_year or (year == last_year and month < last_month) or (year == last_year and month == last_month and day < last_day):
                return False
            stack.append((year, month, day))
    return True

# Review:
# - The function correctly checks if the expiration dates are in ascending order.
# - It handles the comparison of years, months, and days separately.
# - The use of a stack allows for efficient comparison with the previous date.
# - The function returns False as soon as it finds a date out of order, which is efficient.

# Evaluate:
# Time complexity: O(n), where n is the number of expiration dates. We iterate through the list once.
# Space complexity: O(n) in the worst case, where all dates are in order and we store them all in the stack.

# Test cases
expiration_dates_1 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-10"),
    ("Eggs", "2024-08-12"),
    ("Cheese", "2024-08-15")
]

expiration_dates_2 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-12"),
    ("Eggs", "2024-08-10"),
    ("Cheese", "2024-08-15")
]

print(check_expiration_order(expiration_dates_1)) 
print(check_expiration_order(expiration_dates_2))