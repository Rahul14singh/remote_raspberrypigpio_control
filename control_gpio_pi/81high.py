import RPi.GPIO as ir
print "PIN 11 High"
ir.setwarnings(False)
ir.setmode(ir.BOARD)
ir.setup(11,ir.OUT)
ir.output(11,ir.HIGH)
