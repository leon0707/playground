
1. generate private key to decrypt files
```shell
openssl genrsa -des3 -out private.pem 2048
```
generate a 2048-bit rsa private key using triple des

<https://en.wikipedia.org/wiki/Triple_DES>

2. generate public key to encrypt files
```shell
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```
generate a public key which can be used encrypt files

3. generate temporary symmetric key
```shell
openssl rand -out secret.key 32
```
this key will be used to encrypt file, and only be used once.

4. use temporary key to encrypt files
```shell
openssl aes-256-cbc -in vulnerable_file.txt -out encrypted_file -pass file:secret.key
```

5. encrypt the temporary key using public key
```shell
openssl rsautl -encrypt -inkey public.pem -pubin -in secret.key -out secret.key.enc
rm secret.key
```

6. decrypt the temporary key using private key
```shell
openssl rsautl -decrypt -inkey private.pem -in secret.key.enc -out secret.key
```

7. use decrypted temporary key to decrypt encrypted files
```shell
openssl aes-256-cbc -d -in encrypted_file -out out.txt -pass file:secret.key
```