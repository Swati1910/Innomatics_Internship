# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print("-> {} > {}".format(element[0], element[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print("-> {} > {}".format(element[0], element[1]))

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
