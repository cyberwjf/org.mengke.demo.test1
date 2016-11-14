# org.mengke.demo.test1
first demo project
```python
In [184]: bs=struct.pack('>IIIIIIII',0x0a,0xff,0x05,0x92,0x2d,0x01,0x03,0x2f) #将python数字类型转换成大端序无符号整数字节形式

In [185]: bs
Out[185]: b'\x00\x00\x00\n\x00\x00\x00\xff\x00\x00\x00\x05\x00\x00\x00\x92\x00\x00\x00-\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00/'

In [186]: struct.unpack('>IIIIIIII',bs)
Out[186]: (10, 255, 5, 146, 45, 1, 3, 47)
```

Added python and ruby folder to test.


