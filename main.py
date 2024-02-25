import pandas

# TODO 1. Create a dictionary:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_df = pandas.DataFrame(data)
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in data_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_imput = input("Enter a word: ").upper()
user_prompt = [nato_phonetic_alphabet_dict[letter] for letter in user_imput]
print(user_prompt)
