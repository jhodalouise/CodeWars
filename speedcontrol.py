import re

# def to_camel_case(text):
#     final = ''
#     if len(text) == 0:
#         return final
#     else:
#         if re.search('-', text):
#             words = text.split('-')
#         if re.search('_', text):
#             words = text.split('_')
#         c = 1
#         for word in words:
#             if c == 1:
#                 final += word
#                 c += 1
#             else:
#                 word = word.capitalize()
#                 final += word
#         return final

# print(to_camel_case(text))
# print(to_camel_case(''))

def to_camel_case(text):
    final = ''
    if len(text) == 0:
        return final
    else:
        delimiters = re.findall('[^a-zA-Z0-9]', text)
        delimiters = set(delimiters)
        print(delimiters)
        regEx = '|'.join(delimiters)
        words = re.split(regEx, text)
        for i in range(len(words)):
            if i == 0:
                final += words[i]
            else:
                word = words[i].capitalize()
                final += word
        return final

text = "a-Cat-Was_pippi"
# print(to_camel_case(text))
print(text[:1] + text.title()[1:].replace('_', '').replace('-', ''))




    # if re.search('-', text):
    #     words = text.split('-')
    # if re.search('_', text):
    #     words = text.split('_')
    # c = 1
    # for word in words:
    #     if c == 1:
    #         final += word
    #         c += 1
    #     else:
    #         word = word.capitalize()
    #         final += word
    # print(final)
