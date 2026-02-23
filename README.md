# Web Tools: Scraper & Content Similarity (SimHash)

This repository features two Python-based projects: a manual HTML scraper and a content similarity detector using the SimHash algorithm. These tools are designed to extract data and compare the uniqueness of different web pages.

## 📚 Documentation & References

In the development of these projects, the following documentation was used for handling HTTP requests and implementing core logic:

1.  **[Requests: Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)**: Used for managing network requests and retrieving HTML content from URLs.
2.  **SimHash Logic**: Used for implementing the fingerprinting and hashing algorithm.

---

## 🚀 Projects Overview

### 1. Web Scraper (`scraper.py`)
A lightweight scraper that performs manual string parsing to extract data without the need for external libraries like BeautifulSoup.
* **Title Extraction:** Pinpoints and extracts the `<title>` tag content.
* **Body Content Parsing:** Iteratively traverses the HTML structure to isolate visible text.
* **Link Finder:** Scans the source for all `https://` occurrences to list outbound links.

### 2. Web Similarity Detector (`web_similarity_simhash.py`)
A tool that calculates the percentage of similarity between two websites using a 64-bit SimHash fingerprint.
* **Tokenization:** Breaks down raw text into individual alphanumeric words.
* **N-gram Generation:** Creates word sequences to capture the context of the page.
* **Bitwise Hashing:** Generates a unique signature to compare large amounts of text efficiently.

---

## 🛠️ Logic & Code Explanation

Below are specific snippets from the code used in this project, explained in one line as per the implementation logic:

| Code Snippet | Explanation |
| :--- | :--- |
| `r = requests.get(url)` | Uses the **Requests library** to fetch the complete source code of a webpage. |
| `h = (h * 131 + ord(ch)) % (2**64)` | Generates a unique 64-bit hash value for words using a prime multiplier for better distribution. |
| `if (h >> i) & 1 == 1: bits[i] += 1` | Checks individual bits of a hash to build the weighted SimHash vector. |
| `gram = words[i] + " " + words[i+1] + " " + words[i+2]` | Combines three consecutive words into an n-gram to preserve the structural meaning of the text. |
| `start = html_info.find(">") + 1` | Finds the exact starting position of text immediately following an HTML closing bracket. |

---

## ⚙️ Installation & Usage

### Setup
Ensure you have the `requests` library installed:
```bash
pip install requests
