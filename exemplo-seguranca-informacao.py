import bcrypt

password = "fabio"
hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(f'Senha: {password}\nHash: {hashed}')
for password_ in ["fabio", "joao", "$2b$12$081PLlgErO90aADiOjjNuesaRKir5Wn1unJqrDxpPmgoaHs6cCTLy"]:
    print(f'Checando senha: {password_}')
    isMatch = bcrypt.checkpw(password_.encode("utf-8"), hashed)

    print('A senha está correta') if isMatch else print('A senha está incorreta')

print("\n\nO que acontece se tentarmos checar o hash com ele mesmo?")
print(bcrypt.checkpw(b'$2b$12$081PLlgErO90aADiOjjNuesaRKir5Wn1unJqrDxpPmgoaHs6cCTLy', hashed))
print(bcrypt.checkpw(hashed, hashed))