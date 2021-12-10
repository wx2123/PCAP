

# Applying functions on rows and columns
counts <- matrix(c(3, 2, 4, 6, 5, 1, 8, 6, 1), ncol = 3)
colnames(counts) <- c("sparrow", "dove", "crow")
counts

apply(counts, 2, max)
counts[2, 2] <- NA
apply(counts, 2, max)
apply(counts, 2, max, na.rm = TRUE)

sapply(c("a", "b"), switch, a = "Hello", b = "Goodbye")

# loop with for
priceCalculator <- function(hours, pph = 40, client){
  net.price <- hours * pph * ifelse(hours > 100, 0.9, 1)
  
  VAT <- numeric(0)
  for(i in client){
    VAT <- c(VAT, switch(i, private = 1.12, public = 1.06, 1))
  }
  tot.price <- net.price * VAT
  round(tot.price)
}

# loop with sapply
priceCalculator <- function(hours, pph = 40, client){
  net.price <- hours * pph * ifelse(hours > 100, 0.9, 1)
  
  VAT <- sapply(client, switch, private = 1.12, public = 1.06, 1)
  tot.price <- net.price * VAT
  round(tot.price)
}

sapply(clients, class)





# https://stackoverflow.com/questions/53925644/how-to-make-the-equivalent-of-a-sas-macro-with-do-loop-in-r-studio
# create some data

var1 <- 0:5
var2 <- 6:11
var3 <- 12:17 

raw.have2000 <- data.frame(var1,var2,var3)
raw.have2001 <- data.frame(var1,var2,var3)
raw.have2002 <- data.frame(var1,var2,var3)

years <- 2000:2002
dataList <- lapply(years,function(x){
  # create name of data set as a character object
  dsname <- paste0("raw.have",x)
  # use dsname with get() to extract data and subset first 2 variables
  ds <- subset(get(dsname),var1 !=0,select=c(var1,var2))
  ds$year <- x
  # print to have data frame returned in
  # output list 
  ds 
})
# combine data frames 
appended <- do.call(rbind,dataList)

