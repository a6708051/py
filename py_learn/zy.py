s = '\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90';
print(s)
ss = s.encode('raw_unicode_escape')  
print(ss)
sss = ss.decode()
print(sss)

text = '<h3>this is a test!</h3><p>test content</p>'
tx = text.encode();
print(tx)

string = """b'\x1f\x8b\x08\x00/8\xcfX\x02\xff\xa5\x8f[\n\x830\x10E\xb7"\xf3\xdd\x0f\xb1\x8d\x8fn\xa5\x910\x89\x13\x90\xaa\x91$\xd3R\xc4\xbdwl\x97\xe0\xcfp\xb9\xf7p`6\xa0\x18C4\xf9\xb3\x12\xdc\x0b\xf0!\xce\xe6\x85\xd38`\x1e\xc3b~+\\\x8a?\x96\x04\xd9\x80f\x1c\'I\x0f\xd0\xdc\xfa\xa1\xd3|\xa3\n5+\xab\x1a\xcd\xb5\xb5Jn]yi\xbc\x93\xac\xda\xdaj\xee\xdaF\xc8kYV\xd0\x8b\x8f\x13\xc5\x05g:\xebY1\xa5w\x88\xc3)\xcf."t.\xf0\x92\x8d\x8b\x84\x99\x0e\x9f\xc7)\x91,)c\xe6\xe3u\x08O\xd8\xbf.B\xfa\xd12\x01\x00\x00'"""
string_new = string.encode('raw_unicode_escape')
print(string_new)
