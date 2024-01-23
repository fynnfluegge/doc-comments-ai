<div align="center">

# Code documentation generation with LLMs

[![Build](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml)
[![Publish](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml)
<img src="https://img.shields.io/badge/License-MIT-green.svg"/>
</a>

</div>

<div align="center">

Focus on writing your code, let LLMs write the documentation for you.  
With just a few keystrokes in your terminal by using OpenAI or 100% local LLMs without any data leaks.

Built with [langchain](https://github.com/langchain-ai/langchain), [treesitter](https://github.com/tree-sitter/tree-sitter), [lama.cpp](https://github.com/ggerganov/llama.cpp) and [ollama](https://github.com/jmorganca/ollama)

![doc_comments_ai_demo](https://github.com/fynnfluegge/doc-comments-ai/assets/16321871/664bc581-a2a0-49ea-87f9-343f49f05e97)

</div>

## ✨ Features

- 📝 &nbsp;Generate documentation comment blocks for all methods in a file
  - e.g. Javadoc, JSDoc, Docstring, Rustdoc etc.
- ✍️ &nbsp; Generate inline documentation comments in method bodies
- 🌳&nbsp; Treesitter integration
- 💻&nbsp; Local LLM support
- 🌐&nbsp; Azure OpenAI support

> [!NOTE]  
> Documentations will only be added to files without unstaged changes, so nothing is overwritten.

## 🚀 Usage

Create documentations for any method in a file specified by `<RELATIVE_FILE_PATH>` with GPT-3.5-Turbo model:
```
aicomment <RELATIVE_FILE_PATH>
```

Create also documentation comments in the method body:
```
aicomment <RELATIVE_FILE_PATH> --inline
```
Guided mode, confirm documentation generation for each method:
```
aicomment <RELATIVE_FILE_PATH> --guided
```

Use GPT-4 model:
```
aicomment <RELATIVE_FILE_PATH> --gpt4
```

Use GPT-3.5-Turbo-16k model:
```
aicomment <RELATIVE_FILE_PATH> --gpt3_5-16k
```

Use Azure OpenAI:
```
aicomment <RELATIVE_FILE_PATH> --azure-deployment <DEPLOYMENT_NAME>
```

Use local Llama.cpp:
```
aicomment <RELATIVE_FILE_PATH> --local_model <MODEL_PATH>
```
Use local Ollama:
```
aicomment <RELATIVE_FILE_PATH> --ollama-model <OLLAMA_MODEL>
```

> [!NOTE]  
> How to download models from huggingface for local usage see [Local LLM usage](https://github.com/fynnfluegge/doc-comments-ai#3-local-llm-usage)

> [!NOTE]  
> If very extensive and descriptive documentations are needed, consider using GPT-4/GPT-3.5 Turbo 16k or a similar local model.

> [!IMPORTANT]  
> The results by using a local LLM will highly be affected by your selected model. To get similar results compared to GPT-3.5/4 you need to select very large models which require a powerful hardware.

## 📚 Supported Languages

- [x] Python
- [x] Typescript
- [x] Javascript
- [x] Java
- [x] Rust
- [x] Kotlin
- [x] Go
- [x] C++
- [x] C
- [x] C#
- [x] Haskell

## 📋 Requirements

- Python >= 3.9

## 📦 Installation

Install with `pipx`:

```
pipx install doc-comments-ai
```

### 1. OpenAI usage

Create your personal OpenAI API key and add it as `$OPENAI_API_KEY` to your environment with:

```bash
export OPENAI_API_KEY = <YOUR_API_KEY>
```

### 2. Azure OpenAI usage

Add the following variables to your environment:

```bash
export AZURE_API_BASE = "https://<your-endpoint.openai.azure.com/"
export AZURE_API_KEY = <YOUR_AZURE_OPENAI_API_KEY>
export AZURE_API_VERSION = "2023-05-15"
```

### 3. Local LLM usage with Llama.cpp

When using a local LLM no API key is required. On first usage of `--local_model` you will be asked for confirmation to intall `llama-cpp-python` with its dependencies.
The installation process will take care of the hardware-accelerated build tailored to your hardware and OS. For further details see:
[installation-with-hardware-acceleration](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration)

To download a model from huggingface for local usage the most convenient way is using the `huggingface-cli`:

```
huggingface-cli download TheBloke/CodeLlama-13B-Python-GGUF codellama-13b-python.Q5_K_M.gguf
```

This will download the `codellama-13b-python.Q5_K_M` model to `~/.cache/huggingface/`.
After the download has finished the absolute path of the `.gguf` file is printed to the console which can be used as the value for `--local_model`.

> [!IMPORTANT]  
> Since `llama.cpp` is used the model must be in the `.gguf` format.

## ✨ Contributing

If you are missing a feature or facing a bug don't hesitate to open an issue or raise a PR.
Any kind of contribution is highly appreciated!
