

# Applying functions on rows and columns
counts <- matrix(c(3, 2, 4, 6, 5, 1, 8, 6, 1), ncol = 3)
colnames(counts) <- c("sparrow", "dove", "crow")
counts

apply(counts, 2, max)
