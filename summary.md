 Word Counter and Text Analyzer

## Problem Definition
Build a Python 3 tool that analyses a piece of text or a text file and reports the number of words, characters, sentences and the frequency of each word.

Counting is case-insensitive and punctuation is removed before counting words.

## Approach

*Input:* The user types text or gives a file name through a console menu.

*Validation:* Empty text gives "No text to analyse."; a missing file gives a file-not-found message using try/except FileNotFoundError.

*Cleaning:* lower(), replace(), strip() and split().

*Counting:*
- Words = length of the cleaned word list.
- Characters = length of original text (with spaces).
- Sentences = non-empty parts after splitting on ., !, ?.

*Frequency Analysis:* A dictionary stores each word's count.

*Unique Words:* A set removes duplicates.

*Output:* Results sorted by frequency (highest first, ties alphabetical).

## Data Structures Used

| Structure | Purpose |
|---|---|
| String | Cleaning and splitting text |
| List | Holds the words |
| Dictionary | Word → frequency |
| Set | Unique words |

## Test Results

| Test Case | Result |
|---|---|
| Normal input | Words 6, Characters 30, Sentences 2 – Pass |
| Boundary input ("Hello") | Words 1, Characters 5, Sentences 1, Unique 1 – Pass |
| Invalid input | Proper error messages – Pass |
| Frequency scenario | the: 3, dog: 2, Unique words: 5 – Pass |

## Conclusion

The program meets all basic requirements:
- Single .py file.
- Reads from user or file.
- Cleans text with string methods.
- Counts frequency with a dictionary.
- Finds unique words with a set.
- Displays results sorted by frequency.

All four test cases pass.

## Possible Improvements

1. Save the report to a file.
2. Ignore common stop words.
3. Show average word length and longest word.

## Author Details

Name: Kumar Abhinav

Enrollment No.: ERP-Ru-26-02195

Rungta International Skills University
School of Computer Science and Engineering
B.Tech Computer Science and Engineering
