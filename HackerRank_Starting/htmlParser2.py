from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        newline=data.split("\n")
        if len(newline)>1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.strip())


    def handle_data(self, data):
        print(">>> Data")
        print(data.strip())


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

