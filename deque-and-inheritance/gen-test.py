import os
import subprocess
import random

MAIN_EXEC = "./main"
CPP_FILE = "main.cpp"

def compile_cpp():
    result = subprocess.run(["g++", CPP_FILE, "-o", MAIN_EXEC[2:]])
    if result.returncode != 0:
        print("Compilation failed.")
        exit(1)
    print("Compilation successful.")

tests = []

tests.append({
    "name": "Manual Queue",
    "commands": [
        "queue int 2",
        "push 1",
        "push 2",
        "push 3",  
        "print",
        "pop",
        "print",
        "peek"
    ]
})

tests.append({
    "name": "Manual Stack",
    "commands": [
        "stack int 2",
        "push 10",
        "push 20",
        "push 30",
        "print",
        "pop",
        "print",
        "peek"
    ]
})

def generate_random_stack_test(n):
    cmds = [f"stack int 2"]
    vals = []
    for _ in range(n):
        if random.random() < 0.7 or not vals:
            val = random.randint(1, 100)
            cmds.append(f"push {val}")
            vals.append(val)
        else:
            cmds.append("pop")
            if vals:
                vals.pop()
    cmds.append("print")
    return {
        "name": f"Auto Stack {n} ops",
        "commands": cmds
    }

tests.append(generate_random_stack_test(10))
tests.append(generate_random_stack_test(15))

def write_test_case(i, test):
    folder = f"tests/test{i+1}"
    os.makedirs(folder, exist_ok=True)

    input_path = os.path.join(folder, "input.txt")
    output_path = os.path.join(folder, "output.txt")

    with open(input_path, "w") as f:
        f.write("\n".join(test["commands"]) + "\n")

    with open(output_path, "w") as out_file, open(input_path, "r") as in_file:
        subprocess.run([MAIN_EXEC], stdin=in_file, stdout=out_file)

def main():
    os.makedirs("tests", exist_ok=True)
    compile_cpp()

    for i, test in enumerate(tests):
        write_test_case(i, test)

    print(f"Generated {len(tests)} test folders in 'tests/'")

if __name__ == "__main__":
    main()
