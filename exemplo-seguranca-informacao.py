import bcrypt

password = "fabio"
hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(f'Senha: {password}\nHash: {hashed}')
for password_ in ["fabio", "joao", "$2b$12$081PLlgErO90aADiOjjNuesaRKir5Wn1unJqrDxpPmgoaHs6cCTLy"]:
    print(f'Checando senha: {password_}')
    isMatch = bcrypt.checkpw(password_.encode("utf-8"), hashed)
    if isMatch:
        print(f'A senha está correta.')
    else:
        print(f'A senha está incorreta.')

print(bcrypt.checkpw(b'$2b$12$081PLlgErO90aADiOjjNuesaRKir5Wn1unJqrDxpPmgoaHs6cCTLy', hashed))