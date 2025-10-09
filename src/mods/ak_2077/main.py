from openbachelorm.resource import Resource
from openbachelorm.helper import (
    get_known_table_decorator_lst,
    get_mod_level_decorator_lst,
    get_known_table_asset_name_prefix,
)
from openbachelorm.const import KnownTable

IMMUNE_FLAG = True

IMMUNE_LST = [
    "stunImmune",
    "silenceImmune",
    "sleepImmune",
    "frozenImmune",
    "levitateImmune",
    "disarmedCombatImmune",
    "fearedImmune",
    "palsyImmune",
    "attractImmune",
]


def do_mod_enemy_database(enemy_database):
    for enemy_obj in enemy_database["enemies"]:
        for enemy_value in enemy_obj["Value"]:
            enemy_data = enemy_value["enemyData"]

            enemy_data["lifePointReduce"] = {"m_defined": True, "m_value": 0}

            enemy_attr = enemy_data["attributes"]

            if IMMUNE_FLAG:
                for k in IMMUNE_LST:
                    enemy_attr[k] = {"m_defined": True, "m_value": True}

                enemy_attr["massLevel"] = {"m_defined": True, "m_value": 100}

    return enemy_database


def build_sample_mod(client_version: str, res_version: str):
    res = Resource(client_version, res_version)

    res.mod_table(
        KnownTable.ENEMY_DATABASE.value,
        do_mod_enemy_database,
        get_known_table_decorator_lst(
            KnownTable.ENEMY_DATABASE, client_version, res_version
        ),
        table_asset_name_prefix=get_known_table_asset_name_prefix(
            KnownTable.ENEMY_DATABASE
        ),
    )

    res.build_mod("ak_2077")


def main():
    build_sample_mod("2.6.61", "25-09-29-16-32-32_00dc6f")


if __name__ == "__main__":
    main()
