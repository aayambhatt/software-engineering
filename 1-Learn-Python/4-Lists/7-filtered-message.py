def filter_messages(messages):
    unfiltered_message = []   # Final cleaned messages
    dang_count = []           # Dang word counts

    for message in messages:
        words = message.split()   # Break message into words
        new_words = []            # Store filtered words
        removed = 0               # Count of dangs removed

        for word in words:
            if word == "dang":
                removed += 1
            else:
                new_words.append(word)

        cleaned_message = " ".join(new_words)  # Turn list back into string
        unfiltered_message.append(cleaned_message)
        dang_count.append(removed)

    return unfiltered_message, dang_count

msgs = ["dang it bobby!", "look at it go", "dang dang dang"]
print(filter_messages(msgs))
