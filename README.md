# cursor-init

프로젝트 규칙/온톨로지/문서 템플릿을 손쉽게 세팅하는 CLI 도구

---

## ✨ 주요 기능

- `.cursorrules`, rules, docs, 온톨로지 등 템플릿 파일 일괄 복사 및 초기화
- 실무 규칙/자동화/상호 참조 구조를 표준화
- 신규 프로젝트, 팀 온보딩, 문서 일관성 유지에 최적화

---

## 📦 설치

```bash
pip install -e .
```

---

## 🚀 사용법

### 템플릿 초기화

```bash
cursor-init
```

- `-f` 또는 `--force` 옵션: 기존 파일/디렉토리 덮어쓰기

### 도움말

```bash
cursor-init --help
```

---

## 🗂️ 템플릿 구조

```
templates/
├── .cursorrules
├── rules/
├── docs/
└── ontology/
```

- `.cursorrules`: 프로젝트 전체 규칙 정의
- `rules/`: 각종 실무/자동화 규칙(mdc)
- `docs/`: 문서 템플릿
- `ontology/`: 온톨로지/의사결정 템플릿

---

## 🛠️ 개발/기여

1. 이 저장소를 fork/clone
2. 의존성 설치:
   ```bash
   pip install -e .
   ```
3. 템플릿/코어 로직 수정 후 PR 제출

---

## 📝 참고

- pyproject.toml의 `[project.scripts]`로 CLI 명령어 등록
- 템플릿 경로는 프로젝트 루트의 `templates/` 기준
- 자세한 규칙은 `.cursorrules`, `docs/`, `ontology/` 참고
- 온톨로지/문서화/자동화 규칙은 `.cursor/ontology/guide.md`에서 확인

---

## License

MIT
