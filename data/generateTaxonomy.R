# Remember to set your working directory !!!!
# setwd() 

# Read the taxonomy file
tax <- read.csv("taxonomy.csv", stringsAsFactors = F)

# Get a list of directories that need to be generated
dirs <- sapply(tax["uri"], function(x) paste(getwd(), "/input", x, sep = "")) 

# Make the directories
lapply(dirs, function(d) dir.create(d))

library("jsonlite")

# Make a homepage
children <- tax[tax["level"] == "T1",]
taxonomy <- data.frame(children$name, children$uri, stringsAsFactors = F)
colnames(taxonomy) <- c("name", "uri")

page <- list(uri = "/", level = "T0", name = "Homepage", children = taxonomy)
write_json(page, paste(getwd(), "/input/data.json", sep = ""))

# Make some T1 pages
t1s <- tax[tax["level"] == "T1", ]
lapply(t1s$uri, function(t) {
  p <- t1s[t1s$uri == t, ][1,]
  t2s <-tax[tax["level"] == "T2", ]
  children <-t2s[startsWith(t2s$uri, p$uri), ]
  taxonomy <- data.frame(children$name, children$uri, stringsAsFactors = F)
  colnames(taxonomy) <- c("name", "uri")
  page <- list(uri = p$uri[1], level = p$level[1], name = p$name[1], children = taxonomy)
  write_json(page, paste(getwd(), "/input", p$uri, "/data.json", sep = ""))
})

# Make some T2 pages
t2s <- tax[tax["level"] == "T2", ]
lapply(t2s$uri, function(t) {
  p <- t2s[t2s$uri == t, ]
  page <- list(uri = p$uri[1], level = p$level[1], name = p$name[1])
  write_json(page, paste(getwd(), "/input", p$uri, "/data.json", sep = ""))
})
