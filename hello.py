#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""云计算导论 第 13 周实验：一个简单的 Python 程序。

运行：
    python hello.py                             # 使用默认参数
    python hello.py --name 罗子俊 --a 7 --b 6    # 自定义参数
"""

import argparse


def greet(name: str = "云计算导论") -> str:
    """返回一句欢迎语。"""
    return f"你好，{name}！"


def add(a: int, b: int) -> int:
    """返回两数之和。"""
    return a + b


def multiply(a: int, b: int) -> int:
    """返回两数之积。"""
    return a * b


def average(numbers: list) -> float:
    """返回一组数字的平均值；空列表返回 0.0。"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def main() -> None:
    parser = argparse.ArgumentParser(description="云计算导论第 13 周实验程序")
    parser.add_argument("--name", default="云计算导论", help="打招呼的对象")
    parser.add_argument("--a", type=int, default=2, help="第一个操作数")
    parser.add_argument("--b", type=int, default=3, help="第二个操作数")
    args = parser.parse_args()

    print(greet(args.name))
    print(f"{args.a} + {args.b} = {add(args.a, args.b)}")
    print(f"{args.a} * {args.b} = {multiply(args.a, args.b)}")
    print(f"{args.a} 与 {args.b} 的平均值 = {average([args.a, args.b]):.2f}")


if __name__ == "__main__":
    main()
