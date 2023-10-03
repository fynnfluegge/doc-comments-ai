import pytest


@pytest.fixture
def rust_code_fixture():
    return """
/// Returns the corresponding programming language based on the given file extension.
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
/// ```
fn get_programming_language(file_extension: &str) -> Language {
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
}

fn get_file_extension(file_name: &str) -> &str {
    if let Some(last_dot_index) = file_name.rfind('.') {
        &file_name[last_dot_index..]
    } else {
        ""
    }
}
"""
