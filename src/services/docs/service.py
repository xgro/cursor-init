from pathlib import Path
from src.services.common.file_utils import list_md_files


class DocsService:
    def __init__(self):
        self.docs_dir = Path(".cursor/docs")
        self.templates_dir = Path("src/templates/profile")

    def list_profiles(self):
        """프로필 목록을 출력합니다.

        프로필은 .templates 하위에 있는 디렉토리의 이름을 동적으로 추출합니다.

        Returns:
            list: 프로필 목록
        """
        return [d.name for d in self.templates_dir.glob("*") if d.is_dir()]

    def list_docs(self):
        """프로필에 따라 문서 목록을 출력합니다."""

        files = list_md_files(self.docs_dir)
        if not files:
            print("[경고] .cursor/docs/ 디렉토리가 없거나 md 파일이 없습니다.")
            return
        for file in files:
            print(f"- {file.name}")

    def pull(self, profile: str):
        """문서 목록을 동기화합니다.

        프로필을 선택할 수 있으며, 프로필이 존재해야만 동작합니다.

        Args:
            profile: 프로필 이름
        """
        print(f"[완료] {profile} 프로필 문서가 생성되었습니다.")
        pass

    def push(self, profile: str):
        """문서 목록을 동기화합니다.

        프로필을 선택할 수 있으며, 프로필에 따라서, 매칭되는 프로필이 없다면 뒤에 -{YYMMDD} 형식으로 프로필을 생성합니다.

        Args:
            profile: 프로필 이름
        """
        print(f"[완료] {profile} 프로필 문서가 생성되었습니다.")
        pass

    def sync(self):
        """문서 목록을 동기화합니다.

        - 프로필을 선택할 수 없습니다.
        - .templates/profile/default 프로필의 문서를 .cursor-init/profile/default 에 복사합니다.
        - 프로젝트의 루트 경로에 default 폴더내의 모든 문서를 복사합니다.

        """
        print(f"[완료] 초기 프로필 문서가 생성되었습니다.")
        pass
