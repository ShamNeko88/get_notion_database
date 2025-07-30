# Notion上のデータベースのデータを取得するモジュール

## 使い方
- データベースをExcelファイルへエクスポート

```python
import get_notion_database as gnd
import unittest

ins = gnd.GetNotionDatabase(
    "Notion APIトークン",
    "データベースID"
)
ins.notion_to_excel()
```

## Notionのバージョンリスト
- バージョンリスト：https://developers.notion.com/page/changelog