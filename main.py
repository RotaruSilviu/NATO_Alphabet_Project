import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_df = pandas.DataFrame(data)
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in data_df.iterrows()}


def generate_phonetic():
    user_imput = input("Enter a word: ").upper()
    try:
        user_prompt = [nato_phonetic_alphabet_dict[letter] for letter in user_imput]
    except KeyError:
        print("Please enter a letter from the alphabet.")
        generate_phonetic()
    else:
        print(user_prompt)


generate_phonetic()
