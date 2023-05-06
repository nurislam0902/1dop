# 1 дз

# def a(b):
#     c = b.title().split()
#     for i in range(len(c)):
#         print(c[i][0], end='')
# a("Кыргызская Республика")
# 2 дз
# def count_words(phrase):
#     words = phrase.split()
#     word_counts = {}
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts

# # count_words()


# # 3 дз
# def is_isogram(word):
#     return len(set(word)) == len(word)

# # is_isogram()


# # 4 дз
# def reverse_number(n):
#     return int(str(n)[::-1])

# # reverse_number()

# # Доп

# def chat_bot():
#     while True:
#         user_input = input('> ')
#         if not user_input:
#             print('Как классно, когда ты молчишь. Продолжай в том же духе!')
#         elif user_input.isupper():
#             print('Успокойся')
#         elif user_input.endswith('?'):
#             print('Конечно!')
#         else:
#             print('Ну и что')
            
            
# # chat_bot()