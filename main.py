import secrets
import string

alphabet = string.ascii_letters + string.digits
a = ''.join(secrets.choice(alphabet) for i in range(5))
b = ''.join(secrets.choice(alphabet) for i in range(5))
c = ''.join(secrets.choice(alphabet) for i in range(5))
print(str(a),'-',str(b),'-',str(c))


