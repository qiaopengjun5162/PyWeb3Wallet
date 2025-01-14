"""
@Project  : PyWeb3Wallet
@Author   : PaxonQiao
@Time     : 2025/1/14 20:42
@Software : PyCharm
@File     : mnemonic_demo.py
"""

from mnemonic import Mnemonic

# https://github.com/trezor/python-mnemonic
language = "english"
mnemo = Mnemonic(language)
words = mnemo.generate(strength=256)
print(f"word: {words}")

seed = mnemo.to_seed(words, passphrase="")
entropy = mnemo.to_entropy(words)

print(f"entropy: {entropy}")
