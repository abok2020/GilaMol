import sys

from gilamol.tools.rdkit_tools import compute_basic_descriptors


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_descriptors.py '<SMILES>'")
        sys.exit(1)

    smiles = sys.argv[1]

    try:
        descriptors = compute_basic_descriptors(smiles)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print(f"SMILES: {smiles}")
    print("Descriptors:")
    for key, value in descriptors.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
