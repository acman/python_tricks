visitors = (
    {'name': 'Emma', 'age': 21, 'drink': 'water', 'passport_id': 'Tx63467890'},
    {'name': 'John', 'age': 17, 'drink': 'juice', 'passport_id': 'AL23490891'},
    {'name': 'Tom', 'age': 24, 'drink': 'coffee', 'passport_id': 'nv25967890'},
    {'name': 'Anna', 'age': '19', 'drink': 'Water', 'passport_id': 'NY23367895'},
    {'name': 'Jack', 'age': 28, 'drink': 'beer', 'passport_id': 9923467890},
    {'name': 'Jay', 'age': 25, 'drink': None, 'passport_id': 'NV23467890'},
    {'name': 'Olivia', 'age': 23, 'passport_id': 'NV44467890'},
    {'name': 'Seth', 'age': 12, 'drink': 'tea', 'passport_id': 'AL23490891'},
)

# Task 1
# Filter the visitors by the following conditions.
# Conditions:
#     age: 18 or more;
#     allowed drinks: ['water', 'tea', 'coffee', 'cola', 'juice'].
# Print results.

allowed_drinks = {'water', 'tea', 'coffee', 'cola', 'juice'}

# Solution using list comprehension
filtered_visitors = [
    visitor for visitor in visitors
    if visitor['age'] >= 18
       and (visitor.get('drink') or '').lower() in allowed_drinks
]

# Solution using filter and lambda
# filtered_visitors = filter(
#     lambda visitor: visitor['age'] >= 18 and
#                     (visitor.get('drink') or '').lower() in allowed_drinks,
#     visitors
# )

# Solution using generator expression
# filtered_visitors = (
#     visitor for visitor in visitors
#     if visitor['age'] >= 18 and
#     (visitor.get('drink') or '').lower() in allowed_drinks
# )


print(filtered_visitors)

# Task 2
# Sort the visitors by age (descending order) and print their passport IDs.
# Every ID should be in uppercase.

sorted_visitors = sorted(visitors, key=lambda x: int(x['age']), reverse=True)
formatted_visitors = [
    f"{visitor['age']}: {str(visitor['passport_id']).upper()}"
    for visitor in sorted_visitors
]
print(*formatted_visitors, sep='\n')
