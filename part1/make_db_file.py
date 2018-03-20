dbfilename='people-file'
ENDDB='enddb'
ENDREC='endrec'
RECSEP='=>'

def storeDbase(db,dbfilename=dbfilename):
    dbfile=open(dbfilename,'w')
    for key in db:
        print(key,file=dbfile)
        for (name,value) in db[key].items():
            print(name+RECSEP+repr(value),file=dbfile)
        print(ENDREC,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()
    