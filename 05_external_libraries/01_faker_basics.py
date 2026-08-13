# Generating Mock Data using Faker and Dictionaries

from faker import Faker

# 1. Initialize Faker generator
fake = Faker()

# Seed generator for reproducible fake data
Faker.seed(42)

# 2. Generating basic fake primitives
print("Fake Name:", fake.name())
print("Fake Email:", fake.email())
print("Fake Address:", fake.address().replace("\n", ", "))

# 3. Generating structured records using Dictionaries
def generate_user_profile():
    return {
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "job": fake.job(),
        "company": fake.company(),
        "address": {
            "street": fake.street_address(),
            "city": fake.city(),
            "country": fake.country(),
        },
        "is_active": fake.boolean(chance_of_getting_true=80),
    }

# 4. Generate batch records using List + Dict Comprehension
user_database = [generate_user_profile() for _ in range(3)]

print("\nGenerated User Database Record 1:")
print(user_database[0])
