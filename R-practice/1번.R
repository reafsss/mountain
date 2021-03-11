A <- matrix(c(1:8),2,4)
A
apply(A,1,mean)
apply(A,2,mean)
min(apply(A,1,mean)) + max(apply(A,2,mean))
