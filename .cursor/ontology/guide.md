---
doc_id: docs-YYYYMMDD-guide-001
version: "v1.0.0"
related_docs: []
metadata:
  type: "guide"
  subject: "Ontology"
  title: "온톨로지 시스템 가이드"
  author: "작성자"
  owner: "ontology-lead"
  status: "Completed"
  priority: "High"
  impact: "Maintenance"
  related: ["Documentation", "Workflow"]
  tags: ["guide", "documentation", "workflow"]
  description: "온톨로지 시스템을 효과적으로 운영하는 방법을 설명하는 문서"
  system: ["ontology-system", "doc-management"]
  access_level: "internal"
  security_level: "일반"
  automation: ["github-actions", "slack-notify"]
  linked_issues: []
  changelog:
    - date: "YYYY-MM-DD"
      author: "작성자"
      change: "최초 작성"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
reviewers: []
---

# 온톨로지 시스템 가이드

## 1. 목적 및 원칙

- 모든 의사결정, 논의, 리뷰, 승인/반려 이력은 **.cursor/ontology/**에 Markdown 문서로 기록한다.
- **모든 온톨로지 문서는 관련 docs 문서와 반드시 상호 참조(링크)를 남긴다.**
- YAML Frontmatter의 `related_docs` 필드에는 반드시 관련 docs 파일명을 포함한다.
- docs 문서에도 관련 온톨로지 문서의 파일명/링크를 명시한다.
- **문서 작업(생성/수정/삭제) 시 mcp-server-time을 호출하여 created_at, updated_at 필드를 반드시 최신화한다.**
- 파일명은 `YYYY-MM-DD-주제-유형.md`로 작성한다. (예: 2024-06-10-tech-stack-decision.md)
- 모든 문서는 Git으로 버전 관리하며, PR/리뷰/승인 프로세스를 따른다.

---

## 2. 문서 구조 및 Neo4j 연동 메타데이터 표준

- YAML Frontmatter에 아래 항목을 반드시 포함한다.
  - doc_id, version, related_docs, metadata(상세), created_at, updated_at, reviewers 등
- Neo4j 등 그래프DB 연동을 위해 배열/관계형 필드는 항상 명확히 표기한다.
- 관계형 필드는 배열로 표기, 역할/방향성 명확히(예: author, owner, reviewers, tags 등)
- 예시:
  ```yaml
  ---
  doc_id: "docs-20240610-tech-stack-decision-001"
  version: "v1.0.0"
  related_docs: ["docs/00.tech-stack.md"]
  metadata:
    type: "decision"
    subject: "TechStack"
    title: "기술 스택 선정 의사결정"
    author: "xgro"
    owner: "tech-lead"
    status: "Approved"
    priority: "High"
    impact: "Architecture"
    related: ["Documentation"]
    tags: ["decision", "tech-stack"]
    description: "기술 스택 선정 과정 및 결정 근거"
    system: ["uv", "python"]
    access_level: "internal"
    security_level: "일반"
    automation: ["github-actions"]
    linked_issues: ["#123"]
    changelog:
      - date: "2024-06-10"
        author: "xgro"
        change: "최초 작성"
  created_at: "2024-06-10T09:00:00+09:00"
  updated_at: "2024-06-10T09:00:00+09:00"
  reviewers: ["devA", "devB"]
  ---
  ```

---

## 3. 작성/관리 워크플로우

1. **새로운 의사결정/논의/리뷰/승인 이력이 발생하면, 반드시 .cursor/ontology/에 문서를 생성한다.**
2. 문서 생성 시 mcp-server-time을 호출하여 created_at, updated_at을 기록한다.
3. 관련 docs 문서의 상단(Frontmatter 또는 본문)에 해당 온톨로지 문서의 링크를 추가한다.
4. 온톨로지 문서의 `related_docs` 필드에 관련 docs 파일명을 반드시 추가한다.
5. 문서 변경 시 updated_at을 반드시 갱신한다.
6. PR/리뷰/승인 등 협업 프로세스는 GitHub Actions 등 자동화 도구와 연동한다.
7. 정기적으로 온톨로지-문서-코드의 일관성을 검토한다.

---

## 4. 자동화 및 체크리스트

- 문서 생성/수정/삭제 시, 관련 docs와 update_at 필드를 동기화한다.
- 상호 참조가 없는 문서는 "임시(Draft)" 상태로 간주하며, 승인/배포하지 않는다.
- PR, 리뷰, 자동화 도구(GitHub Actions 등)에서 상호 참조 누락 시 경고/수정 요청을 한다.
- 정기적으로 온톨로지-문서-코드의 일관성 검토 및 개선을 실시한다.

---

## 5. 예시: docs와 온톨로지 상호 참조

- docs/00.tech-stack.md 상단에
  > 관련 의사결정: [.cursor/ontology/2024-06-10-tech-stack-decision.md]
- .cursor/ontology/2024-06-10-tech-stack-decision.md의 YAML Frontmatter에  
  related_docs: ["docs/00.tech-stack.md"]

---

## 6. Neo4j(그래프DB) 확장성

- 모든 온톨로지 문서의 메타데이터(YAML Frontmatter)는 Neo4j에서 엔티티/관계로 자동 변환 가능하도록 설계한다.
- doc_id, related_docs, tags, author, owner, reviewers 등은 각각 노드/관계로 매핑한다.
- 관계형 필드는 항상 배열로 표기, 관계 방향성/역할 명확히.
- Neo4j 연동 스크립트/자동화 파이프라인을 통해 온톨로지/문서 변경 시 Neo4j에 자동 반영한다.

---

## 7. 유지보수 및 개선

- 팀 내에서 정기적으로 온톨로지 문서와 docs의 일관성, 최신성, 품질을 검토한다.
- 개발자 피드백을 반영하여 온톨로지 구조와 관리 프로세스를 지속적으로 개선한다.

---

# 반드시 기억할 것!

- **온톨로지와 docs의 상호 참조(related_docs, 링크 등)를 반드시 남길 것!**
- **mcp-server-time을 호출하여 created_at, updated_at을 항상 최신화할 것!**
- **자동화/체크리스트로 누락을 방지할 것!**
- **온톨로지, docs, 코드, Neo4j의 일관성을 항상 유지할 것!**
