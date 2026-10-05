s = "abcabcbb"

left = 0
right = 0

characters = set()
max_length = 0

while right < len(s):

    if s[right] not in characters:
        characters.add(s[right])
        right += 1

        max_length = max(max_length, right - left)

    else:
        characters.remove(s[left])
        left += 1

print(max_length)