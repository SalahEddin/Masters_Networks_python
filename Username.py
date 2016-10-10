def main(f,l):
    print "This Program..."
    if len(l) <= 7:
        print f[0] + l[:]
    else:
        print f[0] + l[:7]

first = raw_input("enter first name:")
last = raw_input("enter last name:")
main(first, last)