# Capture the flag tool

### TODO

- [x] Base 64 encode
- [x] Base 64 decode
- [x] Base 32 encode
- [x] Base 32 decode
- [ ] Md5

## Base64encode and Base64decode

```shell
$ python ctftool.py -64e demo
ZGVtbw==
$ python ctftool.py -64d ZGVtbw==
demo
```

## Base32encode and Base32decode

```shell
$ python ctftool.py -32e demo
MRSW23Y=
$ python ctftool.py -32d MRSW23Y=
demo
```


## Base16encode and Base16decode
```shell
$ python ctftool.py -16e demo
64656D6F
$ python ctftool.py -16d 64656D6F
demo
```
