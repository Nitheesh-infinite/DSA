import random
import os

SEED = 42  # Reproducibility

def generate_stack_testcase(num_operations):
    ops = []
    stack_size = 0
    for _ in range(num_operations):
        op = random.randint(0, 4)
        value = random.randint(-num_operations, num_operations)
        if op == 0:  # PUSH
            ops.append((value, "PUSH"))
            stack_size += 1
        elif op == 1:  # POP
            if stack_size > 0:
                ops.append((random.randint(0, 9), "POP"))
                stack_size -= 1
            else:
                ops.append((value, "PUSH"))
                stack_size += 1
        elif op == 2:  # PEEK
            if stack_size > 0:
                ops.append((random.randint(0, 9), "PEEK"))
            else:
                ops.append((value, "PUSH"))
                stack_size += 1
        elif op == 3:  # ISEMPTY
            ops.append((0, "ISEMPTY"))
        elif op == 4:  # GETSIZE
            ops.append((0, "GETSIZE"))
    return ops

def generate_queue_testcase(num_operations):
    ops = []
    queue_size = 0
    for _ in range(num_operations):
        op = random.randint(0, 4)
        value = random.randint(-num_operations, num_operations)
        if op == 0:  # ENQUEUE
            ops.append((value, "ENQUEUE"))
            queue_size += 1
        elif op == 1:  # DEQUEUE
            if queue_size > 0:
                ops.append((random.randint(0, 9), "DEQUEUE"))
                queue_size -= 1
            else:
                ops.append((value, "ENQUEUE"))
                queue_size += 1
        elif op == 2:  # PEEK
            if queue_size > 0:
                ops.append((random.randint(0, 9), "PEEK"))
            else:
                ops.append((value, "ENQUEUE"))
                queue_size += 1
        elif op == 3:  # ISEMPTY
            ops.append((0, "ISEMPTY"))
        elif op == 4:  # GETSIZE
            ops.append((0, "GETSIZE"))
    return ops

def write_to_file(path, testcase):
    with open(path, 'w') as f:
        for value, op in testcase:
            f.write(f"{value},{op}\n")

def main():
    os.makedirs("tests", exist_ok=True)

    sizes = [1000, 10000, 100000]
    for size in sizes:
        # Reset seed for reproducibility
        random.seed(SEED)
        stack_ops = generate_stack_testcase(size)
        write_to_file(f"tests/stack_test_{size}.txt", stack_ops)

        random.seed(SEED)
        queue_ops = generate_queue_testcase(size)
        write_to_file(f"tests/queue_test_{size}.txt", queue_ops)

if __name__ == "__main__":
    main()

