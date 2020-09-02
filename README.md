# 💻Python Study - missing functions💻

creat functions and use default arguments

# Language
python

# Description
function과 default arguments를 출력에 맞게 생성해 본다<br>


# What I Learned
arguments와 parameter가 익숙하지 않은 때에 좋은 공부가 되었다<br>
list와 list의 여러가지 함수를 같이 써보았다<br>

* Python 기본문법<br>
  
  * What I Used
  
    * functions
    * list , list functions
    * default argument
    * parameter 
    * return 

# Reference
  nomad coders 
  


      #days나 a같은 변수명은 a_list, word와 같이 달리 하는것이 구분하기 더 좋다
      def is_on_list(days=[],a=""): <-정의된 함수의 ()는 default argument 부분이 된다 
        return a in days #1번 (초보자 눈높이에 맞춰 번호로 출력값을 연계하였다)

      def get_x(days=[],a=0): #a변수 대신 index라고 선언하면 보기 더 좋았을 것.
        return days[a] #2번

      def add_x(days=[],a=""):
        return days.append(a) #3번

      def remove_x(days=[],a=""):
        return days.remove(a) #4번 

      # \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

      days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

      print("Is Wed on 'days' list?", is_on_list(days, "Wed")) #1번 

      print("The fourth item in 'days' is:", get_x(days, 3)) #2번 

      add_x(days, "Sat")
      print(days) #3번

      remove_x(days, "Mon")
      print(days) #4번


      # /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
