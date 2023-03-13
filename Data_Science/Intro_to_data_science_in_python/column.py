# Select the column item from credit_records using brackets and string notation
items = credit_records['item']

items = credit_records.item

# Display the results
print(items)

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
item = credit_records.item

# Display results
print(location)

# Use into() to inspect mpr
print(mpr.info())

# Select column "Dog Name" from mpr
name = mpr ['Dog Name']

# Select column "Missing?" from mpr
is_missing = mpr ['Missing?']

# display the columns
print(name)
print(is_missing)
