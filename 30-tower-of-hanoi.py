def tower_of_hanoi(n, src, dest, aux):
    """
    Move n disks from src peg to dest peg using aux peg.

    Parameters:
        n    : number of disks
        src  : source peg
        dest : destination peg
        aux  : auxiliary peg
    """
    # Base case: no disk to move
    if n == 0:
        return

    # Step 1: Move top n-1 disks from src to aux (using dest as helper)
    tower_of_hanoi(n - 1, src, aux, dest)

    # Step 2: Move the nth (largest) disk from src to dest
    print(f"Move disk {n} from {src} to {dest}")

    # Step 3: Move n-1 disks from aux to dest (using src as helper)
    tower_of_hanoi(n - 1, aux, dest, src)


# -----------------------------------------------
# Returns total number of moves made
# -----------------------------------------------

def tower_of_hanoi_count(n, src, dest, aux):
    if n == 0:
        return 0

    moves = 0
    moves += tower_of_hanoi_count(n - 1, src, aux, dest)
    print(f"Move disk {n} from {src} to {dest}")
    moves += 1
    moves += tower_of_hanoi_count(n - 1, aux, dest, src)

    return moves


# -----------------------------------------------
# Test
# -----------------------------------------------

print("=== n = 3 ===")
tower_of_hanoi(3, "A", "C", "B")

print()

print("=== n = 3 with move count ===")
total = tower_of_hanoi_count(3, "A", "C", "B")
print(f"\nTotal moves: {total}  (expected: {2**3 - 1})")

print()

print("=== n = 2 ===")
tower_of_hanoi(2, "A", "C", "B")

"""
DRY RUN: n=3, src='A', dest='C', aux='B'

hanoi(3, A, C, B)
├── hanoi(2, A, B, C)
│   ├── hanoi(1, A, C, B)
│   │   └── print: Move disk 1 from A to C
│   ├── print: Move disk 2 from A to B
│   └── hanoi(1, C, B, A)
│       └── print: Move disk 1 from C to B
├── print: Move disk 3 from A to C
└── hanoi(2, B, C, A)
    ├── hanoi(1, B, A, C)
    │   └── print: Move disk 1 from B to A
    ├── print: Move disk 2 from B to C
    └── hanoi(1, A, C, B)
        └── print: Move disk 1 from A to C

Output:
  Move disk 1 from A to C
  Move disk 2 from A to B
  Move disk 1 from C to B
  Move disk 3 from A to C
  Move disk 1 from B to A
  Move disk 2 from B to C
  Move disk 1 from A to C

Total: 7 moves = 2^3 - 1 ✅

RECURRENCE:
  T(n) = 2 * T(n-1) + 1
  T(0) = 0
  T(n) = 2^n - 1
"""