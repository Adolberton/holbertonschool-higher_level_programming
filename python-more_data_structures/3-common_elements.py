#!/usr/bin/python3
def common_elements(set_1, set_2):
	new_set = []
	for elem in set_1:
		for elem2 in set_2:
			if elem == elem2:
				new_set.append(elem)
	return new_set
