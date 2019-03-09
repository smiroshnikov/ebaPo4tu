import sys

print(f"\nFirst Argument is PATH TO FILE ! \n{sys.argv[0]}")
print(f"\nFirst Argument is PATH TO FILE ! \n{sys.argv[1:]}")
for arg in sys.argv:
    if arg == 'test1' or arg == 'test2':
        print(f"I have received <<{arg}>> ".upper())
    elif arg == 'test5':
        print('test5 is true , cancelling.... ')

print(sys.argv.__len__())

# argv is not the most robust things to use
# people will always use my code wrong
# we will handle this with error handling
