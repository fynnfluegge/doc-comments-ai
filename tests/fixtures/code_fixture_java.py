import pytest


@pytest.fixture
def java_code_fixture():
    return """
import java.util.HashMap;
import java.util.Map;

/**
 * A class for detecting the programming language based on file extension.
 */
public class LanguageDetection {

    /**
     * Enumeration representing various programming languages.
     */
    enum Language {
        PYTHON, JAVASCRIPT, TYPESCRIPT, JAVA, KOTLIN, LUA, UNKNOWN
    }

    /**
     * Gets the corresponding programming language based on the given file extension.
     *
     * @param fileExtension The file extension of the programming file.
     * @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
     */
    public static Language getProgrammingLanguage(String fileExtension) {
        Map<String, Language> languageMapping = new HashMap<>();
        languageMapping.put(".py", Language.PYTHON);
        languageMapping.put(".js", Language.JAVASCRIPT);
        languageMapping.put(".ts", Language.TYPESCRIPT);
        languageMapping.put(".java", Language.JAVA);
        languageMapping.put(".kt", Language.KOTLIN);
        languageMapping.put(".lua", Language.LUA);

        // Return the corresponding language if it exists in the mapping, otherwise return Language.UNKNOWN
        return languageMapping.getOrDefault(fileExtension, Language.UNKNOWN);
    }

    public static String getFileExtension(String fileName) {
        return fileName.substring(fileName.lastIndexOf('.'));
    }
}
"""
