"C:/Users/d-e-m/Desktop/metin_belgeleri/python-3.12.9-amd64.exe"
import cgi,os
print("Content-Type: text/html;charset=utf-8\n")
print()
form=cgi.FieldStorage()
pn=str(form.getvalue("pname"))
des=str(form.getvalue("description"))
fle=form["filename"]
fn=os.path.basename(fle.filename)
upload_dir=("C:/Users/d-e-m/Desktop/python2/tem"+fn,"wb").write(fle.file.read())
os.makedirs(upload_dir,exist_ok=True)
with open(os.path.join(upload_dir,fn),"wb") as file:
    file.write(fle.file.read())
print("<html>")
print("<body>")
print("center")
print("<h1>ürün adı\n(%s)</h1>"%pn)
print("<img src=tem(%s)>"%fn)
print("<h2>%s</h2>"%des)
print("</center></body></html>")