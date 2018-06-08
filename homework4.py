# Python module for homework 4
#
# Timothy Adams
#

#strip end of line character from string
def strip_eol(protseq):
    if '\n' in protseq:
        protseq = protseq.replace('\n','')
        
    return protseq

#help calculate percent
def calcPercent(aminoCount, total):
    return (float(aminoCount)/total)*100

#homework 1 function: returns termini of a string sequence
def hw1(protseq):
    #strip end of line characters 
    protseq = strip_eol(protseq)
              
    #variables and calculations
    percentage    = .2                              # 20%
    totalLength   = len(protseq)                     # length of string
    percentLength = int(totalLength*percentage)     # lenght of 20% of the string
    
    
    #slice our the requested strings
    Nterminus = protseq[:percentLength]                 #first 20% 
    Cterminus = protseq[totalLength-percentLength:]     #final 20% 
    middleRegion = protseq[percentLength:totalLength-percentLength]
        
    #print the requested string
    print Nterminus
    print Cterminus
    print middleRegion

#homework 2 funciton - returns relative percentages of aminos
def hw2(protseq):
    #strip end of line characters 
    protseq = strip_eol(protseq)       
    
    #variables used
    dictAcids = {}             #dictionary to hold amino acids and totals
    totalPercent = 0           #used to sum the percents to make sure they total 100
    totalLength = len(protseq)  #calculate total length once and store it
      
    #loop through the amino acids in the protein sequence and add them to a dictionary
    #amino acid is the key, and the total number found in the string is the value
    for aminoacid in protseq:
        if aminoacid in dictAcids:
            dictAcids[aminoacid] += 1
        else:
            dictAcids[aminoacid] = 1
    
    #loop through the dictionary and for each amino acid calculate and print its 
    #relative percent - for a resonableness check, keep a running total and print it
    #out last to make sure the calculations were correct
    for eachAcid, countAcid in dictAcids.items():
        print eachAcid + ' has a relative percentage of: ' + str(round(calcPercent(countAcid,totalLength),2)) + '%' 
        totalPercent += calcPercent(countAcid,totalLength)
    else:
        print 'These total: ' + str(totalPercent) + '%'
   
#homework 3 function - writes scores from a ponderfit file to a new file     
def hw3a(filename):
    with open(filename,'rt') as pondrfile:
        disprot = pondrfile.read()
        
    list1 = disprot.split()
        
    #Open a file for writing output
    with open('scores.txt','wt') as scoresfile:
        for i in list1[4::4]:
            scoresfile.writelines(i+'\n') 
        
#homeowkr 3 funciton - writes lines starting with ATOM to a new file        
def hw3b(filename):
    with open(filename,'rt') as pdbfile:
        tup = pdbfile.readlines()
    
    #Open a file for writing output
    with open('atom.txt','wt') as atomfile:
        for lines in tup:
            #for each line, if it starts with ATOM, write the line to the file
            if lines.upper().startswith('ATOM'):
                atomfile.writelines(lines)

def main():
    x='''MKLFWLLFTIGFCWAQYSSNTQQGRTSIVHLFEWRWVDIALECERYLAPKGFGGVQVSPP
    NENVAIHNPFRPWWERYQPVSYKLCTRSGNEDEFRNMVTRCNNVGVRIYVDAVINHMCGN
    AVSAGTSSTCGSYFNPGSRDFPAVPYSGWDFNDGKCKTGSGDIENYNDATQVRDCRLSGL
    LDLALGKDYVRSKIAEYMNHLIDIGVAGFRIDASKHMWPGDIKAILDKLHNLNSNWFPEG
    SKPFIYQEVIDLGGEPIKSSDYFGNGRVTEFKYGAKLGTVIRKWNGEKMSYLKNWGEGWG
    FMPSDRALVFVDNHDNQRGHGAGGASILTFWDARLYKMAVGFMLAHPYGFTRVMSSYRWP
    RYFENGKDVNDWVGPPNDNGVTKEVTINPDTTCGNDWVCEHRWRQIRNMVNFRNVVDGQP
    FTNWYDNGSNQVAFGRGNRGFIVFNNDDWTFSLTLQTGLPAGTYCDVISGDKINGNCTGI
    KIYVSDDGKAHFSISNSAEDPFIAIHAESKL'''

    y='class.pondrfit'

    z='1TUP.pdb'

    hw1(x)
    hw2(x)
    hw3a(y)
    hw3b(z)
                              
if __name__ == "__main__":
    main()

    