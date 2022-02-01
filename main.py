import gnupg
import os

gpg = gnupg.GPG("/usr/bin/gpg")
path = ""
my_file = "Extraction_RPPS_Profil1_SavoirFaire.csv.gpg"

with open(path + my_file, "rb") as f:
    status = gpg.decrypt_file(f, passphrase="**********", output = path + my_file +".decrypted")

print(status.ok)
print(status.stderr)
