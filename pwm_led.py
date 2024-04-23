import RPi.GPIO as GPIO
import tkinter as tk

# GPIO pins for LEDs
LED_RED_PIN = 17
LED_GREEN_PIN = 18
LED_BLUE_PIN = 27

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT)

# Initialize PWM instances for each LED
red_pwm = GPIO.PWM(LED_RED_PIN, 100)  # Frequency: 100 Hz
green_pwm = GPIO.PWM(LED_GREEN_PIN, 100)
blue_pwm = GPIO.PWM(LED_BLUE_PIN, 100)

# Function to update LED intensity based on slider value
def update_intensity(color, duty_cycle):
    if color == 'red':
        red_pwm.ChangeDutyCycle(duty_cycle)
    elif color == 'green':
        green_pwm.ChangeDutyCycle(duty_cycle)
    elif color == 'blue':
        blue_pwm.ChangeDutyCycle(duty_cycle)

# Create GUI
root = tk.Tk()
root.title("LED Intensity Controller")

# Slider for red LED
red_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Red LED", command=lambda value: update_intensity('red', int(value)))
red_slider.pack()

# Slider for green LED
green_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Green LED", command=lambda value: update_intensity('green', int(value)))
green_slider.pack()

# Slider for blue LED
blue_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Blue LED", command=lambda value: update_intensity('blue', int(value)))
blue_slider.pack()

# Start PWM
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Run GUI
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
