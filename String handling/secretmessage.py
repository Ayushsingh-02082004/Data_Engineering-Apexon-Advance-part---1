import re

msg = "233345A28578y5893u938589s93593h"

result =  "" .join(re.findall(r'[a-zA-Z]', msg))

print(result)