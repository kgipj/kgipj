# Navi's Notes

這是一個仿照簡潔文字部落格風格的靜態網站。

## 怎麼看

直接用瀏覽器打開 `index.html`。

## 上傳到 GitHub Pages

這個資料夾已經整理成可以直接上傳 GitHub Pages 的靜態網站。

需要上傳的內容：

- `index.html`
- `style.css`
- `posts/`
- `assets/`
- `.nojekyll`
- `README.md`

不用上傳：

- `.DS_Store`

### 發布步驟

1. 到 GitHub 建一個新的 repository
2. 把這個資料夾的檔案上傳到 repository
3. 進入 repository 的 `Settings`
4. 左側找到 `Pages`
5. `Source` 選 `Deploy from a branch`
6. `Branch` 選 `main`
7. 資料夾選 `/root`
8. 按 `Save`

等一兩分鐘後，GitHub Pages 會給你一個網址。

如果 repository 名稱是一般名稱，例如 `my-blog`，網址會像：

```text
https://你的帳號.github.io/my-blog/
```

如果 repository 名稱是 `你的帳號.github.io`，網址會像：

```text
https://你的帳號.github.io/
```

## 怎麼改

- 網站標題：改 `index.html` 裡的 `Navi's Notes`
- 文章列表：改 `<ul class="post-list">` 裡面的每一個 `<li>`
- 顏色與字體：改 `style.css`
- 版權文字：改 `<footer class="site-footer">`

## 怎麼寫新文章

1. 複製 `templates/post-template.html`
2. 貼到 `posts/` 資料夾，改成新的檔名，例如 `my-note.html`
3. 打開新檔案，改文章標題、日期、標籤和內文
4. 回到 `index.html`，在 `<ul class="post-list">` 最上面新增一列文章連結

文章連結範例：

```html
<li>
  <a href="./posts/my-note.html">我的新文章</a>
  <time datetime="2026-05-06">May 6, 2026</time>
</li>
```

## 下一步

如果文章會越來越多，可以把這個版型搬到 Hugo、Astro 或 Next.js，讓文章改成 Markdown 管理。
