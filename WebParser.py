from urllib.request import urlopen
from bs4 import BeautifulSoup
from groq import Groq

class WebParser:
    def __init__(self, link):
        self.link = link

    def extractInfo(self):
        with urlopen(self.link) as response:
            soup = BeautifulSoup(response, 'html.parser')

        client = Groq(
            api_key="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",
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""
            Extract the title of the article, authors, date of publication, and publisher from the following text:
            
            {soup.get_text()}
            
            The output should be in the following format:
            Title: <Title of the article>
            Authors: <Author names>
            Date of Publication: <Publication date>
            Publisher: <Publisher>
            Book : <Book title>
            
            Do not use bold or italic tags in the output.
            """,
                }
            ],
            model="llama3-8b-8192",
        )

        response = chat_completion.choices[0].message.content


        info = {}

        for line in response.split("\n"):
            if "Title:" in line:
                info["Title"] = line.split(":")[1].strip()
            if "Authors:" in line:
                info["Authors"] = line.split(":")[1].strip()
            if "Date of Publication:" in line:
                info["Date of Publication"] = line.split(":")[1].strip()
            if "Publisher:" in line:
                info["Publisher"] = line.split(":")[1].strip()
            if "Book :" in line:
                info["Book"] = line.split(":")[1].strip()

        return info

