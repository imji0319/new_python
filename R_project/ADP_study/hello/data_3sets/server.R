# Server.R

library('shiny')
shinyServer(function(input, output){
  
  
  
  # Data Table
  output$dia_data <- renderDataTable({
    library(ggplot2)
    diamonds[, input$show_vars, drop = FALSE]
  })
  
  output$mt_data <- renderDataTable({
    mtcars}, options = list(bSortClasses = TRUE))
  
  output$iris_data <- renderDataTable({
    iris}, options = list(aLengthMenu = c(5,30,50), iDisplayLength = 5))
  
})