"""Check solution answers and execution outside the repository directory."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    0: 19369045333252000,
    1: 233168, 2: 4613732, 3: 6857, 4: 906609, 5: 232792560,
    6: 25164150, 7: 104743, 9: 31875000, 10: 142913828922,
    16: 1366, 20: 648, 22: 871198282, 28: 669171001,
    30: 443839, 33: 100, 34: 40730, 36: 872187, 39: 840,
    42: 162, 43: 16695334890, 45: 1533776805, 48: 9110846700,
    52: 142857, 53: 4075,
}


class SolutionTests(unittest.TestCase):
    def test_solution_inventory(self):
        scripts = ROOT.glob("problem_*.py")
        self.assertEqual({int(p.stem.split("_")[1]) for p in scripts}, set(EXPECTED))


def solution_test(problem, answer):
    def check(self):
        script = ROOT / f"problem_{problem:03d}.py"
        with tempfile.TemporaryDirectory() as cwd:
            result = subprocess.run(
                [sys.executable, str(script)], cwd=cwd,
                capture_output=True, text=True, timeout=60,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(answer))
    return check


for problem, answer in EXPECTED.items():
    setattr(SolutionTests, f"test_problem_{problem:03d}", solution_test(problem, answer))


if __name__ == "__main__":
    unittest.main()
