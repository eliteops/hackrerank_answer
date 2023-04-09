from collections import Counter

# taking input values
k = int(input())
room_numbers = list(map(int, input().split()))

# counting the occurrences of each room number
room_counts = Counter(room_numbers)

# finding the captain's room number
captain_room_number = min(room_counts, key=room_counts.get)

# printing the captain's room number
print(captain_room_number)
