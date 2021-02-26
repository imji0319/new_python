# ui.R 

library('shiny')

# shinyUI로 시작
shinyUI(pageWithSidebar(     
  headerPanel("Slider"),
  
  sidebarPanel(
    selectInput('variable', 'Variiable: ', 
                list('Cylinders' = "cyl", 
                     "Transmission"="am",
                     "Geers" = "gear")),
    
    checkboxInput("outliers", "Show outliers", FALSE),
    
    sliderInput("obs",
                "Number of Observations : ",
                min = 1,
                max = 1000, 
                value = 500)),
  
  mainPanel(
    h3(textOutput("caption")),
    plotOutput("mpgPlot"))
  
  
))
