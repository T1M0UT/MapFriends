"""
16.02.2022
"""
import json
import sys


def data_processor(local_data):
    while True:
        if isinstance(local_data, list) or isinstance(local_data, tuple):
            print(f"There are {len(local_data)} keys in the list:")
            print([x for x in range(len(local_data))])
            print("select a key: ")
            input_str = input()
            if input_str == '':
                return
            while not input_str.isdigit() or \
                    int(input_str) < 0 or \
                    int(input_str) >= len(local_data):
                print("Key is not a digit, try again: ")
                input_str = input()
                if input_str == '':
                    return
            key = int(input_str)
            data_processor(local_data[key])
        elif isinstance(local_data, dict):
            keys = list(local_data.keys())
            print(f"This is an object with {len(keys)} keys")
            print(keys)
            print("select a key: ")
            input_str = input()
            if input_str == '':
                return
            while input_str not in local_data.keys():
                print("There is no such key, try again: ")
                input_str = input()
                if input_str == '':
                    return
            key = input_str
            data_processor(local_data[key])
        else:
            print(local_data)
            print("You've reached the end. To go back press enter")
            key = input()
            if key == '':
                return
            else:
                sys.exit()


def main():
    with open("twitter1.json", "r") as file:
        data = json.load(file)
    data_processor(data)


if __name__ == "__main__":
    main()
