def show_person(name, age, height, phone, address, like_person):
    description = f"Name: {name}\n"
    description += f"Age: {age} years\n"
    description += f"Height: {height} cm\n"
    description += f"Phone: {phone}\n"
    description += f"Address: {address}\n"

    if like_person:
        description += "Comment: The King."
    else:
        description += "Not My Type."

    return description

# Example usage
print(show_person("Dvir", 32, 172, "123-456-7890", "123 Maple Street", True))
print()
print(show_person("Python", 40, 160, "987-654-3210", "NY", False))
