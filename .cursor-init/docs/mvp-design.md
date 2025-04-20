# MVP 설계 및 구현 (cursor-init)

## 1. MVP 목표

- 다양한 프로젝트/팀/상황에 맞는 규칙/문서/온톨로지 세트를 **프로필 단위**로 손쉽게 관리/동기화할 수 있는 CLI 도구 제공
- **공식 관리 경로는 .cursor-init/docs/ 하위**로, 모든 기술문서/가이드/프로세스 문서는 이곳에 저장/관리
- 실무 규칙, 자동화, 상호 참조 구조를 표준화하여 팀 온보딩 및 문서 일관성 확보

## 2. 핵심 기능 및 관리 원칙

- 모든 문서는 반드시 .cursor-init/docs/ 하위에 저장/관리
- profiles/ 하위에 다양한 프로필(운영, 온톨로지, 스냅샷, 실험 등) 관리 가능
- 각 프로필은 .cursor/, .cursor-init/, .cursorrules, mcp.json, docs, rules, ontology 등 필요한 파일/폴더를 자유롭게 포함
- 문서/프로필/스냅샷의 실제 접근·조작은 커서(코드/CLI/자동화)에서만 처리하며, 규칙 파일에서는 관리 원칙만 명시
- docs/는 프로젝트 전체 기술문서/가이드 등으로 사용
- 문서 생성/수정/삭제 시, 메타데이터(created_at, update_at 등)는 자동화 도구를 통해 관리
- 문서와 온톨로지, 기술문서 등은 반드시 상호 참조(related_docs, 링크 등)를 남김

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
│       ├── ontology/
│       │   └── .cursor/
│       │   │   ├── mcp.json
│       │   │   └── rules/
│       │   └── .cursor-init/
│       │   │   ├── docs/
│       │   │   └── ontology/
│       │   └── .cursorrules
│       ├── snapshot-20240612/
│       │   └── .cursor/
│       │   │   ├── mcp.json
│       │   │   └── rules/
│       │   └── .cursor-init/
│       │   │   ├── docs/
│       │   │   └── ontology/
│       │   └── .cursorrules
│       └── ...
└── ...
```

- `.cursor-init/docs/` : 프로젝트 전체 기술문서/가이드 등 공식 관리 경로
- `.cursor-init/profiles/{profile}/` : 각 프로필별로 `.cursor/`, `.cursor-init/`, `.cursorrules`, `mcp.json`, `rules/`, `docs/`, `ontology/` 등 필요한 구조만 자유롭게 포함
  - `default/` : 실제 운영/작업 공간(온톨로지 미포함, mcp.json, rules, docs 등 포함 가능)
  - `ontology/` : 온톨로지/의사결정/지식그래프 등 특화 기능 실험 및 관리
  - `snapshot-YYYYMMDD/` : 특정 시점의 스냅샷, 실험, 롤백 등 다양한 상태 관리
- 모든 프로필은 동일한 구조와 확장성을 가지며, 필요한 파일/폴더만 자유롭게 포함할 수 있음
- 기존 `docs/` 경로는 더 이상 사용하지 않으며, `.cursor-init/docs/`가 공식 문서 관리 위치입니다.

### 동기화 워크플로우

1. src/.templates/default/의 템플릿/규칙/문서/온톨로지 구조를 준비
2. `cursor-init sync` 실행 → .cursor-init/profiles/default/로 복사
3. **default 프로필 사용 시 온톨로지 관련 파일/폴더는 생성되지 않음**
4. 필요시 force 옵션으로 기존 파일 덮어쓰기

## 4. 자동화 및 실무 적용

- MCP 서버 정보 등록/조회 자동화(`cursor-init mcp add/list`)
- 문서 작업 시 mcp-server-time 기반 created_at, updated_at 자동 기록
- docs/와 온톨로지(.cursor-init/profiles/ontology/.cursor/ontology/) 상호 참조 자동화(온톨로지 프로필에서만 적용)
- PR 리뷰, 자동화 체크리스트, 일관성 검토 필수

## 5. 확장성 및 발전 방향

- **모든 프로필이 동일한 구조/확장성을 가지며, 필요한 파일/폴더만 자유롭게 포함**
- 다양한 규칙/문서/온톨로지 세트 지원(팀/고객/상황별 맞춤화)
- docs create, docs update, docs list 등 문서 관리 기능 확장 예정
- MCP 서버 메타데이터 구조 확장 및 동적 필드 지원
- 온톨로지/문서/코드/자동화 파이프라인 연동(프로필별로 적용)

## 6. 참고 자료

- 폴더/파일 구조: .cursor-init/docs/directory-structure.md
- 워크플로우 및 명령어: .cursor-init/docs/workflow.md
- 기술 스택: .cursor-init/docs/tect-stack.md
- 온톨로지/의사결정: .cursor-init/profiles/ontology/.cursor/ontology/
- 공식 문서 위치: .cursor-init/docs/
