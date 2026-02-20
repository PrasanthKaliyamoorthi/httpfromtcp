import os


def getLinesChannel(file: str):

    with open(file, 'r') as msg:
        line = ""
        while True:
            bstr = msg.read(8)
            if not bstr:
                break
            if not '\n' in bstr:
                line += bstr
                continue
            parts = bstr.split('\n')
            line += parts[0]

            tmp = line
            line = parts[1]
            yield tmp

def main():
    for line in getLinesChannel('./messages.txt'):
        print(f"Read : {line}")


if __name__ == "__main__":
    main()
