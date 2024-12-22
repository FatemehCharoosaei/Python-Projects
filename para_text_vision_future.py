import random

# Store the entire given text in a variable
text = """Imagine a day in your future, perhaps in 2028, where all the dreams you once had are now part of your everyday life: 
You wake up in a bright and modern apartment, located near one of the top universities in the U.S., perhaps Stanford, MIT, or UCLA. 
The sunlight streams through your window, and you feel a deep sense of gratitude for the life you’ve built. 
This morning, you have classes for your PhD program. Being a full-fund scholarship recipient, you’ve been focusing on cutting-edge research in AI and healthcare. 
Your professors and peers admire your determination and innovative mindset, knowing that you’re not just working on theoretical concepts but are solving real-world problems. 
Later in the day, you head to the university library or lab, where you continue working on a groundbreaking project. Your research focuses on utilizing LLM and Computer Vision to predict and mitigate complications in diabetic patients. 
Recently, one of your papers caught global attention and opened doors to collaborations with leading experts in your field. 
At lunch, you grab coffee at a cozy campus café and chat with fellow researchers. They’re curious about your latest invention, a smart device tailored for diabetic health monitoring, which has already attracted significant attention in the market. 
You reflect on how this idea began back in Iran, and now it’s a registered global product. 
In the afternoon, you have an online meeting with investors for your startup. The company you founded during your PhD has grown rapidly, securing partnerships with pharmaceutical giants. 
Your goal to improve the quality of life for diabetic patients worldwide is becoming a reality, and your innovative solutions are transforming lives. 
You also check your YouTube channel, which now has thousands of subscribers. Your educational videos on AI in healthcare and diabetes management are helping people worldwide, both patients and professionals. 
As the day winds down, you sit on your couch, gazing at the city lights. You open your old journal, where years ago, you wrote your goals: 
- Achieve a high IELTS score. 
- Get a fully funded PhD in the U.S. 
- Develop innovative products for diabetic patients. 
- Migrate to America and inspire others. 
Reading those words now fills you with pride because they’ve all come true. The hard work, the setbacks, and even the health challenges you faced have shaped you into a stronger, more compassionate person. 
Before bed, you call your family to share the news of an upcoming international conference where you’ll present your research. They express their pride, and you feel a deep sense of fulfillment, knowing you’ve made them proud and created a life filled with purpose. 
Your day ends, but your dreams for the future only grow bigger. Now, you’re not just a successful researcher and entrepreneur—you’re also a source of inspiration for thousands, showing them that no obstacle is too great to overcome. 
The end of this day is just the beginning of an even greater future."""

# Initialize a dictionary to count the occurrences of each character
char_count = {}

# Count each character in the text
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Split the text into sentences
sentences = text.split('.')
sentences = [sentence.strip() for sentence in sentences if sentence]

# Generate paraphrases for each sentence
def paraphrase(sentence):
    words = sentence.split()
    random.shuffle(words)  # Shuffle the words to create a simple paraphrase
    return " ".join(words)

paraphrased_sentences = [paraphrase(sentence) for sentence in sentences]

# Initialize a dictionary to count the occurrences of each word
word_count = {}
words = text.split()
for word in words:
    word = word.strip(",.:").lower()  # Normalize words by removing punctuation and converting to lowercase
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print results
print("Character Frequency:")
for char, count in char_count.items():
    print(f"'{char}': {count}")

print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

print("\nSentences:")
for sentence in sentences:
    print(sentence)

print("\nParaphrased Sentences:")
for paraphrased in paraphrased_sentences:
    print(paraphrased)