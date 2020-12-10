#import dependencies
import re
import os

paragraph_files = []

# add all the .txt files in raw_data directory to paragraph_files collection
for file in os.listdir("raw_data"):
    if file.endswith(".txt"):
        paragraph_files.append("raw_data/" + file)

paragraph_analysis = ""


def LF_ReadParagraph(paragraph_text):
    with open(paragraph_text, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text


def LF_CountWords(paragraph_text):
    word_count = 0
    for word in paragraph_text.split(" "):
        word_count += 1
    return word_count


def LF_CountSentences(paragraph_text):
    sentence_count = 0
    for sentence in re.split("(?<=[.!?]) +", paragraph_text):
        sentence_count += 1
    return sentence_count


def LF_average(numbers_list):
    total = 0.0
    for number in numbers_list:
        total += number
    avg = total / len(numbers_list)
    return avg


# loop through paragraph_files
for paragraph_file in paragraph_files:
    # Read paragraph text file into text variable # add space between period and double quote
    text = LF_ReadParagraph(paragraph_file).replace(
        ".", ". ").replace(".  ", ". ")

    # Count words
    word_count = LF_CountWords(text)

    # Count sentences
    sentence_count = LF_CountSentences(text)

    # declare list to hold word lengths collection
    word_lengths = []
    for word in text.split(" "):
        # append word length to word_lengths collection
        word_lengths.append(len(word))

    # declare list to hold sentence lengths collection
    sentence_lengths = []
    for sentence in re.split("(?<=[.!?]) +", text):
        # append sentence length to sentence_lengths collection
        sentence_word_count = LF_CountWords(sentence)
        sentence_lengths.append(sentence_word_count)

    paragraph_analysis += "---------------------------------------------------\n"
    paragraph_analysis += "Paragraph Analysis " + paragraph_file + " \n"
    paragraph_analysis += "---------------------------------------------------\n"
    paragraph_analysis += "Approximate Word Count: " + str(word_count) + "\n"
    paragraph_analysis += "Approximate Sentence Count: " + \
        str(sentence_count) + "\n"
    paragraph_analysis += "Average Letter Count per Word: " + \
        str(round(LF_average(word_lengths), 2)) + "\n"
    paragraph_analysis += "Average Sentence Length: " + \
        str(round(LF_average(sentence_lengths), 2)) + "\n"

    sentence_lengths
    paragraph_analysis += "\n\n"

# print report to console
print(paragraph_analysis)

paragraph_report = open(os.path.join(
    '', 'Analysis', 'budget_data_report.txt'), "w")
paragraph_report.write(paragraph_analysis)
paragraph_report.close()
