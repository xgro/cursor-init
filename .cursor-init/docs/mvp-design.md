# MVP 설계 및 구현 (cursor-init)

## 1. MVP 목표

- 다양한 프로젝트/팀/상황에 맞는 규칙/문서 세트를 **프로필 단위**로 손쉽게 관리/동기화할 수 있는 CLI 도구 제공
- **공식 관리 경로는 .cursor-init/docs/ 하위**로, 모든 기술문서/가이드/프로세스 문서는 이곳에 저장/관리
- 실무 규칙, 자동화, 상호 참조 구조를 표준화하여 팀 온보딩 및 문서 일관성 확보

## 2. 핵심 기능 및 관리 원칙

- 모든 문서는 반드시 .cursor-init/docs/ 하위에 저장/관리
- profiles/ 하위에 다양한 프로필(운영, 스냅샷, 실험 등) 관리 가능
- 각 프로필은 .cursor/, .cursor-init/, .cursorrules, mcp.json, docs, rules 등 필요한 파일/폴더를 자유롭게 포함
- 문서/프로필/스냅샷의 실제 접근·조작은 커서(코드/CLI/자동화)에서만 처리하며, 규칙 파일에서는 관리 원칙만 명시
- 문서 생성/수정/삭제 시, 메타데이터(created_at, update_at 등)는 자동화 도구를 통해 관리
- 문서와 기술문서 등은 반드시 상호 참조(related_docs, 링크 등)를 남김

## 3. 구조 및 워크플로우

### 디렉토리 구조 예시

```
프로젝트 루트/
├── .cursor-init/
│   ├── docs/
│   │   ├── tech-stack.md
│   │   ├── mvp-design.md
│   │   └── ...
│   └── profiles/
│       ├── default/
│       │   └── .cursor/
│       │   │   ├── mcp.json
│       │   │   └── rules/
│       │   └── .cursor-init/
│       │   │   └── docs/
│       │   └── .cursorrules
│       ├── snapshot-YYYYMMDD/
│       │   └── .cursor/
│       │   │   ├── mcp.json
│       │   │   └── rules/
│       │   └── .cursor-init/
│       │   │   └── docs/
│       │   └── .cursorrules
│       └── ...
└── ...
```

- `.cursor-init/docs/` : 프로젝트 전체 기술문서/가이드 등 공식 관리 경로
- `.cursor-init/profiles/{profile}/` : 각 프로필별로 `.cursor/`, `.cursor-init/`, `.cursorrules`, `mcp.json`, `rules/`, `docs/` 등 필요한 구조만 자유롭게 포함
  - `default/` : 실제 운영/작업 공간(mcp.json, rules, docs 등 포함)
  - `snapshot-YYYYMMDD/` : 특정 시점의 스냅샷, 실험, 롤백 등 다양한 상태 관리
- 기존 `docs/` 경로는 더 이상 사용하지 않으며, `.cursor-init/docs/`가 공식 문서 관리 위치입니다.

### 동기화 워크플로우

1. cursor_init/templates/profile/default/의 템플릿/규칙/문서 구조를 준비
2. `uvx cursor-init docs sync` 실행 → .cursor-init/profiles/default/로 복사
3. 필요시 force 옵션으로 기존 파일 덮어쓰기

## 4. 자동화 및 실무 적용

- MCP 서버 정보 등록/조회 자동화(`cursor-init mcp add/list`)
- 문서 작업 시 mcp-server-time 기반 created_at, updated_at 자동 기록
- agent(예: AI, 자동화 도구)와 연동하여 요구사항 분석, 시스템 설계, 문서화, 체크리스트 관리 등 실무 전 과정을 일관되게 자동화 가능
- PR 리뷰, 자동화 체크리스트, 일관성 검토 필수

### 실무 적용 예시

1. 템플릿/문서 구조 동기화
   ```bash
   uvx cursor-init docs sync
   ```
2. 요구사항 정의 및 agent 활용
   ```bash
   # 예시: 신규 회원가입 기능 설계 요구사항을 agent에게 입력
   agent "신규 회원가입 기능 설계: 이메일 인증, 비밀번호 정책, API 명세를 포함. 요구사항에 맞게 문서를 업데이트 해주세요."
   ```

- agent를 활용하면 요구사항 분석, 시스템 설계, 문서화, 체크리스트 관리 등 실무 전 과정을 일관되게 자동화할 수 있습니다.
- 팀/고객/상황별로 프로필을 분리해 다양한 규칙/문서 세트를 손쉽게 적용하세요.

## 5. 서비스 구현 현황

- 위치: `cursor_init/services/docs/service.py`
- 주요 기능:
  - `list_profiles()`: 템플릿 디렉토리 내 프로필 목록 동적 추출
  - `pull(profile)`: 지정 프로필의 문서 동기화(구현 중, 메시지 출력)
  - `push(profile)`: 지정 프로필로 문서 스냅샷 저장(구현 중, 메시지 출력)
  - `sync()`: default 프로필 기준 문서 전체 동기화(실제 파일 복사 구현)
- 향후 계획:
  - `list_docs()` 등 문서 목록 조회 기능 추가 예정
  - pull/push의 실제 파일 복사 및 메타데이터 관리 로직 구현 예정
  - 프로필별 문서/규칙 동기화 고도화
- Python 표준 라이브러리(Path, shutil 등) 기반 파일/디렉토리 조작
- 프로필 기반 템플릿 구조(`cursor_init/templates/profile/`)와 공식 관리 경로(`.cursor-init/`) 연동
- 향후 mcp-server-time 연동, created_at/update_at 자동화, 실무 규칙 준수 예정

## 6. 확장성 및 발전 방향

- **모든 프로필이 동일한 구조/확장성을 가지며, 필요한 파일/폴더만 자유롭게 포함**
- 다양한 규칙/문서 세트 지원(팀/고객/상황별 맞춤화)
- docs create, docs update, docs list 등 문서 관리 기능 확장 예정
- MCP 서버 메타데이터 구조 확장 및 동적 필드 지원
- 문서/코드/자동화 파이프라인 연동(프로필별로 적용)

## 7. 참고 자료

- 폴더/파일 구조: .cursor-init/docs/directory-structure.md
- 워크플로우 및 명령어: .cursor-init/docs/workflow.md
- 기술 스택: .cursor-init/docs/tect-stack.md
- 공식 문서 위치: .cursor-init/docs/
