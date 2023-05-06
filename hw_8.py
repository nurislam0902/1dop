# дз 1

# import random
# language =["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# def rand(langua):
#     random_element = random.choice(langua)
#     with open('texti.txt', 'w') as f:
#         f.write(random_element)
#     print(random_element)
# rand(language)

# дз 2
# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# """
# with open('one_file.txt', 'w') as f:
#     f.write(text)
# with open('two_file.txt', 'w') as f:
#     f.write(text)

# дз 3

# def copy_file(source_file, destination_file):
#     with open(source_file, 'r') as f:
#         text = f.read()

#     with open(destination_file, 'w') as f:
#         f.write(text)


# copy_file('one_file.txt', 'new_file.txt')
