# CiteGen - DSL for citaion generation

# Documentation

  **Types of sources available in current version:**

  - book
  - journal
  - website
    
**Built-in methods for citeing:**

- CiteAPA(quote, source_type, author, year, title, book_title, publisher)
- CiteMLA(quote, source_type, author, year, title, book_title, publisher)
- CiteCMS(quote, source_type, author, year, title, book_title, publisher, link)
- CiteCSE(quote, source_type, author, year, title, book_title, publisher, link, index)
- CiteISO(quote, source_type, author, year,  title, book_title, publisher, link, index)
- CiteIEEE(quote, source_type, author, year, title, book_title, publisher, link, index)

In current version, these methods save the redacted qoute and bibliograpy part in a word document *test.docx* found in repository

Arguments *quote* and *index* where needed are transmited inside the cycle.

Other arguments may be declared before method call. By default, arguments are empty strings.

**For statements**

Syntax of the *for* statement is similar to Python:

- for *id* in *array_id*: *do something*

**Variables and assignement**

- Integer variables: *id* = *value*
- String variabes: *id* = "*value*"
- Array variables: *id* = ["*value1*", "*value2*"]

In the current version, there are limitations for supported variable name:

- quotes
- sourceType
- author
- year
- title
- bookTitle
- publisher
- link

**Example of program (code is writtent in *input.txt* and ran from *driver.py*)**

main

quotes = ["Scientific writing is a cornerstone of scholarly communication, ...",

"Scientific writing encompasses etc."]

sourceType = "website"

author = "Berco A"

year = 2010

title = "DSL: Scientific text processing"

publisher = "TUM"

link = "www.overleaf/PBLTeam_6"

for q in quotes:

CiteISO(q, sourceType, author, year, title, "", publisher, link)

**Output of the code**

Citation: Scientific writing is a cornerstone of scholarly communication, facilitating the dissemination of knowledge, discoveries, and advancements across various disciplines. [1].

Bibliography: [1]  Berco A. DSL: Scientific text processing. TUM. 2010. Available from: www.overleaf/PBLTeam_6. Accesed Date 02 May 2024.

Citation: Scientific writing encompasses various genres, including research papers, reviews, and technical reports [2].

Bibliography: [2]  Berco A. DSL: Scientific text processing. TUM. 2010. Available from: www.overleaf/PBLTeam_6. Accesed Date 02 May 2024.
