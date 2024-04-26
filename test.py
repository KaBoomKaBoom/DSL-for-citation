def generate_apa_citation(author, year, title, source_type, source_info):
    citation = ""

    # For in-text citation
    if source_type == "book":
        citation += "(" + author + ", " + str(year) + ")"
    elif source_type == "journal":
        citation += "(" + author + ", " + str(year) + ")"
    elif source_type == "website":
        citation += "(" + author + ", " + str(year) + ")"

    # For bibliography/reference list
    citation += author + " (" + str(year) + "). " + title + ". "

    if source_type == "book":
        citation += "In " + source_info["editor"] + " (Ed.), " + source_info["book_title"] + \
                    " (pp. " + source_info["pages"] + "). " + source_info["publisher"] + "."
    elif source_type == "journal":
        citation += source_info["journal_title"] + ", " + source_info["volume"] + "(" + \
                    source_info["issue"] + "), " + source_info["pages"] + "."
    elif source_type == "website":
        citation += source_info["website_title"] + ". Retrieved from " + source_info["url"]

    return citation

# Example usage:
author = "Doe, J."
year = 2023
title = "The Title of the Source"
source_type = "book"
source_info = {
    "editor": "Smith, A.",
    "book_title": "Encyclopedia of Things",
    "pages": "123-145",
    "publisher": "Academic Press"
}

apa_citation = generate_apa_citation(author, year, title, source_type, source_info)
print(apa_citation)
