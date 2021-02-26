# Server.R

library('shiny')
shinyServer(function(input, output){

  
  # dataset 
  datasetInput <- reactive({
    switch(input$dataset,
           "diamonds" = diamonds,
           "mtcars" = mtcars,
           "iris" = iris)
  })
  
  library(ggplot2)
  library(dplyr)
  
  data(diamonds)
  data(iris)
  data(mtcars)
  
  
  output$plot <- renderPlot({
    dataset <- datasetInput()
    
    if (isTRUE(all_equal(dataset, diamonds))) {
      qplot(cut, price, data = diamonds, geom ='boxplot')
      
    } else if (isTRUE(all_equal(dataset, mtcars))){
      qplot(wt, mpg, data = mtcars)
      
    } else if (all_equal(dataset, iris)){
      ggplot(data = iris, aes(Sepal.Length, Sepal.Width))  + geom_point()
    }
    
  })
  
    
  

  
  
  # summary
  output$summary <- renderPrint({
    summary(datasetInput())
  })
  
  # table
  output$table <- renderTable({
    head(datasetInput(), n = input$obs)
  })
  
})
  


