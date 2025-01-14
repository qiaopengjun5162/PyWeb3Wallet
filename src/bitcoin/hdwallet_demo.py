"""
@Project  : PyWeb3Wallet
@Author   : PaxonQiao
@Time     : 2025/1/14 21:10
@Software : PyCharm
@File     : hdwallet_demo.py
"""

from hdwallet import HDWallet
from hdwallet.entropies import BIP39Entropy, BIP39_ENTROPY_STRENGTHS
from hdwallet.mnemonics import BIP39_MNEMONIC_LANGUAGES
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.hds import BIP32HD
from hdwallet.derivations import CustomDerivation
from hdwallet.const import PUBLIC_KEY_TYPES

import json

# Initialize Bitcoin HDWallet
hdwallet: HDWallet = (
    HDWallet(
        cryptocurrency=Cryptocurrency,
        hd=BIP32HD,
        network=Cryptocurrency.NETWORKS.MAINNET,
        language=BIP39_MNEMONIC_LANGUAGES.KOREAN,
        public_key_type=PUBLIC_KEY_TYPES.COMPRESSED,
        passphrase="talonlab",
    )
    .from_entropy(  # Get Bitcoin HDWallet from entropy
        entropy=BIP39Entropy(
            entropy=BIP39Entropy.generate(
                strength=BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_SIXTY
            )
        )
    )
    .from_derivation(  # Drive from Custom derivation
        derivation=CustomDerivation(path="m/0'/0/0")
    )
)

# Print all Bitcoin HDWallet information's
print(
    json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False)
)  # dump
# print(json.dumps(hdwallet.dumps(exclude={"indexes"}), indent=4, ensure_ascii=False))  # dumps
