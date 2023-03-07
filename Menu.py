import random
import string

def makanan_minuman_random(num_words):
    menu = ["apel ", "pisang ", "ceri ", "jeruk ", "peach ", "pir ", "plum ", "anggur ", "semangka ", "nanas ", "lemon ", "jeruk nipis ", "kiwi ", "blueberry ", "raspberry ", "strawberry ", "blackberry ", "aprikot ", "mangga ", "papaya ", "jambu biji ", "fig ", "kurma ", "kelapa ", "alpukat ", "kacang tanah ", "kacang almond ", "kacang mete ", "kacang walnut ", "kacang filbert ", "kacang macadamia ", "kenari ", "pistachio ", "kayu manis ", "jahe ", "bawang putih ", "bawang bombay ", "tomat ", "kentang ", "wortel ", "selery ", "brokoli ", "kembang kol ", "bayam ", "kale ", "selada ", "mentimun ", "zucchini ", "terong ", "lada ", "jamur ", "kacang ", "kacang polong ", "jagung ", "beras ", "pasta ", "roti ", "keju ", "yogurt ", "susu ", "kopi ", "teh ", "air ", "jus ", "soda ", "bir ", "anggur merah "]
    result = " "
    for i in range(num_words):
        word = random.choice(menu)
        result += word.capitalize()
    return result

# User input
while True:
    answer = input("Bingung Mau Makan/Minum Apa? (y/n) ")
    if answer.lower() == "y":
        print("Cobain Makan Atau Minum Ini Deh: " + makanan_minuman_random(3))
        break
    elif answer.lower() == "n":
        print("Ok, jangan bingung ya!")
        break
    else:
        print("Maaf, sulit di mengerti. semoga harimu suram. Mohon jawab dengan 'y' atau 'n'.")
