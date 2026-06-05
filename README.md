# 📁 Documents

个人文档仓库，用于保存各类文档。

---

A personal repository for storing and organizing documents.

## 📄 文档目录

- **[GraspNet-1Billion 论文解读](https://wangzihao-hub.github.io/Document/GraspNet-1Billion/)** — 网页版 · 可交互阅读

---

## 🔧 如何将本地 HTML 渲染为 GitHub 网页

以 `GraspNet-1Billion/` 为例，发布步骤只有 3 步：

### 1. 重命名 HTML 为 `index.html`

GitHub Pages 默认查找 `index.html` 作为入口文件。把 `xxx.html` 改名为 `index.html`：

```bash
mv GraspNet-1Billion.html index.html
```

### 2. 推送到 GitHub

```bash
git add .
git commit -m "Rename to index.html for Pages"
git push origin master
```

### 3. 启用 GitHub Pages（只需做一次）

进入仓库 **Settings → Pages**，选择分支 `master`，根目录 `/`，保存。

> 或者用 `gh` 命令行一步开启：
> ```bash
> gh api repos/<用户名>/<仓库名>/pages -X POST -F "source[branch]=master" -F "source[path]=/"
> ```

---

### 🎯 访问规则

| 本地路径 | 网页地址 |
|---------|---------|
| `xxx/index.html` | `https://<用户名>.github.io/<仓库名>/xxx/` |
| 根目录 `index.html` | `https://<用户名>.github.io/<仓库名>/` |

**以后新增文档**：只需建一个新文件夹，把 HTML 放进去并命名为 `index.html`，`git push` 即自动上线。<br>
别忘了在这份 README 里补一个链接，方便他人找到入口。
