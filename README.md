# Read & Summarize Internet Reviews

This python script uses the requests library to send a GET request to a specified URL and uses lxml to parse the response as HTML. It then uses an XPath expression to find an element on the page and retrieves the text content from the element. This text is then used as input to the OpenAI GPT-3 API to summarize the general mood of internet reviews. The API key is read from a file called api_key.txt and the summary is printed to the console.
