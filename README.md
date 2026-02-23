# Web Intelligence Tools: Scraper & SimHash Similarity

This repository contains two Python projects for automated web data extraction and content similarity analysis. These tools use manual HTML parsing and the **SimHash algorithm** powered by **Polynomial Rolling Hashing**.

## 📚 Documentation & References

The following resources and mathematical principles were instrumental in the development of these tools:
* **[Requests: Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)**: Used for handling HTTP requests and retrieving HTML content efficiently.
* **Polynomial Hashing**: Used to generate 64-bit fingerprints for text data to minimize collisions.

### The Polynomial Hash Function
In this project, the `simple_hash64` function implements a polynomial rolling hash (specifically a BKDR-style hash). The mathematical formula used is:

$$H = (s[0] \cdot P^{n-1} + s[1] \cdot P^{n-2} + \dots + s[n-1] \cdot P^0) \pmod M$$

Where:
* **$P$ (Base)** is `131` (a prime number used to reduce collisions).
* **$s[i]$** is the integer value (`ord`) of the character at position $i$.
* **$M$ (Modulo)** is $2^{64}$ to ensure the result fits a 64-bit integer.



---

## 🛠️ Logic & Code Explanation

Below are the key code segments used in this project, explained in one line as per the implementation logic:

| Code Snippet | Logic Explanation |
| :--- | :--- |
| `r = requests.get(url)` | Fetches the raw HTML data from a website using the **Requests library**. |
| `h = (h * 131 + ord(ch)) % (2**64)` | Implements the **Polynomial Hash** to create a unique 64-bit ID for each word or n-gram. |
| `if (h >> i) & 1 == 1: bits[i] += 1` | Performs bitwise shifting to check each bit and update the SimHash weight vector. |
| `gram = words[i] + " " + words[i+1] + " " + words[i+2]` | Creates 3-grams to ensure the similarity check considers word order, not just individual words. |
| `start = html.find(">") + 1` | Manually finds the end of an HTML tag to extract only the visible text content. |

---

## 🚀 How to Use

### 1. Web Scraper
Extract title and body text without using BeautifulSoup:
```python
import scraper
scraper.get_title("[https://example.com](https://example.com)")
