import RPi.GPIO as IO            
import time                              

IO.setmode (IO.BOARD)  
     
IO.setup(40,IO.OUT)
IO.setup(38,IO.OUT)
IO.setup(36,IO.OUT)
IO.setup(32,IO.OUT)
IO.setup(28,IO.OUT)
IO.setup(26,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(10,IO.OUT)
IO.setup(37,IO.OUT)
IO.setup(35,IO.OUT)
IO.setup(33,IO.OUT)
IO.setup(31,IO.OUT)

while True:
    IO.output(40,1)
	IO.output(38,1)	
	IO.output(36,1)
	IO.output(32,1)
	IO.output(28,1)
	IO.output(26,1)	
	IO.output(24,1)
	IO.output(22,1)	
	IO.output(18,1)
	IO.output(16,1)
	IO.output(12,1)
	IO.output(10,1)	
	IO.output(37,1)
	IO.output(35,1)	
	IO.output(33,1)
	IO.output(31,1)		
		
	time.sleep(1)    
		
	IO.output(40,0)
	IO.output(38,0)	
	IO.output(36,0)
	IO.output(32,0)
	IO.output(28,0)
	IO.output(26,0)	
	IO.output(24,0)
	IO.output(22,0)	
	IO.output(18,0)
	IO.output(16,0)
	IO.output(12,0)
	IO.output(10,0)	
	IO.output(37,0)
	IO.output(35,0)	
	IO.output(33,0)
	IO.output(31,0)	

	time.sleep(1)                       
