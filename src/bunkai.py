
import os
import pandas as pd
import numpy as np
from typing import List
import prime_energy


def read_csv(filename : str):
    """入力ファイルの読み込む

    Args:
        filename (str): 入力ファイル名

    Returns:
        List: 解析用のデータ

    """
    csv_rows = pd.read_csv(filename)

    analysis_inputs = []
    for i, row in csv_rows.iterrows():
        analysis_input = {
            'general' : {
                'number_of_people': row[0],
                'region': 6,
                'main_habitable_room_floor_area': row[1],
                'other_habitable_room_floor_area': row[2],
                'total_floor_area': row[3],
                'use_electric': bool(row[4]),
                'use_gas': bool(row['エネルギー源_都市ガス']),
                'use_kerosene': bool(row['エネルギー源_灯油'])
            },
            'ventilation' : {
                'use' : bool(row['電気を換気設備に使用しているかの有無']),
                'coeff' :row['調整係数_換気']
            },
            'hot_water_supply' : {
                'use' : bool(row['電気を給湯設備に使用しているかの有無']),
                'coeff' :row['調整係数_給湯']
            },
            'lighting' : {
                'use' : bool(row['電気を照明設備に使用しているかの有無']),
                'coeff' :row['調整係数_照明']
            },
            'electric_appliance' : {
                'use' : bool(row['電気を家電に使用しているかの有無']),
                'coeff' :row['調整係数_家電']
            },
            'cooking' : {
                'use' : bool(row['電気を調理に使用しているかの有無']),
                'coeff' :row['調整係数_調理']
            }
        }

        # 電気の使用が有りの場合
        if analysis_input['general']['use_electric']:
            analysis_input['electric'] = {
                'calorific_value' : 9.76,
                'consumption' : np.array(row[5:17]),
                'heating' : np.array(row[17:29]).astype(dtype=bool),
                'cooling' : np.array(row[29:41]).astype(dtype=bool),
            }

        # ガスの使用が有りの場合
        if analysis_input['general']['use_gas']:
            analysis_input['gas'] = {
                'calorific_value' : 45.0 if row['ガスの種類'] == '都市ガス' else 100,
                'consumption' : np.array(row[42:54]),
                'heating' : np.array(row[54:66]).astype(dtype=bool),
                'cooling' : np.zeros(12, dtype=bool),
            }

        # 灯油の使用が有りの場合
        if analysis_input['general']['use_kerosene']:
            analysis_input['kerosene'] = {
                'calorific_value' : 37.0,
                'consumption' : np.array(row[67:79]),
                'heating' : np.array(row[79:91]).astype(dtype=bool),
                'cooling' : np.zeros(12, dtype=bool),
            }

        analysis_inputs.append(analysis_input)

    return analysis_inputs


def analysis(analysis_inputs: List):
    """解析処理

    Args:
        analysis_inputs (List): 解析用のデータ

    Returns:
        dataframe: 解析の結果

    """
    analysis_results = []

    for d in analysis_inputs:
        # 電気の使用が有りの場合
        if d['general']['use_electric'] is True:
            # 月別の電気の一次エネルギー消費量
            E_p_E_H, E_p_E_C, E_p_E_V, E_p_E_L, E_p_E_HW, E_p_E_AP, E_p_E_CC = prime_energy.get_E_p_E(
                p = d['general']['number_of_people'],
                region = d['general']['region'],
                A_MR = d['general']['main_habitable_room_floor_area'],
                A_OR = d['general']['other_habitable_room_floor_area'],
                A_A = d['general']['total_floor_area'],
                ele_cos = d['electric']['consumption'],
                ele_htg_use = d['electric']['heating'],
                ele_clg_use = d['electric']['cooling'],
                vnt_use = d['ventilation']['use'],
                vnt_coeff = d['ventilation']['coeff'],
                hws_use = d['hot_water_supply']['use'],
                hws_coeff = d['hot_water_supply']['coeff'],
                ltg_use = d['lighting']['use'],
                ltg_coeff = d['lighting']['coeff'],
                eap_use = d['electric_appliance']['use'],
                eap_coeff = d['electric_appliance']['coeff'],
                ckg_use = d['cooking']['use'],
                ckg_coeff = d['cooking']['coeff'],
                f_PE_E = d['electric']['calorific_value']
            )
        else:
            E_p_E_H = E_p_E_C = E_p_E_V = E_p_E_L = E_p_E_HW = E_p_E_AP = E_p_E_CC = np.zeros(12)

        # ガスの使用が有りの場合
        if d['general']['use_gas'] is True:
            E_p_G_H, E_p_G_C, E_p_G_V, E_p_G_L, E_p_G_HW, E_p_G_AP, E_p_G_CC = prime_energy.get_E_p_G(
                p = d['general']['number_of_people'],
                region = d['general']['region'],
                A_MR = d['general']['main_habitable_room_floor_area'],
                A_OR = d['general']['other_habitable_room_floor_area'],
                A_A = d['general']['total_floor_area'],
                gas_cos = d['gas']['consumption'],
                gas_htg_use = d['gas']['heating'],
                gas_clg_use = d['gas']['cooling'],
                hws_use = d['hot_water_supply']['use'],
                hws_coeff = d['hot_water_supply']['coeff'],
                ckg_use = d['cooking']['use'],
                ckg_coeff = d['cooking']['coeff'],
                f_PE_G = d['gas']['calorific_value']
            )
        else:
            E_p_G_H = E_p_G_C = E_p_G_V = E_p_G_L = E_p_G_HW = E_p_G_AP = E_p_G_CC = np.zeros(12)

        # 灯油の使用が有りの場合
        if d['general']['use_kerosene'] is True:
            E_p_K_H, E_p_K_C, E_p_K_V, E_p_K_L, E_p_K_HW, E_p_K_AP, E_p_K_CC = prime_energy.get_E_p_K(
                p = d['general']['number_of_people'],
                region = d['general']['region'],
                A_MR = d['general']['main_habitable_room_floor_area'],
                A_OR = d['general']['other_habitable_room_floor_area'],
                A_A = d['general']['total_floor_area'],
                k_cos = d['kerosene']['consumption'],
                k_htg_use = d['kerosene']['heating'],
                k_clg_use = d['kerosene']['cooling'],
                hws_use = d['hot_water_supply']['use'],
                hws_coeff = d['hot_water_supply']['coeff'],
                f_PE_K = d['kerosene']['calorific_value']
            )
        else:
            E_p_K_H = E_p_K_C = E_p_K_V = E_p_K_L = E_p_K_HW = E_p_K_AP = E_p_K_CC = np.zeros(12)

        # 一次エネルギー消費量
        E_p_H = prime_energy.get_E_p_H_m(E_p_E_H, E_p_G_H, E_p_K_H)         # (5)
        E_p_C = prime_energy.get_E_p_C_m(E_p_E_C, E_p_G_C, E_p_K_C)         # (6)
        E_p_V = prime_energy.get_E_p_V_m(E_p_E_V, E_p_G_V, E_p_K_V)         # (7)
        E_p_L = prime_energy.get_E_p_L_m(E_p_E_L, E_p_G_L, E_p_K_L)         # (8)
        E_p_HW = prime_energy.get_E_p_HW_m(E_p_E_HW, E_p_G_HW, E_p_K_HW)     # (9)
        E_p_AP = prime_energy.get_E_p_AP_m(E_p_E_AP, E_p_G_AP, E_p_K_AP)     # (10)
        E_p_CC = prime_energy.get_E_p_CC_m(E_p_E_CC, E_p_G_CC, E_p_K_CC)     # (11)

        analysis_result = np.concatenate((
                        E_p_E_H, E_p_E_C, E_p_E_V, E_p_E_L, E_p_E_HW, E_p_E_AP, E_p_E_CC, \
                        E_p_G_H, E_p_G_C, E_p_G_V, E_p_G_L, E_p_G_HW, E_p_G_AP, E_p_G_CC, \
                        E_p_K_H, E_p_K_C, E_p_K_V, E_p_K_L, E_p_K_HW, E_p_K_AP, E_p_K_CC, \
                        E_p_H, E_p_C, E_p_V, E_p_L, E_p_HW, E_p_AP, E_p_CC
                    ))

        analysis_results.append(analysis_result)

    return analysis_results


def generate_analysis_results(output_filename, analysis_results):
    """解析の結果を出力する

    Args:
        output_filename (str): 出力ファイル名
        analysis_results (dataframe): 解析の結果

    Returns:

    """
    # 出力CSVファイルのコラム名作成
    months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    equipments = ['暖房', '冷房', '換気', '照明', '給湯', '家電', '調理']

    electric_cols = np.array([np.char.add('電気_' + eq + '_', months) for eq in equipments]).flatten()
    gas_cols = np.array([np.char.add('ガス_' + eq + '_', months) for eq in equipments]).flatten()
    kerosene_cols = np.array([np.char.add('灯油_' + eq + '_', months) for eq in equipments]).flatten()
    energy_cols = np.array([np.char.add('一次エネルギー' + eq + '_', months) for eq in equipments]).flatten()

    df = pd.DataFrame(analysis_results, columns = np.concatenate((electric_cols, gas_cols, kerosene_cols, energy_cols)))

    df.to_csv(output_filename, index=False)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Input File Path')
    parser.add_argument('-o', '--output', type=str, help='Output File Path')

    # 入力ファイルの読み込む
    args = parser.parse_args()
    input = args.input
    analysis_data = read_csv(input)

    # 解析する
    analysis_results = analysis(analysis_data)

    # 解析の結果を出力する
    generate_analysis_results(args.output, analysis_results)
