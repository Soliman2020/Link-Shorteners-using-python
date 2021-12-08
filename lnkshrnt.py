# step 1 : install the module pyshorteners
   
import pyshorteners
s = pyshorteners.Shortener()    
link = input("Plz enter your Link:  ")
count= int(input("How many links you want?\nWrite 1 or 2:  "))
          
newlink1 = s.dagd.short(link)          #Da.gd shortener
newlink2 = s.tinyurl.short(link)       #TinyURL.com shortener
# newlink = s.bitly.short(link)         #Bit.ly shortener
# newlink = s.chilpit.short(link)       #Chilp.it shortener
# newlink = s.cuttly.short(link)        #Cutt.ly shortener
# newlink = s.gitio.short(link)         #Git.io shortener 
# newlink = s.isgd.short(link)          #Is.gd shortener
# newlink = s.osdb.short(link)          #Os.db shortener
# newlink = s.nullpointer.short(link)   #Null Pointer shortener
# newlink = s.owly.short(link)          #Ow.ly shortner
# newlink = s.post.short(link)          #Po.st Shortener
# newlink = s.clckru.short(link)        # Clck.ru shortener

# these are few link shortner api....
        
if count==1:
    print ("\nFeel free to use this link:\n{}\n".format(newlink1))
else:
    print("\nFeel free to use this link:\n{} \n\nOr this one:\n{}\n".format(newlink1,newlink2))
