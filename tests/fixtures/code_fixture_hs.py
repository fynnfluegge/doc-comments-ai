import pytest


@pytest.fixture
def haskell_code_fixture():
    return """
module Test where

import Prelude
import qualified Data.HashMap.String as HM

-- Enumeration representing various programming languages.
data Language = PYTHON | JAVASCRIPT | TYPESCRIPT | JAVA | KOTLIN | LUA | UNKNOWN

{-
  Get the corresponding programming language based on the given file extension.

  @param fileExtension The file extension of the programming file.
  @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
-}
getProgrammingLanguage :: String -> Language
getProgrammingLanguage fileExtension =
    let languageMapping = HM.insert ".py" PYTHON
                          $ HM.insert ".js" JAVASCRIPT
                          $ HM.insert ".ts" TYPESCRIPT
                          $ HM.insert ".java" JAVA
                          $ HM.insert ".kt" KOTLIN
                          $ HM.singleton ".lua" LUA
    in case lookup fileExtension languageMapping of
         Just v -> v
         Nothing -> UNKNOWN
getFileExtension :: String -> String
getFileExtension fileName =
    let dot = dropWhile ((\=) '.') fileName
    in dot
"""
