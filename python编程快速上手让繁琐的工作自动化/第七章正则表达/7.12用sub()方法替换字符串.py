import re

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1)
# CENSORED gave the secret documents to CENSORED.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo2 = agentNamesRegex.sub(r'\1sub', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo2)
# Asub told Csub that Esub knew Bsub was a double agent.
