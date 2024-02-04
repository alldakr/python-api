# 베이스 이미지 설정 (예: Python 3.8 이미지 사용)
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /

# 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사
COPY . /python-api

# 필요한 패키지 설치 (requirements.txt 파일이 있다면 사용)
COPY requirements.txt /python-api/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 실행
CMD ["python", "main.py"]