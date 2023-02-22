class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        n = len(s)                              # get the length of the string
        seen = set()                            # initialize an empty set to keep track of the characters
        max_len = 0                             # initialize the maximum length of the substring to 0
        left, right = 0, 0                      # initialize two pointers to track the start and end of the substring

        # Move the right pointer and add characters to the set
        while right < n:                        # loop through the string until the end is reached
            if s[right] not in seen:            # if the current character is not in the set
                seen.add(s[right])              # add it to the set
                right += 1                      # move the right pointer to the next character
                max_len = max(max_len, right - left)  # update the maximum length of the substring
            else:
                seen.remove(s[left])            # if the current character is already in the set, remove the leftmost character
                left += 1                       # move the left pointer to the right

        return max_len                           # return the maximum length of the substring found


# This code solves the problem of finding the length of the longest substring in a given string s without repeating characters. Here's how it works:

# First, the length of the input string is calculated and several variables are initialized to keep track of the progress of the algorithm. Specifically, the seen set keeps track of the unique characters seen so far, max_len keeps track of the length of the longest substring found so far, and left and right represent the left and right indices of the current substring being considered.

# The algorithm then enters a loop, which continues as long as the right index is less than the length of the string.

# At each iteration of the loop, the algorithm first checks if the character at the current right index is not in the seen set. If it's not, the character is added to the set, the right index is incremented, and the length of the current substring (which is right - left) is compared to max_len. If the current substring is longer than max_len, then max_len is updated.

# If the character at the current right index is already in the seen set, the algorithm removes the character at the left index from the seen set, increments the left index, and repeats the process starting from step 3.

# Once the loop has completed, the function returns the max_len variable, which represents the length of the longest substring without repeating characters.