with open('FW_RTC_template.txt', 'r') as template:
  a = template.read()
conf = open('FW_RTC.txt', 'w')
a = a.format("Y", "N", "", "", "", "", "", "" , "N", "", "", "", "", "", "" , "N", "", "", "", "", "", "" , "N", "", "", "" )
conf.write(a)
conf.close()
