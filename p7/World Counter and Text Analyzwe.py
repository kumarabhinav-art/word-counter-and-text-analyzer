PUNCTUATION = ".,!?;:'\"-()[]{}"


def clean_text(text):
    """Lowercase the text and remove punctuation (lower, replace, strip)."""
    text = text.lower()
    for ch in PUNCTUATION:
        text = text.replace(ch, " ")
    return text.strip()


def get_words(text):
    """Return the list of cleaned words."""
    return clean_text(text).split()


def count_sentences(text):
    """Count sentences ending with . ! or ?  (text without an ending
    punctuation mark still counts as one sentence)."""
    text = text.replace("!", ".").replace("?", ".")
    parts = text.split(".")
    count = 0
    for part in parts:
        if part.strip() != "":
            count += 1
    return count


def word_frequency(words):
    """Count how often each word appears using a dictionary."""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def sort_by_frequency(freq):
    """Sort (word, count) pairs by count (high to low), then A-Z."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def top_words(freq, limit=5):
    """Most frequent words. Only repeated words are listed when any exist."""
    ordered = sort_by_frequency(freq)
    repeated = [item for item in ordered if item[1] > 1]
    chosen = repeated if repeated else ordered
    return chosen[:limit]


def analyse(text):
    """Return a dictionary of all statistics, or None if there is no text."""
    text = text.strip()
    words = get_words(text)
    if text == "" or len(words) == 0:
        return None
    freq = word_frequency(words)
    unique = set(words)
    return {
        "words": len(words),
        "chars": len(text),
        "chars_no_space": len(text.replace(" ", "").replace("\n", "").replace("\t", "")),
        "sentences": count_sentences(text),
        "unique": sorted(unique),
        "freq": freq,
    }


def show_stats(result):
    print("Words: {} | Characters (with spaces): {} | Sentences: {} | Unique words: {}".format(
        result["words"], result["chars"], result["sentences"], len(result["unique"])))
    print("Characters (without spaces):", result["chars_no_space"])


def show_frequency(result):
    top = top_words(result["freq"])
    print("Top words: " + " | ".join("{}: {}".format(w, c) for w, c in top))
    print("Unique words: {} ({})".format(len(result["unique"]), ", ".join(result["unique"])))
    print("\nFull frequency table (sorted by frequency):")
    print("{:<20}{}".format("Word", "Count"))
    print("-" * 26)
    for word, count in sort_by_frequency(result["freq"]):
        print("{:<20}{}".format(word, count))


def read_file(filename):
    """Read a text file. Returns the text, or None if it cannot be read."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
    except (OSError, UnicodeDecodeError):
        print("File '{}' could not be read.".format(filename))
    return None


def menu():
    print("\n=== Word Counter & Text Analyzer ===")
    print("1. Analyse text (word/character/sentence count)")
    print("2. Word frequency")
    print("3. Analyse a text file")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1" or choice == "2":
            text = input("Enter text: ")
            result = analyse(text)
            if result is None:
                print("No text to analyse.")
            elif choice == "1":
                show_stats(result)
            else:
                show_frequency(result)

        elif choice == "3":
            filename = input("Enter file name: ").strip()
            if filename == "":
                print("No file name entered.")
                continue
            text = read_file(filename)
            if text is not None:
                result = analyse(text)
                if result is None:
                    print("No text to analyse.")
                else:
                    show_stats(result)
                    print()
                    show_frequency(result)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
