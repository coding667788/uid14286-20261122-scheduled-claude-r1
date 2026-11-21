"""输入结构错误的统一表示.

任何结构错误都以 {"path": <字段位置>, "code": <错误码>, "message": <说明>}
的形式收集，最终以 InputError 抛出，由 CLI 序列化为 JSON 输出。
"""


class InputError(Exception):
    """案例文档结构校验失败。"""

    def __init__(self, errors):
        self.errors = list(errors)
        message = self.errors[0]["message"] if self.errors else "input error"
        super().__init__(message)


def add_error(errors, path, code, message):
    errors.append({"path": path, "code": code, "message": message})
