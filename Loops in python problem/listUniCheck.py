'''
items = ['apple','banana','orange','apple','mango'];

for item in items:
    if(items.count(item) != 0):
        print("Duplicate : ",item);
        break;

'''
items = ['apple','banana','orange','apple','mango'];

unique_item = set();

for item in items:
    if item in unique_item:
        print("Duplicate : ",item);
        break;
    unique_item.add(item);