Regex_Pattern = r"(?<=[13579])[0-9]"    

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))