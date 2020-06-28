import serial, sys
#import re

strPort1 = sys.argv[1]   # serial port
#strPort2 = sys.argv[2]   # serial port

ser1=serial.Serial(strPort1, 19200)
#ser2=serial.Serial(strPort2, 57600)

print("connected to: " + ser1.portstr)
#print("connected to: " + ser2.portstr)
#count=1

#file=sys.argv[1]  # file name
#regex = re.compile('\d+')
#f=open(file,"w+")
while True:
  try:
    line1 = ser1.readline()
#    line2 = ser2.readline()
#    match = regex.findall(line)
#    f1=match[4]+"."+match[5]+", "+match[6]+"."+match[7]+", "+match[8]+"."+match[9]+", "+match[10]+"."+match[11]+", "+match[12]+"."+match[13]+", "+match[14]+"."+match[15]+", "+match[16]+"."+match[17]+", "+match[18]+"."+match[19]+", "+match[20]+"."+match[21]+", "+match[22]+"."+match[23]
#    data = [float(val) for val in line.split()]
    print(line1);
#    print(line2);
#    f.write(f1+"\n")
  except KeyboardInterrupt:
    print ('exiting')
    break
ser1.flush()
ser1.close()
#f.close()
