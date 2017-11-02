#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import base64

parser = argparse.ArgumentParser(description="Capture The Flag Tool")
parser.add_argument("-64e", "--base64encode", help="encode base64 string")
parser.add_argument("-64d", "--base64decode", help="decode base64 string")
parser.add_argument("-32e", "--base32encode", help="encode base32 string")
parser.add_argument("-32d", "--base32decode", help="decode base32 string")
parser.add_argument("-16e", "--base16encode", help="encode base16 string")
parser.add_argument("-16d", "--base16decode", help="decode base16 string")
args = parser.parse_args()
 

if args.base64encode:
    encode = base64.b64encode(bytes(args.base64encode, encoding='utf-8'))
    print(encode.decode("utf-8"))

if args.base64decode:
    decode = base64.b64decode(args.base64decode)
    print(decode.decode("utf-8"))

if args.base32encode:
    encode = base64.b32encode(bytes(args.base32encode, encoding='utf-8'))
    print(encode.decode("utf-8"))

if args.base32decode:
    decode = base64.b32decode(args.base32decode)
    print(decode.decode("utf-8"))

if args.base16encode:
    encode = base64.b16encode(bytes(args.base16encode, encoding='utf-8'))
    print(encode.decode("utf-8"))

if args.base16decode:
    decode = base64.b16decode(args.base16decode)
    print(decode.decode("utf-8"))
