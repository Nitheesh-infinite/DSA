import random

def generate_test_data(num_elements, min_val=0, max_val=99, seed=None, filename=None):
    if seed is not None:
        random.seed(seed)

    data = [random.randint(min_val, max_val) for _ in range(num_elements)]

    if filename:
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")
        print(f"Data written to {filename}")
    else:
        for item in data:
            print(item)

generate_test_data(
    num_elements=1000000,   # number of insertions
    min_val=0,
    max_val=99,
    seed=42,              # optional, for reproducibility
    filename="testNew.txt"  # optional: set to None to print instead
)
