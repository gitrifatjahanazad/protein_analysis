import redis
pdb = '1out.pdb'

pdb_file = open(pdb,'r')

def space_split(string_line):
    word = ""
    new_word = False
    word_list = []
    for c in string_line:
        if c !=  ' ':
            word += c
            new_word = False
        if c == ' ':
            if not new_word:
                new_word = True
                word_list.append(word)
                word = ""
    return word_list

csv = open('parse_result.csv','w+')
r = redis.StrictRedis(host='localhost', port=6379,db=0)

universal_counter = 0
for line in pdb_file.readlines():
    words = space_split(line)
    if words[0].lower() == 'atom':
        universal_counter += 1
        molecule = words[2]
        chain = words[4]
        x = words[6]
        y = words[7]
        z = words[8]
        # csv.write(molecule+","+chain+","+x+","+y+","+z+"\n")
        r.set(pdb.split('.')[0]+str(universal_counter),dict(molecule=molecule,
                                    chain=chain,
                                    x=x,
                                    y=y,
                                    z=z))
    #end of line
    