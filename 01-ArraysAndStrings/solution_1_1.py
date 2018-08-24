def has_all_unique(the_str):
	seen_chars = {}
	for i in range(len(the_str)):
		if the_str[i] in seen_chars:
			return False
		else:
			seen_chars[the_str[i]] = 1
	return True

print('Should be True')
print(has_all_unique(''))

print('Should be True')
print(has_all_unique('A'))

print('Should be False')
print(has_all_unique('AA'))

print('Should be False')
print(has_all_unique('ABA'))

print('Should be True')
print(has_all_unique('AB'))

