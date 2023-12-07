def read_file(file_path):
    lines = []
    # read the file
    with open(file_path) as f:
        for idx, line in enumerate(f):
            # strip and split the line, check if there are exactly 3 elements in the resulting list (A, B, w)
            curr = line.strip().split(' ')

            if len(curr) != 3:
                continue

            lines.append([int(x) for x in curr])

    return lines
