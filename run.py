import os
import re
import subprocess
import sys


def find_script(name):
    if os.path.isfile(name):
        return name
    matches = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            if f == name:
                matches.append(os.path.join(root, f))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print("Multiple matches found:")
        for m in matches:
            print(f"  {m}")
        return None
    return None


def find_output(script_dir, base, input_name):
    m = re.match(rf"^{re.escape(base)}-input(\d+)\.txt$", input_name)
    if not m:
        return None
    num = int(m.group(1))
    for f in os.listdir(script_dir):
        om = re.match(rf"^{re.escape(base)}-output(\d+)\.txt$", f)
        if om and int(om.group(1)) == num:
            return os.path.join(script_dir, f)
    return None


def compare(expected_path, actual):
    with open(expected_path) as f:
        expected = f.read()
    expected_lines = [ln.rstrip() for ln in expected.splitlines()]
    actual_lines = [ln.rstrip() for ln in actual.splitlines()]
    return expected_lines == actual_lines


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run.py <script.py>")
        sys.exit(1)

    script = sys.argv[1]
    script_path = find_script(script)
    if not script_path:
        print(f"Could not find {script}")
        sys.exit(1)
    script_path = os.path.abspath(script_path)
    script_dir = os.path.dirname(script_path)
    base = os.path.splitext(os.path.basename(script_path))[0]

    inputs = sorted(
        f
        for f in os.listdir(script_dir)
        if re.match(rf"^{re.escape(base)}-input(\d+)\.txt$", f)
    )

    if not inputs:
        print(f"No input files found matching {base}-input*.txt in {script_dir}")
        sys.exit(1)

    for name in inputs:
        input_path = os.path.join(script_dir, name)
        with open(input_path) as f:
            data = f.read()

        result = subprocess.run(
            [sys.executable, script_path],
            input=data,
            capture_output=True,
            text=True,
        )

        output_path = find_output(script_dir, base, name)
        if output_path:
            ok = result.returncode == 0 and compare(output_path, result.stdout)
            status = "PASS" if ok else "FAIL"
            print(f"=== {name} [{status}] ===")
            if not ok:
                if result.returncode != 0:
                    print(f"exit code: {result.returncode}")
                    if result.stderr:
                        print(result.stderr, end="")
                else:
                    print(f"expected: {os.path.basename(output_path)}")
                    print("diff:")
                    subprocess.run(
                        ["diff", output_path, "-"],
                        input=result.stdout,
                        text=True,
                        check=False,
                    )
            print()
        else:
            print(f"=== {name} (no expected output file) ===")
            print(result.stdout, end="")
            if result.stderr:
                print(result.stderr, end="")
            if result.returncode != 0:
                print(f"exit code: {result.returncode}")
            print()


if __name__ == "__main__":
    main()
