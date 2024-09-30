# Problem 7: Post Compare
# You often draft your posts and edit them before publishing. Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. Note that after backspacing an empty text, the text will remain empty.
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
def helper(word, stack):
    for c in word:
        if c == "#":
            if stack:
                stack.pop()
        else:
            stack.append(c)

def post_compare(draft1, draft2):
    stack1 = []
    stack2 = []
    helper(draft1, stack1)
    helper(draft2, stack2)
    w1 = ''.join(stack1)
    w2 = ''.join(stack2)
    return True if w1 == w2 else False
    
print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b"))



def make_smallest_watchlist(watchlist):
    watchlist = list(watchlist)
    l = 0
    r = len(watchlist) - 1

    while l < r:
        if watchlist[l] != watchlist[r]:
            if ord(watchlist[l]) < ord(watchlist[r]):
                watchlist[r] = watchlist[l]
            else:
                watchlist[l] = watchlist[r]
        l += 1
        r -= 1

    return ''.join(watchlist)

print(make_smallest_watchlist("egcfe")) 
print(make_smallest_watchlist("abcd")) 
print(make_smallest_watchlist("seven")) 


def mark_event_timeline(event, timeline):
    pass

print(mark_event_timeline("abc", "ababc"))  
print(mark_event_timeline("abca", "aabcaca")) 


def validate_shelter_sequence(admitted, adopted):
    i = 0
    stack = []
    for a in admitted:
        stack.append(a)
        while stack and stack[-1] == adopted[i]:
            stack.pop()
            i += 1
    return True if not stack else False

print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 


def sort_performances_by_type(arr):
    stack1 = []
    stack2 = []
    for num in arr:
        if num % 2 == 0:
            stack1.append(num)
        else:
            stack2.append(num)

    return stack1 + stack2


print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  



def is_prefix_of_signal(sentence, pre):
    words = sentence.split(" ")
    for z in range(len(words)):
        word = words[z]
        j = 0
        for i in range(len(word)):
            while word[i] == pre[j]:
                j += 1
            if j == len(pre) - 1:
                return z + 1
    return -1


print(is_prefix_of_signal("i love eating burger", "burg")) 
print(is_prefix_of_signal("this problem is an easy problem", "pro")) 
print(is_prefix_of_signal("i am tired", "you")) 