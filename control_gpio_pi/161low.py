import RPi.GPIO as ir
print "PIN 33 Low"
ir.setwarnings(False)
ir.setmode(ir.BOARD)
ir.setup(33,ir.OUT)
ir.output(33,ir.LOW)
