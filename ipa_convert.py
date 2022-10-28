#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
2022.06.03
kazakh_to_ipa() <> ipa_to_kazakh()
test_kazakh()
turkish_to_ipa() <> ipa_to_turkish()
test_turkish()

2022.07.05
kyrgyz_to_ipa() <> ipa_to_kyrgyz()
test_kyrgyz()
uzbek_to_ipa() <> ipa_to_uzbek()
test_uzbek()
azerbaijani_to_ipa() <> ipa_to_azerbaijani()
test_azerbaijani()
turkmen_to_ipa() <> ipa_to_turkmen()
test_turkmen()

2022.07.07
tatar_to_ipa() <> ipa_to_tatar()
test_tatar()
bashkir_to_ipa() <> ipa_to_bashkir()
test_bashkir()
sakha_to_ipa() <> ipa_to_sakha()
test_sakha()

2022.07.12
experimentally added î and â to turkish_to_ipa()

2022.08.04
uyghur_to_ipa() <> ipa_to_uyghur()
'''

import re
    

# kazakh scripts

def kazakh_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list.
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # three-sound convenience vowels:
    text = re.sub("[Юю]", "ǔ", text)

    # two-sound convenience consonants:
    text = re.sub("[Цц]", "š", text)
    text = re.sub("[Чч]", "ʆ", text)

    # two-sound convenience vowels:
    text = re.sub("[Яя]", "ǎ", text)
    text = re.sub("[Ее]", "ě", text)
    text = re.sub("[Ёё]", "ǒ", text)
    text = re.sub("[Ии]", "ǐ", text)
    text = re.sub("[Уу]", "u", text)

    # single-sound consonants:
    text = re.sub("[Бб]", "b", text)
    text = re.sub("[Вв]", "v", text)
    text = re.sub("[Гг]", "g", text)
    text = re.sub("[Ғғ]", "ɣ", text)
    text = re.sub("[Дд]", "d", text)
    text = re.sub("[Жж]", "ʒ", text)
    text = re.sub("[Зз]", "z", text)
    text = re.sub("[Йй]", "j", text)
    text = re.sub("[Кк]", "k", text)
    text = re.sub("[Ққ]", "q", text)
    text = re.sub("[Лл]", "l", text)
    text = re.sub("[Мм]", "m", text)
    text = re.sub("[Нн]", "n", text)
    text = re.sub("[Ңң]", "ŋ", text)
    text = re.sub("[Пп]", "p", text)
    text = re.sub("[Рр]", "r", text)
    text = re.sub("[Сс]", "s", text)
    text = re.sub("[Тт]", "t", text)
    text = re.sub("[Фф]", "f", text)
    text = re.sub("[Хх]", "x", text)
    text = re.sub("[Һһ]", "h", text)
    text = re.sub("[Шш]", "ʃ", text)
    text = re.sub("[Щщ]", "ɕ", text)
    text = re.sub("[Ъъ]", "ʔ", text)
    text = re.sub("[Ьь]", "ʲ", text)

    # single-sound vowels:
    text = re.sub("[Аа]", "ɑ", text)
    text = re.sub("[Әә]", "æ", text)
    text = re.sub("[Оо]", "ɔ", text)
    text = re.sub("[Өө]", "ɵ", text)
    text = re.sub("[Ұұ]", "ʊ", text)
    text = re.sub("[Үү]", "ʏ", text)
    text = re.sub("[Ыы]", "ɤ", text)
    text = re.sub("[Іі]", "ɪ", text)
    text = re.sub("[Ээ]", "e", text)

    # rules

    '''
    rule 1:
    if [æ], [ě], [ɵ], [ʏ], [ɪ] are followed by [l] and [l] is NOT followed by [æ], [ě], [ɵ], [ʏ], [ɪ], or [ʲ],
    use [ł] instead of [l] (e.g., [kěł], [kěłdɪ], but [kělěmɪn], [marsělʲ]).
    '''
    text = re.sub(r"([æěɵʏɪ])(l)([^æěɵʏɪʲ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letters "о" and "ө", [ɔ] and [ɵ] at the beginning of a word are preceded by [w] (e.g., осы [wɔsɤ] not [ɔsɤ], өзі [wɵzɪ] not [ɵzɪ]).
    '''
    text = re.sub(r"\b([ɔɵ])", r"w\1", text)

    '''
    rule 3
    if the letter "у" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdʒzjkqlłmnŋprstfxhʃɕʔšʆʲ])", r"w\1", text)

    '''
    rule 4:
    if the letter "и" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdʒzjkqlłmnŋprstfxhʃɕʔšʆʲ])", r"i\1", text)

    return text

def ipa_to_kazakh(text):
    # three-sound convenience vowels:
    text = re.sub("ǔ", "ю", text)

    # two-sound convenience consonants:
    text = re.sub("š", "ц", text)
    text = re.sub("ʆ", "ч", text)

    # two-sound convenience vowels:
    text = re.sub("ǎ", "я", text)
    text = re.sub("ě", "е", text)
    text = re.sub("ǒ", "ё", text)
    text = re.sub("ǐ", "и", text)
    text = re.sub("u", "у", text)

    # single-sound consonants:
    text = re.sub("b", "б", text)
    text = re.sub("v", "в", text)
    text = re.sub("g", "г", text)
    text = re.sub("ɣ", "ғ",  text)
    text = re.sub("d", "д", text)
    text = re.sub("ʒ", "ж", text)
    text = re.sub("z", "з", text)
    text = re.sub("j", "й", text)
    text = re.sub("k", "к", text)
    text = re.sub("q", "қ", text)
    text = re.sub("l", "л", text)
    text = re.sub("m", "м", text)
    text = re.sub("n", "н", text)
    text = re.sub("ŋ", "ң", text)
    text = re.sub("p", "п", text)
    text = re.sub("r", "р", text)
    text = re.sub("s", "с", text)
    text = re.sub("t", "т", text)
    text = re.sub("f", "ф", text)
    text = re.sub("x", "х", text)
    text = re.sub("h", "һ", text)
    text = re.sub("ʃ", "ш", text)
    text = re.sub("ɕ", "щ", text)
    text = re.sub("ʔ", "ъ", text)
    text = re.sub("ʲ", "ь", text)

    # single-sound vowels:
    text = re.sub("ɑ", "а", text)
    text = re.sub("æ", "ә", text)
    text = re.sub("ɔ", "о", text)
    text = re.sub("ɵ", "ө", text)
    text = re.sub("ʊ", "ұ", text)
    text = re.sub("ʏ", "ү", text)
    text = re.sub("ɤ", "ы", text)
    text = re.sub("ɪ", "і", text)
    text = re.sub("e", "э", text)

    # anti-rules

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([әеөүі])(ł)([^әеөүіь])", r"\1л\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"\bw([оө])", r"\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"w([бвгғджзйкқлмнңпрстфхһцчшщъьчц])", r"у\1", text)

    '''
    anti-rule 4:
    the symbol [i] is used in one case only, so we can just replace it for и.
    '''
    text = re.sub(r"i", r"и", text)

    '''
    anti-rules for Turkish and Kyrgyz Ǯ, Turkish ł, azerbaijani ḡ, sakha ɲ
    '''
    text = re.sub(r"w([Ǯ])", r"у\1", text)
    text = re.sub(r"Ǯ", r"дж", text)
    text = re.sub(r"ł", r"ль", text)
    text = re.sub(r"ḡ", r"гь", text)
    text = re.sub(r"ɲ", r"нь", text)

    return text

# testing kazakh scripts

def test_kazakh(text):
    input_text = text.lower().split()
    output_text = ipa_to_kazakh(kazakh_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# turkish scripts

def turkish_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list.
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # two-sound convenience consonants:
    text = re.sub("[Cc]", "Ǯ", text)
    text = re.sub("[Çç]", "ʆ", text)

    # two-sound convenience vowels:
    text = re.sub("[İi]", "ǐ", text)
    text = re.sub("[Uu]", "u", text)

    # single-sound consonants:
    text = re.sub("[Jj]", "ʒ", text)
    text = re.sub("[Yy]", "j", text)
    text = re.sub("[Bb]", "b", text)
    text = re.sub("[Dd]", "d", text)
    text = re.sub("[Ff]", "f", text)
    text = re.sub("[Gg]", "g", text)
    text = re.sub("[Ğğ]", "ɣ", text)
    text = re.sub("[Hh]", "h", text)
    text = re.sub("[Kk]", "k", text)
    text = re.sub("[Ll]", "l", text)
    text = re.sub("[Mm]", "m", text)
    text = re.sub("[Nn]", "n", text)
    text = re.sub("[Pp]", "p", text)
    text = re.sub("[Rr]", "r", text)
    text = re.sub("[Ss]", "s", text)
    text = re.sub("[Şş]", "ʃ", text)
    text = re.sub("[Tt]", "t", text)
    text = re.sub("[Vv]", "v", text)
    text = re.sub("[Zz]", "z", text)

    # single-sound vowels:
    text = re.sub("[Aa]", "ɑ", text)
    text = re.sub("[Ee]", "e", text)
    text = re.sub("[Iı]", "ɤ", text)
    text = re.sub("[Oo]", "ɔ", text)
    text = re.sub("[Öö]", "ɵ", text)
    text = re.sub("[Üü]", "ʏ", text)
    text = re.sub("[Îî]", "ǐ", text) # experimentally added
    text = re.sub("[Ââ]", "ɑ", text) # experimentally added


    '''
    rule 1:
    if [e], [ɵ], [ʏ], [i] are followed by [l] and [l] is NOT followed by [e], [ɵ], [ʏ], or [i],
    use [ł] instead of [l] (e.g., [geł], [gełdi], but [gelecek]).
    '''
    text = re.sub(r"([eɵʏǐ])(l)([^eɵʏǐ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letter "u" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdʒzklłmnprstfhʃʆǮ])", r"w\1", text)

    '''
    rule 3:
    if the letter "i" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdʒzklłmnprstfhʃʆǮ])", r"i\1", text)

    return text

def ipa_to_turkish(text):
    # two-sound convenience consonants:
    text = re.sub("Ǯ", "c", text)
    text = re.sub("ʆ", "ç", text)

    # single-sound consonants:
    text = re.sub("j", "y", text)
    text = re.sub("ʒ", "j", text)
    text = re.sub("b", "b", text)
    text = re.sub("d", "d", text)
    text = re.sub("f", "f", text)
    text = re.sub("g", "g", text)
    text = re.sub("ɣ", "ğ", text)
    text = re.sub("h", "h", text)
    text = re.sub("k", "k", text)
    text = re.sub("l", "l", text)
    text = re.sub("m", "m", text)
    text = re.sub("n", "n", text)
    text = re.sub("p", "p", text)
    text = re.sub("r", "r", text)
    text = re.sub("s", "s", text)
    text = re.sub("ʃ", "ş", text)
    text = re.sub("t", "t", text)
    text = re.sub("v", "v", text)
    text = re.sub("z", "z", text)

    # single-sound vowels:
    text = re.sub("ɑ", "a", text)
    text = re.sub("e", "e", text)
    text = re.sub("ɤ", "ı", text)
    text = re.sub("ǐ", "i", text)
    text = re.sub("ɔ", "o", text)
    text = re.sub("ɵ", "ö", text)
    text = re.sub("ʏ", "ü", text)

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([eöüi])(ł)([^eöüi])", r"\1l\3", text)

    '''
    anti-rule 2:
    the symbol [w] is used in one case only, so we can just replace it for u.
    '''
    text = re.sub(r"w", r"u", text)

    '''
    anti-rule 3:
    the symbol [i] is used in one case only, so we can just replace it for i.
    '''
    text = re.sub(r"i", r"i", text)

    return text

# testing turkish scripts

def test_turkish(text):
    input_text = text.lower().split()
    output_text = ipa_to_turkish(turkish_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# kyrgyz scripts

def kyrgyz_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # three-sound convenience vowels:
    text = re.sub("[Юю]", "ǔ", text)

    # two-sound convenience consonants:
    text = re.sub("[Цц]", "š", text)
    text = re.sub("[Чч]", "ʆ", text)
    text = re.sub("[Жж]", "Ǯ", text)

    # two-sound convenience vowels:
    text = re.sub("[Яя]", "ǎ", text)
    text = re.sub("[Ее]", "ě", text)
    text = re.sub("[Ёё]", "ǒ", text)
    text = re.sub("[Ии]", "ǐ", text)
    text = re.sub("[Уу]", "u", text)

    # single-sound consonants:
    text = re.sub("[Бб]", "b", text)
    text = re.sub("[Вв]", "v", text)
    text = re.sub("[Гг]", "g", text)
    text = re.sub("[Дд]", "d", text)
    text = re.sub("[Зз]", "z", text)
    text = re.sub("[Йй]", "j", text)
    text = re.sub("[Кк]", "k", text)
    text = re.sub("[Лл]", "l", text)
    text = re.sub("[Мм]", "m", text)
    text = re.sub("[Нн]", "n", text)
    text = re.sub("[Ңң]", "ŋ", text)
    text = re.sub("[Пп]", "p", text)
    text = re.sub("[Рр]", "r", text)
    text = re.sub("[Сс]", "s", text)
    text = re.sub("[Тт]", "t", text)
    text = re.sub("[Фф]", "f", text)
    text = re.sub("[Хх]", "x", text)
    text = re.sub("[Шш]", "ʃ", text)
    text = re.sub("[Щщ]", "ɕ", text)
    text = re.sub("[Ъъ]", "ʔ", text)
    text = re.sub("[Ьь]", "ʲ", text)

    # single-sound vowels:
    text = re.sub("[Аа]", "ɑ", text)
    text = re.sub("[Оо]", "ɔ", text)
    text = re.sub("[Өө]", "ɵ", text)
    text = re.sub("[Үү]", "ʏ", text)
    text = re.sub("[Ыы]", "ɤ", text)
    text = re.sub("[Ээ]", "e", text)

    # rules 1-4 are similar to those for Kazakh:

    '''
    rule 1:
    if [ě], [ɵ], [ʏ], are followed by [l] and [l] is NOT followed by [ě], [ɵ], [ʏ], or [ʲ],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([ɵʏě])(l)([^ɵʏěʲ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letters "о" and "ө", [ɔ] and [ɵ] at the beginning of a word are followed by [w] (e.g., осы [wɔsɤ] not [ɔsɤ], өзі [wɵzɪ] not [ɵzɪ]).
    '''
    text = re.sub(r"\b([ɔɵ])", r"w\1", text)

    '''
    rule 3
    if the letter "у" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdzjkqlłmnŋprstfxhʃɕʔšʆǮʲ])", r"w\1", text)

    '''
    rule 4:
    if the letter "и" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdzjkqlłmnŋprstfxhʃɕʔšʆǮʲ])", r"i\1", text)

    # rules 5-6 are specific to Kyrgyz:

    '''
    rule 5
    ɑ|ɔ|u|ɤ + k + ɑ|ɔ|u|ɤ
    '''
    text = re.sub(r"([ɑɔwɤ])k", r"\1q", text)
    text = re.sub(r"k([ɑɔuɤ])", r"q\1", text)

    '''
    rule 6
    ɑ|ɔ|u|ɤ + g + ɑ|ɔ|u|ɤ
    '''
    text = re.sub(r"([ɑɔwɤ])g", r"\1ɣ", text)
    text = re.sub(r"g([ɑɔuɤ])", r"ɣ\1", text)

    return text

def ipa_to_kyrgyz(text):
    # three-sound convenience vowels:
    text = re.sub("ǔ", "ю", text)

    # two-sound convenience consonants:
    text = re.sub("š", "ц", text)
    text = re.sub("ʆ", "ч", text)
    text = re.sub("Ǯ", "ж", text)

    # two-sound convenience vowels:
    text = re.sub("ǎ", "я", text)
    text = re.sub("ě", "е", text)
    text = re.sub("ǒ", "ё", text)
    text = re.sub("ǐ", "и", text)
    text = re.sub("u", "у", text)

    # single-sound consonants:
    text = re.sub("b", "б", text)
    text = re.sub("v", "в", text)
    text = re.sub("g", "г", text)
    text = re.sub("ɣ", "г", text)
    text = re.sub("d", "д", text)
    text = re.sub("z", "з", text)
    text = re.sub("j", "й", text)
    text = re.sub("k", "к", text)
    text = re.sub("l", "л", text)
    text = re.sub("m", "м", text)
    text = re.sub("n", "н", text)
    text = re.sub("ŋ", "ң", text)
    text = re.sub("p", "п", text)
    text = re.sub("q", "к", text)
    text = re.sub("r", "р", text)
    text = re.sub("s", "с", text)
    text = re.sub("t", "т", text)
    text = re.sub("f", "ф", text)
    text = re.sub("x", "х", text)
    text = re.sub("ʃ", "ш", text)
    text = re.sub("ɕ", "щ", text)
    text = re.sub("ʔ", "ъ", text)
    text = re.sub("ʲ", "ь", text)

    # single-sound vowels:
    text = re.sub("ɑ", "а", text)
    text = re.sub("ɔ", "о", text)
    text = re.sub("ɵ", "ө", text)
    text = re.sub("ʏ", "ү", text)
    text = re.sub("ɤ", "ы", text)
    text = re.sub("e", "э", text)

    # anti-rules 1-4 are similar to those for Kazakh:

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([өүе])(ł)([^өүеʲ])", r"\1л\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"\bw([оө])", r"\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"w([бвгдзйклмнңпрстфхцчшщъьчцж])", r"у\1", text)

    '''
    anti-rule 4:
    '''
    text = re.sub(r"i([бвгдзйклмнңпрстфхцчшщъьчцж])", r"и\1", text)

    return text

# testing kyrgyz scripts

def test_kyrgyz(text):
    input_text = text.lower().split()
    output_text = ipa_to_kyrgyz(kyrgyz_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# uzbek scripts

def uzbek_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # two-sound convenience consonants:
    text = re.sub("[Jj]", "Ǯ", text)
    text = re.sub("Ch", "ʆ", text)
    text = re.sub("ch", "ʆ", text)

    # two-sound convenience vowels:
    text = re.sub("[Ii]", "ǐ", text)
    text = re.sub("[Uu]", "u", text)

    # single-sound consonants:
    text = re.sub("[Bb]", "b", text)
    text = re.sub("[Dd]", "d", text)
    text = re.sub("[Ff]", "f", text)
    text = re.sub("G‘", "ɣ", text)
    text = re.sub("g‘", "ɣ", text)
    text = re.sub("[Gg]", "g", text)
    text = re.sub("[Hh]", "h", text)
    text = re.sub("[Kk]", "k", text)
    text = re.sub("[Ll]", "l", text)
    text = re.sub("[Mm]", "m", text)
    text = re.sub("[Nn]", "n", text)
    text = re.sub("Ng", "ŋ", text)
    text = re.sub("ng", "ŋ", text)
    text = re.sub("[Pp]", "p", text)
    text = re.sub("[Qq]", "q", text)
    text = re.sub("[Rr]", "r", text)
    text = re.sub("[Ss]", "s", text)
    text = re.sub("Sh", "ʃ", text)
    text = re.sub("sh", "ʃ", text)
    text = re.sub("[Tt]", "t", text)
    text = re.sub("[Vv]", "v", text)
    text = re.sub("[Xx]", "x", text)
    text = re.sub("[Yy]", "j", text)
    text = re.sub("[Zz]", "z", text)

    # single-sound vowels:
    text = re.sub("[Aa]", "æ", text)
    text = re.sub("[Ee]", "e", text)
    text = re.sub("Oʻ", "ɵ", text)
    text = re.sub("oʻ", "ɵ", text)
    text = re.sub("[Oo]", "ɔ", text)

    # hard sign
    text = re.sub("'", "ʔ", text)

    '''
    rule 1:
    if [æ], [e], [ɵ], [ǐ] are followed by [l] and [l] is NOT followed by [æ], [e], [ɵ], [ǐ],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æɵǐe])(l)([^æɵǐe])", r"\1ł\3", text)

    '''
    rule 2:
    if the letter "u" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdzjkqlłmnŋprstfxhʃʔʆǮ])", r"w\1", text)

    '''
    rule 3:
    if the letter "i" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdzjkqlłmnŋprstfxhʃʔʆǮ])", r"i\1", text)

    return text

def ipa_to_uzbek(text):
    # two-sound convenience consonants:
    text = re.sub("j", "y", text)  # exception! precedence issue
    text = re.sub("Ǯ", "j", text)
    text = re.sub("ʆ", "ch", text)

    # two-sound convenience vowels:
    text = re.sub("ǐ", "i", text)
    text = re.sub("u", "u", text)

    # single-sound convenience consonants:
    text = re.sub("b", "b", text)
    text = re.sub("d", "d", text)
    text = re.sub("f", "f", text)
    text = re.sub("g", "g", text)
    text = re.sub("ɣ", "g‘", text)
    text = re.sub("h", "h", text)
    text = re.sub("k", "k", text)
    text = re.sub("l", "l", text)
    text = re.sub("m", "m", text)
    text = re.sub("n", "n", text)
    text = re.sub("ŋ", "ng", text)
    text = re.sub("p", "p", text)
    text = re.sub("q", "q", text)
    text = re.sub("r", "r", text)
    text = re.sub("s", "s", text)
    text = re.sub("ʃ", "sh", text)
    text = re.sub("t", "t", text)
    text = re.sub("v", "v", text)
    text = re.sub("x", "x", text)
    text = re.sub("z", "z", text)

    # single-sound convenience vowels:
    text = re.sub("æ", "a", text)
    text = re.sub("e", "e", text)
    text = re.sub("ɵ", "o‘", text)
    text = re.sub("ɔ", "o", text)

    # hard sign
    text = re.sub("ʔ", "'", text)

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([aei‘])(ł)([^aei‘])", r"\1l\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"w([bcvgɣdjzklmnpqrstfhyx])", r"u\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"i([bcvgɣdjzklmnpqrstfhyx])", r"i\1", text)

    return text

# testing uzbek scripts

def test_uzbek(text):
    input_text = text.lower().split()
    output_text = ipa_to_uzbek(uzbek_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# azerbaijani scripts

def azerbaijani_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # two-sound convenience consonants:
    text = re.sub("[Cc]", "Ǯ", text)
    text = re.sub("[Çç]", "ʆ", text)
    text = re.sub("[Gg]", "ḡ", text)

    # two-sound convenience vowels:
    text = re.sub("[İi]", "ǐ", text)
    text = re.sub("[Uu]", "u", text)

    # single-sound consonants:
    text = re.sub("[Jj]", "ʒ", text)
    text = re.sub("[Yy]", "j", text)
    text = re.sub("[Bb]", "b", text)
    text = re.sub("[Dd]", "d", text)
    text = re.sub("[Ff]", "f", text)
    text = re.sub("[Ğğ]", "ɣ", text)
    text = re.sub("[Hh]", "h", text)
    text = re.sub("[Xx]", "x", text)
    text = re.sub("[Kk]", "k", text)
    text = re.sub("[Qq]", "g", text)
    text = re.sub("[Ll]", "l", text)
    text = re.sub("[Mm]", "m", text)
    text = re.sub("[Nn]", "n", text)
    text = re.sub("[Pp]", "p", text)
    text = re.sub("[Rr]", "r", text)
    text = re.sub("[Ss]", "s", text)
    text = re.sub("[Şş]", "ʃ", text)
    text = re.sub("[Tt]", "t", text)
    text = re.sub("[Vv]", "v", text)
    text = re.sub("[Zz]", "z", text)

    # single-sound vowels:
    text = re.sub("[Aa]", "ɑ", text)
    text = re.sub("[Ee]", "e", text)
    text = re.sub("[Əə]", "æ", text)
    text = re.sub("[Iı]", "ɤ", text)
    text = re.sub("[Oo]", "ɔ", text)
    text = re.sub("[Öö]", "ɵ", text)
    text = re.sub("[Üü]", "ʏ", text)

    '''
    rule 1:
    if [æ], [e], [ɵ], [ʏ], [i] are followed by [l] and [l] is NOT followed by [æ], [e], [ɵ], [ʏ], or [i],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æeɵʏǐ])(l)([^æeɵʏǐ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letter "u" [ʊw] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgḡɣdʒzklłmnprstfhxʃʆǮ])", r"w\1", text)

    '''
    rule 3:
    if the letter "i" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgḡɣdʒzklłmnprstfhxʃʆǮ])", r"i\1", text)

    return text

def ipa_to_azerbaijani(text):
    # two-sound convenience consonants:
    text = re.sub("Ǯ", "c", text)
    text = re.sub("ʆ", "ç", text)
    text = re.sub("g", "q", text)  # precedence issue
    text = re.sub("ḡ", "g", text)

    # single-sound consonants:
    text = re.sub("j", "y", text)
    text = re.sub("ʒ", "j", text)
    text = re.sub("b", "b", text)
    text = re.sub("d", "d", text)
    text = re.sub("f", "f", text)
    text = re.sub("ɣ", "ğ", text)
    text = re.sub("h", "h", text)
    text = re.sub("x", "x", text)
    text = re.sub("k", "k", text)
    text = re.sub("l", "l", text)
    text = re.sub("m", "m", text)
    text = re.sub("n", "n", text)
    text = re.sub("p", "p", text)
    text = re.sub("r", "r", text)
    text = re.sub("s", "s", text)
    text = re.sub("ʃ", "ş", text)
    text = re.sub("t", "t", text)
    text = re.sub("v", "v", text)
    text = re.sub("z", "z", text)

    # single-sound vowels:
    text = re.sub("ɑ", "a", text)
    text = re.sub("e", "e", text)
    text = re.sub("æ", "ə", text)
    text = re.sub("ɤ", "ı", text)
    text = re.sub("ǐ", "i", text)
    text = re.sub("ɔ", "o", text)
    text = re.sub("ɵ", "ö", text)
    text = re.sub("ʏ", "ü", text)

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([əeöüiě])(ł)([^əeöüiě])", r"\1l\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"w([bvgğdjzkqlmnprstfhxşçc])", r"u\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"i([bcvgğdjzkqlmnprstfhxşç])", r"i\1", text)

    return text

# testing azerbaijani scripts

def test_azerbaijani(text):
    input_text = text.lower().split()
    output_text = ipa_to_azerbaijani(azerbaijani_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# turkmen scripts

def turkmen_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # two-sound convenience consonants:
    text = re.sub("[Çç]", "ʆ", text)
    text = re.sub("[Jj]", "Ǯ", text)

    # two-sound convenience vowels:
    text = re.sub("[İi]", "ǐ", text)
    text = re.sub("[Uu]", "u", text)

    # single-sound consonants:
    text = re.sub("[Bb]", "b", text)
    text = re.sub("[Dd]", "d", text)
    text = re.sub("[Ff]", "f", text)
    text = re.sub("[Gg]", "g", text)
    text = re.sub("[Hh]", "h", text)
    text = re.sub("[Žž]", "ʒ", text)
    text = re.sub("[Kk]", "k", text)
    text = re.sub("[Ll]", "l", text)
    text = re.sub("[Mm]", "m", text)
    text = re.sub("[Nn]", "n", text)
    text = re.sub("[Ňň]", "ŋ", text)
    text = re.sub("[Pp]", "p", text)
    text = re.sub("[Rr]", "r", text)
    text = re.sub("[Ss]", "s", text)  # θ
    text = re.sub("[Şş]", "ʃ", text)
    text = re.sub("[Tt]", "t", text)
    text = re.sub("[Ww]", "v", text)
    text = re.sub("[Ýý]", "j", text)
    text = re.sub("[Zz]", "z", text)  # ð

    # single-sound vowels:
    text = re.sub("[Aa]", "ɑ", text)
    text = re.sub("[Ää]", "æ", text)
    text = re.sub("[Ee]", "e", text)
    text = re.sub("[Oo]", "ɔ", text)
    text = re.sub("[Öö]", "ɵ", text)
    text = re.sub("[Üü]", "ʏ", text)
    text = re.sub("[Yy]", "ɤ", text)

    # rules:

    '''
    rule 1:
    if [æ], [e], [ɵ], [ʏ], [i] are followed by [l] and [l] is NOT followed by [æ], [e], [ɵ], [ʏ], or [i],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æeɵʏǐ])(l)([^æeɵʏǐ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letter "u" [ʊw] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣqdʒzkqlłmnprstfhʃʆǮw])", r"w\1", text)

    '''
    rule 3:
    if the letter "i" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣqdʒzkqlłmnprstfhʃʆǮ])", r"i\1", text)

    # rules 4-5 are specific to Turkmen:

    '''
    rule 4:
    a, o, u, y + k + a, o, u, y:
    '''
    text = re.sub(r"k([ɑɔuɤ])", r"q\1", text)
    text = re.sub(r"([ɑɔwɤ])k", r"\1q", text)

    '''
    rule 5:
    a, o, u, y + g + a, o, u, y:
    '''
    text = re.sub(r"g([ɑɔuɤ])", r"ɣ\1", text)
    text = re.sub(r"([ɑɔwɤ])g", r"\1ɣ", text)

    return text

def ipa_to_turkmen(text):
    # two-sound convenience consonants:
    text = re.sub("j", "ý", text)  # precedence issue
    text = re.sub("Ǯ", "j", text)
    text = re.sub("ʆ", "ç", text)

    # single-sound consonants: # w --> v can be found where the letter u anti-rule is
    text = re.sub("b", "b", text)
    text = re.sub("d", "d", text)
    text = re.sub("f", "f", text)
    text = re.sub("g", "g", text)
    text = re.sub("ɣ", "g", text)
    text = re.sub("h", "h", text)
    text = re.sub("ʒ", "ž", text)
    text = re.sub("k", "k", text)
    text = re.sub("q", "k", text)
    text = re.sub("l", "l", text)
    text = re.sub("m", "m", text)
    text = re.sub("n", "n", text)
    text = re.sub("ŋ", "ň", text)
    text = re.sub("p", "p", text)
    text = re.sub("r", "r", text)
    text = re.sub("s", "s", text)
    text = re.sub("ʃ", "ş", text)
    text = re.sub("t", "t", text)
    text = re.sub("z", "z", text)

    # single-sound vowels:
    text = re.sub("ɑ", "a", text)
    text = re.sub("e", "e", text)
    text = re.sub("æ", "ä", text)
    text = re.sub("ǐ", "i", text)
    text = re.sub("ɔ", "o", text)
    text = re.sub("ɵ", "ö", text)
    text = re.sub("ʏ", "ü", text)
    text = re.sub("ɤ", "y", text)

    # anti-rules:

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([äeöüiě])(ł)([^äeöüiě])", r"\1l\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"w([bdfghžklmnňprsştýzjçɣqv])", r"u\1", text)  # precedence issue
    text = re.sub("v", "w", text)  # precedence issue

    '''
    anti-rule 3:
    '''
    text = re.sub(r"i([bdfghžklmnňprsştwýzjçɣq])", r"i\1", text)

    return text

# testing turkmen scripts

def test_turkmen(text):
    input_text = text.lower().split()
    output_text = ipa_to_turkmen(turkmen_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# tatar scripts

def tatar_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # three-sound convenience vowels:
    text = re.sub("[Юю]", "ǔ", text)

    # two-sound convenience consonants:
    text = re.sub("[Цц]", "š", text)
    text = re.sub("[Чч]", "ʆ", text)
    text = re.sub("[Җҗ]", "Ǯ", text)

    # two-sound convenience vowels:
    text = re.sub("[Яя]", "ǎ", text)
    text = re.sub("[Ее]", "ě", text)
    text = re.sub("[Ёё]", "ǒ", text)
    text = re.sub("[Ии]", "ǐ", text)
    text = re.sub("[Уу]", "u", text)

    # single-sound consonants:
    text = re.sub("[Бб]", "b", text)
    text = re.sub("[Вв]", "v", text)
    text = re.sub("[Гг]", "g", text)
    text = re.sub("[Дд]", "d", text)
    text = re.sub("[Жж]", "ʒ", text)
    text = re.sub("[Зз]", "z", text)
    text = re.sub("[Йй]", "j", text)
    text = re.sub("[Кк]", "k", text)
    text = re.sub("[Лл]", "l", text)
    text = re.sub("[Мм]", "m", text)
    text = re.sub("[Нн]", "n", text)
    text = re.sub("[Ңң]", "ŋ", text)
    text = re.sub("[Пп]", "p", text)
    text = re.sub("[Рр]", "r", text)
    text = re.sub("[Сс]", "s", text)
    text = re.sub("[Тт]", "t", text)
    text = re.sub("[Фф]", "f", text)
    text = re.sub("[Хх]", "x", text)
    text = re.sub("[Һһ]", "h", text)
    text = re.sub("[Шш]", "ʃ", text)
    text = re.sub("[Щщ]", "ɕ", text)
    text = re.sub("[Ъъ]", "ʔ", text)
    text = re.sub("[Ьь]", "ʲ", text)

    # single-sound vowels:
    text = re.sub("[Аа]", "ɑ", text)
    text = re.sub("[Әә]", "æ", text)
    text = re.sub("[Оо]", "ɔ", text)
    text = re.sub("[Өө]", "ɵ", text)
    text = re.sub("[Үү]", "ʏ", text)
    text = re.sub("[Ыы]", "ɤ", text)
    text = re.sub("[Ээ]", "e", text)

    # rules 1-4 are similar to those for Kazakh:

    '''
    rule 1:
    if [ě], [ɵ], [ʏ], are followed by [l] and [l] is NOT followed by [ě], [ɵ], [ʏ], or [ʲ],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æɵʏě])(l)([^æɵʏěʲ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letters "о" and "ө", [ɔ] and [ɵ] at the beginning of a word are followed by [w] (e.g., осы [wɔsɤ] not [ɔsɤ], өзі [wɵzɪ] not [ɵzɪ]).
    '''
    text = re.sub(r"\b([ɔɵ])", r"w\1", text)

    '''
    rule 3
    if the letter "у" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdʒzjkqlłmnŋprstfxhʃɕʔšʆǮʲ])", r"w\1", text)

    '''
    rule 4:
    if the letter "и" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdʒzjkqlłmnŋprstfxhʃɕʔšʆǮʲ])", r"i\1", text)

    # rules 5-6 are specific to Tatar:

    '''
    rule 5:
    а, о, у, ы, ъ + к + а, о, у, ы, ъ
    '''
    text = re.sub(r"k([ɑɔwɤʔ])", r"q\1", text)
    text = re.sub(r"([ɑɔwɤʔ])k", r"\1q", text)

    '''
    rule 6:
    а, о, у, ы, ъ + г + а, о, у, ы, ъ
    '''
    text = re.sub(r"g([ɑɔwɤʔ])", r"ɣ\1", text)
    text = re.sub(r"([ɑɔwɤʔ])g", r"\1ɣ", text)

    return text

def ipa_to_tatar(text):
    # three-sound convenience vowels:
    text = re.sub("ǔ", "ю", text)

    # two-sound convenience consonants:
    text = re.sub("š", "ц", text)
    text = re.sub("ʆ", "ч", text)
    text = re.sub("Ǯ", "җ", text)

    # two-sound convenience vowels:
    text = re.sub("ǎ", "я", text)
    text = re.sub("ě", "е", text)
    text = re.sub("ǒ", "ё", text)
    text = re.sub("ǐ", "и", text)
    text = re.sub("u", "у", text)

    # single-sound consonants:
    text = re.sub("b", "б", text)
    text = re.sub("v", "в", text)
    text = re.sub("g", "г", text)
    text = re.sub("ɣ", "г", text)
    text = re.sub("d", "д", text)
    text = re.sub("ʒ", "ж", text)
    text = re.sub("z", "з", text)
    text = re.sub("j", "й", text)
    text = re.sub("k", "к", text)
    text = re.sub("l", "л", text)
    text = re.sub("m", "м", text)
    text = re.sub("n", "н", text)
    text = re.sub("ŋ", "ң", text)
    text = re.sub("p", "п", text)
    text = re.sub("q", "к", text)
    text = re.sub("r", "р", text)
    text = re.sub("s", "с", text)
    text = re.sub("t", "т", text)
    text = re.sub("f", "ф", text)
    text = re.sub("x", "х", text)
    text = re.sub("h", "һ", text)
    text = re.sub("ʃ", "ш", text)
    text = re.sub("ɕ", "щ", text)
    text = re.sub("ʔ", "ъ", text)
    text = re.sub("ʲ", "ь", text)

    # single-sound vowels:
    text = re.sub("ɑ", "а", text)
    text = re.sub("æ", "ә", text)
    text = re.sub("ɔ", "о", text)
    text = re.sub("ɵ", "ө", text)
    text = re.sub("ʏ", "ү", text)
    text = re.sub("ɤ", "ы", text)
    text = re.sub("e", "э", text)

    # anti-rules 1-4 are similar to those for Kazakh:

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([әөүе])(ł)([^әөүеʲ])", r"\1л\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"\bw([оө])", r"\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"w([бвгдзйклмнңпрстфхһцчшщъьчцжҗqɣ])", r"у\1", text)

    '''
    anti-rule 4:
    '''
    text = re.sub(r"i([бвгдзйклмнңпрстфхһцчшщъьчцжҗqɣ])", r"и\1", text)

    return text

# testing tatar scripts

def test_tatar(text):
    input_text = text.lower().split()
    output_text = ipa_to_tatar(tatar_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# bashkir scripts

def bashkir_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we shall later convert them to conventional symbols.

    # three-sound convenience vowels:
    text = re.sub("[Юю]", "ǔ", text)

    # two-sound convenience consonants:
    text = re.sub("[Цц]", "š", text)
    text = re.sub("[Чч]", "ʆ", text)

    # two-sound convenience vowels:
    text = re.sub("[Яя]", "ǎ", text)
    text = re.sub("[Ее]", "ě", text)
    text = re.sub("[Ёё]", "ǒ", text)
    text = re.sub("[Ии]", "ǐ", text)
    text = re.sub("[Уу]", "u", text)

    # single-sound consonants:
    text = re.sub("[Бб]", "b", text)
    text = re.sub("[Вв]", "v", text)
    text = re.sub("[Гг]", "g", text)
    text = re.sub("[Ғғ]", "ɣ", text)
    text = re.sub("[Дд]", "d", text)
    text = re.sub("[Ҙҙ]", "z", text)
    text = re.sub("[Жж]", "ʒ", text)
    text = re.sub("[Зз]", "z", text)
    text = re.sub("[Йй]", "j", text)
    text = re.sub("[Кк]", "k", text)
    text = re.sub("[Ҡҡ]", "q", text)
    text = re.sub("[Лл]", "l", text)
    text = re.sub("[Мм]", "m", text)
    text = re.sub("[Нн]", "n", text)
    text = re.sub("[Ңң]", "ŋ", text)
    text = re.sub("[Пп]", "p", text)
    text = re.sub("[Рр]", "r", text)
    text = re.sub("[Сс]", "s", text)
    text = re.sub("[Ҫҫ]", "s", text)
    text = re.sub("[Тт]", "t", text)
    text = re.sub("[Хх]", "x", text)
    text = re.sub("[Фф]", "f", text)
    text = re.sub("[Һһ]", "h", text)
    text = re.sub("[Шш]", "ʃ", text)
    text = re.sub("[Щщ]", "ɕ", text)
    text = re.sub("[Ъъ]", "ʔ", text)
    text = re.sub("[Ьь]", "ʲ", text)

    # single-sound vowels:
    text = re.sub("[Аа]", "ɑ", text)
    text = re.sub("[Әә]", "æ", text)
    text = re.sub("[Оо]", "ɔ", text)
    text = re.sub("[Өө]", "ɵ", text)
    text = re.sub("[Үү]", "ʏ", text)
    text = re.sub("[Ыы]", "ɤ", text)
    text = re.sub("[Ээ]", "e", text)

    # rules 1-4 are similar to those for Kazakh:

    '''
    rule 1:
    if [ě], [ɵ], [ʏ], are followed by [l] and [l] is NOT followed by [ě], [ɵ], [ʏ], or [ʲ],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æɵʏě])(l)([^æɵʏěʲ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letters "о" and "ө", [ɔ] and [ɵ] at the beginning of a word are followed by [w] (e.g., осы [wɔsɤ] not [ɔsɤ], өзі [wɵzɪ] not [ɵzɪ]).
    '''
    text = re.sub(r"\b([ɔɵ])", r"w\1", text)

    '''
    rule 3
    if the letter "у" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdʒzjkqlłmnŋprstfxhʃɕʔšʆʲ])", r"w\1", text)

    '''
    rule 4:
    if the letter "и" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdʒzjkqlłmnŋprstfxhʃɕʔšʆʲ])", r"i\1", text)

    return text

def ipa_to_bashkir(text):
    # three-sound convenience vowels:
    text = re.sub("ǔ", "ю", text)

    # two-sound convenience consonants:
    text = re.sub("š", "ц", text)
    text = re.sub("ʆ", "ч", text)

    # two-sound convenience vowels:
    text = re.sub("ě", "е", text)
    text = re.sub("ǒ", "ё", text)
    text = re.sub("ǐ", "и", text)
    text = re.sub("u", "у", text)
    text = re.sub("ǎ", "я", text)

    # single-sound consonants:
    text = re.sub("b", "б", text)
    text = re.sub("v", "в", text)
    text = re.sub("g", "г", text)
    text = re.sub("ɣ", "ғ", text)
    text = re.sub("d", "д", text)
    text = re.sub("z", "з", text)
    text = re.sub("ʒ", "ж", text)
    text = re.sub("j", "й", text)
    text = re.sub("k", "к", text)
    text = re.sub("q", "ҡ", text)
    text = re.sub("l", "л", text)
    text = re.sub("m", "м", text)
    text = re.sub("n", "н", text)
    text = re.sub("ŋ", "ң", text)
    text = re.sub("p", "п", text)
    text = re.sub("r", "р", text)
    text = re.sub("s", "с", text)
    text = re.sub("t", "т", text)
    text = re.sub("f", "ф", text)
    text = re.sub("x", "х", text)
    text = re.sub("h", "һ", text)
    text = re.sub("ʃ", "ш", text)
    text = re.sub("ɕ", "щ", text)
    text = re.sub("ʔ", "ъ", text)
    text = re.sub("ʲ", "ь", text)

    # single-sound vowels:
    text = re.sub("ɑ", "а", text)
    text = re.sub("æ", "ә", text)
    text = re.sub("ɔ", "о", text)
    text = re.sub("ɵ", "ө", text)
    text = re.sub("ʏ", "ү", text)
    text = re.sub("ɤ", "ы", text)
    text = re.sub("e", "э", text)

    # anti-rules 1-4 are similar to those for Kazakh:

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([әөүе])(ł)([^әөүеʲ])", r"\1л\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"\bw([оө])", r"\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"w([бвгғдзйкҡлмнңпрстфхһцчшщъьчцж])", r"у\1", text)

    '''
    anti-rule 4:


    '''
    text = re.sub(r"i([бвгғдзйкҡлмнңпрстфхһцчшщъьчцж])", r"и\1", text)

    return text

# testing bashkir scripts

def test_bashkir(text):
    input_text = text.lower().split()
    output_text = ipa_to_bashkir(bashkir_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# sakha scripts

def sakha_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # three-sound convenience vowels:
    text = re.sub("[Юю]", "ǔ", text)

    # two-sound convenience consonants:
    text = re.sub("[Цц]", "š", text)
    text = re.sub("[Чч]", "ʆ", text)
    text = re.sub("ДЬ", "Ǯ", text)
    text = re.sub("дь", "Ǯ", text)
    text = re.sub("Дь", "Ǯ", text)
    text = re.sub("дЬ", "Ǯ", text)
    text = re.sub("НЬ", "ɲ", text)
    text = re.sub("нь", "ɲ", text)
    text = re.sub("Нь", "ɲ", text)
    text = re.sub("нЬ", "ɲ", text)

    # two-sound convenience vowels:
    text = re.sub("[Яя]", "ǎ", text)
    text = re.sub("[Ее]", "ě", text)
    text = re.sub("[Ёё]", "ǒ", text)
    text = re.sub("[Ии]", "ǐ", text)
    text = re.sub("[Уу]", "u", text)

    # single-sound consonants:
    text = re.sub("[Бб]", "b", text)
    text = re.sub("[Вв]", "v", text)
    text = re.sub("[Гг]", "g", text)
    text = re.sub("[Ҕҕ]", "ɣ", text)
    text = re.sub("[Дд]", "d", text)
    text = re.sub("[Жж]", "ʒ", text)
    text = re.sub("[Зз]", "z", text)
    text = re.sub("[Йй]", "j", text)
    text = re.sub("[Кк]", "k", text)
    text = re.sub("[Лл]", "l", text)
    text = re.sub("[Мм]", "m", text)
    text = re.sub("[Нн]", "n", text)
    text = re.sub("[Ҥҥ]", "ŋ", text)
    text = re.sub("[Пп]", "p", text)
    text = re.sub("[Рр]", "r", text)
    text = re.sub("[Сс]", "s", text)
    text = re.sub("[Тт]", "t", text)
    text = re.sub("[Хх]", "x", text)
    text = re.sub("[Фф]", "f", text)
    text = re.sub("[Һһ]", "h", text)
    text = re.sub("[Шш]", "ʃ", text)
    text = re.sub("[Щщ]", "ɕ", text)
    text = re.sub("[Ъъ]", "ʔ", text)
    text = re.sub("[Ьь]", "ʲ", text)

    # single-sound vowels:
    text = re.sub("[Аа]", "ɑ", text)
    text = re.sub("[Әә]", "æ", text)
    text = re.sub("[Оо]", "ɔ", text)
    text = re.sub("[Өө]", "ɵ", text)
    text = re.sub("[Үү]", "ʏ", text)
    text = re.sub("[Ыы]", "ɤ", text)
    text = re.sub("[Ээ]", "e", text)

    # rules 1-4 are similar to those for Kazakh:

    '''
    rule 1:
    if [ě], [ɵ], [ʏ], are followed by [l] and [l] is NOT followed by [ě], [ɵ], [ʏ], or [ʲ],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æɵʏě])(l)([^æɵʏěʲ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letters "о" and "ө", [ɔ] and [ɵ] at the beginning of a word are followed by [w] (e.g., осы [wɔsɤ] not [ɔsɤ], өзі [wɵzɪ] not [ɵzɪ]).
    '''
    text = re.sub(r"\b([ɔɵ])", r"w\1", text)

    '''
    rule 3
    if the letter "у" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdʒzjklłmnŋɲprstfxhʃɕʔšʆǮʲ])", r"w\1", text)

    '''
    rule 4:
    if the letter "и" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdʒzjklłmnŋɲprstfxhʃɕʔšʆǮʲ])", r"i\1", text)

    return text

def ipa_to_sakha(text):
    # three-sound convenience vowels:
    text = re.sub("ǔ", "ю", text)

    # two-sound convenience consonants:
    text = re.sub("š", "ц", text)
    text = re.sub("ʆ", "ч", text)
    text = re.sub("Ǯ", "дь", text)
    text = re.sub("ɲ", "нь", text)

    # two-sound convenience vowels:
    text = re.sub("ě", "е", text)
    text = re.sub("ǒ", "ё", text)
    text = re.sub("ǐ", "и", text)
    text = re.sub("u", "у", text)
    text = re.sub("ǎ", "я", text)

    # single-sound consonants:
    text = re.sub("b", "б", text)
    text = re.sub("v", "в", text)
    text = re.sub("g", "г", text)
    text = re.sub("ɣ", "ҕ", text)
    text = re.sub("d", "д", text)
    text = re.sub("z", "з", text)
    text = re.sub("ʒ", "ж", text)
    text = re.sub("j", "й", text)
    text = re.sub("k", "к", text)
    text = re.sub("l", "л", text)
    text = re.sub("m", "м", text)
    text = re.sub("n", "н", text)
    text = re.sub("ŋ", "ҥ", text)
    text = re.sub("p", "п", text)
    text = re.sub("r", "р", text)
    text = re.sub("s", "с", text)
    text = re.sub("t", "т", text)
    text = re.sub("f", "ф", text)
    text = re.sub("x", "х", text)
    text = re.sub("h", "һ", text)
    text = re.sub("ʃ", "ш", text)
    text = re.sub("ɕ", "щ", text)
    text = re.sub("ʔ", "ъ", text)
    text = re.sub("ʲ", "ь", text)

    # single-sound vowels:
    text = re.sub("ɑ", "а", text)
    text = re.sub("æ", "ә", text)
    text = re.sub("ɔ", "о", text)
    text = re.sub("ɵ", "ө", text)
    text = re.sub("ʏ", "ү", text)
    text = re.sub("ɤ", "ы", text)
    text = re.sub("e", "э", text)

    # anti-rules 1-4 are similar to those for Kazakh:

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([әөүе])(ł)([^әөүеʲ])", r"\1л\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"\bw([оө])", r"\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"w(дь)", r"у\1", text)
    text = re.sub(r"w(нь)", r"у\1", text)
    text = re.sub(r"w([бвгҕдзйклмнҥпрстфхһцчшщъьчцж])", r"у\1", text)

    '''
    anti-rule 4:
    '''
    text = re.sub(r"i(дь)", r"и\1", text)
    text = re.sub(r"i(нь)", r"и\1", text)
    text = re.sub(r"i([бвгҕдзйклмнҥпрстфхһцчшщъьчцж])", r"и\1", text)

    return text

# testing sakha scripts

# testing bashkir scripts

def test_sakha(text):
    input_text = text.lower().split()
    output_text = ipa_to_sakha(sakha_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)

# uyghur scripts

def uyghur_to_ipa(text):
    # we shall begin with sound combinations:
    # the longer a combination, the upper it is on the list
    # single sounds should go to the bottom, with consonants taking precedence over vowels.
    # consonants are less likely to change than vowels.

    # for convenience, we shall use single symbols to denote multiple-sound combinations.
    # we can later convert them to conventional symbols.

    # two-sound convenience consonants:
    text = re.sub("[Jj]", "Ǯ", text)
    text = re.sub("Ch", "ʆ", text)
    text = re.sub("ch", "ʆ", text)

    # two-sound convenience vowels:
    text = re.sub("[Ii]", "ǐ", text)
    text = re.sub("[Uu]", "u", text)

    # single-sound consonants:
    text = re.sub("[Bb]", "b", text)
    text = re.sub("[Dd]", "d", text)
    text = re.sub("[Ff]", "f", text)
    text = re.sub("Gh", "ɣ", text)
    text = re.sub("gh", "ɣ", text)
    text = re.sub("[Gg]", "g", text)
    text = re.sub("[Hh]", "h", text)
    text = re.sub("[Kk]", "k", text)
    text = re.sub("[Ll]", "l", text)
    text = re.sub("[Mm]", "m", text)
    text = re.sub("[Nn]", "n", text)
    text = re.sub("Ng", "ŋ", text)
    text = re.sub("ng", "ŋ", text)
    text = re.sub("[Pp]", "p", text)
    text = re.sub("[Qq]", "q", text)
    text = re.sub("[Rr]", "r", text)
    text = re.sub("[Ss]", "s", text)
    text = re.sub("Sh", "ʃ", text)
    text = re.sub("sh", "ʃ", text)
    text = re.sub("[Tt]", "t", text)
    text = re.sub("[Ww]", "v", text)
    text = re.sub("[Xx]", "x", text)
    text = re.sub("[Yy]", "j", text)
    text = re.sub("[Zz]", "z", text)
    text = re.sub("Zh", "ʒ", text)
    text = re.sub("zh", "ʒ", text)

    # single-sound vowels:
    text = re.sub("[Aa]", "ɑ", text)
    text = re.sub("[Ee]", "æ", text)
    text = re.sub("[ËÉëé]", "e", text)
    text = re.sub("[Oo]", "ɔ", text)
    text = re.sub("[Öö]", "ɵ", text)
    text = re.sub("[Üü]", "ʏ", text)

    # hard sign
    text = re.sub("'", "ʔ", text)

    '''
    rule 1:
    if [æ], [e], [ɵ], [ǐ] are followed by [l] and [l] is NOT followed by [æ], [e], [ɵ], [ǐ],
    use [ł] instead of [l].
    '''
    text = re.sub(r"([æɵǐeʏ])(l)([^æɵǐeʏ])", r"\1ł\3", text)

    '''
    rule 2:
    if the letter "u" [u] is followed by consonants, use [w] instead of [u].
    '''
    text = re.sub(r"u([bvgɣdzjkqlłmnŋprstfxhʃʆǮʒ])", r"w\1", text)

    '''
    rule 3:
    if the letter "i" [ǐ] is followed by consonants, use [i] instead of [ǐ].
    '''
    text = re.sub(r"ǐ([bvgɣdzjkqlłmnŋprstfxhʃʆǮʒ])", r"i\1", text)

    return text

def ipa_to_uyghur(text):
    # two-sound convenience consonants:
    text = re.sub("j", "y", text)  # exception! precedence issue
    text = re.sub("Ǯ", "j", text)
    text = re.sub("ʆ", "ch", text)
    text = re.sub("ʒ", "zh", text)

    # two-sound convenience vowels:
    text = re.sub("ǐ", "i", text)
    text = re.sub("u", "u", text)

    # single-sound convenience consonants:
    text = re.sub("b", "b", text)
    text = re.sub("d", "d", text)
    text = re.sub("f", "f", text)
    text = re.sub("g", "g", text)
    text = re.sub("ɣ", "gh", text)
    text = re.sub("h", "h", text)
    text = re.sub("k", "k", text)
    text = re.sub("l", "l", text)
    text = re.sub("m", "m", text)
    text = re.sub("n", "n", text)
    text = re.sub("ŋ", "ng", text)
    text = re.sub("p", "p", text)
    text = re.sub("q", "q", text)
    text = re.sub("r", "r", text)
    text = re.sub("s", "s", text)
    text = re.sub("ʃ", "sh", text)
    text = re.sub("t", "t", text)
    text = re.sub("v", "w", text)
    text = re.sub("x", "x", text)
    text = re.sub("z", "z", text)

    # single-sound convenience vowels:
    text = re.sub("ɑ", "a", text)
    text = re.sub("e", "ë", text) # precedence
    text = re.sub("æ", "e", text)
    text = re.sub("ɵ", "ö", text)
    text = re.sub("ɔ", "o", text)
    text = re.sub("ʏ", "ü", text)

    # hard sign
    text = re.sub("ʔ", "'", text)

    '''
    anti-rule 1:
    '''
    text = re.sub(r"([eëiöü])(ł)([^eëiöü])", r"\1l\3", text)

    '''
    anti-rule 2:
    '''
    text = re.sub(r"w([bcvgdjzklmnpqrstfhyx])", r"u\1", text)

    '''
    anti-rule 3:
    '''
    text = re.sub(r"i([bcvgdjzklmnpqrstfhyx])", r"i\1", text)

    return text

# testing uyghur scripts

def test_uyghur(text):
    input_text = text.lower().split()
    output_text = ipa_to_uyghur(uyghur_to_ipa(text)).split()

    input_difference = []
    output_difference = []
    for item in input_text:
        if item not in output_text:
            input_difference.append(item)
    for item in output_text:
        if item not in input_text:
            output_difference.append(item)

    if input_text == output_text:
        print("input text and output text -- identical")
    else:
        print("input text and output text -- different")
        print("input:", input_difference)
        print("output:", output_difference)