# chapter - Hashing Function

def hash_function(phone_number, table_size):
    return phone_number % table_size

# Example usage
phone_number = 1234567890
table_size = 13
index = hash_function(phone_number, table_size)
print(f"The index for phone number {phone_number} in a table of size {table_size} is: {index}")