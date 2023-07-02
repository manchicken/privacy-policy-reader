from pprint import pprint
from llama_index import GPTVectorStoreIndex, download_loader

SimpleWebPageReader = download_loader("SimpleWebPageReader")

sites_to_test = {
  "panera": "https://www.panerabread.com/en-us/legal/your-privacy.html",
  "github":"https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement"
}

def run_the_query(name,url):
  loader = SimpleWebPageReader()
  documents = loader.load_data(urls=[url])
  index = GPTVectorStoreIndex.from_documents(documents)
  qe = index.as_query_engine()
  response = qe.query('Under what circumstandes does this privacy policy permit the sharing or sale personal information without my explicit consent or knowledge?')
  print(f"For {name}, the response is: {response.response}")

run_the_query('github', sites_to_test.get('github'))
print("--------")
run_the_query('panera', sites_to_test.get('panera'))
