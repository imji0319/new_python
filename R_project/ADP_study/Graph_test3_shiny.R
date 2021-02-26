# 샤이니 Shiny

options(repos = c(RStudio = 'http://rstudio.org/_packages', getOption('repos')))
install.packages('shiny')
library(shiny)

runExample('01_hello')
runExample('02_text')
runExample('03_reactivity')



