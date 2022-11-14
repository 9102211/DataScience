single_q_str = '안녕하세요.'
print(single_q_str)

#single_q_str = ''안녕하세요' 라고 철수가 말했다.' #싱글사용시 ''인용부호사용못함

double_q_str =  "'안녕하세요' 라고 철수가 말했다."
print(double_q_str)

#double_q_str = ""안녕하세요" 라고 철수가 말했다." #더블사용시 ""인용부호사용못함
single_q_str = '"안녕하세요" 라고 철수가 말했다.'
print(single_q_str)

#mix_str = ""수리수리!" 이것은 말 그대로 '괴변'이야!! "  # '," 공존하는 문자열 처리
mix_str = "\"수리수리!\" 이것은 말 그대로 '괴변'이야!! " # 특수문자 처리(\ : escape문자)로 문제해결
print(mix_str)

str_escape = "1. 수리수리! \t마수리!"
print(str_escape)
str_escape = "2. 수리수리 \n마수리!"
print(str_escape)
str_escape = "3. 수리수리! \n마수리! \n일어나라!"
print(str_escape)
tripple_str = """
수리수리!
마수리!
일어나라!
"""
print(tripple_str)