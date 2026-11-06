#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""云计算导论 第 13 周实验：一个简单的 Python 程序。

运行：python hello.py
"""


def greet(name: str = "云计算导论") -> str:
    """返回一句欢迎语。"""
    return f"你好，{name}！"


def add(a: int, b: int) -> int:
    """返回两数之和。"""
    return a + b


def main() -> None:
    print(greet())
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
