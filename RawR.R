##Going to refamiliarize myself with R a bit

Greeting <- "I love democ(R)acy, I love the (R)epublic."
print(Greeting)

mynumber <- 5
mynumber <- 5*mynumber
a <- 4
b <- 3
X <- a*b
print(X)
##time for something a bit more interesting
var1 <- exp(5)
print(var1)

my.vec <- c(pi,45, 912.8,0)
print(my.vec[1])
print(my.vec[2])
print(my.vec[3])
print(my.vec[4]) ##I can still comment here muauahahaha
point.vec1 <- 1:20
print(point.vec1)
##Into the Down Under
point.vec2 <- 0:-20
print(point.vec2)
print(point.vec1[4:8])
print(point.vec2[c(1,5,11)])

##Sequences where difference between values is _different_ than 1
my.vec_cust <- seq(30,70,4)
print(my.vec_cust)