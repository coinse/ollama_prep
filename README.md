## Ollama 설치

### 1. 다운로드

[Ollama 다운로드 링크](https://ollama.com/download/)를 방문해서 본인이 사용하는 운영체제를 위한 실행파일을 다운로드하고 설치합니다. 현재 Ollama는 macOS, Linux, Windows를 지원합니다. 

### 2. 모델 다운로드

Ollama를 이용해 구동할 LLM 모델을 다운로드합니다. 설치를 마친 후 터미널 또는 윈도우즈 Powershell에서 다음 명령어를 입력하면 Llama 3.2 모델이 다운로드됩니다. 용량이 2G 정도 되므로 시간이 조금 필요합니다.

```
$ ollama pull llama3.2
```

### 2. Python 라이브러리 설치

이 저장소에 포함된 `requirement.txt`를 이용해 Ollama 파이썬 라이브러리를 설치합니다.

```
pip install -r requirements.txt
```

### 3. 예제 코드 실행

이 저장소에 포함된 `hello.py`를 실행해, 모델이 인사에 답하는지 확인합니다.

```
$ python hello.py
It's nice to meet you. Is there something I can help you with, or would you like to chat?
$ 
```


