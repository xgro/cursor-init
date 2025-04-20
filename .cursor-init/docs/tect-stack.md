# 기술 스택 문서

## 1. 프로젝트 개요

- 본 프로젝트는 다양한 규칙/문서/온톨로지 세트를 프로필 기반으로 관리·동기화할 수 있는 CLI 도구(MVP)를 목표로 한다.
- 공식 관리 경로는 `.cursor-init/docs/` 하위이며, 모든 기술문서/가이드/프로세스 문서는 이곳에 저장·관리한다.
- 실무 규칙, 자동화, 상호 참조 구조를 표준화하여 팀 온보딩 및 문서 일관성 확보를 지향한다.

## 2. 기술 스택 선정 기준

- 오픈소스 및 커뮤니티 활성도
- 러닝커브(빠른 MVP 구현 가능성)
- 유지보수성 및 확장성
- 자동화/테스트/문서화 친화성
- 실무 적용 경험 및 레퍼런스

## 3. 주요 기술 스택

### 백엔드

- Python 3.10 이상
- FastAPI (비동기 REST API 서버)
- uvicorn (ASGI 서버)
- pydantic (데이터 검증 및 직렬화)

### 프론트엔드

- 없음 (MVP CLI 중심, 추후 필요시 React/Next.js 등 도입 가능)

### 데이터베이스

- SQLite (내장형, MVP 단계에서 빠른 개발/테스트용)
- (확장 시 PostgreSQL 고려)

### 인프라/배포

- Docker (로컬 개발 및 배포 환경 일관성)
- GitHub Actions (CI/CD, 자동화)

### 기타 도구

- Poetry (Python 패키지/의존성 관리)
- pre-commit (코드 스타일 자동화)
- ripgrep, fzf (문서/코드 검색)
- mcp-server-time (문서 메타데이터 자동화)

## 4. 기술 스택 버전 및 호환성

- Python 3.11 이상 권장
- FastAPI 0.110.x 이상
- SQLite 3.x (내장)
- Docker Desktop 4.x 이상
- GitHub Actions 최신
- Poetry 1.7.x 이상
- 운영체제: macOS 13+, Ubuntu 22.04+, Windows 11 지원

## 5. 기술 도입/변경 이력

- 2025-04-20 MVP 기준 tech-stack 최초 정의 (FastAPI, SQLite, Poetry 등)
- 2025-04-20 CI/CD 자동화(GitHub Actions) 및 pre-commit 도입

## 6. 기술별 참고/공식 문서

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Poetry 공식 문서](https://python-poetry.org/docs/)
- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [Docker 공식 문서](https://docs.docker.com/)
- [pre-commit 공식 문서](https://pre-commit.com/)

## 7. 기술 스택 관련 FAQ

- Q: 왜 FastAPI와 SQLite를 선택했나요?
  - A: 빠른 MVP 구현, 러닝커브, 문서화/테스트/자동화 친화성, 확장성(추후 PostgreSQL 등으로 이관 용이)
- Q: 프론트엔드는 왜 제외됐나요?
  - A: MVP 단계에서는 CLI/백엔드 중심으로, 추후 필요시 React 등 도입 검토
- Q: Poetry와 pre-commit을 도입한 이유는?
  - A: 의존성 관리, 코드 품질, 자동화 효율성 극대화 목적

# 프로필 기반 기술 스택 관리 전략

## 문서 목적

- 본 문서는 프로젝트의 기술 스택(언어, 프레임워크, 도구 등)과 그 관리 전략을 명확히 정의합니다.
- 프로필 기반 템플릿 구조와 push/pull/sync/list 명령어를 활용한 tech-stack 관리 방법을 안내합니다.

## 관리 원칙

- 기술 스택 정보는 반드시 .cursor/docs/tect-stack.md에 최신화
- 주요 변경 시, 관련 온톨로지 및 규칙 문서(.cursorrules, .cursor/ontology/)와 상호 참조
- 프로필별로 다양한 기술 스택/환경을 관리할 수 있도록 구조화

## 프로필별 tech-stack 관리

- `.templates/{profile}/.cursor/docs/tect-stack.md` 형태로 각 프로필별 기술 스택 관리 가능
- 실험/고객/상황별로 독립적인 tech-stack 세트 운영 가능
- push 명령어로 현재 tech-stack을 스냅샷 저장, pull/sync로 손쉽게 복원/적용

## 명령어 연계 예시

```bash
# 현재 tech-stack을 snapshot-20240612 프로필로 저장
cursor-init docs push --name snapshot

# 특정 프로필의 tech-stack을 프로젝트에 적용
cursor-init docs pull --profile snapshot-20240612

# default 프로필의 tech-stack을 동기화
cursor-init docs sync

# 저장된 모든 프로필 리스트 확인
cursor-init docs list
```

## 실무 적용 예시

- 신규 프로젝트/고객/실험 환경별로 tech-stack을 분리 관리
- 팀원별/상황별로 최적화된 스택을 빠르게 적용 및 롤백
- 기술 스택 변경 이력 추적 및 복원 용이

## 장점

- 다양한 기술 스택/환경을 안전하게 실험 및 적용 가능
- 실수/변경/실험 후 언제든 특정 시점의 tech-stack으로 복원
- 팀/고객/상황별 맞춤형 tech-stack 관리에 최적

## 연계 문서

- 폴더/파일 구조: docs/directory-structure.md
- 워크플로우 및 명령어: docs/workflow.md
- 온톨로지/의사결정: .cursor/ontology/
- 공식 문서 위치: .cursor/docs/
