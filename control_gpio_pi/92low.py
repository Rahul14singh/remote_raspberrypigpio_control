import RPi.GPIO as ir
print "PIN 24 Low"
ir.setwarnings(False)
ir.setmode(ir.BOARD)
ir.setup(24,ir.OUT)
ir.output(24,ir.LOW)
