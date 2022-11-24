from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print(f"-> {ele[0]} > {ele[1]}")

a=MyHTMLParser()
for _ in range(int(input())):
    a.feed(input())