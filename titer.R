#R code for titer
titer <- function(col,n1,n2,tdk){
    #basic parameters
    N        <- 6
    dilution <- sqrt(10)
    interval <- 0.95
    n0       <- 6
    n3       <- 0
    #searching for most probable number
    s   <- seq(0,1000)    #the number of virus in the solution
    p0  <- (1-46/(1000*dilution^0))^s  #the possibility that one tube on n0 column is sterile
    p1  <- (1-46/(1000*dilution^1))^s  #the possibility that one tube on n1 column is sterile
    p2  <- (1-46/(1000*dilution^2))^s  #the possibility that one tube on n2 column is sterile
    p3  <- (1-46/(1000*dilution^3))^s  #the possibility that one tube on n3 column is sterile
    pro <- (choose(N,n0)*(1-p0)^n0*p0^(N-n0) * choose(N,n1)*(1-p1)^n1*p1^(N-n1) *
    choose(N,n2)*(1-p2)^n2*p2^(N-n2) * choose(N,n3)*(1-p3)^n3*p3^(N-n3))   #the possibilty of the result
    pos <- which(pro==max(pro))
    dens<- s[pos] #the most probable number of virus
    #how to define confidence interval?
}
