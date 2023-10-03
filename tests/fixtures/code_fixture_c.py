import pytest


@pytest.fixture
def c_code_fixture():
    return """
#include <stdio.h>
#include <string.h>

// Enumeration representing various programming languages.
enum Language {
    PYTHON, JAVASCRIPT, TYPESCRIPT, JAVA, KOTLIN, LUA, UNKNOWN
};

/**
 * Get the corresponding programming language based on the given file extension.
 *
 * @param fileExtension The file extension of the programming file.
 * @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
 */
enum Language getProgrammingLanguage(const char *fileExtension) {
    // Define a mapping of file extensions to programming languages.
    struct LanguageMapping {
        const char *extension;
        enum Language language;
    };
    
    struct LanguageMapping languageMapping[] = {
        {".py", PYTHON},
        {".js", JAVASCRIPT},
        {".ts", TYPESCRIPT},
        {".java", JAVA},
        {".kt", KOTLIN},
        {".lua", LUA},
    };
    
    int numMappings = sizeof(languageMapping) / sizeof(languageMapping[0]);
    
    // Iterate through the mappings and check if the file extension matches.
    for (int i = 0; i < numMappings; i++) {
        if (strcmp(fileExtension, languageMapping[i].extension) == 0) {
            return languageMapping[i].language;
        }
    }
    
    return UNKNOWN;
}

const char *getFileExtension(const char *fileName) {
    const char *dot = strrchr(fileName, '.');
    if (!dot || dot == fileName) {
        return ""; // No file extension found.
    }
    return dot;
}
"""
