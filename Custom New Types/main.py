from typing import NewType, TypeVar

ZipCode = NewType('ZipCode', int)


def increment_zip_code_and_return(code: ZipCode) -> ZipCode:
    return ZipCode(code + 1)


print(type(1234))
print(type(ZipCode(1234)))

T = TypeVar('T')


def add_zip_codes(code1: T, code2: T):
    return code1 + code2


print(add_zip_codes(1234, 5678))
print(add_zip_codes("1234", "5678"))
print(add_zip_codes(1234, 456.7))
