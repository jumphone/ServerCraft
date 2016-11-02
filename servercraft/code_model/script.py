SCRIPT=r'''
import sys
fi=open(sys.argv[1])
fo=open(sys.argv[2],'w')
fo.write(fi.read())
fi.close()
fo.close()
'''