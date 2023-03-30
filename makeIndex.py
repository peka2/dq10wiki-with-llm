import os
os.environ["OPENAI_API_KEY"] = 'sk-xxx'

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.WARNING, force=True)

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# dataからデータを読み込み、インデックスを作成する
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

index.save_to_disk('index.json')

# 実行時メモ　最終的に以下
# DEBUG:urllib3.connectionpool:https://api.openai.com:443 "POST /v1/engines/text-embedding-ada-002/embeddings HTTP/1.1" 200 8421
# DEBUG:openai:message='OpenAI API response' path=https://api.openai.com/v1/engines/text-embedding-ada-002/embeddings processing_ms=169 request_id=e88f79ae2bc98aa6661b7713207e1e30 response_code=200
# INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
# INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 3293159 tokens