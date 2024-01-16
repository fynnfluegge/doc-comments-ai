import pytest


@pytest.fixture
def csharp_code_fixture():
    return """
using System;
using System.Collections.Generic;

/// <summary>
/// A class for detecting the programming language based on file extension.
/// </summary>
public class LanguageDetection
{
    /// <summary>
    /// Enumeration representing various programming languages.
    /// </summary>
    public enum Language
    {
        PYTHON, JAVASCRIPT, TYPESCRIPT, JAVA, KOTLIN, LUA, UNKNOWN
    }

    /// <summary>
    /// Gets the corresponding programming language based on the given file extension.
    /// </summary>
    /// <param name="fileExtension">The file extension of the programming file.</param>
    /// <returns>The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.</returns>
    public static Language GetProgrammingLanguage(string fileExtension)
    {
        Dictionary<string, Language> languageMapping = new Dictionary<string, Language>();
        languageMapping[".py"] = Language.PYTHON;
        languageMapping[".js"] = Language.JAVASCRIPT;
        languageMapping[".ts"] = Language.TYPESCRIPT;
        languageMapping[".java"] = Language.JAVA;
        languageMapping[".kt"] = Language.KOTLIN;
        languageMapping[".lua"] = Language.LUA;

        // Return the corresponding language if it exists in the mapping, otherwise return Language.UNKNOWN
        return languageMapping.TryGetValue(fileExtension, out var language) ? language : Language.UNKNOWN;
    }

    public static string GetFileExtension(string fileName)
    {
        int dotPosition = fileName.LastIndexOf('.');
        if (dotPosition != -1)
        {
            return fileName.Substring(dotPosition);
        }
        return "";
    }
"""
