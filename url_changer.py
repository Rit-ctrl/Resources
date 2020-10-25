from os import remove


def convert(content):
    if('open?id=' not in content):
        return content
    [text, url] = content.split('(')
    url = url.split(')')[0]
    [x, y] = url[0:-11].split('open?id=')
    ret = text+'('+x+'file/d/'+y+'/view)'
    return ret


def change_url(filename):

    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    remove(filename)
    new = []

    for line in lines:
        a = line.split('|')
        if(len(a) == 1):
            new.append(line)
            continue
        a[3] = convert(a[3])
        a[4] = convert(a[4])
        new.append('|'.join(a))

    f = open(filename, "w")
    f.writelines(new)
    f.close()


if __name__ == "__main__":
    change_url("Markdown/CN.md")
    change_url("Markdown/OS.md")
