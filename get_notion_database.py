import requests


class GetNotionDatabase:
    """ Notion上のデータベースのデータを取得するモジュール

    Arguments:
        token (str): Notion APIのトークン
        database_id (str): 取得するデータベースのID
        notion_version (str): Notion APIのバージョン（デフォルトは"2022-06-28"）

    Remarks:
        - Notionのバージョンリスト: https://developers.notion.com/page/changelog
    """

    def __init__(self, token, database_id, notion_version="2022-06-28"):
        self.token = token
        self.database_id = database_id
        self.notion_version = notion_version
        self.url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": self.notion_version,
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers)
        data = response.json()
        return data
