#1 & 2
import re



strings = ['ab', 'abb', 'abbb', 'ba', 'bab']

pattern = r'a(b*)'
pattern_2 = r'a(bb|bbb)'



for string in strings:
    match = re.match(pattern_2, string)
    if match:
        print(f"{string} matches")
    else:
        print(f"{string} does not match")

#3
pattern_3 = r'[a-z]+_[a-z]+'
string = "as_adfs_dsdg_sg"
matches = re.findall(pattern_3, string)

print(*matches)

#4
pattern_4 = r'[A-Z][a-z]+'
string = "Ghjk;Koiudfg"
matches = re.findall(pattern_4, string)

print(*matches)

#5
pattern_5 = r'a.*b$'
string = "ahgb afjsbbj"
matches = bool(re.findall(pattern_5, string))

print(matches)

#6
pattern = r"[ ,.]"

input_string = "fgidf.sgshsdf,swgwhgws.gshs/"
output_string = re.sub(pattern, ":", input_string)
print(output_string)

#7
input_string = "gsdh_sdgsh_sdgsdfh_dfhjd"
words = input_string.split("_")
capital_words = [word.capitalize() if i > 0 else word for i, word in enumerate(words)]

output_string = "".join(capital_words)
print(output_string)

#8
string = "IWantSomeBeer"
result = re.findall('[A-Z][^A-Z]*', string)

print(*result)

#9
string = "IWantAPieceOfPizzaAndACupOfBeer"
result = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

print(result)

#10
camel_string = "CamelAppleBear"
snake_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_string).lower()

print(snake_string)