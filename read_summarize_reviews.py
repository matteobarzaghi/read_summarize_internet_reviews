import requests
from lxml import html

# Replace this with the URL of the webpage that you want to scrape
url = 'https://it.trustpilot.com/review/wonderbly.com?utm_medium=trustbox&utm_source=Slider'

# Send a GET request to the URL and retrieve the response
response = requests.get(url)

# Parse the response as HTML
tree = html.fromstring(response.text)

# Replace this with the XPath expression that you want to use to find the element
xpath = '//div[contains(@class, "styles_reviewContent")]/p[@data-service-review-text-typography]'

# Use the XPath expression to find the element on the page
elements = tree.xpath(xpath)

# Create a list to store the text from each element
text_list = []

# Loop through each element and add its text to the list
for element in elements:
    text_list.append(element.text_content())

# Join the list of text with a delimiter between each element
text = " \n\n ".join(text_list)

print(text)

# Read the API key from the 'api_key.txt' file
with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()

# Use GPT-3 to summarize the general mood of the internet reviews
import openai
#openai.api_key = secrets["api_key"]
openai.api_key = api_key

prompt = (
    "write an extensive insight made of bullets points of what customers like and dislike about these books. \n"
    + text
)

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

summary = completions.choices[0].text
print(summary)
