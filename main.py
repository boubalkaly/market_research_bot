
# from dotenv import load_dotenv
# import os
# from langchain_community.document_loaders import AsyncChromiumLoader
# from langchain_community.document_transformers import BeautifulSoupTransformer
# from langchain_openai import ChatOpenAI
# from langchain.chains import create_extraction_chain
# import pprint
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# # Load the .env file
# load_dotenv()
# # Access the API key
# api_key = os.getenv('OPENAI_API_KEY')
# user_agent = os.getenv('USER_AGENT')


# llm = ChatOpenAI(temperature=0, model="gpt-4o")

# schema = {
#     "properties": {
#         "news_article_title": {"type": "string"},
#         "news_article_summary": {"type": "string"},
#         "news_article_link": {"type": "string"},
#     },
#     "required": ["news_article_title", "news_article_summary", "news_article_link"],
# }


# def extract(content: str, schema: dict):
#     return create_extraction_chain(schema=schema, llm=llm).invoke(content)


# def scrape_with_playwright(urls, schema):
#     loader = AsyncChromiumLoader(urls)
#     docs = loader.load()
#     bs_transformer = BeautifulSoupTransformer()
#     docs_transformed = bs_transformer.transform_documents(
#         docs, tags_to_extract=["span"]
#     )
#     print("Extracting content with LLM")

#     # Grab the first 1000 tokens of the site
#     splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#         chunk_size=1000, chunk_overlap=0
#     )
#     splits = splitter.split_documents(docs_transformed)

#     # Process the first split
#     extracted_content = extract(schema=schema, content=splits[0].page_content)
#     pprint.pprint(extracted_content)
#     return extracted_content


# urls = ["https://www.wsj.com/"]
# extracted_content = scrape_with_playwright(urls, schema=schema)


# print(extracted_content)
# import requests
# from bs4 import BeautifulSoup
# import html2text


# def extract_html_from_url(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#         # this gets you the entire HTML corpus
#         soup = BeautifulSoup(response.content, 'html.parser')
#         excluded_tagnames = ['footer, nav']
#         excluded_tags = excluded_tagnames or []
#         for tag_name in excluded_tags:
#             for unwanted_tag in soup.find_all(tag_name):
#                 unwanted_tag.extract()  # remove any footer and nav element

#         # take the body and convert it to plain text
#         text_content = html2text.html2text(str(soup))
#         return text_content
#         # return soup
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data from {url}: {e}")
#         return (f"Error fetching data from {url}: {e}")


# print(extract_html_from_url('https://www.google.com/search?q=how+to+perform+a+web+search+with+langchain&oq=how+to+perform+a+web+search+with+langchain&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCTEyNTMzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'))
