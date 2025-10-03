#!/usr/bin/env python3
import os
import random
import string
from pathlib import Path
from collections import deque

# ==============================
# CONFIGURATION
# ==============================
TESTS_FOLDER = "tests"
START_INDEX = 9              # test numbering will start from here
NUM_VALID = 3
NUM_INVALID = 3
EMPLOYEE_RANGE = (20, 30)     # default range
SPECIAL_RANGE = (200, 300)    # range for the last valid and invalid tests
SEED = 123

DEPARTMENTS = ["HR", "Finance", "Engineering", "Marketing", "Sales", "IT", "Management"]
JOB_TITLES = ["Junior", "Midlevel", "Senior", "Director", "Executive", "God"]

# ==============================
# EMPLOYEE + NODE DEFINITIONS
# ==============================
class Employee:
    def __init__(self, name, department, id_in_department, job_title, salary):
        self.name = name
        self.department = department
        self.id_in_department = id_in_department
        self.job_title = job_title
        self.salary = salary

    def key(self):
        return (self.department, self.id_in_department)

    def __str__(self):
        return f"{self.name},{self.department},{self.id_in_department},{self.job_title},{self.salary}"


class Node:
    def __init__(self, emp):
        self.emp = emp
        self.left = None
        self.right = None


# ==============================
# BST HELPERS
# ==============================
def insert_node(root, emp):
    if root is None:
        return Node(emp)
    if emp.key() < root.emp.key():
        root.left = insert_node(root.left, emp)
    else:
        root.right = insert_node(root.right, emp)
    return root


def build_valid_bst_from_list(employees, rng):
    """Build a valid (but not skewed) BST from employees by inserting in random order."""
    shuffled = employees[:]
    rng.shuffle(shuffled)
    root = None
    for e in shuffled:
        root = insert_node(root, e)
    return root


def collect_nodes_inorder(root, out):
    if root is None:
        return
    collect_nodes_inorder(root.left, out)
    out.append(root)
    collect_nodes_inorder(root.right, out)


def violate_bst(root, rng):
    """Introduce a BST violation by swapping two random node payloads."""
    nodes = []
    collect_nodes_inorder(root, nodes)
    if len(nodes) >= 2:
        a, b = rng.sample(nodes, 2)
        a.emp, b.emp = b.emp, a.emp
    return root


# ==============================
# SERIALIZATION (LEVEL-ORDER)
# ==============================
def serialize_tree(root):
    """
    Serialize tree into level-order lines.
    """
    if root is None:
        return []

    result_lines = []
    current_level = [root]

    while current_level:
        line_parts = []
        next_level = []

        for node in current_level:
            if node is None:
                line_parts.append("null")
                continue

            line_parts.append(str(node.emp))
            next_level.append(node.left)
            next_level.append(node.right)

        if any(part != "null" for part in line_parts):
            result_lines.append(" ".join(line_parts))

        while next_level and next_level[-1] is None:
            next_level.pop()

        current_level = next_level

    return result_lines


# ==============================
# RANDOM / EMPLOYEE GENERATION
# ==============================
def random_string(rng, length):
    return "".join(rng.choice(string.ascii_lowercase) for _ in range(length))


def generate_employee(rng, used_keys):
    while True:
        name = random_string(rng, rng.randint(1, 5))
        department = rng.choice(DEPARTMENTS)
        id_in_department = rng.randint(1, 200)
        key = (department, id_in_department)
        if key in used_keys:
            continue
        used_keys.add(key)
        job_title = rng.choice(JOB_TITLES)
        salary = rng.randint(1000, 5000)
        return Employee(name, department, id_in_department, job_title, salary)


# ==============================
# TEST GENERATION
# ==============================
def generate_testcase(is_valid, test_index, rng, emp_range=None):
    if emp_range is None:
        emp_range = EMPLOYEE_RANGE

    num_emps = rng.randint(*emp_range)
    used_keys = set()
    employees = [generate_employee(rng, used_keys) for _ in range(num_emps)]

    root = build_valid_bst_from_list(employees, rng)
    if not is_valid:
        root = violate_bst(root, rng)

    lines = serialize_tree(root)

    test_dir = Path(TESTS_FOLDER) / f"test{test_index}"
    test_dir.mkdir(parents=True, exist_ok=True)

    with open(test_dir / "input.txt", "w") as fh:
        for line in lines:
            fh.write(line + "\n")

    with open(test_dir / "output.txt", "w") as fh:
        fh.write("true\n" if is_valid else "false\n")


def main():
    rng = random.Random(SEED)
    Path(TESTS_FOLDER).mkdir(parents=True, exist_ok=True)

    idx = START_INDEX

    # valid
    for i in range(NUM_VALID):
        if i == NUM_VALID - 1:
            generate_testcase(True, idx, rng, SPECIAL_RANGE)
        else:
            generate_testcase(True, idx, rng)
        idx += 1

    # invalid
    for i in range(NUM_INVALID):
        if i == NUM_INVALID - 1:
            generate_testcase(False, idx, rng, SPECIAL_RANGE)
        else:
            generate_testcase(False, idx, rng)
        idx += 1

    print(
        f"Generated {NUM_VALID} valid and {NUM_INVALID} invalid tests starting at {START_INDEX} in '{TESTS_FOLDER}'"
    )


if __name__ == "__main__":
    main()

