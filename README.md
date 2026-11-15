# Reinforce Game

무기를 강화하고 판매하며 더 높은 단계의 무기를 획득하는 Tkinter 게임입니다.
본 프로젝트는 2024.2.16 개발되었으며, 2026.11.16에 코드 일부를 수정하여 github에 업로드하였습니다.

## 실행 환경

- Python 3.9 이상
- Tkinter가 포함된 Python 설치
- Pillow

## 설치 및 실행

프로젝트 폴더에서 다음 명령을 실행합니다.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

macOS 또는 Linux:

```sh
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python main.py
```

Tkinter를 가져올 수 없는 경우 운영체제의 Python 설치에 Tk 지원을 추가해야 합니다.

## 게임 방법

- **강화하기**: 다음 무기의 강화 비용을 지불하고 확률에 따라 강화합니다. 실패하면 무기 단계가 하나 내려가며, 최저 단계 아래로 내려가지 않습니다.
- **판매하기**: 현재 무기를 판매하고 잔액을 얻으며, 무기는 처음 단계로 돌아갑니다.
- 게임 상태는 실행 중에만 유지됩니다.

## 프로젝트 구조

```text
main.py             게임 실행
game/game_logic.py  강화 및 판매 규칙
ui/game_ui.py       Tkinter 화면
data/weapons.json   무기 정보
data/messages.json  화면에 표시할 문구
image/              무기 이미지
```

무기 정보와 화면 문구는 각각 `data/weapons.json`과 `data/messages.json`에서 수정할 수 있습니다. 메시지의 `{weapon_name}`, `{balance:,}` 같은 항목은 실행 중 값으로 대체되므로 수정할 때 유지해야 합니다. 무기 이름을 변경하면 `image/`의 이미지 파일 이름도 함께 맞춰야 합니다.
