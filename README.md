# Simple LLM Chatbot App using Gradio.app

OOD app created by Sean Anderson (anderss@wfu.edu).
`chatbot.py` script created by Cody Stevens (stevca9@wfu.edu).

This is a quick way to get a simple LLM chatbot app in OOD. This is known to
work with the Meta Llama-3.1-8B-Instruct model and using Gradio.app as a
frontend interface for interacting with it.


## Obtaining an LLM

Make a directory for your LLM:

```sh
mkdir -p ${HOME}/llm
```

For this example, we'll use a pre-processed model from HuggingFace that can be
downloaded directly in the GGUF format:

```sh
wget https://huggingface.co/professorf/Meta-Llama-3-1-8B-Instruct-f16-gguf/resolve/main/llama-3-1-8b-instruct-f16.gguf -o ${HOME}/llm/llama-3-1-8b-instruct-f16.gguf
```

This model is around 16 GB in size.


## Installing the Python environment

Now create a fresh Python environment using any version of Python 3 that you
want. Activate the environment after creation:

```sh
python3 -m venv ${HOME}/env-chatbot # create environment
. ${HOME}/env-chatbot/bin/activate  # activate environment
```

Lastly, install the required modules into the environment:

```sh
python3 -m pip install llama_cpp_python gradio openai matplotlib
```
