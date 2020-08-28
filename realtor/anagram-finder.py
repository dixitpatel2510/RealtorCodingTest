# Complete the anagram function below.
import sys
import datetime
import os

try:
    print("========Welcome to Anagram Finder ========")
    file_name = sys.argv[1]

    while True:
        user_input = input("\nAnagramFinder>")
        if user_input.lower() == 'exit':
            os._exit(1)
        else:
            def anagram(user_input):

                start = datetime.datetime.now()
                sorted_input = sorted(user_input.lower())
                sorted_string = "".join(sorted_input)
                print(sorted_string)

                with open(file_name.lower(), "r") as file:

                    formatted_list = list(file)
                    file_list = []
                    for i in formatted_list:
                        file_list.append(i.strip('\n'))

                    result = []
                    for i in file_list:
                        if len(i) == len(sorted_string):
                            sorted_data = sorted(i)
                            data_string = "".join(sorted_data)

                            if data_string == sorted_string:
                                result.append(i)
                    end = datetime.datetime.now()
                    total_time = end - start
                    final_time = total_time.microseconds // 10000
                    if len(result) != 0:

                        print('{0} Anagrams found for {1} in {2}ms '.format(len(result), user_input, final_time))
                        print(*result, sep=',')
                    else:
                        print('No Anagrams found for {0} in {1}ms '.format(user_input, final_time))


            anagram(user_input)
except:
    print("Please provide a dictionary file.")
