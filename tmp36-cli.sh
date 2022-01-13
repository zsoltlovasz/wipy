#!/bin/bash

wipy_temp_sens_reading=$(nc 192.168.1.4 11111)
echo $wipy_temp_sens_reading " analog read"
wipy_temp_sens_volt=$(echo -e "scale=6\n${wipy_temp_sens_reading}*1400/4096" | bc)
echo $wipy_temp_sens_volt " mV"
wipy_temp_sens_celsius=$(echo -e "scale=6\n${wipy_temp_sens_reading}*1400/4096/10-50" | bc)
echo $wipy_temp_sens_celsius " C"
