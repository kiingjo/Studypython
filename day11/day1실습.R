getwd()
exam=read.csv("./Data/csv_exam.csv")
exam

head(exam) # 상위 6개

tail(exam) # 하위 6개

View(exam) # 시각적(표로 확인), V는 대문자

dim(exam) # 데이터 양과 컬럼 갯수 확인(차원수확인)

str(exam) # 컬럼 타이틀 확인(형식)

summary(exam) # 요약본(숫자값만 기초통계 도출)

mpg=as.data.frame(ggplot2::mpg)
mpg
head(mpg,10)

install.packages("dplyr")
library(dplyr)

df=data.frame(var1=c(4,3,8),
              var2=c(2,6,1))
df

# 행추가 
df$var_sum=df$var1+df$var2
df

df$var_sum=10
df

# 평균 행 추가
df$var_mean=(df$var1+df$var2)/2
df

head(mpg)

#통합 연비 변수 생성
mpg$total=(mpg$cty + mpg$hwy)/2
str(mpg)

# 히스토그램 그래프
hist(mpg$total)

# ifelse ( 조건, True일 때 리턴할 값, False일 때 리턴할 값)
mpg$test=ifelse(mpg$total>=20,"pass","fail")
mpg$test

mpg

str(mpg)

table(mpg$test)

library(ggplot2)
qplot(mpg$total)

# if로 범주만들기(A,B,C)
mpg$grade=ifelse(mpg$total>=30,"A",
                 ifelse(mpg$total>=20,"B","C"))
mpg$grade
table(mpg$grade)

qplot(mpg$grade)


midwest=as.data.frame(ggplot2::midwest)
midwest
dim(midwest)
str(midwest)

# 컬럼명 변경
colnames(midwest)[5]="total"
colnames(midwest)[10]="asian"

str(midwest)
names(midwest)


midwest$ratio=midwest$asian/midwest$total *100
hist(midwest$ratio)

mean(midwest$ratio)
str(midwest)
head(midwest)


midwest$group=ifdlse(midwest$ratio >0.4872462, )

#전처리-dplyr패키지
#filter(): 행추출
#arrange():정렬
#mutate(): 변수추가
#Left_join:데이터합치기(열)
#right_join:데이터합치기(행)

exam #데이터프레임

#exam에서 class가 1인 경우만 추출하여 출력
exam %>% filter(class==1) # %>%: ~중에서 

#1이 아닌것만 출력
exam %>% filter(class!=1)

# 초과,이상,미만,이하 필터 출력

#여러 조건 충족하는 행 출력
# 1반 이면서 수학 점수가 50점 이상인 경우
exam %>% filter(class==1 & math >= 50) # & : 그리고(and)

# 또는일 경우 (|)
# 수학 점수 90점이상이거나 영어점수 90이상인경우
exam %>% filter(math>=90 | english>=90)

# 조건 여러개인경우
exam %>% filter(class==1 | class==2 | class==3)

class1=exam %>% filter(class %in% c(1,3,5)) #1,3,5 해당하면 추출

mean(class1$math)

# %% : 나눗셈의 나머지
# %/% : 나눗셈의 몫

mpg
names(mpg)
##########################
tmp=mpg %>% filter(displ<=4)
dipl4=tmp$hwy
mean(dipl4)



tmp1=mpg %>% filter(displ>=5)
dipl5=tmp1$hwy

mean(dipl5)

#####################
tmp1=mpg %>% filter(manufacturer=="audi")
mean(tmp1$cty)


tmp3=mpg %>% filter(manufacturer=="toyota")
mean(tmp3$cty)


######################

class1=mpg %>% filter(manufacturer %in% c("chevrolet","ford","honda"))
tmp5=class1$hwy

mean(class1$hwy)


# 원하는 변수만 뽑아와 새로운 데이터셋 만들기

exam %>% select(class,math,english)

# 특정컬럼 제외하고 다 불러오기기

exam %>% select(-math)

# class가 1인 행만 추출한 다음 english만 추출

exam %>% filter(class==1) %>% select(english)

# id, math 뽑은뒤 상위 6개만 조회
exam %>% select(id,math) %>% head

####################33
tmp=mpg %>% select(class,cty)


########################
head(tmp)

df_suv=tmp %>% filter(class=="suv")
mean(df_suv$cty)

tmp1=subset(tmp, class=="suv") # subset은 filter 개념
mean(tmp1$cty)

df_compact=tmp %>% filter(class=="compact")
mean(df_compact$cty)


tmp2=subset(tmp, class=="compact") 
mean(tmp2$cty)



#############################