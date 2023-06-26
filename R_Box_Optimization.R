# Install and load the lpSolve package
if(!require(lpSolve)) {
  install.packages("lpSolve")
  library(lpSolve)
}

# Define the objective function coefficients
f.obj <- c(0.09, .44, .53)

# Define the constraint matrix
f.con <- matrix(c(10, 1000, 50), nrow = 1)

# Define the right-hand side (RHS) vector
f.rhs <- 640

# Define the direction of the constraints
f.dir <- "="

# Solve the LP problem
optimum <- lp("min", f.obj, f.con, f.dir, f.rhs, all.int = TRUE)

# Print the results
print(optimum$solution)

