"""
@Project  : PyWeb3Wallet
@Author   : PaxonQiao
@Time     : 2025/1/16 15:05
@Software : PyCharm
@File     : hex_to_decimal.py
"""


def hex_to_decimal(hex_value: str) -> int:
    # Check for proper input type
    if not isinstance(hex_value, str):
        raise TypeError(f"Expected a string, got {type(hex_value).__name__}")

    try:
        # Convert hexadecimal string to decimal
        decimal_value = int(hex_value, 16)
        return decimal_value
    except ValueError:
        # Handle invalid hexadecimal strings
        raise ValueError(f"Invalid hexadecimal string: {hex_value}")


if __name__ == "__main__":
    hex_v = "0x18b"
    decimal_v = hex_to_decimal(hex_v)
    print(f"hex_to_decimal: {decimal_v}")
