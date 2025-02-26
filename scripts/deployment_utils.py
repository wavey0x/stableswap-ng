from dataclasses import dataclass

from eth_typing import Address

# ------ IMMUTABLES ------


GAUGE_CONTROLLER = "0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB"
ADDRESS_PROVIDER = "0x0000000022d53366457f9d5e68ec105046fc4383"
FIDDYRESEARCH = "0xE6DA683076b7eD6ce7eC972f21Eb8F91e9137a17"
FIDDYDEPLOYER = "0x2d12D0907A388811e3AA855A550F959501d303EE"
BABE = "0xbabe61887f1de2713c6f97e567623453d3C79f67"


# -------------- CURVE DATA --------------


@dataclass
class CurveNetworkSettings:
    dao_ownership_contract: Address
    fee_receiver_address: Address
    metaregistry_address: Address = ""
    base_pool_registry_address: Address = ""
    address_provider: Address = "0x0000000022d53366457f9d5e68ec105046fc4383"


curve_dao_network_settings = {
    # Ethereum
    "ethereum:sepolia": CurveNetworkSettings(
        dao_ownership_contract="0xE6DA683076b7eD6ce7eC972f21Eb8F91e9137a17",
        fee_receiver_address="0xE6DA683076b7eD6ce7eC972f21Eb8F91e9137a17",
    ),
    "ethereum:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0x40907540d8a6C65c637785e8f8B742ae6b0b9968",
        fee_receiver_address="0xeCb456EA5365865EbAb8a2661B0c503410e9B347",
        metaregistry_address="0xF98B45FA17DE75FB1aD0e7aFD971b0ca00e379fC",
        base_pool_registry_address="0xDE3eAD9B2145bBA2EB74007e58ED07308716B725",
    ),
    # Layer 2
    "arbitrum:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xb055ebbacc8eefc166c169e9ce2886d0406ab49b",  # proxy
        fee_receiver_address="0xd4f94d0aaa640bbb72b5eec2d85f6d114d81a88e",
    ),
    "optimism:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",  # proxy
        fee_receiver_address="0xbF7E49483881C76487b0989CD7d9A8239B20CA41",
    ),
    "base:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xe8269B33E47761f552E1a3070119560d5fa8bBD6",  # proxy
        fee_receiver_address="0xe8269B33E47761f552E1a3070119560d5fa8bBD6",  # proxy
    ),
    "linea:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        fee_receiver_address="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
    ),
    "scroll:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xf3A431008396df8A8b2DF492C913706BDB0874ef",  # proxy
        fee_receiver_address="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
    ),
    "zksync:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xCb8799BFF48bb549F7B69Bb9BE60DbA7cd4F1BB7",
        fee_receiver_address="0xCb8799BFF48bb549F7B69Bb9BE60DbA7cd4F1BB7",
    ),
    "pzkevm:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0x8b3EFBEfa6eD222077455d6f0DCdA3bF4f3F57A6",
        fee_receiver_address="0x8b3EFBEfa6eD222077455d6f0DCdA3bF4f3F57A6",
    ),
    # Layer 1
    "polygon:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",  # proxy
        fee_receiver_address="0x774D1Dba98cfBD1F2Bc3A1F59c494125e07C48F9",
    ),
    "gnosis:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",  # proxy
        fee_receiver_address="0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",  # proxy
    ),
    "avax:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",  # proxy
        fee_receiver_address="0x06534b0BF7Ff378F162d4F348390BDA53b15fA35",
    ),
    "ftm:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xB055EbbAcc8Eefc166c169e9Ce2886D0406aB49b",  # proxy
        fee_receiver_address="0x2B039565B2b7a1A9192D4847fbd33B25b836B950",
    ),
    "kava:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0x1f0e8445Ebe0D0F60A96A7cd5BB095533cb15B58",
        fee_receiver_address="0x1f0e8445Ebe0D0F60A96A7cd5BB095533cb15B58",
    ),
    "celo:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0x56bc95Ded2BEF162131905dfd600F2b9F1B380a4",
        fee_receiver_address="0x56bc95Ded2BEF162131905dfd600F2b9F1B380a4",
    ),
    "aurora:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        fee_receiver_address="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
    ),
    "bsc:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0x98B4029CaBEf7Fd525A36B0BF8555EC1d42ec0B6",
        fee_receiver_address="0x98B4029CaBEf7Fd525A36B0BF8555EC1d42ec0B6",
    ),
    "fraxtal:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0x8b3EFBEfa6eD222077455d6f0DCdA3bF4f3F57A6",  # proxy
        fee_receiver_address="0x8b3EFBEfa6eD222077455d6f0DCdA3bF4f3F57A6",
    ),
    "tron:mainnet": CurveNetworkSettings(dao_ownership_contract="", fee_receiver_address=""),
    "mantle:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        fee_receiver_address="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
    ),
    "xlayer:mainnet": CurveNetworkSettings(
        dao_ownership_contract="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
        fee_receiver_address="0xf3A431008396df8A8b2DF492C913706BDB0874ef",
    ),
}


CURVE_DAO_OWNERSHIP = {
    "agent": "0x40907540d8a6c65c637785e8f8b742ae6b0b9968",
    "voting": "0xe478de485ad2fe566d49342cbd03e49ed7db3356",
    "token": "0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2",
    "quorum": 30,
}
