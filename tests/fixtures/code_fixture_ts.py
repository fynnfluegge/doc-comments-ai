import pytest


@pytest.fixture
def typescript_code_fixture():
    return """
/**
 * Returns the corresponding programming language based on the given file extension.
 *
 * @param {string} fileExtension - The file extension of the programming file.
 * @returns {Language} The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
 */
function getProgrammingLanguage(fileExtension: string): Language {
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
}

function getFileExtension(fileName: string): string {
    // This code extracts the file extension by finding the last dot in the file name.
    const lastDotIndex = fileName.lastIndexOf(".");
    if (lastDotIndex !== -1) {
        return fileName.slice(lastDotIndex);
    } else {
        return "";
    }
}
"""
