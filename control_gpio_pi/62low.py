import RPi.GPIO as ir
print "PIN 16 Low"
ir.setwarnings(False)
ir.setmode(ir.BOARD)
ir.setup(16,ir.OUT)
ir.output(16,ir.LOW)
