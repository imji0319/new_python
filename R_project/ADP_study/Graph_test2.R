library(ggplot2)
library(googleVis)

require(stats)
require(datasets)

# 고정 데이터 수집 
install.packages('XML')
library(XML)
url <- "https://en.wikipedia.org/wiki/List_of_countries_by_credit_rating"
x <- readHTMLTable(readLines(url), which = 3, header = T)

head(x)
levels(x$Rating) <- substring(levels(x$Rating), 4, nchar(levels(x$Rating)))
x$Ranking <- x$Rating

levels(x$Ranking) <- nlevels(x$Rating):1
x$Ranking <- as.character(x$Ranking)
x$Rating <- paste(x$`Country/Region`, x$Rating, sep=": ")
G8 <- gvisGeoChart(x, "Country/Region", "Ranking", hovervar = "Rating",
                   options = list(gvis.editor="S&P",
                                  colorAxis = "{colors : ['#91BFDB', '#FC8D59']}"))
plot(G8)



# 가변 데이터 : 최근 30일 간의 진도 4.0이상 지진발생 데이터

url <- "http://ds.iris.edu/seismon/eventlist/index.phtml"

eq <- readHTMLTable(readLines(url),
                    colClasses= c("factor", rep("numeric", 4), "factor"))$evTable 

names(eq) <- c("DATE", "LAT","LON","MAG","DEPTH","LOCATION_NAME", "IRIS_ID")

head(eq)
eq$loc = paste(eq$LAT, eq$LON, sep = ":")

head(eq)


G9 <- gvisGeoChart(eq, "loc", "DEPTH", "MAG", 
                  options = list(displayMode = "Markers",
                                 colorAxis = "{colors:['purple','red','orange','grey']}",
                                 backgroundColor = "lightblue"), 
                  chartid = "EQ")

plot(G9)

