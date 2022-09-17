import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "http://www.dgsw.hs.kr/index.do" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#BCA9F5", "#BE81F7"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김민혁")
write("description", "안녕 김민혁이야 잘부탁해!")
write("button", "대소마고home page")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "1.음식": "다 잘먹어",
  "2.좋아하는 것": "협동게임 좋아해",
  "3.첫만남": "조금 소심해;;",
  "4.마무리": " :-)"
}
information(informations)
