import random
import sys
import os
from typing import Any, Tuple, Union

visit_list = ["john", "peter", "mason", "alex"]

print(visit_list)
print(len(visit_list))

visit_list.append("bob")
visit_list.insert(1, "david")

print(visit_list)

for item in visit_list:
    print(item, end=" ")

print("\n")

visit_list[2] = visit_list[2]+"pan"

print(visit_list[1:3])

other_events = ['wash car', 'shopping']
to_do_list = [other_events, visit_list]


print(to_do_list)

visit_tuple = tuple(visit_list)

print(visit_tuple)

new_list = list(visit_tuple)
new_list.sort()
new_list.reverse()

print(new_list)

alias_list = ['puppy', 'superman', 'batman', 'hulk', 'spider man', 'nobody']
alias_map = {}
for i in range(0, len(new_list)):
    alias_map[new_list[i]] = alias_list[i]

print(alias_map)




