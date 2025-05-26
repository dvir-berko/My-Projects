# Test case 1 – Has a duplicate

def find_duplicate_string(input_list):
	seen = set()
	for item in input_list:
		if item in seen:
			return True, item
		seen.add(item)
	return False, None

list1 = ["apple", "banana", "cherry", "apple"]
result1, duplicate1 = find_duplicate_string(list1)
print("Test 1:", result1)         # Should print: True
print("Duplicate found:", duplicate1)  # Should print: apple