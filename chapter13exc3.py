def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile,"w")
    count = 0
    while True:
        count +=1
        text = infile.readline()
        if len(text) == 0:
            break

        outfile.write("{0: >4} {1}".format(count, text))
        outfile.write(text)
    infile.close()
    outfile.close()

filter("exc4chap7..py", "copyof.txt")

#slices