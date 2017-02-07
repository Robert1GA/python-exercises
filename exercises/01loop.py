# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

def p_times(statement,times):
    for i in range (0, times):
        print(statement)

p_times("Hello World",5)
p_times("Guess Who's Back",2)
