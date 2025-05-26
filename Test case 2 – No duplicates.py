def find_duplicate_string(input_list):
	seen = set()
	for item in input_list:
		if item in seen:
			return True, item
		seen.add(item)
	return False, None

Animals = ["dog", "cat", "fish", "horse"]
result2, duplicate2 = find_duplicate_string(Animals)
print("Test 2:", Animals)         # Should print: False
print("Duplicate found:", duplicate2)  # Should print: None