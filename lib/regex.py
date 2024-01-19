import re

my_pattern = r"[A-z0-9',]+\s[A-z0-9',]+\s[A-z0-9',]+\s[A-z0-9',]+\s[A-z0-9',]+\s[A-z0-9',]+[.?!]"
my_regex = re.compile(my_pattern)

