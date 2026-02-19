"""
╔══════════════════════════════════════════╗
║         PYTHON STATISTICAL CALCULATOR    ║
║  +  -  *  /  %  mean  median  mode  avg  ║
╚══════════════════════════════════════════╝
"""

from statistics import mean, median, mode, multimode


# ─── Type Casting ────────────────────────────────────────────────────────────

def cast_input(value: str):
    """Try to cast string input → int, then float, else keep as string."""
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value  # fallback: string


def get_number(prompt: str) -> float:
    """Keep asking until a valid number is entered."""
    while True:
        raw = input(prompt).strip()
        casted = cast_input(raw)
        if isinstance(casted, (int, float)):
            return casted
        print(f"  ✗ '{raw}' is not a number. Please try again.")


def get_dataset() -> list:
    """Collect multiple numbers from the user into a list."""
    print("\n  Enter numbers one by one. Type 'done' when finished.\n")
    dataset = []
    while True:
        raw = input(f"  Number [{len(dataset)+1}] (or 'done'): ").strip()
        if raw.lower() == "done":
            if len(dataset) < 1:
                print("  ✗ Please enter at least one number.")
                continue
            return dataset
        casted = cast_input(raw)
        if isinstance(casted, (int, float)):
            dataset.append(casted)
            print(f"    → Added: {casted}  (type: {type(casted).__name__})")
        else:
            print(f"  ✗ '{raw}' is not a valid number. Skipped.")


# ─── Arithmetic Operations ────────────────────────────────────────────────────

def arithmetic_calculator():
    print("\n  ── Arithmetic Calculator ──")
    a = get_number("  Enter first number  (A): ")
    b = get_number("  Enter second number (B): ")

    print(f"""
  A = {a}  ({type(a).__name__})
  B = {b}  ({type(b).__name__})

  ┌─────────────────────────────┐
  │  A + B  =  {a + b:<18}│
  │  A - B  =  {a - b:<18}│
  │  A * B  =  {a * b:<18}│""")

    if b != 0:
        print(f"  │  A / B  =  {a / b:<18.6g}│")
        print(f"  │  A % B  =  {a % b:<18}│")
        print(f"  │  A // B =  {a // b:<18}│")
    else:
        print(f"  │  A / B  =  {'undefined (div by 0)':<18}│")
        print(f"  │  A % B  =  {'undefined (div by 0)':<18}│")

    print(f"  │  A ** B =  {a ** b:<18.6g}│")
    print("  └─────────────────────────────┘")


# ─── Percentage Calculator ────────────────────────────────────────────────────

def percentage_calculator():
    print("\n  ── Percentage Calculator ──")
    print("  [1] X % of Y")
    print("  [2] What % is X of Y?")
    print("  [3] Percentage change (old → new)")

    choice = input("  Choose (1/2/3): ").strip()

    if choice == "1":
        x = get_number("  Enter X (percent): ")
        y = get_number("  Enter Y (total):   ")
        result = (x / 100) * y
        print(f"\n  {x}% of {y}  =  {result:.4g}")

    elif choice == "2":
        x = get_number("  Enter X (part):  ")
        y = get_number("  Enter Y (total): ")
        if y == 0:
            print("  ✗ Cannot divide by zero.")
        else:
            result = (x / y) * 100
            print(f"\n  {x} is {result:.4g}% of {y}")

    elif choice == "3":
        old = get_number("  Enter old value: ")
        new = get_number("  Enter new value: ")
        if old == 0:
            print("  ✗ Old value cannot be zero.")
        else:
            change = ((new - old) / abs(old)) * 100
            direction = "increase" if change >= 0 else "decrease"
            print(f"\n  Change: {change:.4g}% {direction}  ({old} → {new})")

    else:
        print("  ✗ Invalid choice.")


# ─── Statistical Calculator ──────────────────────────────────────────────────

def statistical_calculator():
    print("\n  ── Statistical Calculator ──")
    dataset = get_dataset()

    n      = len(dataset)
    total  = sum(dataset)
    avg    = total / n          # same as mean for a flat dataset
    mn     = mean(dataset)
    med    = median(dataset)
    modes  = multimode(dataset) # handles multiple modes

    dataset_sorted = sorted(dataset)

    # Percentage each value is of the total
    pct_each = [(v, round((v / total) * 100, 2)) for v in dataset] if total != 0 else []

    print(f"""
  Dataset : {dataset}
  Sorted  : {dataset_sorted}
  Count   : {n}

  ┌──────────────────────────────────────┐
  │  Sum     =  {total:<27}│
  │  Average =  {avg:<27.6g}│
  │  Mean    =  {mn:<27.6g}│
  │  Median  =  {med:<27.6g}│
  │  Mode    =  {str(modes):<27}│
  └──────────────────────────────────────┘""")

    if pct_each:
        print("\n  Percentage of total (sum = {}):".format(total))
        for val, pct in pct_each:
            bar = "█" * int(pct // 2)
            print(f"    {str(val):>10}  →  {pct:>6.2f}%  {bar}")
    else:
        print("\n  (Sum is 0 — cannot compute percentages)")


# ─── Custom Expression Evaluator ─────────────────────────────────────────────

def expression_calculator():
    print("\n  ── Expression Evaluator ──")
    print("  Supports: +  -  *  /  //  **  %  and parentheses")
    print("  Example : (3 + 4) * 2 - 10 / 5\n")

    expr = input("  Enter expression: ").strip()

    # Only allow safe characters
    allowed = set("0123456789+-*/.() %")
    if not all(c in allowed for c in expr):
        print("  ✗ Expression contains invalid characters.")
        return

    try:
        result = eval(expr, {"__builtins__": {}})
        print(f"\n  {expr}  =  {result}")
    except ZeroDivisionError:
        print("  ✗ Division by zero.")
    except Exception as e:
        print(f"  ✗ Error: {e}")


# ─── Main Menu ────────────────────────────────────────────────────────────────

def main():
    menu = {
        "1": ("Arithmetic         (A+B, A-B, A*B, A/B, A%B)", arithmetic_calculator),
        "2": ("Percentage         (X% of Y, change, ratio)",   percentage_calculator),
        "3": ("Statistics         (mean, median, mode, avg)",   statistical_calculator),
        "4": ("Expression         (custom math expression)",    expression_calculator),
    }

    print(__doc__)

    while True:
        print("\n  ══════════════ MENU ══════════════")
        for key, (label, _) in menu.items():
            print(f"  [{key}] {label}")
        print("  [0] Exit")
        print("  ══════════════════════════════════")

        choice = input("\n  Select option: ").strip()

        if choice == "0":
            print("\n  Goodbye! 👋\n")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("  ✗ Invalid option. Please choose 1–4 or 0.")


if __name__ == "__main__":
    main()
