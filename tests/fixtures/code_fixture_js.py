import pytest


@pytest.fixture
def javascript_code_fixture():
    return """
/**
 * Returns the corresponding programming language based on the given file extension.
 *
 * @param {string} fileExtension - The file extension of the programming file.
 * @returns {string} The corresponding programming language if it exists in the mapping, otherwise 'Unknown'.
 */
function getProgrammingLanguage(fileExtension) {
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
}

function getFileExtension(fileName) {
    return fileName.slice(((fileName.lastIndexOf(".") - 1) >>> 0) + 2);
}
    """
