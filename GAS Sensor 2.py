from machine import Pin, ADC
import time

# هەردوو جۆر تاقی بکەرەوە
digital_pin = Pin(28, Pin.IN)
analog_pin = ADC(Pin(28))

print("Testing sensor type...")

while True:
    # تاقیکردنەوەی دیجیتاڵ
    digital_value = digital_pin.value()
    
    # تاقیکردنەوەی ئانالۆگ
    analog_value = analog_pin.read_u16()
    
    print(f"Digital: {digital_value}, Analog: {analog_value}")
    
    if digital_value == 0 or digital_value == 1:
        print("✓ Digital sensor detected")
    else:
        print("✗ No digital signal")
    
    if analog_value > 0:
        print(f"✓ Analog sensor detected: {analog_value}")
    
    time.sleep(1)