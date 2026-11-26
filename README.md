# cloud-computing-lab

云计算导论 · 第 13 周实验：使用 GitHub 的开发流程

## 关于我

- 姓名：罗子俊
- GitHub：[@GZLns](https://github.com/GZLns)
- 学院：广州大学 经济与统计学院
- 专业方向：数据科学与大数据技术

## 这个仓库放了什么

| 文件 | 说明 |
|---|---|
| `hello.py` | 一个简单的 Python 程序：打招呼，并做加、乘、求平均值三种计算 |
| `README.md` | 本文件，仓库说明与自我介绍 |
| `.gitignore` | 忽略 Python 运行时产生的缓存文件 |

## 运行方式

默认参数运行：

```bash
python hello.py
```

预期输出：

```
你好，云计算导论！
2 + 3 = 5
2 * 3 = 6
2 与 3 的平均值 = 2.50
```

也可以自己指定参数：

```bash
python hello.py --name 罗子俊 --a 7 --b 6
```

预期输出：

```
你好，罗子俊！
7 + 6 = 13
7 * 6 = 42
7 与 6 的平均值 = 6.50
```

## 实验步骤与命令记录

```bash
# 1. 配置提交身份
git config --global user.name  "GZLns"
git config --global user.email "13425121993@163.com"

# 2. 本地初始化并与远程仓库关联
git init
git remote add origin https://github.com/GZLns/cloud-computing-lab.git

# 3. 首次提交与推送
git add .
git commit -m "feat: 初始化仓库，添加 README 与 hello.py"
git push -u origin main

# 4. 修改代码后再次提交推送
git add .
git commit -m "feat: 新增 multiply 函数并补充 README 输出示例"
git push

# 5. 查看提交历史
git log --oneline
```

## 本次实验完成的事情

1. 在 GitHub 上创建远程仓库 `cloud-computing-lab`
2. 配置本地 Git 仓库与提交身份
3. 编写 `hello.py` 与 `README.md`，完成首次 `add` / `commit` / `push`
4. 新增 `multiply` 函数并推送，第一次走通「改代码 → 提交 → 推送」
5. 为 `hello.py` 增加命令行参数解析与 `average` 函数，补全个人信息后再次提交推送，完整走通一遍开发流程

## 实验过程中遇到的问题

- Windows 下 Git 提示 `LF will be replaced by CRLF`：属于换行符自动转换提示，不是错误；
  需要保持文件原样时可用 `git config core.autocrlf input`。
- 首次推送需要指定上游分支，使用 `git push -u origin main` 之后即可简写为 `git push`。
- `git add .` 会连同新文件一起暂存，提交前先跑一次 `git status` 确认暂存内容，
  可以避免把无关文件误提交上去。
