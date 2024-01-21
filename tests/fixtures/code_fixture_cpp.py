import pytest


@pytest.fixture
def cpp_code_fixture():
    return """
#include <iostream>
#include <string>
#include <unordered_map>

/**
 * Enumeration representing various programming languages.
 */
enum class Language {
    PYTHON, JAVASCRIPT, TYPESCRIPT, JAVA, KOTLIN, LUA, UNKNOWN
};

/**
 * A function to get the corresponding programming language based on the given file extension.
 *
 * @param fileExtension The file extension of the programming file.
 * @return The corresponding programming language if it exists in the mapping, otherwise Language::UNKNOWN.
 */
Language getProgrammingLanguage(const std::string& fileExtension) {
    std::unordered_map<std::string, Language> languageMapping;
    languageMapping[".py"] = Language::PYTHON;
    languageMapping[".js"] = Language::JAVASCRIPT;
    languageMapping[".ts"] = Language::TYPESCRIPT;
    languageMapping[".java"] = Language::JAVA;
    languageMapping[".kt"] = Language::KOTLIN;
    languageMapping[".lua"] = Language::LUA;

    // Return the corresponding language if it exists in the mapping, otherwise return Language::UNKNOWN
    auto it = languageMapping.find(fileExtension);
    if (it != languageMapping.end()) {
        return it->second;
    }
    return Language::UNKNOWN;
}

std::string getFileExtension(const std::string& fileName) {
    size_t dotPos = fileName.find_last_of('.');
    if (dotPos != std::string::npos) {
        return fileName.substr(dotPos);
    }
    return "";
}
"""


@pytest.fixture
def cpp_code_fixture_no_do_comment():
    return """
#include <iostream>
#include <string>
#include <unordered_map>

/**
 * Enumeration representing various programming languages.
 */
enum class Language {
    PYTHON, JAVASCRIPT, TYPESCRIPT, JAVA, KOTLIN, LUA, UNKNOWN
};

Language getProgrammingLanguage(const std::string& fileExtension) {
    std::unordered_map<std::string, Language> languageMapping;
    languageMapping[".py"] = Language::PYTHON;
    languageMapping[".js"] = Language::JAVASCRIPT;
    languageMapping[".ts"] = Language::TYPESCRIPT;
    languageMapping[".java"] = Language::JAVA;
    languageMapping[".kt"] = Language::KOTLIN;
    languageMapping[".lua"] = Language::LUA;

    // Return the corresponding language if it exists in the mapping, otherwise return Language::UNKNOWN
    auto it = languageMapping.find(fileExtension);
    if (it != languageMapping.end()) {
        return it->second;
    }
    return Language::UNKNOWN;
}

std::string getFileExtension(const std::string& fileName) {
    size_t dotPos = fileName.find_last_of('.');
    if (dotPos != std::string::npos) {
        return fileName.substr(dotPos);
    }
    return "";
}
"""
