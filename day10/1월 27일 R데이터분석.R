install.packages('cowsay')
library(cowsay)


byNameList=c('cat','ghost','ant')
length(byNamelist)

for (byName in byNameList){
say('hello world',by=byName)}

for(index in 1:length(byNameList)){
	say('heoo', by=byNameList[index])}

#-------------------------------------------------------

install.packages('reshape2')
library('reshape2')

# 자료 파악 : 변수의 성격과 해설
############### 요소에 대한 name설정
# total_bill : 전체지불비용
# tip : tip비용
# sex : 성별
# somker : 흡연석/비흡연석
# day : 요일
# time : 방문시간
# size : 방문인원
head(tips)

# 결측치 확인
sum(is.na(tips))

unique(tips[,3]) #열 즉 sex에 있는 것들

if (class(tips[,3])=='factor'){ 
print(unique(tips[,3])}


##############################################
########### 가설과 검증
########### 
##############################################
# 1번 가설 : 성별(독립변수,x값)에 따르는 tips(종속변수,y값, 레이블)의 비용은 같다
#		0가설(귀무가설)
#		검증을 통해서 비용은 같다-> 귀무가설 선택
#		비용이 다르다 -> 귀무가설 기각/대립가설 선택
#		pvalue통해서 확인함.(통계에서는)
# 일반적인 가설검증은 데이터집계를 통해서 비교

table(tips[,3]) # 성별의 빈도수, 전체데이터에서 발생횟수
table(tips[,4])
table(tips[,5])
table(tips[,6])

for (i in 3:7){   # for문 안에는 print 넣어줘야 output 가능
	print(table(tips[,i])) 
		}

for (i in 3:7){ # 각각의 정보 표시 한줄 더
	print(paste('-----', names(tips[i]),'------'))
	print(table(tips[,i]))
		}

x=unique(tips$time) # unique는 변수로 사용가능하다 즉 인덱스번호 사용가능
x[1]
x[2] # 인덱스번호로 자동화 가능

din=subset(tips, time=='Dinner') # 시간이 dinner인 것들만 따로 빼냄
lun=subset(tips, time=='Lunch')  

table(tips$time)
table(din$day)
table(lun$day)

din
head(din)


table(tips$time)
colMeans(din[c('total_bill', 'tip', 'size')]) # 행의 평균
colMeans(lun[c('total_bill', 'tip', 'size')])

colSums(din[c('total_bill', 'tip', 'size')]) # 행의 합계
colSums(lun[c('total_bill', 'tip', 'size')])


# 한눈에 알아보기 위해 차트화 

par(mfrow=c(1,2)) # 한 화면에 분할
plot(din$tip,main='din') # main="my title",xlab="x name",ylab="y name"
plot(lun$tip,main='lun')

summary(lun)
tmp=subset(lun, tip>=4)
summary(tmp)

summary(lun)

tmp=subset(tips, tips$day=='Fri'))
barplot(table(tmp$size))

#----------------------------------------
성별에 따른 팁의 가설이 없다.

table(tips$sex) # tips 성별별 빈도수 확인



man=subset(tips, sex=='Male')
woman=subset(tips, sex=='Female')

summary(man)
summary(woman)

par(mfrow=c(1,2))
plot(man$tip,main='tip of man')
plot(woman$tip,main='tip of woman')



colSums(man[c('total_bill','tip','size')]) # 성별: 남자의 팁 총합계
colSums(woman[c('total_bill','tip','size')]) # 성별 : 여자의 팁 총합계

#####-------결론 : 성별의 차이보다는 size의 차이에 따라 다르다.

#####산점도(scatter plot) : 퍼져있는 정도를 보는 것


tips

names(tips)
plot(tips[,1])

head(tips[,1])

plot(tips[,1],tips[,2])
plot(tips[,7],tips[,1],
	main='인원수-지불금액',
	xlab='인원수',
	ylab='지불금액')

str(tips)

colNum=c(1,2,7)

par(mfrow=c(3,1))

for (i in colNum){
plot(tips[,i], main=names(tips[i]))}



mtcars
str(mtcars)

plot(mtcars)

x=mtcars[,c(1,3,5,6)]
plot(x)

# 피어슨 상관계수R(-1~1사이값)
# 상관계수가 1이나 -1이면 둘사이 연관성이 크다, 0부근이면 큰 연관성은 없다.
cor(x) # -> 숫자만 있어야만 계산 가능! 즉 factor나 문자 등은 숫자로 바꿔줘야 한다.

cor(mtcars)

Q??
종속 독립은 어떻게 선정?
###########산점도의 데이터가 몰려있다면 연관관계가 크다!!!

# 상관도를 plot으로 나타내주는 패키지

install.packages("PerformanceAnalytics")
library(PerformanceAnalytics)
chart.Correlation(mtcars, histogram=TRUE, pch=19)


par(mfrow=c(1,1))

par(mfrow=c(2,2))
tmp=subset(tips,day=='Fri')

boxplot(tip~size, data=tmp)
boxplot(tip~sex, data=tmp)
boxplot(tip~smoker, data=tmp)
boxplot(tip~time, data=tmp)

tt=subset(tips,tip<5)
summary(tt)


mtcars
str(mtcars)
boxplot(mtcars$mpg)
par(mfrow=c(2,2))
boxplot(mtcars$mpg~mtcars$gear) # 기어 4개인 모델의 연비가 높다.
################################# ~: '~에 따라'라고 생각

plot(mtcars$mpg~mtcars$gear)
boxplot(mtcars$mpg~mtcars$vs) # 1자형 엔진이 연비 높다
boxplot(mtcars$mpg~mtcars$am) # am=1이 연비 더 좋다
############################### 다들 0,1 로 나온이유: 계산하기 위해


boxplot(mtcars)

tmp=scale(mtcars) # scale: 정규화시키는 함수
summary(tmp)
boxplot(tmp)
