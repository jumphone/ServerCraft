SCRIPT=r'''
import sys,time
fi=open(sys.argv[1])
time.sleep(8)
fo=open(sys.argv[2],'w')
fo.write(fi.read())
fi.close()
fo.close()
'''
