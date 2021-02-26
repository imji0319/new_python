# ui.R


# sidebar : Diamonds + mtcars + iris dataset 선택 
# 각 3개 탭 생성 : dataTableOutput, renderPlot, summary 


# 1. sidebar
library(shiny)
shinyUI(pageWithSidebar(
  
  headerPanel("3 dataset Boxplot"),
  
  sidebarPanel(
    selectInput('dataset', "Choose a dataset",
                choices = c('diamonds','mtcars','iris')),
    numericInput("obs", "Number of observations to view : ", 10),
    
    submitButton("Update View")

  ),
  
  mainPanel(
    tabsetPanel(
      tabPanel("Plot", plotOutput("plot")), 
      tabPanel("Summary", verbatimTextOutput("summary")),
      tabPanel("Table", dataTableOutput('table'))
    
  ))
  
))