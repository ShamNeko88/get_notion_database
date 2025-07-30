import requests
import pandas as pd


class GetNotionDatabase:
    """ Notion上のデータベースのデータを取得するモジュール

    Arguments:
        token (str): Notion APIのトークン
        database_id (str): 取得するデータベースのID
        notion_version (str): Notion APIのバージョン（デフォルトは"2022-06-28"）

    Methods:
        get_data() -> dict: データベースの全データをJSON形式で取得する
        notion_to_dataframe() -> pd.DataFrame: データベースのデータをDataFrameに変換する
        notion_to_excel(): データベースのデータをExcelファイルで出力する

    Example:
        >>> # インスタンス生成
        >>> ins = GetNotionDatabase("your_token", "your_database_id")
        >>> ins.notion_to_excel("output.xlsx")  # Excelファイルに出力

    Remarks:
        - 下記のプロパティの型以外は正しく取得できない可能性があります。:
            - title
            - rich_text
            - select
            - multi_select
            - date
            - number
            - checkbox
            - email
            - url
            - people
        - Notionのバージョンリスト: https://developers.notion.com/page/changelog
    """

    def __init__(
            self,
            token: str,
            database_id: str,
            notion_version: str = "2022-06-28"
    ):
        self.token = token
        self.database_id = database_id
        self.notion_version = notion_version
        self.url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": self.notion_version,
        }

    # 全データをjson形式で取得するメソッド
    def get_data(self) -> dict:
        response = requests.post(self.url, headers=self.headers)
        data = response.json()
        return data

    # NotionのデータベースをDataflameに変換するメソッド
    def notion_to_dataframe(self) -> pd.DataFrame:
        data = self.get_data()
        # 各行を処理
        rows = []
        for page in data.get("results", []):  # 各レコードを処理
            row = {}
            for name, prop in page["properties"].items():  # 各カラムを処理
                prop_type = prop["type"]  # プロパティのタイプを取得
                value = prop.get(prop_type)  # プロパティの値を取得
                # *****************************
                # 型に応じて値を取り出す
                # *****************************
                # テキスト系
                if prop_type in ("title", "rich_text"):
                    row[name] = value[0]["plain_text"] if value else ""
                # 単一選択肢
                elif prop_type == "select":
                    row[name] = value["name"] if value else None
                # 複数選択肢（カンマ区切りで取得）
                elif prop_type == "multi_select":
                    row[name] = ", ".join([v["name"] for v in value]) if value else None
                # 日付
                elif prop_type == "date":
                    row[name] = value["start"] if value else None
                # 数値
                elif prop_type in ("number", "checkbox", "email", "url"):
                    row[name] = value if value else None
                # ユーザー
                elif prop_type == "people":
                    row[name] = ", ".join([p["name"] for p in value]) if value else None
                # 未対応の型
                else:
                    row[name] = value if value else None
            # 上記の処理で取得した値を行に追加
            rows.append(row)
        # DataFrameに変換
        df = pd.DataFrame(rows)
        return df

    # NotionのデータべースをExcelに変換するメソッド
    def notion_to_excel(self, file_name="notion_database.xlsx"):
        df = self.notion_to_dataframe()
        df.to_excel(file_name, index=False)
