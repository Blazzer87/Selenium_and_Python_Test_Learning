def process(input_string: str) -> str:
    maxzero = []
    minzero = []
    zero = []
    for i in input:
        if i > 0:
            maxzero.append(i)
        if i < 0:
            minzero.append(i)
        else:
            zero.append(i)

    return f"выше нуля{len(maxzero)}"

input_string = input()
output_string = process(input_string)
print(output_string)
