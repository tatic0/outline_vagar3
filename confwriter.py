
def confmaker(model, options):
  # model will be used to support the other Contour models
  # as of now, only Roam3 is supported
  with open('FW_RTC_template.txt', 'r') as template:
    a = template.read()
  conf = open('FW_RTC.txt', 'w')
  #a = a.format("Y", "N", "", "", "", "", "", "" , "N", "", "", "", "", "", "" , "N", "", "", "", "", "", "" , "N", "", "", "" )
  a = a.format(*options)
  conf.write(a)
  conf.close()
