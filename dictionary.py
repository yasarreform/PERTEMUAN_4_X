siswa = ["Anda","XI",85]
print(siswa[0])
print(siswa[1])
print(siswa[2])

siswa={"nama":"Andi","kelas":"XI","nilai":85}
print(siswa["nama"])
print(siswa["kelas"])
print(siswa["nilai"])

#print(siswa["jurusan"])

print(siswa.get("nama"))
print(siswa.get("jurusan"))
print(siswa.get("jurusan", "Belum diisi"))

siswa["nilai"]=90
siswa["jurusan"]="IPA"
siswa["minat"]="Coding"

del siswa["minat"]

print(siswa.keys())
print(siswa.values())
print(siswa.items())
print(len(siswa))