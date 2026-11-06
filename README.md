# cloud-computing-lab

云计算导论 · 第 13 周实验：使用 GitHub 的开发流程

## 关于我

- 姓名：李同学（请替换为真实姓名）
- 学号：2026xxxxxx（请替换为真实学号）
- GitHub：[@GZLns](https://github.com/GZLns)
- 专业方向：数据科学与大数据技术

## 这个仓库放了什么

| 文件 | 说明 |
|---|---|
| `hello.py` | 一个简单的 Python 程序，打印欢迎语并做一次小计算 |
| `README.md` | 本文件，仓库说明与自我介绍 |

## 运行方式

```bash
python hello.py
```

预期输出：

```
你好，云计算导论！
2 + 3 = 5
3 * 4 = 12
```

## 本次实验完成的事情

1. 在 GitHub 上创建远程仓库 `cloud-computing-lab`
2. 配置本地 Git 仓库与提交身份
3. 编写 `hello.py` 与 `README.md`，完成首次 `add` / `commit` / `push`
4. 修改代码后再次提交并推送，完整走一遍开发流程

## 实验过程中遇到的问题

- Windows 下 Git 提示 `LF will be replaced by CRLF`：属于换行符自动转换提示，不是错误；
  需要保持文件原样时可用 `git config core.autocrlf input`。
- 首次推送需要指定上游分支，使用 `git push -u origin main` 之后即可简写为 `git push`。
