# Notion上のデータベースのデータを取得するモジュール
Notionを操作するPython製GUIアプリ作ってます。
とりあえず簡単なGUIツールをリリースしました。[こちら](https://github.com/ShamNeko88/notion_tools/releases/tag/ver.1.0.0)


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


# インスタンス生成
ins = gnd.GetNotionDatabase(
    "Notion APIトークン",
    "データベースID"
)
# エクセルファイル化
ins.notion_to_excel("Excelファイル名")
```

## 詳細
- Notionのバージョン指定
```Python
# インスタンス生成時に指定する
ins = gnd.GetNotionDatabase(
    "Notion APIトークン",
    "データベースID",
    notion_version = "xxxx-xx-xx"  # デフォルトは"2022-06-28"
)
```

- バージョンリスト：https://developers.notion.com/page/changelog
