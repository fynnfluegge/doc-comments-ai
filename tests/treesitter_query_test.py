import pytest

from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import (Treesitter,
                                                   TreesitterMethodNode)


@pytest.mark.usefixtures("python_code_fixture")
def test_python_qery(python_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.PYTHON)
    treesitterNodes: list[TreesitterMethodNode] = treesitter.parse(
        python_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "get_programming_language"

    assert treesitterNodes[1].name == "get_file_extension"

    assert (
        treesitterNodes[0].doc_comment
        == """\"\"\"
    Returns the corresponding programming language based on the given file extension.

    Args:
        file_extension (str): The file extension of the programming file.

    Returns:
        Language: The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
    \"\"\""""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """def get_programming_language(file_extension: str) -> Language:
    \"\"\"
    Returns the corresponding programming language based on the given file extension.

    Args:
        file_extension (str): The file extension of the programming file.

    Returns:
        Language: The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
    \"\"\"
    language_mapping = {
        ".py": Language.PYTHON,
        ".js": Language.JAVASCRIPT,
        ".ts": Language.TYPESCRIPT,
        ".java": Language.JAVA,
        ".kt": Language.KOTLIN,
        ".lua": Language.LUA,
    }
    return language_mapping.get(file_extension, Language.UNKNOWN)"""
    )


@pytest.mark.usefixtures("java_code_fixture")
def test_java_qery(java_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.JAVA)
    treesitterNodes: list[TreesitterMethodNode] = treesitter.parse(
        java_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "getProgrammingLanguage"

    assert treesitterNodes[1].name == "getFileExtension"

    assert (
        treesitterNodes[0].doc_comment
        == """/**
     * Gets the corresponding programming language based on the given file extension.
     *
     * @param fileExtension The file extension of the programming file.
     * @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
     */"""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """public static Language getProgrammingLanguage(String fileExtension) {
        Map<String, Language> languageMapping = new HashMap<>();
        languageMapping.put(".py", Language.PYTHON);
        languageMapping.put(".js", Language.JAVASCRIPT);
        languageMapping.put(".ts", Language.TYPESCRIPT);
        languageMapping.put(".java", Language.JAVA);
        languageMapping.put(".kt", Language.KOTLIN);
        languageMapping.put(".lua", Language.LUA);

        // Return the corresponding language if it exists in the mapping, otherwise return Language.UNKNOWN 
        return languageMapping.getOrDefault(fileExtension, Language.UNKNOWN);
    }"""
    )


@pytest.mark.usefixtures("javascript_code_fixture")
def test_javascript_qery(javascript_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.JAVASCRIPT)
    treesitterNodes: list[TreesitterMethodNode] = treesitter.parse(
        javascript_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "getProgrammingLanguage"

    assert treesitterNodes[1].name == "getFileExtension"

    assert (
        treesitterNodes[0].doc_comment
        == """/**
 * Returns the corresponding programming language based on the given file extension.
 *
 * @param {string} fileExtension - The file extension of the programming file.
 * @returns {string} The corresponding programming language if it exists in the mapping, otherwise 'Unknown'.
 */"""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """function getProgrammingLanguage(fileExtension) {
    const languageMapping = {
        ".py": Language.PYTHON,
        ".js": Language.JAVASCRIPT,
        ".ts": Language.TYPESCRIPT,
        ".java": Language.JAVA,
        ".kt": Language.KOTLIN,
        ".lua": Language.LUA,
    };

    // Return the corresponding language if it exists in the mapping, otherwise return 'Unknown'
    return languageMapping[fileExtension] || Language.UNKNOWN;
}"""
    )


@pytest.mark.usefixtures("typescript_code_fixture")
def test_typescript_qery(typescript_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.TYPESCRIPT)
    treesitterNodes: list[TreesitterMethodNode] = treesitter.parse(
        typescript_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "getProgrammingLanguage"

    assert treesitterNodes[1].name == "getFileExtension"

    assert (
        treesitterNodes[0].doc_comment
        == """/**
 * Returns the corresponding programming language based on the given file extension.
 *
 * @param {string} fileExtension - The file extension of the programming file.
 * @returns {Language} The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
 */"""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """function getProgrammingLanguage(fileExtension: string): Language {
    const languageMapping: { [key: string]: Language } = {
        ".py": Language.PYTHON,
        ".js": Language.JAVASCRIPT,
        ".ts": Language.TYPESCRIPT,
        ".java": Language.JAVA,
        ".kt": Language.KOTLIN,
        ".lua": Language.LUA,
    };

    // Return the corresponding language if it exists in the mapping, otherwise return Language.UNKNOWN
    return languageMapping[fileExtension] || Language.UNKNOWN;
}"""
    )


@pytest.mark.usefixtures("rust_code_fixture")
def test_rust_qery(rust_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.RUST)
    treesitterNodes: list[TreesitterMethodNode] = treesitter.parse(
        rust_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "get_programming_language"

    assert treesitterNodes[1].name == "get_file_extension"

    assert (
        treesitterNodes[0].doc_comment
        == """/// Returns the corresponding programming language based on the given file extension.
///
/// # Arguments
///
/// * `file_extension` - The file extension of the programming file.
///
/// # Returns
///
/// * The corresponding programming language if it exists in the mapping, otherwise Language::UNKNOWN.
///
/// # Example
///
/// ```
/// let file_extension = ".py";
/// let language = get_programming_language(file_extension);
/// assert_eq!(language, Language::PYTHON);
/// ```"""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """fn get_programming_language(file_extension: &str) -> Language {
    let language_mapping: std::collections::HashMap<&str, Language> = [
        (".py", Language::PYTHON),
        (".js", Language::JAVASCRIPT),
        (".ts", Language::TYPESCRIPT),
        (".java", Language::JAVA),
        (".kt", Language::KOTLIN),
        (".lua", Language::LUA),
    ]
    .iter()
    .cloned()
    .collect();

    // Return the corresponding language if it exists in the mapping, otherwise return Language::UNKNOWN
    *language_mapping.get(file_extension).unwrap_or(&Language::UNKNOWN)
}"""
    )


@pytest.mark.usefixtures("kotlin_code_fixture")
def test_kotlin_qery(kotlin_code_fixture):
    tree_sitter = Treesitter.create_treesitter(Language.KOTLIN)
    treesitterNodes: list[TreesitterMethodNode] = tree_sitter.parse(
        kotlin_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "getProgrammingLanguage"

    assert treesitterNodes[1].name == "getFileExtension"

    assert (
        treesitterNodes[0].doc_comment
        == """/**
 * Gets the corresponding programming language based on the given file extension.
 *
 * @param fileExtension The file extension of the programming file.
 * @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
 */"""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """fun getProgrammingLanguage(fileExtension: String): Language {
    val languageMapping = HashMap<String, Language>()
    languageMapping[".py"] = Language.PYTHON
    languageMapping[".js"] = Language.JAVASCRIPT
    languageMapping[".ts"] = Language.TYPESCRIPT
    languageMapping[".java"] = Language.JAVA
    languageMapping[".kt"] = Language.KOTLIN
    languageMapping[".lua"] = Language.LUA

    // Return the corresponding language if it exists in the mapping, otherwise return Language.UNKNOWN
    return languageMapping.getOrDefault(fileExtension, Language.UNKNOWN)
}"""
    )


@pytest.mark.usefixtures("go_code_fixture")
def test_go_qery(go_code_fixture):
    tree_sitter = Treesitter.create_treesitter(Language.GO)
    treesitterNodes: list[TreesitterMethodNode] = tree_sitter.parse(
        go_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == "getProgrammingLanguage"

    assert treesitterNodes[1].name == "getFileExtension"

    assert (
        treesitterNodes[0].doc_comment
        == """// getProgrammingLanguage gets the corresponding programming language based on the given file extension."""
    )

    assert treesitterNodes[1].doc_comment is None

    assert (
        treesitterNodes[0].method_source_code
        == """func getProgrammingLanguage(fileExtension string) Language {
	languageMapping := map[string]Language{
		".py":     PYTHON,
		".js":     JAVASCRIPT,
		".ts":     TYPESCRIPT,
		".java":   JAVA,
		".kt":     KOTLIN,
		".lua":    LUA,
	}

	language, exists := languageMapping[fileExtension]
	if exists {
		return language
	}
	// TODO: Add more languages
	return UNKNOWN
}"""
    )
