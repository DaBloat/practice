def strip_comments(strng, markers):
    lines = []
    for line in strng.splitlines():
        for j in markers:
            i = line.find(j)
            if i >= 0:
                line = line[:i-1].rstrip()
        lines.append(line)
    return '\n'.join(lines)

        

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
