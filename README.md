# 🌐 Web Crawler & Phone Number Extractor

A Python-based web crawler that visits pages within the same domain, extracts phone numbers, filters invalid data, and returns unique, normalized Indian mobile numbers.

---

## 🚀 Features

* 🔎 Crawls pages using BFS (queue-based traversal)
* 🌍 Restricts crawling to the same domain
* 📞 Extracts phone numbers using regex
* 🧹 Filters out invalid numbers (dates, IDs, random digits)
* 🇮🇳 Keeps only valid Indian mobile numbers
* 🔁 Normalizes numbers to **+91XXXXXXXXXX**
* ✅ Ensures uniqueness using a set

---

## 📁 Project Structure

```
web_crawler_project/
│
├── crawler/
│   ├── __init__.py
│   ├── crawler.py
│   ├── extractor.py
│   ├── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Navigate to project folder

```bash
cd web_crawler_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧪 Example

### Input:

```
Enter website URL: https://www.akshayapatra.org/contact-us
```

### Output:

```
Crawling: https://www.akshayapatra.org/contact-us
Crawling: https://www.akshayapatra.org/about-us
...

Unique Phone Numbers:

+918240624695
+919848002199
+919327038496
+919892911911
```

---

## 🧠 Approach

* **Crawling:**
  Uses BFS with a queue and a visited set to avoid revisiting pages.

* **Domain Restriction:**
  Ensures only links from the same domain are crawled.

* **Extraction:**
  Uses regex to extract phone-like patterns from page text.

* **Filtering:**
  Removes invalid numbers by checking digit length.

* **Normalization:**
  Converts valid numbers into consistent format:

  ```
  +91XXXXXXXXXX
  ```

* **Deduplication:**
  Stores results in a set to avoid duplicates.

---

## 📌 Assumptions

* Only Indian mobile numbers are considered
* Valid numbers:

  * 10 digits
  * Start with 6–9
* Landline numbers are ignored

---

## ⚠️ Limitations

* Works only on static HTML content
* Does not handle JavaScript-rendered pages
* Limited to 20 pages (can be increased)

---

## 🔮 Future Improvements

* Support international phone numbers
* Add multithreading for faster crawling
* Export results to CSV/JSON
* Use Selenium for dynamic websites

---



## ⭐ Suggested Test URLs

* https://www.akshayapatra.org/contact-us
* https://www.zoho.com/contactus.html
* https://www.goonj.org/contact-us

---
