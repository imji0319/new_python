# ui.R


# Diamonds + mtcars + iris datatable tap 
# 각 데이터 별 변수 선택 -> boxplot reactivity plot 
# 상단 plot , 하단 dataset

# 1. 3개 탭 만들기 
library(shiny)
shinyUI(pageWithSidebar(
  
  headerPanel("3 dataset Boxplot"),
  
  sidebarPanel(
    checkboxGroupInput('show_vars', 'Columns in diamonds to show : ', names(diamonds),
                       selected = names(diamonds)),
    
    helpText('For the diamonds data, we can select variables to show in the table; 
             for the mtcars example, we use bSortClasses = TRUE 
             so that sorted columns are colored since they have special CSS classes attached ; 
             for the iris data, we customize the length menu so we can display 5 rows per page')
    
    
  ),
  
  mainPanel(
    tabsetPanel(
      tabPanel("Diamonds", 
               plotOutput('dia_plot'),
               dataTableOutput('dia_data')),
      tabPanel("mtcars",
               plotOutput('mt_plot'),
               dataTableOutput('mt_data')),
      tabPanel("iris",
               plotOutput('iris_plot'),
               dataTableOutput('iris_data'))
    
  ))
  
))