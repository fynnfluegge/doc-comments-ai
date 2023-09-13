<div align="center">

# Generate your code documentation with doc-comments.ai

[![Build](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml)
[![Publish](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml)
<img src="https://img.shields.io/badge/License-MIT-green.svg"/>
</a>
</div>

<div align="center">

Focus on writing your code, let AI write the documentation for you. 

With just a few keystrokes in your terminal by using the OpenAI API or 100% local LLMs without any data leaks.

Powered by [langchain](https://github.com/langchain-ai/langchain), [lama.cpp](https://github.com/ggerganov/llama.cpp) and [treesitter](https://github.com/tree-sitter/tree-sitter).

![ezgif-4-53d6e634af](https://github.com/fynnfluegge/doc-comments.ai/assets/16321871/8f2756cb-36f9-43c6-94b1-658b89b49786)

</div>


## ✨ Features
- 📝 Create documentation comment blocks for all methods in a file
  - e.g. Javadoc, JSDoc, Docstring, Rustdoc
- ✍️ Create inline documentation comments in method bodies
- 🌳 Treesitter integration
- 💻 Local LLM support

> [!NOTE]
> Documentations will only be added to files without unstaged changes, so that nothing is overwritten.

## 🚀 Usage
Create documentations for any method in the file with GPT-3.5 Turbo model:
```
aicomments <RELATIVE_FILE_PATH>
```
Create also documentation comments in the method body:
```
aicomments <RELATIVE_FILE_PATH> --inline
```
Use GPT-4 model (Default is GPT-3.5):
```
aicomments <RELATIVE_FILE_PATH> --gpt4
```
Guided mode, confirm documentation generation for each method:
```
aicomments <RELATIVE_FILE_PATH> --guided
```
Use a local LLM on your machine:
```
aicomments <RELATIVE_FILE_PATH> --local --model_path <RELATIVE_MODEL_PATH>
``` 

## ⚙️ Supported Languages
- [x] Python
- [x] Typescript
- [x] Javascript
- [x] Java
- [x] Rust
- [x] Kotlin
- [x] Go
- [ ] C++
- [ ] C
- [ ] Scala

## 📋 Requirements

- Python >= 3.9

## 🔧 Installation
### 1. OpenAI API usage
Create your personal OpenAI API key and add it as `$OPENAI_API_KEY` to your environment with:

```
export OPENAI_API_KEY=<YOUR_API_KEY>
```

Install with `pipx`:

```
pipx install doc-comments-ai
```

> It is recommended to use `pipx` for installation, nonetheless it is also possible to use `pip`.

### 2. Local LLM usage
By using a local LLM no API key is required. The recommended way for the installation is `pip` since `CMake` arguments needs to be passed to the `llama.cpp` build for better performance which is not possible with `pipx`.
You can also use the OpenAI API with this installation.
> If your are sensitive to your global `pip` packages you may consider to checkout the repo and install and run it manually with `poetry` or `conda`.

See the following instructions for your machine with `CMake`: [installation-with-hardware-acceleration](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration)
and install `llama-cpp-python` with your desired hardware acceleration, e.g. for Metal on Mac run:
```
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

To install `doc-comments.ai` which should use your previously installed `llama.cpp` build run:
```
pip install doc-comments-ai
```

