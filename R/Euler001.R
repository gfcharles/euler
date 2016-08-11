# Euler 01
x <- c(1:999)
result <- sum(x[x %% 3 == 0 | x %% 5 == 0])

print(result)

sumOfMultiples<-function(n, num)
{
  m <- n %/% num
  (num * m * (m+1)) %/% 2;
}

print(sumOfMultiples(999, 3) + sumOfMultiples(999, 5) - sumOfMultiples(999, 3 * 5))
