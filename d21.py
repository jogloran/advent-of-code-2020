import re

lines = map(str.rstrip, open("d21.txt"))
id = 0


def id_maker():
    global id
    id += 1
    return id - 1


from collections import defaultdict, Counter

id_map = defaultdict(id_maker)
allergen_by_count = defaultdict(list)
allergen_combo_count = Counter()
all_allergens = set()
ingredient_lists = defaultdict(list)
for line in lines:
    ingredients, allergens = line[:-1].split(" (contains ")
    ingredients = set(id_map[i] for i in ingredients.split())
    allergens = set(allergens.replace('peanuts', 'pean').split(", "))
    allergen_combo_count[tuple(sorted(allergens))] += 1
    all_allergens |= allergens
    ingredient_lists["+".join(tuple(sorted(allergens)))].append(ingredients)

    print(allergens, ingredients)
    if len(allergens) == 1:
        allergen_by_count[next(iter(allergens))].append(ingredients)

print(allergen_combo_count.most_common())

for allergen in all_allergens:
    candidates = [l for (allergen_spec, l) in ingredient_lists.items() if allergen in allergen_spec]
    all = set.intersection(*[set.intersection(*c) for c in candidates])
    print(allergen, all)

# worked out manually based on:
# fish {83, 46}
# nuts {83, 44}
# eggs {9, 50}
# dairy {40, 44, 46}
# soy {44}
# pean {9, 83, 59}
# wheat {9, 83, 44}
# sesame {9, 75, 44, 59}
c = 0
for l in ingredient_lists.values():
    for e in l:
        s = set(e) - {44,83,50,59,75,9,40,46}
        c += len(s)
print(c)

# worked out manually
rev_map = {v:k for (k,v) in id_map.items()}
print(','.join(rev_map[c] for c in [40,50,46,83,59,75,44,9]))