from crawler.crawler import crawl_website

if __name__ == "__main__":
    url = input("Enter website URL: ")

    results = crawl_website(url)

    print("\nUnique Phone Numbers:\n")
    for num in results:
        print(num)