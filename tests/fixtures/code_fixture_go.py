import pytest


@pytest.fixture
def go_code_fixture():
    return """
// getProgrammingLanguage gets the corresponding programming language based on the given file extension.
func getProgrammingLanguage(fileExtension string) Language {
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
	return UNKNOWN
}

func getFileExtension(fileName string) string {
	lastDotIndex := strings.LastIndex(fileName, ".")
	if lastDotIndex != -1 {
		return fileName[lastDotIndex:]
	}
	return ""
}
"""
