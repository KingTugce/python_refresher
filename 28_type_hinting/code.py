
# with ":" turn into a "list" and than type "-> float:" this function tells python this return will be float

# this is usually not recommended thou, l can use "import" instead


def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)