# Open the text file (replace 'example.txt' with your file name)
file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()  # Read all lines from the file
    
    # Iterate through each line
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()  # Remove leading/trailing spaces
        if not line:  # Skip empty lines
            continue

        # Split the line into sentences using '.', '!', or '?' as sentence delimiters
        sentences = [sentence.strip() for sentence in line.split('.') if sentence]

        # Count sentences in the line
        num_sentences = len(sentences)
        print(f"Line {line_number}: {num_sentences} sentence(s)")

        # Count words in each sentence
        for sentence_number, sentence in enumerate(sentences, start=1):
            words = sentence.split()  # Split the sentence into words
            num_words = len(words)
            print(f"  Sentence {sentence_number}: {num_words} word(s)")

except FileNotFoundError:
    print(f"The file '{file_name}' was not found. Please make sure the file exists in the same directory as this script.")