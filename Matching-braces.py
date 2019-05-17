ebarat= input("ebarat khod ra vared konid : ")
stak = []  #yek poshte baz mikonim va tebghe harf khodeton parantez ha ra dar an mirizim

a = {}# yek dic ham baray tatbigh parantez estefade mikonim
c=0     # yek shomarande hast baray donestan andis patantez va karakter ha 
khata=0
w=0
if len(ebarat)<=70: # shart ma baray karekterhay bishtar az 70 nabayad kar konad 

    for i in ebarat: # baray har karekter dakhel ebarat ke chek shavad parantez hast ya na 
            c+=1 #shomare andis har dafe yeki biyad jolo
            if i == '(':    # agar parantez baz didi be stak ezafe kon
                 stak.append(c)

                 
            if i == ')':# agar parantez baste didi az to stak bardar va indexerrore didi yeki be w beshmar

                try:
                    a[stak.pop()] = c 
                except IndexError: 
                    khata+=1#agar yek parantez ham motabeghat nadasht an hayi ke motabeghat darand ra neshan nade
                    w+=1
                    
    if w>0:# tedad parantez baste 
        d=str(w)
        print("vojod darad "+d+" parantez ) ke motabeghat nadarad \n")

    if stak:  # chek kon stak khali hast ya na baray parantez baz 
        e=str(len(stak))
        print("vojod darad "+e+" parantez ( ke motabeghat nadarad ")
        khata+=1
        
    if khata==0: # agar hame parantez ha motabeghat dashtand dic ra chap kon    
        print(a)
        print ("\nlisti az joft parantez ha ke ba ham motabeghat darand .\n")
        lena=(str(len(a)))
        print ("va tedad joft parantez ha barabar ast ba:"+lena )


    h=str(c)
    print ("\nva tedad karekter barabar ast ba "+h)
    
    
else :# agar tedad karakter bishtar az 70 bod print kon khata 
    t =str (len(ebarat))
    print ("ebarat shoma barabar ast ba "+t+" va az 70 karekter bishtar ast")
    

