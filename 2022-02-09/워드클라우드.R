####텍스트마이닝(Text mining)
#문자로 된 데이터에서 정보얻어내는 분석 기법
#사람들이 어떤 이야기를 나누고 있는지 파악할 때 사용
#형태소분석:문장을 구성하는 어절들이 어떤 품사로 되어 있는지 분석
#분석절차
#-형태소 분석
#-명사, 동사 형용사 등 의미를 지닌 품사 단어 추출
#-빈도표 만들기
#-시각화

install.packages("usethis")
usethis::edit_r_environ() # 탭하나 뜬다
#PATH="${RTOOLS40_HOME}\usr\bin;${PATH}" 이거 적기

Sys.which("make")

install.packages("rJava")
install.packages("remotes")
remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch"))


library(KoNLP)
text <- "R은 통계 계산과 그래픽을 위한 프로그래밍 언어이자 소프트웨어 환경이자 프리웨어이다.[2] 뉴질랜드 오클랜드 대학의 로버트 젠틀맨(Robert Gentleman)과 로스 이하카(Ross Ihaka)에 의해 시작되어 현재는 R 코어 팀이 개발하고 있다. R는 GPL 하에 배포되는 S 프로그래밍 언어의 구현으로 GNU S라고도 한다. R는 통계 소프트웨어 개발과 자료 분석에 널리 사용되고 있으며, 패키지 개발이 용이해 통계 소프트웨어 개발에 많이 쓰이고 있다."
extractNoun(text)

#패키지로드
library(dplyr)
library(KoNLP)

# 사전 설정하기
useNIADic()

#데이터불러오기
txt=readLines("./Data/hiphop.txt", encoding = "UTF-8")
head(txt)



