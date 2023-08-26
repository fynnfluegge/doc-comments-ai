import pytest


@pytest.fixture
def kotlin_code_fixture():
    return """
/**
 * Gets the corresponding programming language based on the given file extension.
 *
 * @param fileExtension The file extension of the programming file.
 * @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
 */
fun getProgrammingLanguage(fileExtension: String): Language {
    val languageMapping = HashMap<String, Language>()
    languageMapping[".py"] = Language.PYTHON
    languageMapping[".js"] = Language.JAVASCRIPT
    languageMapping[".ts"] = Language.TYPESCRIPT
    languageMapping[".java"] = Language.JAVA
    languageMapping[".kt"] = Language.KOTLIN
    languageMapping[".lua"] = Language.LUA

    return languageMapping.getOrDefault(fileExtension, Language.UNKNOWN)
}

fun getFileExtension(fileName: String): String {
    return fileName.substring(fileName.lastIndexOf('.'))
}
    """
