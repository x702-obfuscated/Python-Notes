# `Python Regular Expressions`

*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

<br>

___

<br>

Covered in this file:
1. [`Regular Expression Defined`](#regular-expression-defined)
1. [`Regex Symbols`](#regex-symbols)
1. [`Regex patterns`](#regex-patterns)
1. [`The re module`](#the-re-module)
    1. [`re methods`](#re-methods)
    1. [`Special Flags`](#special-flags)



<br>

___

<br>

# `Regular Expression Defined`

`Regular expressions` (often shortened to `regex` or `regexp`) are sequences of characters that define search patterns, typically used for pattern matching within strings. They provide a powerful way to search, replace, and validate text by specifying flexible search patterns. 

<br>

[Back to Top](#python-regular-expressions)

___

<br>

# `Regex Symbols`

| Symbol| Description | Example|
|:-:|-|-|
| `.`            | Matches any character except a newline. With the `DOTALL` flag, it matches any character including a newline. | `(?s:.)` matches any character.      |
| `^`            | Matches the start of the string. In `MULTILINE` mode, also matches immediately after each newline. | `^foo` matches "foo" at the start.  |
| `$`            | Matches the end of the string or just before the newline at the end of the string. In `MULTILINE` mode, matches before a newline. | `foo$` matches "foo" but not "foobar". |
| `*`            | Matches 0 or more repetitions of the preceding RE.                                                 | `ab*` matches "a", "ab", or "a" followed by any number of "b"s. |
| `+`            | Matches 1 or more repetitions of the preceding RE.                                                | `ab+` matches "a" followed by any non-zero number of "b"s. |
| `?`            | Matches 0 or 1 repetitions of the preceding RE.                                                   | `ab?` matches either "a" or "ab".   |
| `*?`, `+?`, `??` | Non-greedy versions of `*`, `+`, and `?`. These match as few characters as possible.             | `.*?` matches the smallest possible portion. |
| `*+`, `++`, `?+` | Possessive quantifiers; these do not allow backtracking.                                         | `a*+a` will fail to match "aaaa".    |
| `{m}`          | Matches exactly `m` copies of the previous RE.                                                   | `a{6}` matches exactly six "a"s.     |
| `{m,n}`        | Matches between `m` and `n` repetitions of the preceding RE.                                       | `a{3,5}` matches from 3 to 5 "a"s.   |
| `{m,n}?`       | Non-greedy version of `{m,n}`, matching as few repetitions as possible.                           | `a{3,5}?` matches the smallest number of "a"s. |
| `{m,n}+`       | Possessive version of `{m,n}`, which does not allow backtracking.                                 | `a{3,5}+aa` will fail if there are fewer than 7 "a"s. |
| `\`            | Escapes special characters or denotes special sequences.                                           | `\$` matches a literal dollar sign.  |
| `[]`           | Denotes a set of characters.                                                                         | `[a-z]` matches any lowercase letter. |
| `\|`            | Alternation, matches either the pattern before or after the `\|`.                                   | `A\|B` matches "A" or "B".            |
| `(...)`        | Groups patterns.                                                                                    | `(abc)` matches "abc".               |
| `(?:...)`      | Non-capturing group.                                                                                | `(?:abc)` matches "abc" without storing the match. |
| `(?P<name>...)`| Named capturing group.                                                                             | `(?P<quote>['"]).*?(?P=quote)` matches quoted strings. |
| `(?=...)`      | Positive lookahead.                                                                                 | `Isaac (?=Asimov)` matches "Isaac" only if followed by "Asimov". |
| `(?!...)`      | Negative lookahead.                                                                                 | `Isaac (?!Asimov)` matches "Isaac" only if not followed by "Asimov". |
| `(?<=...)`     | Positive lookbehind.                                                                                | `(?<=abc)def` matches "def" if preceded by "abc". |
| `(?<!...)`     | Negative lookbehind.                                                                                | `(?<!abc)def` matches "def" if not preceded by "abc". |
| `\A`           | Matches only at the start of the string.                                                           | `\Afoo` matches "foo" only at the beginning. |
| `\Z`           | Matches only at the end of the string.                                                             | `foo\Z` matches "foo" only at the end. |
| `\d`           | Matches any Unicode decimal digit (equivalent to `[0-9]`).                                       | `\d{3}` matches any three digits.     |
| `\D`           | Matches any character that is not a decimal digit.                                                 | `\D` matches any non-digit character. |
| `\s`           | Matches any whitespace character (spaces, tabs, etc.).                                             | `\s+` matches one or more whitespace characters. |
| `\S`           | Matches any character that is not whitespace.                                                       | `\S` matches any non-whitespace character. |
| `\w`           | Matches any word character (alphanumeric or underscore).                                           | `\w+` matches one or more word characters. |
| `\W`           | Matches any character that is not a word character.                                                | `\W` matches any non-word character.  |
| `\b`           | Matches a word boundary (between `\w` and `\W` characters).                                        | `\bword\b` matches "word" but not "sword". |
| `\B`           | Matches a position that is not a word boundary.                                                     | `\Bword\B` matches "word" in "sword". |




<br>

[Back to Top](#python-regular-expressions)

___

<br>

# `Regex Patterns`

When using regular expressions in python to parse text, raw strings prevent certain escape character issues.
* Use the prefix `r` to set a raw string. Raw strings are interpreted literally ignoring the backslash special meaning. 

The string that identifies the regular expression to search for is called a `pattern`



<br>


Regex Pattern Examples:
```python
wildcard = r"."  
# Matches any single character except newline.
```
```python
atoz = r"[a-z]"  
# Matches any single lowercase letter from 'a' to 'z'.
```
```python
AtoZ = r"[A-Z]"  
# Matches any single uppercase letter from 'A' to 'Z'.
```
```python
digits = r"[0-9]"  
# Matches any single digit from '0' to '9'.
```
```python
not_inbrackets = r"[^aeiou]"  
# Matches any character that is NOT a vowel (negated character class).
```
```python
zero_more = r"a*"  
# Matches 0 or more occurrences of the character 'a'.
```
```python
zero_more = r"abc*"  
# Matches the string 'ab' followed by 0 or more occurrences of 'c' (i.e., 'ab', 'abc', 'abcc', etc.).
```
```python
one_more = r"a+"  
# Matches 1 or more occurrences of the character 'a'.
```
```python
one_more = r"abc+"  
# Matches the string 'ab' followed by 1 or more occurrences of 'c' (i.e., 'abc', 'abcc', etc.).
```
```python
zero_one = r"a?"  
# Matches 0 or 1 occurrence of the character 'a' (optional 'a').
```
```python
zero_one = r"abc?"  
# Matches the string 'ab' followed by 0 or 1 occurrence of 'c' (i.e., 'ab' or 'abc').
```
```python
grouping = r"(\w+)\s+(\w+),\s+(\d+)\s+(\w+\s+\w+\.)\s+(\w+),\s+(\w+)"  
# Matches a pattern with 6 groups: 
# 1) a word, 
# 2) a second word, 
# 3) a number, 
# 4) two words ending in a period, 
# 5) a word, 
# 6) another word. 
# This could match patterns like "John Doe, 32 Elm St. City, State".
```
```python
match_or = r"com|net|org"  
# Matches either 'com', 'net', or 'org' (logical OR).
```
```python
literal = r"\.\?"  
# Matches a literal period followed by a question mark (i.e., ".?").
```
```python
beginning = r"^starting"  
# Matches the string 'starting' only if it appears at the beginning of a line.
```
```python
ending = r"$ending"  
# Matches the string 'ending' only if it appears at the end of a line.
```
```python
escape_backslash = r"C:\\"
# Matches the string 'C:\', escaping the backslash so that it is treated as a literal character.
```
```python
n = 5
n_occurences = rf"a{n}"
n_occurences = r"a{5}"  
# Matches exactly 5 occurrences of the character 'a' (i.e., 'aaaaa').
```

<br>

[Back to Top](#python-regular-expressions)

___

<br>


# `The re module`
The `re` module in Python provides support for working with regular expressions (regex). It allows you to search for patterns in strings, match text, and manipulate string data using regular expressions. The module offers a range of functions to work with regex for tasks like searching, splitting, replacing, and more.

<br>

re module official Python documentation: [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)

<br>

## `re methods`

`re.compile()` is used to compile a regular expression pattern into a regex object, which can then be used to perform matches against strings. This is useful for optimizing performance, especially when the same regex pattern will be used multiple times.
```python
import re

pattern = re.compile(r'[a-z]')
```

<br>


`re.match()` Tries to match a pattern at the beginning of a string. If the pattern is found at the start, it returns a match object; otherwise, it returns None.
```python
import re
result = re.match(r'Hello', 'Hello, world!')
print(result)  # Output: <re.Match object; span=(0, 5), match='Hello'>

result = re.match(r'Goodbye', 'Hello, world!')
print(result)  # Output: None
```

<br>

`re.search()` Searches the entire string for the first occurrence of a pattern. Returns a match object if the pattern is found anywhere in the string, otherwise None

```python
import re

result = re.search(r'world', 'Hello, world!')
print(result)  # Output: <re.Match object; span=(7, 12), match='world'>

result = re.search(r'goodbye', 'Hello, world!')
print(result)  # Output: None
```

<br>

`re.group()`, `re.start()`, `re.end()`, `re.span()`


`re.group()`: Returns the part of the string where there was a match.

`re.start()` and `re.end()`: Return the starting and ending positions of the match.

`re.span()`: Returns a tuple with the start and end positions of the match.
```python
import re

pattern = r'\d+'
text = 'There are 24 apples.'
match = re.search(pattern, text)
if match:
    print(match.group())  # '24'
    print(match.start())  # 10
    print(match.end())    # 12
    print(match.span())   # (10, 12)
```
<br>

`re.findall()` Returns a list of all non-overlapping matches of the pattern in the string.
```python
import re

result = re.findall(r'\d+', 'There are 24 apples, 15 oranges, and 9 bananas.')
print(result)  # Outputs: ['24', '15', '9']
```

<br>

`re.finditer()` Returns an iterator yielding match objects for all non-overlapping matches of the pattern.
```python
import re

result = re.finditer(r'\d+', 'There are 24 apples, 15 oranges, and 9 bananas.')
for match in result:
    print(match.group())  

# Output: 
# 24
# 15
# 9
```

<br>

`re.sub()` Replaces occurrences of the pattern with a replacement string.
Useful for replacing patterns in strings
```python
import re

result = re.sub(r'\d+', 'many', 'There are 24 apples and 9 bananas.')
print(result)  # Output: There are many apples and many bananas.
```

<br>

`re.split()` Splits a string by the occurrences of a pattern and returns a list of substrings.
```python
import re

result = re.split(r'\s+', 'Split this string on spaces.')
print(result)  # Output: ['Split', 'this', 'string', 'on', 'spaces.']
```

<br>

Searching and matching example:
```python
import re

text = "userame@email.com"

pattern = r"(\w+)[@](\w+)[\.](com|net|org)"
match = re.search(pattern,text)

if match.group() == text:
    print("Valid Email : ", match.group())
else:
    print("Invalid Email")
```
<br>

[Back to Top](#python-regular-expressions)

___

<br>

## Special Flags

`re.IGNORECASE (re.I)`: Makes the pattern matching case-insensitive.

```python
import re

pattern_i = re.compile(r'hello', re.IGNORECASE)
text_i = 'Hello World'
match_i = pattern_i.search(text_i)
print(f"re.IGNORECASE: {match_i.group() if match_i else 'No match'}")  # Output: Hello
```

<br>

`re.MULTILINE (re.M)`: Allows `^` and `$` to match the start and end of each line within a string, not just the start and end of the string.

```python
import re

pattern_m = re.compile(r'^foo', re.MULTILINE)
text_m = 'foo\nbar\nfoo'
matches_m = pattern_m.findall(text_m)
print(f"re.MULTILINE: {matches_m}")  # Output: ['foo', 'foo']
```

<br>

`re.DOTALL (re.S)`: Allows the `.` character to match newlines as well.
```python
import re

pattern_s = re.compile(r'foo.bar', re.DOTALL)
text_s = 'foo\nbar'
match_s = pattern_s.search(text_s)
print(f"re.DOTALL: {match_s.group() if match_s else 'No match'}")  # Output: foo\nbar
```

<br>

[Back to Top](#python-regular-expressions)

___

<br>

*Created and maintained by Mr. Merritt*

