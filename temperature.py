temp_file = open("/sys/bus/w1/devices/28-00000890bf46/w1_slave", "r")
temp_raw = temp_file.read()
temp_value = temp_raw[-6:-1]
temp_base = temp_value / 1000
