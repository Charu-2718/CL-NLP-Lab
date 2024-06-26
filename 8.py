<<<<<<< HEAD
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function to generate text summary
def generate_summary(text, num_sentences=2):
    # Process the input text
    doc = nlp(text)

    # Get sentences with highest scores based on token ranks
    sentences = list(doc.sents)
    sentence_scores = {sentence: sum(token.rank for token in sentence) for sentence in sentences}
    top_sentences = sorted(sentences, key=lambda x: sentence_scores[x], reverse=True)[:num_sentences]

    # Join the top sentences to generate the summary
    summary = " ".join(str(sentence) for sentence in top_sentences)
    return summary

# Input text
text = """
King Krishnadevaraya loved horses and had the best collection of horse breeds in the Kingdom. Well, one day, a trader came to the King and told him that he had brought with him a horse of the best breed in Arabia.He invited the King to inspect the horse. King Krishnadevaraya loved the horse; so the trader said that the King could buy this one and that he had two more like this one, back in Arabia that he would go back to get. The King loved the horse so much that he had to have the other two as well. He paid the trader 5000 gold coins in advance. The trader promised that he would return within two days with the other horses.Two days turned into two weeks, and still, there was no sign of the trader and the two horses. One evening, to ease his mind, the King went on a stroll in his garden. There he spotted Tenali Raman writing down something on a piece of paper. Curious, the King asked Tenali what he was jotting down.Tenali Raman was hesitant, but after further questioning, he showed the King the paper. On the paper was a list of names, the King’s being at the top of the list. Tenali said these were the names of the biggest fools in the Vijayanagara Kingdom!As expected, the King was furious that his name was at the top and asked Tenali Raman for an explanation. Tenali referred to the horse story, saying the King was a fool to believe that the trader, a stranger, would return after receiving 5000 gold coins.Countering his argument, the King then asked, what happens if/when the trader does come back? In true Tenali humour, he replied saying, in that case, the trader would be a bigger fool, and his name would replace the King’s on the list!"""

# Generate summary
summary = generate_summary(text)

with open("summary.txt", "w") as file:
    file.write(summary)

# Print confirmation message
print("Summary saved to summary.txt")
=======
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function to generate text summary
def generate_summary(text, num_sentences=2):
    # Process the input text
    doc = nlp(text)

    # Get sentences with highest scores based on token ranks
    sentences = list(doc.sents)
    sentence_scores = {sentence: sum(token.rank for token in sentence) for sentence in sentences}
    top_sentences = sorted(sentences, key=lambda x: sentence_scores[x], reverse=True)[:num_sentences]

    # Join the top sentences to generate the summary
    summary = " ".join(str(sentence) for sentence in top_sentences)
    return summary

# Input text
text = """
King Krishnadevaraya loved horses and had the best collection of horse breeds in the Kingdom. Well, one day, a trader came to the King and told him that he had brought with him a horse of the best breed in Arabia.He invited the King to inspect the horse. King Krishnadevaraya loved the horse; so the trader said that the King could buy this one and that he had two more like this one, back in Arabia that he would go back to get. The King loved the horse so much that he had to have the other two as well. He paid the trader 5000 gold coins in advance. The trader promised that he would return within two days with the other horses.Two days turned into two weeks, and still, there was no sign of the trader and the two horses. One evening, to ease his mind, the King went on a stroll in his garden. There he spotted Tenali Raman writing down something on a piece of paper. Curious, the King asked Tenali what he was jotting down.Tenali Raman was hesitant, but after further questioning, he showed the King the paper. On the paper was a list of names, the King’s being at the top of the list. Tenali said these were the names of the biggest fools in the Vijayanagara Kingdom!As expected, the King was furious that his name was at the top and asked Tenali Raman for an explanation. Tenali referred to the horse story, saying the King was a fool to believe that the trader, a stranger, would return after receiving 5000 gold coins.Countering his argument, the King then asked, what happens if/when the trader does come back? In true Tenali humour, he replied saying, in that case, the trader would be a bigger fool, and his name would replace the King’s on the list!"""

# Generate summary
summary = generate_summary(text)

with open("summary.txt", "w") as file:
    file.write(summary)

# Print confirmation message
print("Summary saved to summary.txt")
>>>>>>> 02114d985a0e029ed23a4cdc33e4e602871ec8ec
