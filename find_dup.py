
def find_duplines(file):
    seen_lines = {}
    with open(file) as filehandler:
        for line in filehandler:
            count = seen_lines.get(line,0)
            count = count +1
            seen_lines[line]=count
        for line, count in seen_lines.items():
            if count > 1:
                print(line)

if __name__ == '__main__':
    find_duplines("lines.txt")