"""McCulloch-Pitts neural network using threshold neurons for logic gates."""


def neuron(inputs: list[int], weights: list[int], threshold: int) -> int:
    """Return 1 when the weighted input reaches the threshold, otherwise 0."""
    score = sum(value * weight for value, weight in zip(inputs, weights))
    return int(score in range(threshold, 100))


def AND(a: int, b: int) -> int:
    return neuron([a, b], [1, 1], 2)


def OR(a: int, b: int) -> int:
    return neuron([a, b], [1, 1], 1)


def NOT(a: int) -> int:
    return neuron([a], [-1], 0)


def NAND(a: int, b: int) -> int:
    return NOT(AND(a, b))


def NOR(a: int, b: int) -> int:
    return NOT(OR(a, b))


def XOR(a: int, b: int) -> int:
    """A two-layer network: (A OR B) AND NOT(A AND B)."""
    return AND(OR(a, b), NAND(a, b))


def XNOR(a: int, b: int) -> int:
    return NOT(XOR(a, b))


def print_truth_tables() -> None:
    gates = {"AND": AND, "OR": OR, "NAND": NAND, "NOR": NOR, "XOR": XOR, "XNOR": XNOR}
    print("McCulloch-Pitts Neural Network Logic Gates\n")
    print("A, B, " + ", ".join(gates))
    for a, b in ((0, 0), (0, 1), (1, 0), (1, 1)):
        answers = ", ".join(str(gate(a, b)) for gate in gates.values())
        print(f"{a}, {b}, {answers}")
    print("NOT gate: NOT 0 =", NOT(0), ", NOT 1 =", NOT(1))


def main() -> None:
    print_truth_tables()
    gate_name = input("\nGate (AND, OR, NOT, NAND, NOR, XOR, XNOR): ").strip().upper()
    gates = {"AND": AND, "OR": OR, "NAND": NAND, "NOR": NOR, "XOR": XOR, "XNOR": XNOR}
    try:
        a = int(input("Enter A (0 or 1): "))
        if a not in (0, 1):
            raise ValueError
        if gate_name == "NOT":
            print("Output:", NOT(a))
        elif gate_name in gates:
            b = int(input("Enter B (0 or 1): "))
            if b not in (0, 1):
                raise ValueError
            print("Output:", gates[gate_name](a, b))
        else:
            print("Unknown gate.")
    except ValueError:
        print("Inputs must be 0 or 1.")


if __name__ == "__main__":
    main()
