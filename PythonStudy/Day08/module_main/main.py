# main.py 파일
import test_module

print("# 메인의 __name__ 출력하기")
print(__name__)
print()

# 코드를 실행하면 엔트리 포인트 파일에서
# "__main__"를 출력하지만 module 파일에서는 모듈 이름을 출력한다.