


items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]

sorted_items = sorted(items, key=lambda items: items[1][-1])

print (sorted_items)