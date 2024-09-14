# `Python Strings`

Covered in this file:
1. [`Defining Characters`](#defining-characters)
1. [`Special Characters`](#special-characters)
    1. [`Special Character in Python`](#special-characters-in-python)
    1. [`Escape Character`](#escape-character)
    1. [`ASCII Linefeed (Newline Character)`](#ascii-linefeed-newline-character)
    1. [`Backslash Character`](#backslash-character)
    1. [`Quotes: Single and Double`](#quotes-single-and-double)
    1. [`UTF-8 Encoding (1 byte) Hexadecimal Bytes`](#utf-8-encoding-1-byte-hexadecimal-bytes)
    1. [`UTF-16 Encoding (2 bytes)`](#utf-16-encoding-2-bytes)
    1. [`UTF-32 Encoding (4 bytes)`](#utf-32-encoding-4-bytes)
    1. [`Tab Character`](#tab-character)
    1. [`Carriage Return Character`](#carriage-return-character)
    1. [`Backspace Character`](#backslash-character)
1. [`Converting Between Character Encodings`](#converting-between-character-encodings)
    1. [`Convert to an Integer int()`](#convert-to-an-integer-int)
    1. [`Convert to Binary bin()`](#convert-to-binary-bin)
    1. [`Convert From Character to Binary`](#convert-from-a-character-to-binary)
    1. [`Convert to Hexadecimal hex()`](#convert-to-hexadecimal-hex)
    1. [`Convert from a Character to Hexadecimal`](#convert-from-a-character-to-hexadecimal)
    1. [`Convert to a String`](#convert-to-a-string)
    1. [`Convert from a Character to an Integer ord()`](#convert-from-an-integer-to-a-character-chr)
1. [`Defining a String`](#defining-a-string)
1. [`Multiline Strings`](#multiline-strings)
1. [`String Concatenation`](#string-concatenation)
    1. [`Manually Concatenate with + `](#manually-concatenate)
    1. [`Compound Concatenate and Assign String += `](#compound-concatenate-and-assign-strings)
1. [`String Duplication`](#string-duplication)
    1. [`Compound Duplicate and Assign Strings *= `](#compound-duplicate-and-assign-strings)
1. [`String Comparision`](#string-comparision)
    1. [`Equality Comparision == `](#equality-comparision)
    1. [`NOT Equal != `](#not-equal)
    1. [`Greater Than > and Less Than < `](#greater-than-and-less-than)
    1. [`Length Comparision`](#length-comparision)
1. [`String Indexing`](#string-indexing)
    1. [`Why do indexes start at 0?`](#why-do-indexes-start-at-0)
    1. [`Accessing Characters in a String`](#accessing-characters-in-a-string)
    1. [`Changing Characters in a String`](#changing-characters-in-a-string)
1. [`Substrings: Slicing`](#string-slicing)
    1. [`Ascending Slices`](#ascending-slices)
    1. [`Descending Slices`](#descending-slices)
1. [`Built-in String Function Calls`](#built-in-string-function-calls)
1. [`Built-in String Method Calls`](#built-in-string-method-calls)
1. [`Format Strings: f-strings`](#format-strings-f-strings)
    1. [`Inserting Variables Directly Into Strings`](#inserting-variables-directly-into-strings)
    1. [`Formatting Numbers for Output`](#formatting-numbers-for-output)
    1. [`Formatting Expression for Output`](#formatting-expressions-for-output)
    1. [`Padding and Alignment`](#padding-and-alignment)
    1. [`Removing quotes from output`](#removing-quotes-from-output)
1. [`Raw Strings`](#raw-strings)
1. [`Bytes Strings`](#bytes-strings)
1. [`Appendix`](#appendix)

<br>

___

<br>

# `Defining Characters`

`Characters:`  
Basically: a basic unit of information that represents a letter, number, symbol, or control code 


Specifically: a binary value mapped to a specific symbol as defined by ASCII or UTF

<br>

`American Standard Code for Information Interchange (ASCII)`  
ASCII is a character encoding standard used to represent text in computers and other devices that use text. ACSII defines a mapping of binary values to human readable characters. 
> * defines a set of 128 characters, where each character is represented by a unique 7-bit binary number.
> * forms the basis for more extensive character encoding schemes like Unicode.

<br>

`Unicode`   
Unicode is a universal character encoding standard designed to represent and handle text in most of the world's writing systems.
> * The Unicode standard assigns a unique code point to every character, regardless of platform, program, or language
> * These code points are hexadeximal values prefixed with 'U+'

<br>

`Unicode Transformation Format (UTF)`  
UTF is a family of character encoding schemes used to represent Unicode characters. 
> * The most common encodings are UTF-8, UTF-16, and UTF-32. These encoding transform unicode code points into sequences of bytes.

`.py files in Python3 are encoded with UTF-8 by default`

<br>

*NOTE*: 
> * 1 byte equals 8 bits
> * The prefix 0b indicates a binary value
> * The prefix 0x indicates a hexadecimal value

<br>

|Encoding Scheme|Size|Range|Character|Encoding|Unicode Code Point|
|:-:|:-:|:-:|:-:|:-:|:-:|
|ASCII|7 bits|128 possible values| "a"|0b01100001| U+0065 |
|UTF-8|1 to 4 bytes|1,112,064 possible values| "a"|0x65|U+0065|
|UTF-16|2 or 4 bytes|1,112,064 possible values| "a"|0x0065|U+0065|
|UTF-32|4 bytes|4,294,967,296 possible values| "a" |0x00000065|U+0065|

For more on Unicode and character encodings: [https://home.unicode.org/](https://home.unicode.org/)

<br>

## Character Examples:
```python
"a"
"b"
"@"
"$"
"1"
"0"
```

`7-bit American Standard Code for Information Interchange (ASCII)`  
7 bit ASCII defines 128 characters including all alphanumeric characters
> * In many cases this is the only table we will need to interact with characters

*NOTE*: 
> You may notice that this table does not include all 128 characters, this is because the omitted codes are control codes and not currently relevant.

|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|:-:|:-:|:-:|:-:|:-:|:-:|
| SPACE |U+0020|32|0x20|0b100000|0o40|
|!|U+0021|33|0x21|0b100001|0o41|
|"|U+0022|34|0x22|0b100010|0o42|
|#|U+0023|35|0x23|0b100011|0o43|
|$|U+0024|36|0x24|0b100100|0o44|
|%|U+0025|37|0x25|0b100101|0o45|
|&|U+0026|38|0x26|0b100110|0o46|
|'|U+0027|39|0x27|0b100111|0o47|
|(|U+0028|40|0x28|0b101000|0o50|
|)|U+0029|41|0x29|0b101001|0o51|
|*|U+002a|42|0x2a|0b101010|0o52|
|+|U+002b|43|0x2b|0b101011|0o53|
|,|U+002c|44|0x2c|0b101100|0o54|
|-|U+002d|45|0x2d|0b101101|0o55|
|.|U+002e|46|0x2e|0b101110|0o56|
|/|U+002f|47|0x2f|0b101111|0o57|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|0|U+0030|48|0x30|0b110000|0o60|
|1|U+0031|49|0x31|0b110001|0o61|
|2|U+0032|50|0x32|0b110010|0o62|
|3|U+0033|51|0x33|0b110011|0o63|
|4|U+0034|52|0x34|0b110100|0o64|
|5|U+0035|53|0x35|0b110101|0o65|
|6|U+0036|54|0x36|0b110110|0o66|
|7|U+0037|55|0x37|0b110111|0o67|
|8|U+0038|56|0x38|0b111000|0o70|
|9|U+0039|57|0x39|0b111001|0o71|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|:|U+003a|58|0x3a|0b111010|0o72|
|;|U+003b|59|0x3b|0b111011|0o73|
|<|U+003c|60|0x3c|0b111100|0o74|
|=|U+003d|61|0x3d|0b111101|0o75|
|>|U+003e|62|0x3e|0b111110|0o76|
|?|U+003f|63|0x3f|0b111111|0o77|
|@|U+0040|64|0x40|0b1000000|0o100|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|A|U+0041|65|0x41|0b1000001|0o101|
|B|U+0042|66|0x42|0b1000010|0o102|
|C|U+0043|67|0x43|0b1000011|0o103|
|D|U+0044|68|0x44|0b1000100|0o104|
|E|U+0045|69|0x45|0b1000101|0o105|
|F|U+0046|70|0x46|0b1000110|0o106|
|G|U+0047|71|0x47|0b1000111|0o107|
|H|U+0048|72|0x48|0b1001000|0o110|
|I|U+0049|73|0x49|0b1001001|0o111|
|J|U+004a|74|0x4a|0b1001010|0o112|
|K|U+004b|75|0x4b|0b1001011|0o113|
|L|U+004c|76|0x4c|0b1001100|0o114|
|M|U+004d|77|0x4d|0b1001101|0o115|
|N|U+004e|78|0x4e|0b1001110|0o116|
|O|U+004f|79|0x4f|0b1001111|0o117|
|P|U+0050|80|0x50|0b1010000|0o120|
|Q|U+0051|81|0x51|0b1010001|0o121|
|R|U+0052|82|0x52|0b1010010|0o122|
|S|U+0053|83|0x53|0b1010011|0o123|
|T|U+0054|84|0x54|0b1010100|0o124|
|U|U+0055|85|0x55|0b1010101|0o125|
|V|U+0056|86|0x56|0b1010110|0o126|
|W|U+0057|87|0x57|0b1010111|0o127|
|X|U+0058|88|0x58|0b1011000|0o130|
|Y|U+0059|89|0x59|0b1011001|0o131|
|Z|U+005a|90|0x5a|0b1011010|0o132|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|[|U+005b|91|0x5b|0b1011011|0o133|
|\\ |U+005c|92|0x5c|0b1011100|0o134|
|]|U+005d|93|0x5d|0b1011101|0o135|
|^|U+005e|94|0x5e|0b1011110|0o136|
|_|U+005f|95|0x5f|0b1011111|0o137|
|`|U+0060|96|0x60|0b1100000|0o140|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|a|U+0061|97|0x61|0b1100001|0o141|
|b|U+0062|98|0x62|0b1100010|0o142|
|c|U+0063|99|0x63|0b1100011|0o143|
|d|U+0064|100|0x64|0b1100100|0o144|
|e|U+0065|101|0x65|0b1100101|0o145|
|f|U+0066|102|0x66|0b1100110|0o146|
|g|U+0067|103|0x67|0b1100111|0o147|
|h|U+0068|104|0x68|0b1101000|0o150|
|i|U+0069|105|0x69|0b1101001|0o151|
|j|U+006a|106|0x6a|0b1101010|0o152|
|k|U+006b|107|0x6b|0b1101011|0o153|
|l|U+006c|108|0x6c|0b1101100|0o154|
|m|U+006d|109|0x6d|0b1101101|0o155|
|n|U+006e|110|0x6e|0b1101110|0o156|
|o|U+006f|111|0x6f|0b1101111|0o157|
|p|U+0070|112|0x70|0b1110000|0o160|
|q|U+0071|113|0x71|0b1110001|0o161|
|r|U+0072|114|0x72|0b1110010|0o162|
|s|U+0073|115|0x73|0b1110011|0o163|
|t|U+0074|116|0x74|0b1110100|0o164|
|u|U+0075|117|0x75|0b1110101|0o165|
|v|U+0076|118|0x76|0b1110110|0o166|
|w|U+0077|119|0x77|0b1110111|0o167|
|x|U+0078|120|0x78|0b1111000|0o170|
|y|U+0079|121|0x79|0b1111001|0o171|
|z|U+007a|122|0x7a|0b1111010|0o172|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|{|U+007b|123|0x7b|0b1111011|0o173|
|\||U+007c|124|0x7c|0b1111100|0o174|
|}|U+007d|125|0x7d|0b1111101|0o175|
|~|U+007e|126|0x7e|0b1111110|0o176|

<br>

[Back to Top](#python-strings)
___

<br>

# `Special Characters`
`Special Characters` have a special meaning and are used to perform specific functions in strings and some other types of data.  
> * These characters are typically difficult or impossible to represent directly  
> * Most of these characters have other default meanings and therefore must be "escaped" in order to perform the special function.  

*NOTE*: 
> "escaping a character" refers to the use of special sequences or combinations of characters to represent characters that are difficult or impossible to represent directly.

## `Special Characters in Python`
|Character|Description|
|:-:|:-|
|\\ | Escape |
|\n |ASCII Linefeed (Newline)|
|\\\\ |Backslash|
|\\'|Single Quote|
|\\"|Double Quote|
|\xhh|Hexadecimal Byte |
|\uxxxx|UTF-16 2 bytes |
|\Uxxxxxxxx|UTF-32 4 bytes |
|r or R| Raw String Prefix|

**Others that don't get used as much:**
|Character|Description|
|:-:|:-|
|\a| ASCII Bell Sound|
|\b| ASCII Backspace|
|\f| ASCII Form Feed|
|\r| ASCII Carriage Return|
|\t | ASCII Tab|
|\v| ASCII Vertical Tab|
|\e|ASCII Escape|
|\ooo| Character Octal Value|
|\N{name}| Unicode Character By Name|

<br>


## `Escape Character`
`Escape Character \`

In Python, as well as many other languages, the backslash character `\` is used as the escape character.
> * Placing a backslash `\` in front of another character we "escape" that characters normal function, and indicate a different one.

example:
```python
"\n \\ \' \" \x61 \u0061 \U00000061"

"\a \b \f \r \t \v \e \141 \N{GREEK SMALL LETTER ALPHA}"
```

<br>

## `ASCII Linefeed (Newline Character)`
`ASCII Linefeed (Newline Character) ( \n )`
> * the newline character returns the cursor to the beginning next line

```python
print("First line\nSecond line")
#                 ^ 
# Output:
# First line 
# Second line
```

<br>

## `Backslash Character`
`Backslash Character ( \\ )`

Because the backslash character `\` is used to escape other characters, it is necessary to use two backslashes `\\` in order to treat the second backslash as a literal. 

*NOTE*: 
> This will often come up when using Windows file paths in your code. Windows uses \\ to seperate folder/file names in the path

```python
print( "C:\\Users\\USERNAME\\Documents" )
#         ^      ^         ^
# Output: 
# C:\Users\USERNAME\Documents 
```

<br>

## `Quotes: Single and Double`
`Quotes: Single ( ' ), Double( " )`

Because single quotes `'` and double quotes `"`  are used in the syntax of Python to indicate a string literal.
>  * It is necessary to escape these characters in order to make them apart of a string. 

```python
print('It\'s an escaped character!')
#        ^
# Output: 
# It's an escaped character!

print('It's an escaped character!') 
# Output: SyntaxError: unterminated string literal
```

```python
print("\"This text includes the quotes!\"")
#      ^                               ^
# Output: 
# "This text includes the quotes!"

print(""This text includes the quotes!"")
# Output: SyntaxError: invalid syntax.
```

<br>

## `UTF-8 Encoding (1 byte) Hexadecimal Bytes`
`UTF-8 Encoding (1 byte) Hexadecimal Bytes ( \xhh )`

Binary data is often difficult for humans to read easily so much of the time binary data is represented as hexadecimal bytes.
> * Use \xhh in Python in order to represent data as a byte 

*NOTE*: 
> `hh` indicates two places for a hexadecimal value

```python
print("\x68\x65\x6c\x6c\x6f")
# Output: hello
```

<br>

## `UTF-16 Encoding (2 bytes)`
`UTF-16 Encoding (2 bytes) ( \uxxxx )`

In order to represent characters not available on the keyboard, such as the greek alphabet, UTF encoding escape sequences are neccessary.

> *For example the code below prints out the uppercase, and lowercase greek alphabet*

```python
print("\u0391 \u0392 \u0393 \u0394 \u0395 \u0396 \u0397 \u0398 \u0399 \u039a \u039b \u039c \u039d \u039e \u039f \u03a0 \u03a1 \u03a2 \u03a3 \u03a4 \u03a5 \u03a6 \u03a7 \u03a8 \u03a9")
# Output: Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ ΢ Σ Τ Υ Φ Χ Ψ Ω

print("\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8 \u03b9 \u03ba \u03bb \u03bc \u03bd \u03be \u03bf \u03c0 \u03c1 \u03c2 \u03c3 \u03c4 \u03c5 \u03c6 \u03c7 \u03c8 \u03c9")
# Output: α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς σ τ υ φ χ ψ ω
```

<br>

## `UTF-32 Encoding (4 bytes)`
`UTF-32 Encoding (4 bytes) ( \uxxxxxxxx )`
In order to represent characters not available on the keyboard, such as emojies, UTF encoding escape sequences are neccessary.

> *For example the code below prints out the common smiley face emojies*
```python
emojies = [
    "\U0001f600","\U0001f601","\U0001f602","\U0001f603",
    "\U0001f604","\U0001f605","\U0001f606","\U0001f607",
    "\U0001f608","\U0001f609","\U0001f60a","\U0001f60b",
    "\U0001f60c","\U0001f60d","\U0001f60e","\U0001f60f",
    "\U0001f610","\U0001f611","\U0001f612","\U0001f613",
    "\U0001f614","\U0001f615","\U0001f616","\U0001f617",
    "\U0001f618","\U0001f619","\U0001f61a","\U0001f61b",
    "\U0001f61c","\U0001f61d","\U0001f61e","\U0001f61f",
    "\U0001f620","\U0001f621","\U0001f622","\U0001f623",
    "\U0001f624","\U0001f625","\U0001f626","\U0001f627",
    "\U0001f628","\U0001f629","\U0001f62a","\U0001f62b",
    "\U0001f62c","\U0001f62d","\U0001f62e","\U0001f62f",
    "\U0001f630","\U0001f631","\U0001f632","\U0001f633",
    "\U0001f634","\U0001f635","\U0001f636"
]

print(emojies)

# Output: 
# [ 
#   😀, 😁, 😂, 😃, 
#   😄, 😅, 😆, 😇, 
#   😈, 😉, 😊, 😋, 
#   😌, 😍, 😎, 😏,
#   😐, 😑, 😒, 😓,
#   😔, 😕, 😖, 😗,
#   😘, 😙, 😚, 😛,
#   😜, 😝, 😞, 😟,
#   😠, 😡, 😢, 😣,
#   😤, 😥, 😦, 😧,
#   😨, 😩, 😪, 😫,
#   😬, 😭, 😮, 😯,
#   😰, 😱, 😲, 😳,
#   😴, 😵, 😶 
# ]

```

<br>


## `Tab Character`
`Tab Character ( \t )`

`\t` is used to insert horizontal spacing.

```python
print( "First\tSecond\tThird" )
#            ^       ^
# Output: 
# First   Second  Third
```

<br>

## `Carriage Return Character`
`Carriage Return Character ( \r )`

`\r` returns the cursor to the beginning of the current line

```python
print("123\rabc")
#         ^
# Output: 
# abc
```

<br>

## `Backspace Character`
`Backspace Character ( \b )`  
`\b` is used to delete the preceding character
```python
print("abc\bd")
#         ^
# Output:
# abd
```

<br>

[Back to Top](#python-strings)
___

<br>

# `Converting Between Character Encodings`
Characters can be represented in multiple ways called encodings.
> * There are builtin function calls to convert between these encodings

> * `int()`, `bin()`, `hex()`, `oct()`, `str()`, `chr()`, `ord()`

## `Convert to an Integer int()`
syntax:
```
int(object, base=10)
```

> * `int()` converts a number or string into an integer object
> * can be used to convert between bases (>= 2 and <=36) 
>    * base 2  (binary) (prefix: 0b)
>    * base 8  (octal) (prefix: 0o)
>    * base 16 (hexadecimal) (prefix: 0x)

*NOTE*: 
> Floats are truncated to Integers. Truncating means to cut off at the floating point, NOT round.


```python
int(2.17)         # 2  float to int   truncates, does not round (cuts off at the floating point)
int("97")         # 97 str to int
int(0b1100001)    # 97 binary to int 
int("1100001",2)  # 97 binary to int
int(0x61)         # 97 hexadecimal to int 
int("61",16)      # 97 hexadecimal to int
```

<br>

## `Convert to Binary bin()`
syntax:
```
bin(number)
```
> * bin() converts decimal to base 2 (binary)
> * coverts from a number to binary
> * 0b is used to indicate binary values in Python

```python
bin(97)     #Returns: 0b1100001  decimal to binary
bin(0x61)   #Returns: 0b1100001 hex to binary
```

<br>

## `Convert From a Character to Binary`
`bin()` cannot directly convert characters to binary

Use the `ord(str)` call to convert to decimal value first


```python
bin("a")      # Output: TypeError: 'str' object cannot be interpreted as an integer
bin(ord("a")) # Returns: 0b1100001 
```

<br>

## `Convert to Hexadecimal hex()`
`hex()` converts decimal to base 16 (hexadecimal)
> * 0x is used to indicate hex values in Python

syntax:
```
hex(number)
```

*NOTE*: 
> In other areas of computing hexadecimal is also indicated using 0x, #, and h .


```python
hex(97)         # Returns: 0x61 decimal to hex
hex(0b1100001)  # Returns: 0x61 binary to hex
```

<br>

## `Convert From a Character to Hexadecimal`
`hex()` cannot directly convert characters to hexadecimal
Use the `ord(str)` call to convert to decimal first

```python
hex("a")      # Output: TypeError: 'str' object cannot be interpreted as an integer
hex(ord("a")) # Returns: 0x61
```

<br>

## `Convert to a String`
`str()` creates a new string object from another object type
> * ie. converts to a string
> * works on custom classes with the \_\_str\_\_ method defined

syntax:
```
str(object) 
```
```python
null = None
str(null)       # Returns: 'None'
type(str(null)) # Returns: <class 'str'>
```
```python
boo = True
str(boo)        # Returns: 'True'
type(str(boo))  # Returns: <class 'str'>
```
```python
num = 123
str(num)        # Returns: "123"
type(str(num))  # Returns: <class 'str'>
```
```python
flo = 3.14
str(flo)        # Returns: "3.14"
type(str(flo))  # Returns: <class 'str'>
```
```python
complex_num = 1 + 2j
str(complex_num)        # Returns: '(1+2j)'
type(str(complex_num))  # Returns: <class 'str'> 
```
```python
list1d = ["a","b","c"]
str(list1d)         # Returns: "['a', 'b', 'c']"
type(str(list1d))   # Returns: <class 'str'>
# tuples, sets, dictionaries all work similiarly
```
```python
str(len)        # Returns: '<built-in function len>'
type(str(len))  # Returns: <class 'str'>
```

<br>

## `Convert from an Integer to a Character chr()`
`chr()` converts an integer `i` to its character representation

syntax:
```
chr(i)
```
```python
chr(97)         # Returns: "a" decimal to character
chr(0b1100001)  # Returns: "a" binary to character
chr(0x61)       # Returns: "a" hex to character
```

<br>

## `Convert from a Character to an Integer ord()`
`ord()` converts a character `c` to its Unicode code point (a base 10 integer) representing the given character.

syntax:
```
ord(c)
```
 

```python
ord('a') #Returns: 97
ord('b') #Returns: 98
ord('c') #Returns: 99
ord('d') #Returns: 100
ord('e') #Returns: 101
ord('f') #Returns: 102
ord('g') #Returns: 103
ord('h') #Returns: 104
```

<br>

[Back to Top](#python-strings)
___

<br>

# `Defining a String`
Basically: `Strings` are text surrounded by single or double quotes.

Specifically: `Strings` are immutable (cannot be changed) sequences of characters surrounded by quotation marks ("" or '').
> * If you need to change the string you must create a new string.

*NOTE*: 
> Fundamentally, a string is just an array of characters


## String Example:

```python
"Hello World" 
```

```python
'Hello World'
```

> variables can be pointed to strings
```python
str_ = "This is some text"
```

<br>

## Strings are objects of the *str* class in python

```python
type("My String") # Returns: <class 'str'>
```

<br>

[Back to Top](#python-strings)
___

<br>


# `Multiline Strings`
String literals can span multiple lines by using triple quotes (`'''` or `"""`) and automatically include the newline character `\n` at the end. 

*use \ to remove the automatic newline character at the end (does not work for the first line).*

```python
print("""  
line 1\
line 2\
line 3\
""") 

#Output: line 1line 2line 3
```

<br>

[Back to Top](#python-strings)
___

<br>


# `String Concatenation`
`Concatenate` means to join
> *  use `+` to concatenate two strings

<br>

String literals next to each other are automatically concatenated
>   * useful for breaking up long strings

```python
print(
"Python is an easy to learn, powerful programming language."
"It has efficient high-level data structures and a simple but "
"effective approach to object-oriented programming."
"Python’s elegant syntax and dynamic typing, together with its interpreted nature, "
"make it an ideal language for scripting and rapid application development in many areas"
" on most platforms."
)

# Output:
# Python is an easy to learn, powerful programming language.It has efficient high-level data structures and a simple but effective approach to object-oriented programming.Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
```
<br>

## `Manually Concatenate`
Use `+` to concatenate two strings


```python
"Hello" + " World" # Returns: Hello World
#          ^ don't forget the space
```

> Concatenation is often practically used with variables
```python
first = "John" 
last = "Smith" 

print("Hello my name is " + first + " " + last)
# Output:
# Hello my name is John Smith
```

<br>

## `Compound Concatenate and Assign Strings`
Use `+=` to concatenate and assign


> Compound Assignment operations perform the operation and assign the result to the variable on the left hand side


```python
letters = "" 
letters += "a" # letters = "" + "a"
letters += "b" # letters = "a" + "b"
letters += "c" # letters = "ab" + "c"

print(letters) # Output: abc
```

<br>

[Back to Top](#python-strings)
___

<br>

# `String Duplication`
`Duplicate` means to make a copy.
> *  use `*` to duplicate a string




```python
print("000 " * 10)
#Output:
#000 000 000 000 000 000 000 000 000 000 
```

<br>

## `Compound Duplicate and Assign Strings`
Use `*=` to duplicate a string and assign

> Compound Assignment operations perform the operation and assign the result to the variable on the left hand side


```python
pattern = "_--[O]--_"
pattern *= 5

print(pattern)
# Output: _--[O]--__--[O]--__--[O]--__--[O]--__--[O]--_
```

<br>

[Back to Top](#python-strings)
___

<br>

# `String Comparision`
Strings are compared `Lexicographically`

`Lexicographical Comparision`  
* Basically: is like comparing the alphabetical order of characters or strings.

* Specifically: is the comparision of strings character by character, taking the difference between their Unicode codepoint (base 10 integer) values. 

<br>
 
How it works:
> 1. Compare the first character of each string. 
> 2. If the two characters are equal, move on to the next character. 
> 3. If the two characters are not equal return the difference between the first and second.
> 4. If every character is equal return 0. 


## `Equality Comparision`
`Equality Comparision ==`  
Compares the value of two strings, returns True if they are equal and False if they are not. 


```python
"Hello" == "Hello" # Returns: True
"hello" == "Hello" # Returns: False

first = "Jane"
last = "Smith"  
first == last # Returns: False
```

<br>

## `NOT Equal`
`NOT Equal !=`  
Compares the value of two strings, returns True if they are NOT equal and False if they are equal. 


```python
"Hello" != "Hello" # Returns: False 
"hello" != "Hello" # Returns: True 

first = "Jane"
last = "Smith"  
first != last # Returns: True
```

<br>

## `Greater Than and Less Than`
`Greater Than > and Less Than <`  

`>` Compares if the first string is lexicographically `greater than `the second.  

`<` Compares if the first string is lexicographically `lesser than` the second. 

*NOTE*: 
> This is similiar to comparing based on alphabetical order, but instead is based on Unicode codepoints to compare non-alphabetical characters.*


```python
str1 = "apple"; str2 = "banana"

str1 < str2   # Returns: True (lexicographically smaller)

str1 > str2   # Returns: False 
#apple comes before banana
```

<br>

## `Length Comparision`
If the strings have different lengths but the shorter string is identical to the longer one up to the length of the shorter string, Python considers the shorter string less than the longer one.  
> For example, "abc" is less than "abcd".


```python
str3 = "abc"
str4 = "abcd"

str3 < str4 #Returns: True (because 'abc' is shorter)
```

<br>

[Back to Top](#python-strings)
___

<br>

# `String Indexing`

Basically: `Indexing` is the assigment of a number to each element starting at 0 and increasing for each element (character).

Specifically: `Indexing` is the association of a specific identifier (index) with each element of and iterable, which can be used to directly locate and access the data in a collection.

> * Strings are a sequence or "string" of characters.
> * Strings can be thought of as a list of characters.
> * Strings can be indexed like lists
> * each character in the string is given an index starting from 0.

IMPORTANT --> `spaces are counted as characters`

<br> 

## Example with the string "Programming"

|String|P|r|o|g|r|a|m|m|i|n|g|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Index|0|1|2|3|4|5|6|7|8|9|10
|Reverse|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|


<br>
<br>

## `Why do indexes start at 0?`  
TLDR: The beginning of the array and the first element are the same spot in memory

<br> 

*The convention of starting indexes at 0 was solidified by early programming languages like C, which was heavily influenced by the needs and constraints of the hardware at the time.*
*C, developed in the early 1970s, adopted 0-based indexing and became one of the most influential programming languages. Many subsequent languages, such as C++, Java, and Python, followed this convention due to C's widespread influence.*

***0-based indexing:***  
*When using 0-based indexing, the index directly corresponds to an offset from the beginning of the array in memory.* 
*This simplifies the calculation of the address of an element in memory:*

    Address = Base Address + (Index * Element Size)

*When the index is 0 the address of the element is equal to the base address of the array*  


<br>



## `Accessing Characters in a String`
Individual characters of a string can be accessed using subscripting with `[]`  
> * Use the index of the character and subscripting to access it  

syntax:
```
string[index]
```

```python
txt = "Programming" 

print( txt[0] )# Output: P
print( txt[1] )# Output: r
print( txt[2] )# Output: o

#Reverse/Negative Indexing
print( txt[-1] )# Output: g
print( txt[-2] )# Output: n
print( txt[-3] )# Output: i
```

<br>

## `Changing Characters in a String`
Strings are immutable meaning its values cannot be changed
> * new strings can be created, but cannot change the original string
> * attempting to change the value of a string results in an error. 


```python
txt = "Programming" 

txt[0] = "a" 
# Output: TypeError: 'str' object does not support item assignment
```

<br>

[Back to Top](#python-strings)
___

<br>

# `String Slicing`
`Slicing` is the creation a substring, by returning parts of the orginal string
> * use slicing notation [ : : ] to return a substring

Example with the string "Programming"

|String|P|r|o|g|r|a|m|m|i|n|g|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Index|0|1|2|3|4|5|6|7|8|9|10
|Reverse|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

"Prog" is a substring "Programming"

<br>

Slicing Syntax:    
```
string[start_index:stop_index:step]
```
> * start_index is inclusive (the character at start_index will appear in the substring)
> * stop_index is exclusive (the character at the stop_index will NOT appear in the substring)

Be sure to pick the right stop_index
> * for ascending ( + step ) substrings add one to the last index you want to include (stop + 1)  
> * for descending ( - step ) substring subtract one from the last index you want to include (stop - 1)


## Slicing Examples:

```python
txt = "Programming" 

# Ascending
print( txt[1:6:2] )  # Returns: rga
print( txt[0:9:3] ) # Returns: Pgm
print( txt[2:8:3] ) # Returns: oa
print( txt[1:7:1] ) # Returns: rogram

# Descending
print( txt[4:1:-1] )    # Returns: rgo
print( txt[-1:-5:-1])   # Returns: gnim
print( txt[7:0:-1])     # Returns: mmargor
print( txt[8:0:-2] )    # Returns: imro
```

## `Ascending Slices`
> * Default start_index is 0
> * Default stop_index is len(string) (end of the string)
> * Default step is 1
> * The slice includes the start_index, but excludes the stop_index


```python
txt = "Programming" 

#If a start_index is not provided the default is 0
txt[:5:1]   # Returns: Progr
txt[:6:3]   # Returns: Pg

#If a stop_index is not provided the default is len(list)
txt[3:]     # Returns:  gramming
txt[4::1]   # Returns:  ramming
txt[::2]    # Returns:  Pormig

# If the step is not specified the default is 1 
txt[0:7]    # Returns: Program
txt[:5]     # Returns: Progr
txt[6::]    # Returns: mming
```

<br>

## `Descending Slices`
> * Default start_index is len(list) (end of the list)
> * Default stop_index is the beginning of the list
>   * In order to include the character at index 0 you must use the default stop_index 
> * Must specify a negative step
> * The slice includes the start_index, but excludes the stop_index


```python
#If a start_index is not provided the default is len(list)
txt[:4:-1]     # Returns: gnimma
txt[:-6:-1]    # Returns: gnimm
txt[::-1]      # Returns: gnimmargorP

#If a stop_index is not provided the default is len(list)
txt[5::-1]     # Returns: argorP
txt[-3::-1]    # Returns: immargorP
txt[::-3]      # Returns: gmrr
```

<br>

[Back to Top](#python-strings)
___

<br>

# `Built-in String Function Calls`
`Functions` are blocks of reusable code, that perform a specific task.
> * must be defined before they are called
> * are typically called using their name followed by parenthesis with any required arguments inside.


`Built-in Functions are pre-defined by the Python standard library`

<br>

`len(obj)`

> * returns the number of characters in the string   
> * subtracting 1 from the length of a string or list returns the last index of that sequence

IMPORTANT --> `spaces are counted as characters`

```python
len("Hello World!") # Returns: 12


txt = "Programming"
len(txt)            # Returns: 11

len(txt)-1          # Returns: 10 
# 10 is the last index in "Programming"

```

<br>

`max(iterable)`
Returns the maximum character (according to Unicode code point) in a string.
> * an `iterable` is a sequence that can return its members one by one (like a list)


```python
txt = "Programming"
max(txt) # Returns: r
```

<br>

`min(iterable)`
Returns the minimum character (according to Unicode code point) in a string.
> * an `iterable` is a sequence that can return its members one by one (like a list)

```python
txt = "Programming"
min(txt) # Returns: P
```

<br>

[Back to Top](#python-strings)
___

<br>

# `Built-in String Method Calls`
`Methods` are functions defined by a class
> * are typically called using an object or class and dot ( . ) syntax

<br>

> syntax for methods which require objects:

    object.method(arguments)

> syntax for methods which DO NOT require objects:

    class.method(arguments)

`Built-in methods are pre-defined by classes pre-defined by the standard library`

> To see what methods you can call on an object use:  
    
    dir(object)  

> To see more information on a specific method use:  
    
    help(object.method)

```python
txt = "Programming"


#txt.capitalize()  No parameters
txt.capitalize()    
# Returns a copy of the string with the first character capitalized

#txt.casefold()  No parameters
txt.casefold()      
# Returns a casefolded copy of the string, suitable for case-insensitive comparisons

#txt.center(width, fillchar=" ") 'width' (required): the width of the centered string, 'fillchar' (optional): character used for padding
txt.center()        
# Returns a centered txt of a specified width

# txt.count(substring, start, end) 'substring' (required): the substring to count, 'start' (optional): starting index for the search, 'end' (optional): ending index for the search
txt.count("m")         
# Returns the number of occurrences of a substring in the string

# txt.encode(encoding="utf-8", errors="strict")  'encoding' (optional): encoding type, 'errors' (optional): how to handle encoding errors
txt.encode()        
# Returns the encoded version of the string


# txt.endswith(suffix, start, end) 'suffix' (required): suffix to check, 'start' (optional): start index for the slice, 'end' (optional): end index for the slice
txt.endswith()      
# Checks if the string ends with a specified suffix


# txt.expandtabs(tabsize=8) 'tabsize' (optional): size of the tab character
txt.expandtabs()    
# Expands tabs in the string to spaces


# txt.find(substring, start, end) 'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
txt.find("m")          
# Returns the lowest index of a substring in the string


# txt.format(*args, **kwargs) *args (optional): positional arguments, **kwargs (optional): keyword arguments
txt.format()        
# Formats the string


# txt.format_map(mapping) 'mapping' (required): mapping object containing the formatting parameters
txt.format_map()    
# Formats the string using a mapping


# txt.index(substring, start, end) 'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
txt.index("ing")         
# Returns the lowest index of a substring in the string


# txt.isalnum() No parameters
txt.isalnum()       
# Checks if all characters in the string are alphanumeric

# txt.isalpha() No parameters
txt.isalpha()       
# Checks if all characters in the string are alphabetic


# txt.isascii() No parameters
txt.isascii()       
# Checks if the string contains only ASCII characters


# txt.isdecimal() No parameters
txt.isdecimal()     
# Checks if all characters in the string are decimal


# txt.isdigit() No parameters
txt.isdigit()       
# Checks if all characters in the string are digits


# txt.isidentifier() No parameters
txt.isidentifier()  
# Checks if the string is a valid identifier


# txt.islower() No parameters
txt.islower()       
# Checks if all characters in the string are lowercase


# txt.isnumeric() No parameters
txt.isnumeric()     
# Checks if all characters in the string are numeric


# txt.isprintable() No parameters
txt.isprintable()   
# Checks if all characters in the string are printable


# txt.isspace() No parameters
txt.isspace()       
# Checks if all characters in the string are whitespaces


# txt.istitle() No parameters
txt.istitle()       
# Checks if the string is titlecased


# txt.isupper() No parameters
txt.isupper()       
# Checks if all characters in the string are uppercase


# txt.join(iterable) 'iterable' (required): iterable of strings to join
txt.join(" in Python")          
# Joins the elements of an iterable to create a string


# txt.ljust(width, fillchar) 'width' (required): width of the resulting string, 'fillchar' (optional): character used for padding
txt.ljust(20)         
# Returns a left-justified string of a specified width


# txt.lower() No parameters
txt.lower()         
# Returns a copy of the string converted to lowercase


# txt.lstrip(chars) 'chars' (optional): characters to be stripped from the beginning
txt.lstrip()        
# Returns a copy of the string with leading whitespace removed


# txt.maketrans(x, y, z)  'x' (required): characters to replace, 'y' (required): corresponding replacement characters, 'z' (optional): characters to delete
txt.maketrans()     
# Returns a translation table usable for str.translate()


# txt.partition(separator)  'separator' (required): separator to partition the txt
txt.partition()     
# Splits the string at the first occurrence of a separator


# txt.removeprefix(prefix)  'prefix' (required): prefix to remove
txt.removeprefix()  
# Removes a prefix from the string


# txt.removesuffix(suffix)  'suffix' (required): suffix to remove
txt.removesuffix()  
# Removes a suffix from the string


# txt.replace(old, new, count)  'old' (required): substring to be replaced, 'new' (required): substring to replace with, 'count' (optional): number of occurrences to replace
txt.replace()       
# Returns a copy of the string with occurrences of a substring replaced


# txt.rfind(substring, start, end)  'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
txt.rfind()         
# Returns the highest index of a substring in the string


# txt.rindex(substring, start, end) 'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
txt.rindex()        
# Returns the highest index of a substring in the string


# txt.rjust(width, fillchar)  'width' (required): width of the resulting string, 'fillchar' (optional): character used for padding
txt.rjust()         
# Returns a right-justified string of a specified width


# txt.rpartition(separator) 'separator' (required): separator to partition the string
txt.rpartition()    
# Splits the string at the last occurrence of a separator


# txt.rsplit(separator, maxsplit)  'separator' (optional): separator to split the string, 'maxsplit' (optional): maximum number of splits
txt.rsplit()        
# Splits the string into a list, starting from the right


# txt.splitlines(keepends)  'keepends' (optional): whether to keep the line endings
txt.splitlines()    
# Splits the string at line breaks and returns a list of lines


# txt.startswith(prefix, start, end)  'prefix' (required): prefix to check, 'start' (optional): start index for the slice, 'end' (optional): end index for the slice
txt.startswith()    
# Checks if the string starts with a specified prefix


# txt.strip(chars)  'chars' (optional): characters to be stripped from both ends
txt.strip()         
# Returns a copy of the string with leading and trailing whitespace removed


# txt.swapcase()  No parameters
txt.swapcase()      
# Returns a copy of the string with uppercase characters converted to lowercase and vice versa


# txt.title() No parameters
txt.title()         
# Returns a titlecased version of the string


# txt.translate(table) 'table' (required): translation table
txt.translate()     
# Returns a copy of the string where each character has been mapped through the given translation table


# txt.upper() No parameters
txt.upper()         
# Returns a copy of the string converted to uppercase


# txt.zfill(width) 'width' (required): width of the resulting string
txt.zfill()         
# Returns a copy of the string padded with zeros to a specified width

```

<br> 

[Back to Top](#python-strings)
___

<br>

# `Format Strings: f-strings`
Introduced in Python 3.6, f-strings provide a convenient way to embed expressions inside string literals. 


Basically: `Format Strings` are a way to use variables inside of strings

Specifically: `Format Strings` are a way to embed expressions inside of string literals  
> * They are prefixed with an 'f' or 'F' character and contain expressions enclosed in curly braces { }.

syntax:

    f"literal {var} text"

<br>

## `Inserting Variables Directly Into Strings`
f-strings can be used to add variables to strings without the need for concatenation (+)
> * prefix strings with 'f' or 'F' to indicate a f-string
> * enclose variables within { } inside of the f-string


```python
name = "Sam"
age = 30

greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Sam and I am 30 years old.

```

<br>

## `Formatting Numbers for Output`
Use a `:` to seperate the variable from format information

> Numbers can be formated with `_` or with `,` for readability
```python
#Integers
n = 1000000000
# _ and , can be used to format larger numbers
print( f'{n:_}' ) #Output: 1_000_000_000 
print( f'{n:,}' ) #Output: 1,000,000,000
```

> Floats can be rounded to `n` decimal places with ( : .`n`f )
```python
#Floats (.nf) to round to n decimal places
n = 1234.56789
f"{n:.0f}" # Returns: 1235
f"{n:.1f}" # Returns: 1234.6

# with separators
f"{n:_.2f}" # Returns: 1_234.57
f"{n:,.3f}" # Returns: 1,234.568
```

> Scientific Notation can be used with ( :e )
```python
n = 602200000000000000000000

print(f'{n:e}') #6.022000e+23
print(f'{n:.3e}') #6.022e+23
```

<br>


## `Formatting Expressions for Output`
Expressions can be inserted into strings
> * this can be helpful with debugging and logging


```python
a = 2; b = 3

f'{a = }'     # Returns: a = 2
f'{b = }'     # Returns:  b = 3
f'{a + b = }' # Returns:  a + b = 5

c = 0.1; d = 0.2
f'{c + d = :.1f}' # Returns:  c + d = 0.3
```

> formatting information can be stored inside of a string variable
```python
c = 3.141592665
form = ".2f"
f'{c:{form}}'  # Returns: 3.14
```

<br>

## `Padding and Alignment`
* right align with `>`
* left align with `<`
* center align with `^`
* align and pad with numbers (see examples)


```python
var = "x"
#right align(>) and pad to n with spaces
print(f'|{var:>5}|') #Output: |    x|

#left align(<) and pad to n with spaces
print(f'|{var:<5}|') #Output: |x    |

#center align (^) and pad to n with spaces
print(f'|{var:^5}|') #Output: |  x  |

#align and pad to n with character
print(f'|{var:_>5}|') #Output: _x|
print(f'|{var:#<5}|') #Output: |x####|
print(f'|{var:|^5}|') #Output: |||x|||
print(f'|{var:a^5}|') #Output: |aaxaa|
```

<br> 

## `Removing quotes from output`
Use `!s` to remove quotes from output expressions

```python
name = "Alice"
f'{name = }' #Returns: name = 'Alice'
f'{name = !s}' #Returns: name = Alice
```

<br>

[Back to Top](#python-strings)
___

<br>

# `Raw Strings`
`Raw strings` are string literals prefixed with an `r` or `R` character. 
> * r-strings treat backslashes `\` as literal characters, and they are often used for regular expressions, file paths, or any string where backslashes are prevalent and should not be treated as escape characters.

> * prefix strings with `r` or `R` to indicate a raw string

syntax:

    r"literal text"

    R"literal text"


```python
#instead of this
print('C:\\Users\\Username\\Desktop\\Myfolder') 
#Output:  C:\Users\Username\Desktop\Myfolder

#Try this
print(r'C:\Users\Username\Desktop\Myfolder') 
#Output:  C:\Users\Username\Desktop\Myfolder

```

<br>

[Back to Top](#python-strings)
___

<br>

# `Bytes Strings`
`Bytes Strings`, prefixed with a `b` or `B` character, represent sequences of bytes. 
> * Bytes strings are used to store binary data such as images, audio files, or any data that is not necessarily text.
> * prefix strings with `b` to indicate a bytes literal

syntax:
```
b"bytes literal"

B"bytes literal"
```


```python
b'\x48\x65\x6C\x6C\x6F' #bytes literal
```

> decode bytes literals with `.decode(encoding='utf-8', errors='strict')`

```python
print(b'\x48\x65\x6C\x6C\x6F'.decode()) # Hello
print(b'Hello') # b'Hello'
```

<br>

[Back to Top](#python-strings)
___

<br>

# `Appendix`


```python
'You can generate a unicode dictionary with the code below'
def gen_unicode_table(start = 1, stop = 1024, print_out = False):
    table = {"Character" : ("Unicode Code Point", "Decimal", "Hexadecimal","Binary","Octal")}
    for num in range(start,stop+1):
        table[chr(num)] =(f"U+{num:04x}",num,hex(num),bin(num), oct(num))

    if(print_out):
        # print(str(table).replace("),","),\n"))
        for char,encodings in table.items():
           print(f"|{char}|{encodings[0]}|{encodings[1]}|{encodings[2]}|{encodings[3]}|{encodings[4]}|")
           
    return table


gen_unicode_table()
```


```python
#Function to display the bytes
def return_bytes(txt):
  '''prints and returns the byte values for each character in txt '''
  string = r""
  for byte in txt:
    string += str(hex(byte)).replace("0","\\")

  print(string)
  return(string)


return_bytes(b"hello")
```
<br>

___

[Back to Top](#python-strings)
___

<br>

*Created and maintained by Mr. Merritt* 
