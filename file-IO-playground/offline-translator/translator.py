from translate import Translator

try:
    with open("./short.txt", mode='r') as my_file:
        text = my_file.read()
        translator = Translator(to_lang='ja')
        translation = translator.translate(text)
        with open('short_ja.txt', mode='w',  encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError:
    print("File not  found my boy")

japanese = translator.translate("This is a pen")
print(japanese)