# cursor-init

프로젝트 규칙/문서 템플릿을 손쉽게 세팅하는 CLI 도구 (PyPI 배포용)

---

## ✨ 주요 기능

- `.cursorrules`, rules, docs 등 실무 규칙/문서 템플릿 일괄 복사 및 초기화
- 실무 규칙/자동화/상호 참조 구조를 표준화
- 신규 프로젝트, 팀 온보딩, 문서 일관성 유지에 최적화

---

## 🗂️ 템플릿/문서 구조

```
cursor_init/templates/profile/
├── default/
│   ├── .cursorrules
│   ├── .cursor/
│   │   ├── mcp.json
│   │   └── rules/
│   └── .cursor-init/
│       └── docs/
└── ... (프로필별 디렉토리)

.cursor-init/
├── docs/           # 공식 기술문서/가이드/프로세스 관리 경로
└── profiles/       # 프로필별 문서/규칙/스냅샷 관리
```

- `.cursorrules`: 프로젝트 전체 규칙 정의
- `rules/`: 각종 실무/자동화 규칙(mdc)
- `docs/`: 공식 기술문서/가이드/프로세스
- `profiles/`: 프로필별 문서/규칙/스냅샷 관리

---

## 🚀 사용법

### 템플릿 초기화

```bash
cursor-init docs sync
```

### 도움말

```bash
cursor-init --help
```

---

## 💡 실무 적용 예시

1. 템플릿/문서 구조 동기화

   ```bash
   cursor-init docs sync
   ```

2. 요구사항 정의 및 agent 활용
   ```bash
   # 예시: 신규 회원가입 기능 설계 요구사항을 agent에게 입력
   agent "신규 회원가입 기능 설계: 이메일 인증, 비밀번호 정책, API 명세를 포함. 요구사항에 맞게 문서를 업데이트 해주세요."
   ```

- agent를 활용하면 요구사항 분석, 시스템 설계, 문서화, 체크리스트 관리 등 실무 전 과정을 일관되게 자동화할 수 있습니다.
- 팀/고객/상황별로 프로필을 분리해 다양한 규칙/문서 세트를 손쉽게 적용하세요.

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
- 템플릿 경로는 `cursor_init/templates/profile/` 기준
- 공식 문서/구조/규칙은 `.cursor-init/docs/`, `.cursor-init/profiles/` 참고
- 자세한 구조/실무 규칙은 `.cursor-init/docs/` 내 문서 참조

---

## License

MIT
