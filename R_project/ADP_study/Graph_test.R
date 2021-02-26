install.packages('ggplot2')
library(ggplot2)


data("ChickWeight")
head(ChickWeight)

# 기본 XY 그래프 
ggplot(ChickWeight, aes(x = Time, y = weight,  
                        colour = Diet, group = Chick)) + 
  geom_line()

# 점 그래프 
ggplot(ChickWeight, aes(x = Time, y = weight,  
                        colour = Diet)) + geom_point(alpha = 0.3) 

# 스무스 그래프(Smooth Graph)
ggplot(ChickWeight, aes(x = Time, y = weight,  
                        colour = Diet)) + geom_smooth(alpha = .4, size = 3) 

ggplot(ChickWeight, aes(x = Time, y = weight,  
                        colour = Diet)) + 
         geom_point(alpha = .3) + 
         geom_smooth(alpha = .2, size =1) 


# 히스토그램 
ggplot(subset(ChickWeight, Time = 21), aes(x= weight, file = Diet)) +
  geom_histogram(colour = 'black', binwidth = 50) + facet_grid(Diet ~ . )


data(mtcars)
head(mtcars)

# 기본 그래프 
p = qplot(wt, mpg, colour= hp, data = mtcars)
p + coord_cartesian(ylim = c(0, 40)) +
  scale_colour_continuous(breaks = c(100, 300)) +
  guides(colour = 'colourbar')


# 치환 데이터를 이용한 포인트 그래프 

m <- mtcars[1:10, ]
p%+%m # %+%


# 막대 그래프 
c <- ggplot(mtcars, aes(factor(cyl))) + geom_bar()
c + geom_bar(fill ='white', colour ='red')

# 시계열 데이터 
data(economics)
head(economics)

# 선 그래프 
b <- ggplot(economics, aes(x=date, y = unemploy))
b+geom_line( colour = 'blue', size = .3, linetype = 3)


# 효과 주기 

data(diamonds)
head(diamonds)

# 히스토그램 
k <- ggplot(diamonds, aes(carat, ..density.. )) + geom_histogram(binwidth = .2)
k + facet_grid(.~cut)

# 막대 그래프 
w <- ggplot(diamonds, aes(clarity, fill = cut))
w + geom_bar()


# 선형 모델링 
dmod <- lm(price ~ cut, data = diamonds)
cuts <- data.frame(cut = unique(diamonds$cut), 
                   predict(dmod, data.frame(cut = unique(diamonds$cut)), se = TRUE)[c('fit', 'se.fit')])

se <- ggplot(cuts, aes(x = cut, y = fit, ymin = fit - se.fit, 
                       ymax = fit + se.fit, colour = cut))

se + geom_pointrange()


# 포인트 그래프 - 박스로 강조 

p <- ggplot(mtcars, aes(wt, mpg)) + geom_point()
p + annotate("rect", xmin = 2, xmax = 3.5, ymin = 2, ymax = 25, fill = 'dark gray',
             alpha = .5)

# 축 범위 지정 
p <- qplot(disp, wt, data = mtcars) + geom_smooth()
p + scale_x_continuous(limits = c(325, 500))

# box plot 
qplot(cut, price, data = diamonds, geom ='boxplot')

last_plot() + coord_flip() # 가로 그래프 

# qplot
qplot(cut, data = diamonds, geom='bar')




# 구글 비즈 Google Vis

install.packages('googleVis')
library(googleVis)

data(Fruits)
head(Fruits)

# 모션 차트 

M1 <- gvisMotionChart(Fruits, idvar = 'Fruit', timevar  = 'Year')
plot(M1)


# 지오 차트 
data(Exports)
head(Exports)

# 전세계 국가별 수출, 수익크기 
G1 <- gvisGeoChart(Exports, locationvar = 'Country', colorvar = 'Profit')
plot(G1)


# 유럽 국가별 수익 크기 : region = '150'
G2 <- gvisGeoChart(Exports, "Country", "Profit", options= list(region='150'))
plot(G2)


require(datasets)
states <- data.frame(state.name, state.x77)
head(states)


# 미국의 주별 문맹률 정보 
G3 <- gvisGeoChart(states, "state.name", "Illiteracy", 
                   options = list(region='US', displayMode='regions', resolution ='provinces',
                                  width = 600, height = 400))
plot(G3)

# 허리케인 경로 : 색상으로 표시 
head(Andrew)

G5 <- gvisGeoChart(Andrew, "LatLong", colorvar = 'Speed_kt', 
                   options = list(region ='US'))
plot(G5)


# 허리케인 경로 : 원크기로 표시 
G6 <- gvisGeoChart(Andrew, "LatLong", sizevar = 'Speed_kt',
                   colorvar = 'Pressure_mb',
                   options = list(region='US'))
plot(G6)


require(stats)
data(quakes)
head(quakes)

# 깊이 표시 

quakes$latlong = paste(quakes$lat , quakes$long, sep=":")
head(quakes$latlong)

G7 <- gvisGeoChart(quakes, "latlong", "depth", "mag",
                   options = list(displayMode = 'Markers', region ='009', 
                                  colorAxis = "{colors:['red','gray']}", 
                                  backgroundColor = 'lightblue'))
plot(G7)





