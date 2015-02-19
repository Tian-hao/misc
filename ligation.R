#R code
ligation <- function(vectorconc, insertconc, vectorlength, insertlength, i2vratio, ligationtotal){
  vectorv <- ligationtotal/(vectorconc+vectorconc*i2vratio*insertlength/vectorlength)
  insertv <- (ligationtotal - vectorconc*vectorv)/insertconc
#  print ('vector volume: ')
  print (vectorv)
#  print ('insert volume: ')
  print (insertv) 
#  print ('water volume: ')
  print (7-vectorv-insertv)
  }
