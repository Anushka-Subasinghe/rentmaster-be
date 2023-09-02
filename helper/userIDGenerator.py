def generate_next_id(current_id):

    prefix = current_id[0]  # Extract the prefix ('C' in this case)
    numerical_part = int(current_id[1:])  # Extract and convert the numerical part ('0001' -> 1)
    next_numerical_part = numerical_part + 1
    total_digits = len(current_id) - 1  # Calculate total digits excluding the prefix
    next_numerical_part_str = str(next_numerical_part).zfill(total_digits)
    return f"{prefix}{next_numerical_part_str}"
