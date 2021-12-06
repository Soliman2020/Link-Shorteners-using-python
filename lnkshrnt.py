step 1 : install the module pyshorteners
step 2 : start coding .....
  
  
  
import pyshorteners
s = pyshorteners.Shortener()    
link = input("Enter the Link : ")


newlink = s.clckru.short(link)        # Clck.ru shortener
# newlink = s.tinyurl.short(link)       #TinyURL.com shortener
# newlink = s.bitly.short(link)         #Bit.ly shortener
# newlink = s.chilpit.short(link)       #Chilp.it shortener
# newlink = s.cuttly.short(link)        #Cutt.ly shortener
# newlink = s.dagd.short(link)          #Da.gd shortener
# newlink = s.gitio.short(link)         #Git.io shortener 
# newlink = s.isgd.short(link)          #Is.gd shortener
# newlink = s.osdb.short(link)          #Os.db shortener
# newlink = s.nullpointer.short(link)   #Null Pointer shortener
# newlink = s.owly.short(link)          #Ow.ly shortner
# newlink = s.post.short(link)          #Po.st Shortener

# these are few link shortner api....

print(" New link is : ", newlink)
