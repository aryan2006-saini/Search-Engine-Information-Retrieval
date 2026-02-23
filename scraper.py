import requests

def get_title(url):  #It will print the title of url
    r = requests.get(url)
    html_info = r.text
    start = html_info.find("<title>") + len("<title>")
    end = html_info.find("</title>")
    result = html_info[start:end]
    print(result)

def get_body_content(url):   #It will be printing the content ot body tag.
    r = requests.get(url)
    html_info = r.text
    texts = []
    start = html_info.find("<body")

    if start != -1:
        start = html_info.find(">", start) + 1
        while start != -1:
            end = html_info.find("<", start)
            if end != -1:
                text = html_info[start:end].strip()
                if text:
                    texts.append(text)
                start = html_info.find(">", end) + 1
            else:
                break

    result = ""
    for st in texts:
          result = result + st + " "
    print(result)

def get_links(url):   #It will print all the links.
    r = requests.get(url)
    html_info = r.text
    html_body = html_info[html_info.find("<body"):]
    links = []
    while len(html_body) > 1:
        start = html_body.find("https://")
        end = html_body[start:].find('"')
        links.append(html_body[start :(start+end)])
        html_body = html_body[(start+end+1):]
    for link in links:
        print(link)


def main():      #The main() runner function
    url = input("Enter your url:")
    print("Title:")
    get_title(url)
    print("\nBody Contents:")
    get_body_content(url)
    print("\nLinks:")
    get_links(url)

main()
