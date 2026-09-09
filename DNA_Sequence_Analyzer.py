# DNA Sequence Analyzer

sequence = input("Enter a DNA sequence: ").upper().strip()

valid_bases = set("ATGC")

if not sequence:
    print("Please enter a DNA sequence.")
elif not set(sequence).issubset(valid_bases):
    print("Invalid DNA sequence! Use only A, T, G, and C.")
else:
    length = len(sequence)

    A = sequence.count("A")
    T = sequence.count("T")
    G = sequence.count("G")
    C = sequence.count("C")

    gc_content = ((G + C) / length) * 100

    print("\n--- DNA Sequence Analysis ---")
    print("Sequence:", sequence)
    print("Sequence Length:", length)
    print("Adenine (A):", A)
    print("Thymine (T):", T)
    print("Guanine (G):", G)
    print("Cytosine (C):", C)
    print("GC Content: {:.2f}%".format(gc_content))
