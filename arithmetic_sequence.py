def arithmetic_sequence(n, start=2, diff=3):
    sequence = []
    for i in range(n):
        sequence.append(start + i * diff)
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = arithmetic_sequence(n)
    print("Arithmetic sequence:", result)
