import RPi.GPIO as ir
print "PIN 32 Low"
ir.setwarnings(False)
ir.setmode(ir.BOARD)
ir.setup(32,ir.OUT)
ir.output(32,ir.LOW)
