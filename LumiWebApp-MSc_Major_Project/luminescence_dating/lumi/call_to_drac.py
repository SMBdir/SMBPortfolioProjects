from logging import currentframe
import subprocess
import requests
import re
from mechanize import Browser
#!/usr/local/bin/php


def DracInterface(inputStr):
  print(inputStr)
  drac_test_input = "DRAC-TEST Quartz Q Guerinetal2011 3.4 0.51 14.47 1.69 1.2 0.14 0 0 N X X X X X X X X X X X X X X X X X N 90 125 Brennanetal1991 Guerinetal2012-Q 8 10 Bell1979 0 0 5 2 2.22 0.05 1.8 0.1 30 70 150 X X 20 0.2"
  drac_test_name = "test Name"

  br = Browser()
  br.set_handle_robots(False)
  br.set_handle_refresh(False)
  response = br.open("https://www.aber.ac.uk/en/dges/research/quaternary/luminescence-research-laboratory/dose-rate-calculator/?show=calculator")
  # Selects the correct form to use the DRAC Calculator
  br.form = list(br.forms())[2]
  # Inputs the sample data to the correct input fields
  br["drac_data[name]"] = drac_test_name 
  br["drac_data[table]"] = inputStr 
  #Submits the form
  response = br.submit()  
  #saves the response from DRAC
  my_data=response.get_data()

  #Parsing the Data returned
  triple_comma_count = 0
  output_list = []
  decoded_data = my_data.decode("utf-8")

  current_entry = []
  for i in range(len(decoded_data)):
    current = decoded_data[i]
    previous = decoded_data[i-1]
    two_previous = decoded_data[i-2]
    third_previous = decoded_data[i-3]

    if(previous == ',' and two_previous == ',' and third_previous == ',' and current != ','):
      triple_comma_count = triple_comma_count + 1
     
    if(triple_comma_count == 8):
      if(current == ','):  
        output_list.append(''.join(current_entry))
        current_entry = []
      else:
        current_entry.append(current)

    
  
  return output_list
 
