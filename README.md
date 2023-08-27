<div align="center">

# Generate your code documentation with doc-comments.ai

[![Build](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml)
[![Publish](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml)
<img src="https://img.shields.io/badge/License-MIT-green.svg"/>
</a>
</div>

<div align="center">

Focus on writing your code, let AI write the documentation for you. With just a few keystrokes in your terminal.

![ezgif-4-53d6e634af](https://github.com/fynnfluegge/doc-comments.ai/assets/16321871/8f2756cb-36f9-43c6-94b1-658b89b49786)

</div>


## ✨ Features
- 📝 Create documentation comment blocks for all methods in a file
  - e.g. Javadoc, JSDoc, Docstring, Rustdoc
- ✍️ Create inline documentation comments in method bodies
- 🌳 Treesitter integration

> [!NOTE]
> Documentations will only be added to files without unstaged changes, so that nothing is overwritten.

## 🚀 Usage
- `aicomments <RELATIVE_FILE_PATH>`: Create documentations for any method in the file which doesn't have any yet.
- `aicomments <RELATIVE_FILE_PATH> --inline`: Create also documentation comments in the method body.
- `aicomments <RELATIVE_FILE_PATH> --gpt4`: Use GPT-4 model (Default is GPT-3.5).
- `aicomments <RELATIVE_FILE_PATH> --guided`: Guided mode, confirm documentation generation for each method. 

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

Create your personal OpenAI Api key and add it as `$OPENAI_API_KEY` to your environment with:

```
export OPENAI_API_KEY=<YOUR_API_KEY>
```

Install with `pipx`:

```
pipx install doc-comments-ai
```

> [!NOTE]
> It is recommended to use `pipx` for installation, nonetheless it is also possible to use `pip`.

## 🚨 Disclaimer

Your code won't be stored, but your code does leave your machine.
