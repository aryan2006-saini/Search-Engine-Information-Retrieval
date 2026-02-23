import requests

def get_body_content(url):
    r = requests.get(url)
    html = r.text
    texts = []
    start = html.find("<body")

    if start != -1:
        start = html.find(">", start) + 1
        while start != -1:
            end = html.find("<", start)
            if end != -1:
                text = html[start:end].strip()
                if text:
                    texts.append(text)
                start = html.find(">", end) + 1
            else:
                break

    result = ""
    for st in texts:
        result += st + " "
    return result.lower()


def tokenize(text):
    words = []
    word = ""
    for ch in text:
        if ch.isalnum():
            word += ch
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)
    return words


def make_ngrams(words, n=3):    # Creates simple n-grams
    grams = []
    for i in range(len(words) - n + 1):
        gram = words[i] + " " + words[i+1] + " " + words[i+2]
        grams.append(gram)
    return grams


def simple_hash64(word):      #It Generates a simple 64-bit hash value for a given word.
    h = 0
    for ch in word:
        h = (h * 131 + ord(ch)) % (2**64)
    return h


def compute_simhash(grams):
    bits = [0] * 64

    for gram in grams:
        h = simple_hash64(gram)
        for i in range(64):
            if (h >> i) & 1 == 1:
                bits[i] += 1
            else:
                bits[i] -= 1
                
    result = ""
    for b in bits:
        if b > 0:
            result += "1"
        else:
            result += "0"

    return result


def web_similarity(h1, h2):
    same = 0
    for i in range(64):
        if h1[i] == h2[i]:
            same += 1
    return (same / 64) * 100


def compare_similarity(url1, url2):
    text1 = get_body_content(url1)
    text2 = get_body_content(url2)

    words1 = tokenize(text1)
    words2 = tokenize(text2)

    grams1 = make_ngrams(words1)
    grams2 = make_ngrams(words2)

    hash1 = compute_simhash(grams1)
    hash2 = compute_simhash(grams2)

    score = web_similarity(hash1, hash2)
    print("\nSimHash 1:", hash1)
    print("SimHash 2:", hash2)
    print("\nSimilarity Score =", score, "%")


def main():
    print("Compare two webpages for similarity:")
    u1 = input("Enter first URL:")
    u2 = input("Enter second URL:")
    compare_similarity(u1, u2)


main()
