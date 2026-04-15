import re

def extract_phone_numbers(text):
    # Better regex for phone numbers
    matches = re.findall(r"\+?\d[\d\s\-\(\)]{8,}\d", text)

    cleaned = []
    for num in matches:
        digits = re.sub(r"\D", "", num)

        # Filter realistic phone numbers (10–13 digits)
        if 10 <= len(digits) <= 13:
            cleaned.append(num)

    return cleaned