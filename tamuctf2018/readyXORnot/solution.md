### readyXORnot

original data: "El Psy Congroo"
encrypted data: "IFhiPhZNYi0KWiUcCls="
encrypted flag: "I3gDKVh1Lh4EVyMDBFo="


Simple XOR known text attack

```
➜  ~ python             
>>> import pwn
>>> pwn.xor(pwn.b64d('IFhiPhZNYi0KWiUcCls='), 'El Psy Congroo')
'e4Bne4Bne4Bne4'
>>> pwn.xor(pwn.b64d('I3gDKVh1Lh4EVyMDBFo='), 'e4Bne4Bne4Bne4')
'FLAG=Alpacaman'
```
