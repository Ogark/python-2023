import decimal

SENSOR_TPL = '/sys/class/thermal/thermal_zone{num}/temp'

class SensorValue:
    _PREC = 3
    
    def __init__(self, value=None):
        self.value = value

    @classmethod
    def convert_value(cls, value):
        value = int(value)
        val = f'{value}.' + '0' * cls._PREC
        dec = decimal.Decimal(val) / (10 ** cls._PREC)
        return dec

    def get_raw_value(self):
        raise NotImplementedError("Subclasses must implement get_raw_value method.")

    def get_value(self):
        val = self.get_raw_value()
        return self.convert_value(val)

    @property
    def value(self):
        if not hasattr(self, '_value'):
            self._value = self.get_value()
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class dBLoudness(SensorValue):
    _TEMPLATE = '/path/to/microphone/noise_level_file'  # Replace with the actual path
    
    def get_raw_value(self):
        with open(self._TEMPLATE, 'r') as file:
            val = file.readline().strip()

        return val

class CameraColor(SensorValue):
    _TEMPLATE = '/path/to/camera/color_file'  # Replace with the actual path
    
    def get_raw_value(self):
        with open(self._TEMPLATE, 'r') as file:
            val = file.readline().strip()

        return val

def get_temp(sensor_num=0, *, _template=SENSOR_TPL):
    sensor_num = int(sensor_num)
    fname = _template.format(num=sensor_num)
    with open(fname, 'r') as file:
        val = file.readline().strip()

    val = int(val)
    dec = decimal.Decimal(f'{val}.000') / 1000
    return dec

class Sensor(SensorValue):
    _TEMPLATE = '/sys/class/thermal/thermal_zone{num}/temp'
    
    def __init__(self, sensor_num=0):
        super().__init__(sensor_num)

    def get_raw_value(self):
        with open(self._TEMPLATE.format(num=self.value), 'r') as file:
            val = file.readline().strip()

        return val

if __name__ == '__main__':
    # Example usage of the new classes
    temperature_sensor = Sensor(0)
    temperature_value = temperature_sensor.value
    print(f"Temperature: {temperature_value} °C")

    noise_sensor = dBLoudness()
    noise_value = noise_sensor.value
    print(f"Noise Level: {noise_value} dB")

    color_sensor = CameraColor()
    color_value = color_sensor.value
    print(f"Camera Color: {color_value}")
