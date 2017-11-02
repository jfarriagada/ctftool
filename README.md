# Capture the flag tool

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
