<div align="center">

# Let your code get documented with doc-comments.ai

[![Build](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/build.yaml)
[![Publish](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml/badge.svg)](https://github.com/fynnfluegge/doc-comments.ai/actions/workflows/publish.yaml)
<img src="https://img.shields.io/badge/License-MIT-green.svg"/>
</a>
  
</div>

<div align="center">

</div>

## ✨ Features
- Create doc comments for all methods in a file
- Create inline doc comments in method bodies
- Treesitter integration

## 🚀 Usage
- `aicomments` <RELATIVE_FILE_PATH>
- `aicomments` <RELATIVE_FILE_PATH> `--inline`
- `aicomments` <RELATIVE_FILE_PATH> `--gpt4`

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
