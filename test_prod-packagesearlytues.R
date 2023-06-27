# Install and load Packages
if(!require(lpSolve)) {
  install.packages("lpSolve")
  library(lpSolve)
}

if(!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}

# Define the objective function coefficients
f.obj <- c(0.11, 0.15, 0.264062)

# Define the constraint matrix (how many units per each, respectively)
f.con <- matrix(c(43, 100, 229), nrow = 1) #Assuming the P3-4 hybrid volume is about 43 cubic inches

# Define the direction of the constraints (do we want to consider partial fill)
f.dir <- "="

# Define the demand range (simulation range)
demand_range <- 1:750

# Initialize vectors to store the results
total_cost <- numeric(length(demand_range))
package_type <- character(length(demand_range))

# Define the package names (Medium/Golden/Minibulk, etc?)
package_names <- c("P4", "Golden", "C6")

# Loop over the demand values
for (i in seq_along(demand_range)) {
  
  # Get the current demand value
  f.rhs <- demand_range[i]
  
  # Solve the LP problem
  optimum <- lp("min", f.obj, f.con, f.dir, f.rhs, all.int = TRUE)
  
  # Check if the solution is empty
  if (length(optimum$solution) == 0) {
    # If the solution is empty, assign "None" to package_type[i]
    package_type[i] <- "None"
  } else {
    # Otherwise, store the total cost and the type of the optimal package
    total_cost[i] <- sum(f.obj * optimum$solution)  # Modified here
    package_type[i] <- package_names[which.max(optimum$solution)]
  }
}

# Create a data frame of the results
results <- data.frame(Demand = demand_range, TotalCost = total_cost, PackageType = package_type)

# Plot the results
ggplot(results, aes(x = Demand, y = TotalCost, color = PackageType)) +
  geom_line() +
  labs(title = "Optimal Packaging Solution", x = "Cubic Volume", y = "Total Cost ($)") +
  scale_color_discrete(name = "Pack Type")

