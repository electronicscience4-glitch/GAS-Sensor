from machine import Pin, ADC
import time

# ڕێکخستنی سێنسەری گازی MQ
# بۆ سێنسەری MQ، پێویستە بە ADC بخوێنرێتەوە نەک بە دیجیتاڵی
SENSOR_PIN = 28  # GP28 کە توانای ADC هەیە
sensor = ADC(Pin(SENSOR_PIN))

# سنووری تیشکی گاز (دەتوانێت بگۆڕدرێت بەپێی کاڵیبرکردن)
GAS_THRESHOLD = 20000  # نرخی ناوەند لە نێوان 0-65535

def setup():
    """دانانی سەرەتایی"""
    print("Gas Sensor Program Started")
    print("Sensor connected to GP28 (ADC2)")
    print("=" * 40)

def read_gas_level():
    """خوێندنەوەی نرخی گاز"""
    # خوێندنەوەی چەند خوێندنەوەیەک بۆ کەمکردنەوەی ناڕێکی
    total = 0
    samples = 10
    
    for i in range(samples):
        total += sensor.read_u16()
        time.sleep(0.01)
    
    average_value = total / samples
    return int(average_value)

def loop():
    """لووبی سەرەکی"""
    # خوێندنەوەی نرخی گاز
    gas_value = read_gas_level()
    
    # دیاریکردنی دۆخی گاز
    if gas_value > GAS_THRESHOLD:
        gas_state = 1  # گاز بوونی نییە یان کەمە
        status_text = "NO Gas detected"
    else:
        gas_state = 0  # گاز هەیە
        status_text = "GAS DETECTED!"
    
    # نیشاندانی ئەنجامەکان
    print(f"ADC Value: {gas_value}/65535")
    print(f"Status: {status_text}")
    print(f"Threshold: {GAS_THRESHOLD}")
    
    # هەڵسەنگاندی زیاتر
    if gas_state == 1:
        print("The gas is NOT present / Low concentration")
    else:
        print("⚠️ WARNING: The gas IS present!")
        print("⚠️ Check for leaks immediately!")
    
    print("=" * 40)
    
    # پشووی کورتتر بۆ نیشاندانی زیاتر
    time.sleep(0.5)

# سەرەتاکەی بەرنامە
if __name__ == "__main__":
    setup()
    
    # کاڵیبرکردنی سێرسەر (ئارەزوویە)
    print("Calibrating sensor...")
    print("Please ensure no gas is present during calibration")
    time.sleep(3)
    
    # خوێندنەوەی نرخی سەرەتایی بۆ دیاریکردنی تیشک
    cal_values = []
    for i in range(5):
        cal_values.append(sensor.read_u16())
        time.sleep(0.5)
    
    avg_cal = sum(cal_values) / len(cal_values)
    print(f"Average calibration value: {avg_cal:.0f}")
    print(f"Using threshold: {GAS_THRESHOLD}")
    print("Calibration complete!")
    print("=" * 40)
    
    # لووبی سەرەکی
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")