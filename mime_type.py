''' MIME types are used in numerous internet protocols to associate a media
type (html, image, video ...) with the content sent. The MIME type is
generally inferred from the extension of the file to be sent.
You have to write a program that makes it possible to detect the MIME type of
a file based on its name. '''
n = int(input())
q = int(input())
info = {}

for _ in range(n):
    ext, mt = input().split()
    info[ext.lower()] = mt

mime_type = []
for _ in range(q):
    fname = input().lower()
    if "." in fname:
        ext = fname.rsplit(".", 1)[-1]
        mime_type.append(info.get(ext, "UNKNOWN"))
    else:
        mime_type.append("UNKNOWN")

for mt in mime_type:
    print(mt)
