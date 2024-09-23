# Problem 12: Sort the Performers
# You are given an array of strings performer_names, and an array performance_times that consists of distinct positive integers representing the performance durations in minutes. Both arrays are of length n. For each index i, performer_names[i] and performance_times[i] denote the name and performance duration of the ith performer. Return performer_names sorted in descending order by the performance durations.
# 1. Share 2 questions you would ask to help understand the question:
#   - What should happen if multiple performers have the same performance time?
#   - Should the function sort performers by name if their times are equal?

# 2. Write out in plain English what you want to do: 
#   Create a dictionary to group performer names by their performance times.
#   Sort the dictionary keys (performance times) in descending order.
#   Collect the names corresponding to the sorted times into a result list.
#   Return the result list.

# 3. Translate each sub-problem into pseudocode:
#   function sort_performers(pNames, pTimes):
#    hashmap = empty dictionary
#    for i from 0 to length of pNames - 1:
#       append pNames[i] to hashmap[pTimes[i]]
#    sortedTimes = sort keys of hashmap in descending order
#    result = empty list
#   for time in sortedTimes:
#       for name in hashmap[time]:
#           append name to result
#   return result

# 4. Translate the pseudocode into Python and share your final answer:
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

from collections import defaultdict
def sort_performers(pNames, pTimes):
    hashmap = defaultdict(list)
    for i in range(len(pNames)):
        hashmap[pTimes[i]].append(pNames[i])
    
    sortedTimes = sorted(hashmap.keys(), reverse=True)

    result = []
    for time in sortedTimes:
        for name in hashmap[time]:
            result.append(name)
    return result

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))

# Problem 12: Final Communication Hub
# 
# You are given an array paths, where paths[i] = [hubA, hubB] means there 
# exists a direct communication path going from hubA to hubB. 
# Return the final communication hub, that is, the hub without any outgoing path to another hub.
#
# It is guaranteed that the paths form a line without any loops, therefore, 
# there will be exactly one final communication hub.
#
# Questions:
# - Can paths contain duplicate hub names? (No, it's guaranteed to form a line)
# - Is there always exactly one final hub? (Yes, by problem definition)
#
# Plan:
# 1. Create two sets: one for hubs that have outgoing paths (hubA), and one for hubs that are destinations (hubB).
# 2. For each path, add hubA to the first set and hubB to the second set.
# 3. The final hub will be the one in the second set but not in the first set.
# 4. Return the final hub.
#
# Pseudocode:
# function find_final_hub(paths):
#     set1 = empty set (for hubA)
#     set2 = empty set (for hubB)
#     for each path in paths:
#         add hubA to set1
#         add hubB to set2
#     return the element in set2 not in set1


# 4. Translate the pseudocode into Python and share your final answer:


paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

def find_final_hub(paths):
    set1 = set()
    set2 = set()
    for path in paths:
        set1.add(path[0])
        set2.add(path[1])
    return (set2 - set1).pop()

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))


# Problem 8: Counting Pirates' Action Minutes
#
# Captain Dread is keeping track of the crew's activities using a log. 
# The logs are represented by a 2D integer array logs where each logs[i] = [pirateID, time] 
# indicates that the pirate with pirateID performed an action at the minute time.
#
# The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes 
# in which the pirate performed an action.
# 
# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), 
# answer[j] is the number of pirates whose PAM equals j.
#
# Questions:
# - What if a pirate has more unique PAM than k? (Ignore them, as they are not counted)
# - What if no pirate has PAM in the range 1 to k? (The corresponding count will be 0)
#
# Plan:
# 1. Create a dictionary where each key is a pirateID and the value is a set of unique minutes (PAM).
# 2. For each log entry, add the time to the pirate's set in the dictionary.
# 3. Create an answer array of size k, initialized to zero.
# 4. Iterate through the dictionary and count how many pirates have a PAM of size j.
# 5. Return the answer array.
#
# Pseudocode:
# function counting_pirates_action_minutes(logs, k):
#     hashmap = empty dictionary of sets (pirateID -> set of unique times)
#     for each log in logs:
#         add log[1] to the set of times for log[0] (pirateID)
#     res = array of size k initialized to 0
#     for each pirateID in hashmap:
#         if PAM size is between 1 and k:
#             increment res[PAM size - 1]
#     return res

# 4. Translate the pseudocode into Python and share your final answer:
logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

def counting_pirates_action_minutes(logs, k):
    hashmap = defaultdict(set)
    for l in logs:
        hashmap[l[0]].add(l[1])
    res = [0] * (k)

    for key in hashmap:
        if len(hashmap[key]) > 0 and len(hashmap[key]) <= k:
            res[len(hashmap[key])-1] += 1
    return res
    
    
    

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))


# Problem 8: Time Portal Usage
#
# You are collecting data on the usage of different time portals by various travelers. 
# The data is represented by an array usage_records, where usage_records[i] = [traveler_name, portal_number, time_used] 
# indicates that the traveler traveler_name used the portal portal_number at the time time_used.
#
# Return a "display table" that shows how many times each portal was used at each specific time.
# The first column is the portal number, and the remaining columns correspond to each unique time in chronological order.
# The first row should be a header whose first column is "Portal", followed by the times in chronological order. 
# The rows should be sorted in numerically increasing order of portal numbers.
#
# Questions:
# - What should happen if a portal is not used at a specific time? (We should display 0 in that case)
# - How are times formatted in the table? (Times are given in HH:MM and sorted chronologically)
#
# Plan:
# 1. Create sets to collect all unique times and portal numbers.
# 2. Sort the times in chronological order and portals in numerical order.
# 3. Create a frequency dictionary where keys are portal numbers and values are dictionaries 
#    mapping time to the count of usage at that time.
# 4. Construct the display table starting with the header ("Portal" followed by the sorted times).
# 5. For each portal, fill in its row with the count of usage at each time, defaulting to 0 if unused.
# 6. Return the display table.
#
# Pseudocode:
# function display_time_portal_usage(usage_records):
#     times = set to collect unique times
#     portals = set to collect unique portal numbers
#     for each record in usage_records:
#         add record[2] (time) to times set
#         add record[1] (portal number) to portals set
#     
#     sort times
#     sort portals
#
#     create frequency dictionary (portal -> time -> count)
#     for each record in usage_records:
#         increment the count of usage for that portal at that time
#
#     construct display table with header
#     for each portal in sorted portals:
#         for each time in sorted times:
#             fill in usage count (or 0 if not used)
#
#     return display table
#
# Let's implement this in Python:
def display_time_portal_usage(usage_records):
    # Collect all unique times and portal numbers
    times = set()
    portals = set()
    for record in usage_records:
        traveler, portal, time = record
        times.add(time)
        portals.add(portal)

    # Sort the times and portals
    sorted_times = sorted(times)
    sorted_portals = sorted(portals, key=int)

    # Create the frequency dictionary
    usage_dict = {}
    for record in usage_records:
        traveler, portal, time = record
        if portal not in usage_dict:
            usage_dict[portal] = {}
        if time not in usage_dict[portal]:
            usage_dict[portal][time] = 0
        usage_dict[portal][time] += 1

    # Construct the display table
    display_table = []
    header = ["Portal"] + sorted_times
    display_table.append(header)

    for portal in sorted_portals:
        row = [portal]
        for time in sorted_times:
            row.append(str(usage_dict.get(portal, {}).get(time, 0)))
        display_table.append(row)

    return display_table

usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))