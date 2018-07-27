import re

phoneRegex = re.compile(r'''(
                        (\d{3}|\(d{3}\))?
                        (\s|-|\.)
                        \d{3}
                        (\s|-|\.)
                        \d{4}
                        (\s*(ext|x|ext. )\s*\d{2,5})?
                        )''', re.VERBOSE)
mo1 = phoneRegex.search("415.555-4242")
print(mo1.group())
# 415.555-4242

