comand=""
while comand!="exit":
    comand=(input("perintah="))

    if comand=="exit":
        break

    if comand !="+"and comand !="-" and comand!="*"and comand!="/"and comand!="**"and comand!="%"and comand!="&"and comand!="|"and comand!="^"and comand!="~":
        print("Tidak dikenali")
        continue
    a=int(input("Masukkan angka pertama="))
    b=int(input("Masukkan angka kedua="))

    if comand=="+":
        jawaban=a+b
    elif comand=="-":
        jawaban=a-b
    elif comand=="*":
        jawaban=a*b
    elif comand=="/":
        jawaban=a/b
    elif comand=="**":
        jawaban=a**b
    elif comand=="%":
        jawaban=a%b
    elif comand=="&":
        jawaban=a&b
    elif comand=="|":
        jawaban=a|b
    elif comand=="^":
        jawaban=a^b

    



    print(f"hasil:{jawaban}")


print("Terima Kasih")

