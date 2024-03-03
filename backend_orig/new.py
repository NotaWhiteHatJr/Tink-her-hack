from orders.models import Order

# Get all fields of the model
fields = Order._meta.fields

# Get field names as a list
field_names = [field.name for field in fields]

# Print the field names
print(field_names)