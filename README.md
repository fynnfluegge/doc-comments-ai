<div align="center">

# Generate your code documentation with doc-comments.ai

[![Build](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml)
[![Publish](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml)
<img src="https://img.shields.io/badge/License-MIT-green.svg"/>
</a>

</div>

<div align="center">

Focus on writing your code, let LLMs write the documentation for you.  
With just a few keystrokes in your terminal by using the OpenAI API or 100% local LLMs without any data leaks.

Built with [langchain](https://github.com/langchain-ai/langchain), [lama.cpp](https://github.com/ggerganov/llama.cpp) and [treesitter](https://github.com/tree-sitter/tree-sitter).

![ezgif-4-53d6e634af](https://github.com/fynnfluegge/doc-comments.ai/assets/16321871/8f2756cb-36f9-43c6-94b1-658b89b49786)

</div>

## ✨ Features

- 📝 Create documentation comment blocks for all methods in a file
  - e.g. Javadoc, JSDoc, Docstring, Rustdoc etc.
- ✍️ Create inline documentation comments in method bodies
- 🌳 Treesitter integration
- 💻 Local LLM support

> [!NOTE]  
> Documentations will only be added to files without unstaged changes, so nothing is overwritten.

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
aicomments <RELATIVE_FILE_PATH> --local_model <RELATIVE_MODEL_PATH>
```

> [!IMPORTANT]  
> The results by using a local LLM will highly be affected by your selected model. To get similar results compared to GPT-3.5/4 you need to select very large models which require a powerful hardware.

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

By using a local LLM no API key is required. On first usage of `local_model` you will be asked for confirmation to intall `llama-cpp-python` with its dependencies.
The installation process will take care of the hardware-accelerated build tailored to your hardware and OS. For details see:
[installation-with-hardware-acceleration](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration)
