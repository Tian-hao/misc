#R code for titer
titer <- function(high, low, highcol,dilfactor){
  return (10**((high/6-0.5)/(high/6-low/6)*0.5+(highcol-1)/2-0.5)*dilfactor*10)
  }
