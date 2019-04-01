import argparse

parser = argparse.ArgumentParser("My parser text")
parser.add_argument("filename", help="filename is required !")
parser.add_argument("filename1", help="filename1 is required !")
parser.add_argument("filename2", help="filename2 is required !")
parser.add_argument("filename3", help="filename3 is required !")
parser.add_argument("filename4", help="filename4 is required !")

if __name__ == '__main__':
    args_list = parser.parse_args()  # remember this !
    print(f"type of variable is {type(args_list)}")  # Namespace Simple object for storing attributes.
    print(f"type of variable is {type(args_list.filename)}")
    for element in args_list.__dict__:
        print(f"{element} <- element of namespace its type {type(element)}")
