# 기술 스택 문서

## 1. 목적

- 본 문서는 프로젝트의 기술 스택(언어, 프레임워크, 도구 등)과 그 관리 전략을 명확히 정의합니다.
- 프로필 기반 템플릿 구조와 push/pull/sync/list 명령어를 활용한 tech-stack 관리 방법을 안내합니다.

## 2. 기술 스택 선정 기준

- 오픈소스 및 커뮤니티 활성도
- 러닝커브(빠른 MVP 구현 가능성)
- 유지보수성 및 확장성
- 자동화/테스트/문서화 친화성
- 실무 적용 경험 및 레퍼런스

## 3. 주요 기술 스택

- **백엔드**: (현재는 별도 서버 없이 CLI/파일 시스템 기반, 추후 REST API 등 확장 시 FastAPI 등 도입 가능)
- **데이터베이스**: SQLite (MVP 단계, 확장 시 PostgreSQL 고려)
- **인프라/배포**: Docker, GitHub Actions
- **기타 도구**: Poetry, pre-commit, ripgrep, fzf, mcp-server-time
- **프론트엔드**: 없음 (MVP CLI 중심, 필요시 React/Next.js 등 도입 가능)

## 4. 기술 스택 버전 및 호환성

- Python 3.10 이상 권장
- 운영체제: macOS 13+, Ubuntu 22.04+

## 5. 관리 원칙

- 기술 스택 정보는 반드시 .cursor-init/docs/tect-stack.md에 최신화
- 주요 변경 시, 관련 규칙 문서(.cursorrules 등)와 상호 참조
- 프로필별로 다양한 기술 스택/환경을 관리할 수 있도록 구조화

## 6. 프로필별 tech-stack 관리

- `.templates/{profile}/.cursor/docs/tect-stack.md` 형태로 각 프로필별 기술 스택 관리 가능
- 실험/고객/상황별로 독립적인 tech-stack 세트 운영 가능
- push 명령어로 현재 tech-stack을 스냅샷 저장, pull/sync로 손쉽게 복원/적용

## 7. 명령어 연계 및 실무 적용 예시

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

- 신규 프로젝트/고객/실험 환경별로 tech-stack을 분리 관리
- 팀원별/상황별로 최적화된 스택을 빠르게 적용 및 롤백
- 기술 스택 변경 이력 추적 및 복원 용이
- agent 등 자동화 도구와 연동하여 실무 전 과정을 일관되게 자동화 가능

## 8. 장점

- 다양한 기술 스택/환경을 안전하게 실험 및 적용 가능
- 실수/변경/실험 후 언제든 특정 시점의 tech-stack으로 복원
- 팀/고객/상황별 맞춤형 tech-stack 관리에 최적

## 9. 연계 문서

- 폴더/파일 구조: .cursor-init/docs/directory-structure.md
- 워크플로우 및 명령어: .cursor-init/docs/workflow.md
- 공식 문서 위치: .cursor-init/docs/

## 10. 기술 스택 관련 FAQ

- Q: 왜 FastAPI와 SQLite를 선택했나요?
  - A: 빠른 MVP 구현, 러닝커브, 문서화/테스트/자동화 친화성, 확장성(추후 PostgreSQL 등으로 이관 용이)
- Q: 프론트엔드는 왜 제외됐나요?
  - A: MVP 단계에서는 CLI/백엔드 중심으로, 추후 필요시 React 등 도입 검토
- Q: Poetry와 pre-commit을 도입한 이유는?
  - A: 의존성 관리, 코드 품질, 자동화 효율성 극대화 목적

## 11. 서비스 구현 현황 (2025-04-21 기준)

- 문서/프로필 관리 자동화는 Python 표준 라이브러리(shutil 등)와 mcp-server-time 기반으로 구현 중
- push/pull/sync 명령어의 메타데이터 자동화 및 실무 규칙 연동 예정
