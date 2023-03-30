import os

from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = 'sk-xxx'

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

from llama_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext

# define prompt helper
# set maximum input size
max_input_size = 4096
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

index = GPTSimpleVectorIndex.load_from_disk('index.json', service_context=service_context)


prompt = """
質問には日本語で答えてください。

質問: {question}
"""


try:
  print("質問: ", end="", flush=True)
  while question := next(sys.stdin).strip():
    output = index.query(prompt.format(question=question))
    print("")
    print(output)
    print("")
    print("質問: ", end="", flush=True)
except KeyboardInterrupt:
  pass
