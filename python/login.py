import random
import string
from string import Formatter
from string import Template

# user_name="".join(random.choices((string.ascii_lowercase),k=8))
# print(user_name)
# user_pass="".join(random.choices((string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation),k=8))
# print(user_pass)

# formatter=Formatter()
# # print(formatter.format('{user_name}',user_name='admin'))
# print(formatter.format("{} {user_name} {}","merhaba","görkem",user_name='admin'))

# T=Template("Kulanıcı adı= $user_name \nkulanıcı şifresi= $user_pass \nSon giriş tarihi= $user_log").substitute(user_name='Görkem',user_pass="123456",user_log="12.02.2025")
# print(T)
