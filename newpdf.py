	
#!/usr/bin/python
import gfx

doc = gfx.open("pdf", "/home/hardik/Desktop/sample.pdf")

print "Author:", doc.getInfo("author")
print "Subject:", doc.getInfo("subject")
print "PDF Version:", doc.getInfo("version")