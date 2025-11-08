# QRGen

一個簡單的 QR Code 生成器，支援在 QR Code 中心嵌入 Logo 圖片。

## 功能特色

- 生成標準 QR Code
- 支援在 QR Code 中心嵌入自訂 Logo
- 可調整 QR Code 大小
- 使用高容錯率 (ERROR_CORRECT_H) 確保掃描穩定性

## 安裝

使用 [uv](https://github.com/astral-sh/uv) 管理依賴：

```bash
uv sync
```

或使用 pip：

```bash
pip install qrcode pillow
```

## 使用方式

### 基本用法

生成簡單的 QR Code：

```bash
python main.py -d "https://example.com"
```

### 帶 Logo 的 QR Code

```bash
python main.py -d "https://example.com" -l logo.png -o output.png
```

### 完整參數

```bash
python main.py -d "https://example.com" -l logo.png -o qrcode.png -s 15
```

## 參數說明

- `-d, --data`: (必填) 要編碼的資料或網址
- `-l, --logo`: (可選) Logo 圖片路徑
- `-o, --output`: (可選) 輸出檔案名稱 (預設: `qr.png`)
- `-s, --scale`: (可選) QR Code 方塊大小 (預設: `10`)

## 範例

```bash
# 生成網址 QR Code
python main.py -d "https://github.com"

# 生成帶 Logo 的 QR Code
python main.py -d "https://github.com" -l mylogo.png

# 自訂輸出檔名和大小
python main.py -d "Contact: +886912345678" -o contact.png -s 12
```

## 技術細節

- 使用 `qrcode` 函式庫生成 QR Code
- 使用 `Pillow (PIL)` 處理圖片
- Logo 自動調整為 QR Code 寬度的 1/4
- 採用高容錯率 (ERROR_CORRECT_H) 以容納中心 Logo

## 授權

MIT License
