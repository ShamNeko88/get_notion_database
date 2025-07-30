# Notion上のデータベースのデータを取得するモジュール

## 使い方
- ディレクトリ構成（共通）
```powershell
├─get_notion_database.py
└─main.py
```


- データベースをExcelファイルへエクスポート

```python
# main.py
import get_notion_database as gnd
import unittest

ins = gnd.GetNotionDatabase(
    "Notion APIトークン",
    "データベースID"
)
ins.notion_to_excel("Excelファイル名")
```

## Notionのバージョンリスト
- バージョンリスト：https://developers.notion.com/page/changelog