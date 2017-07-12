formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")

print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

#these get printed with single ''s instead of ""s
print (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )

#extra credit
#Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
# Python tries to be efficient and output the 'smallest' possible data, so it uses the single ' character where possible, even though the string uses the " character.
