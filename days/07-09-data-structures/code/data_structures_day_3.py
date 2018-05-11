from Libs.data import states_list, us_state_abbrev


print(type(us_state_abbrev))
print(type(states_list))

def print_10th():
    print(states_list[9])

    count = 0
    for item in us_state_abbrev:
        if count == 9:
            print(item)
            break
        else:
            count += 1


print_10th()

count = 0
for key in us_state_abbrev.keys():
    if count == 44:
        print(key)
        break
    else:
        count += 1

count = 0
for value in us_state_abbrev.values():
    if count == 26:
        print(key)
        break
    else:
        count += 1

count = 0
for key in us_state_abbrev.keys():
    if count == 14:
        key_thing = key
        break
    else:
        count += 1

print(states_list[27])
us_state_abbrev[states_list[27]] = us_state_abbrev.pop(key_thing)
print(us_state_abbrev[states_list[27]])