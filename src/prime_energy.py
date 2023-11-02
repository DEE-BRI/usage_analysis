import numpy as np
from typing import List
import energy
import electricity as ele
import gas as gas
import kerosene as k

"""4.月別の一次エネルギー消費量"""

def get_E_p_total_m(
    E_p_H_m: float,
    E_p_C_m: float,
    E_p_V_m: float,
    E_p_L_m: float,
    E_p_HW_m: float,
    E_p_AP_m: float,
    E_p_CC_m: float
) -> float:
    """月mにおける一次エネルギー消費量(合計) 式(1)

    Args:
        E_p_H_m (float): 月mにおける暖房設備の一次エネルギー消費量, MJ
        E_p_C_m (float): 月mにおける冷房設備の一次エネルギー消費量, MJ
        E_p_V_m (float): 月mにおける換気設備の一次エネルギー消費量, MJ
        E_p_L_m (float): 月mにおける照明設備の一次エネルギー消費量, MJ
        E_p_HW_m (float): 月mにおける給湯設備の一次エネルギー消費量, MJ
        E_p_AP_m (float): 月mにおける家電の一次エネルギー消費量, MJ
        E_p_CC_m (float): 月mにおける調理の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける一次エネルギー消費量(合計), MJ
    """
    E_p_total_m = E_p_H_m + E_p_C_m + E_p_V_m + \
        E_p_L_m + E_p_HW_m + E_p_AP_m + E_p_CC_m
    return E_p_total_m


def get_E_p_E_total_m(
    E_p_E_H_m: float,
    E_p_E_C_m: float,
    E_p_E_V_m: float,
    E_p_E_L_m: float,
    E_p_E_HW_m: float,
    E_p_E_AP_m: float,
    E_p_E_CC_m: float
) -> float:
    """月mにおける電気の一次エネルギー消費量(合計) 式(2)

    Args:
        E_p_E_H_m (float): 月mにおける電気の暖房設備の一次エネルギー消費量, MJ
        E_p_E_C_m (float): 月mにおける電気の冷房設備の一次エネルギー消費量, MJ
        E_p_E_V_m (float): 月mにおける電気の換気設備の一次エネルギー消費量, MJ
        E_p_E_L_m (float): 月mにおける電気の照明設備の一次エネルギー消費量, MJ
        E_p_E_HW_m (float): 月mにおける電気の給湯設備の一次エネルギー消費量, MJ
        E_p_E_AP_m (float): 月mにおける電気の家電の一次エネルギー消費量, MJ
        E_p_E_CC_m (float): 月mにおける電気の調理の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける電気の一次エネルギー消費量(合計), MJ
    """
    E_p_E_total_m = E_p_E_H_m + E_p_E_C_m + E_p_E_V_m + \
        E_p_E_L_m + E_p_E_HW_m + E_p_E_AP_m + E_p_E_CC_m
    return E_p_E_total_m


def get_E_p_G_total_m(
    E_p_G_H_m: float,
    E_p_G_C_m: float,
    E_p_G_V_m: float,
    E_p_G_L_m: float,
    E_p_G_HW_m: float,
    E_p_G_AP_m: float,
    E_p_G_CC_m: float
) -> float:
    """月mにおけるガスの一次エネルギー消費量(合計) 式(3)

    Args:
        E_p_G_H_m (float): 月mにおけるガスの暖房設備の一次エネルギー消費量, MJ
        E_p_G_C_m (float): 月mにおけるガスの冷房設備の一次エネルギー消費量, MJ
        E_p_G_V_m (float): 月mにおけるガスの換気設備の一次エネルギー消費量, MJ
        E_p_G_L_m (float): 月mにおけるガスの照明設備の一次エネルギー消費量, MJ
        E_p_G_HW_m (float): 月mにおけるガスの給湯設備の一次エネルギー消費量, MJ
        E_p_G_AP_m (float): 月mにおけるガスの家電の一次エネルギー消費量, MJ
        E_p_G_CC_m (float): 月mにおけるガスの調理の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおけるガスの一次エネルギー消費量(合計), MJ
    """
    E_p_G_total_m = E_p_G_H_m + E_p_G_C_m + E_p_G_V_m + \
        E_p_G_L_m + E_p_G_HW_m + E_p_G_AP_m + E_p_G_CC_m
    return E_p_G_total_m


def get_E_p_K_total_m(
    E_p_K_H_m: float,
    E_p_K_C_m: float,
    E_p_K_V_m: float,
    E_p_K_L_m: float,
    E_p_K_HW_m: float,
    E_p_K_AP_m: float,
    E_p_K_CC_m: float
) -> float:
    """月mにおける灯油の一次エネルギー消費量(合計) 式(4)

    Args:
        E_p_K_H_m (float): 月mにおける灯油の暖房設備の一次エネルギー消費量, MJ
        E_p_K_C_m (float): 月mにおける灯油の冷房設備の一次エネルギー消費量, MJ
        E_p_K_V_m (float): 月mにおける灯油の換気設備の一次エネルギー消費量, MJ
        E_p_K_L_m (float): 月mにおける灯油の照明設備の一次エネルギー消費量, MJ
        E_p_K_HW_m (float): 月mにおける灯油の給湯設備の一次エネルギー消費量, MJ
        E_p_K_AP_m (float): 月mにおける灯油の家電の一次エネルギー消費量, MJ
        E_p_K_CC_m (float): 月mにおける灯油の調理の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける灯油の一次エネルギー消費量(合計), MJ
    """
    E_p_K_total_m = E_p_K_H_m + E_p_K_C_m + E_p_K_V_m + \
        E_p_K_L_m + E_p_K_HW_m + E_p_K_AP_m + E_p_K_CC_m
    return E_p_K_total_m


def get_E_p_H_m(
    E_p_E_H_m: float,
    E_p_G_H_m: float,
    E_p_K_H_m: float
) -> float:
    """月mにおける暖房設備の一次エネルギー消費量 式(5)

    Args:
        E_p_E_H_m (float): 月mにおける電気の暖房設備の一次エネルギー消費量, MJ
        E_p_G_H_m (float): 月mにおけるガスの冷房設備の一次エネルギー消費量, MJ
        E_p_K_H_m (float): 月mにおける灯油の換気設備の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける暖房設備の一次エネルギー消費量, MJ
    """
    E_p_H_m = E_p_E_H_m + E_p_G_H_m + E_p_K_H_m
    return E_p_H_m


def get_E_p_C_m(
    E_p_E_C_m: float,
    E_p_G_C_m: float,
    E_p_K_C_m: float
) -> float:
    """月mにおける冷房設備の一次エネルギー消費量 式(6)

    Args:
        E_p_E_C_m (float): 月mにおける電気の冷房設備の一次エネルギー消費量, MJ
        E_p_G_C_m (float): 月mにおけるガスの冷房設備の一次エネルギー消費量, MJ
        E_p_K_C_m (float): 月mにおける灯油の冷房設備の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける冷房設備の一次エネルギー消費量, MJ
    """
    E_p_C_m = E_p_E_C_m + E_p_G_C_m + E_p_K_C_m
    return E_p_C_m


def get_E_p_V_m(
    E_p_E_V_m: float,
    E_p_G_V_m: float,
    E_p_K_V_m: float
) -> float:
    """月mにおける換気設備の一次エネルギー消費量 式(7)

    Args:
        E_p_E_V_m (float): 月mにおける電気の換気設備の一次エネルギー消費量, MJ
        E_p_G_V_m (float): 月mにおけるガスの換気設備の一次エネルギー消費量, MJ
        E_p_K_V_m (float): 月mにおける灯油の換気設備の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける換気設備の一次エネルギー消費量, MJ
    """
    E_p_V_m = E_p_E_V_m + E_p_G_V_m + E_p_K_V_m
    return E_p_V_m


def get_E_p_L_m(
    E_p_E_L_m: float,
    E_p_G_L_m: float,
    E_p_K_L_m: float
) -> float:
    """月mにおける照明設備の一次エネルギー消費量 式(8)

    Args:
        E_p_E_L_m (float): 月mにおける電気の照明設備の一次エネルギー消費量, MJ
        E_p_G_L_m (float): 月mにおけるガスの照明設備の一次エネルギー消費量, MJ
        E_p_K_L_m (float): 月mにおける灯油の照明設備の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける照明設備の一次エネルギー消費量, MJ
    """
    E_p_L_m = E_p_E_L_m + E_p_G_L_m + E_p_K_L_m
    return E_p_L_m


def get_E_p_HW_m(
    E_p_E_HW_m: float,
    E_p_G_HW_m: float,
    E_p_K_HW_m: float
) -> float:
    """月mにおける給湯設備の一次エネルギー消費量 式(9)

    Args:
        E_p_E_HW_m (float): 月mにおける電気の給湯設備の一次エネルギー消費量, MJ
        E_p_G_HW_m (float): 月mにおけるガスの給湯設備の一次エネルギー消費量, MJ
        E_p_K_HW_m (float): 月mにおける灯油の給湯設備の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける給湯設備の一次エネルギー消費量, MJ
    """
    E_p_HW_m = E_p_E_HW_m + E_p_G_HW_m + E_p_K_HW_m
    return E_p_HW_m


def get_E_p_AP_m(
    E_p_E_AP_m: float,
    E_p_G_AP_m: float,
    E_p_K_AP_m: float
) -> float:
    """月mにおける家電の一次エネルギー消費量 式(10)

    Args:
        E_p_E_AP_m (float): 月mにおける電気の家電の一次エネルギー消費量, MJ
        E_p_G_AP_m (float): 月mにおけるガスの家電の一次エネルギー消費量, MJ
        E_p_K_AP_m (float): 月mにおける灯油の家電の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける家電の一次エネルギー消費量, MJ
    """
    E_p_AP_m = E_p_E_AP_m + E_p_G_AP_m + E_p_K_AP_m
    return E_p_AP_m


def get_E_p_CC_m(
    E_p_E_CC_m: float,
    E_p_G_CC_m: float,
    E_p_K_CC_m: float
) -> float:
    """月mにおける調理の一次エネルギー消費量 式(11)

    Args:
        E_p_E_CC_m (float): 月mにおける電気の調理の一次エネルギー消費量, MJ
        E_p_G_CC_m (float): 月mにおけるガスの調理の一次エネルギー消費量, MJ
        E_p_K_CC_m (float): 月mにおける灯油の調理の一次エネルギー消費量, MJ

    Returns:
        float: 月mにおける調理の一次エネルギー消費量, MJ
    """
    E_p_CC_m = E_p_E_CC_m + E_p_G_CC_m + E_p_K_CC_m
    return E_p_CC_m




def get_E_p_E(p, region, A_MR, A_OR, A_A, ele_cos,
              ele_htg_use, ele_clg_use, vnt_use, vnt_coeff, hws_use, hws_coeff,
              ltg_use, ltg_coeff, eap_use, eap_coeff, ckg_use, ckg_coeff, f_PE_E):
    """月別の電気の一次エネルギー消費量

    Args:
        p (int): 世帯の人数
        region (int): 地域の区分
        A_MR (float): 主たる居室の床面積
        A_OR (float): その他の居室の床面積
        A_A (float): 床面積の合計
        ele_cos (np.array): 電気の月別消費量
        ele_htg_use (np.array): 暖房を使用しているかの有無
        ele_clg_use (np.array): 冷房を使用しているかの有無
        vnt_use (bool): 電気を換気設備に使用しているかの有無
        vnt_coeff (float): 電気を換気設備に使用している場合の調整係数
        hws_use (bool): 電気を給湯設備に使用しているかの有無
        hws_coeff (float): 電気を給湯設備に使用している場合の調整係数
        ltg_use (bool): 電気を照明設備に使用しているかの有無
        ltg_coeff (float): 電気を照明設備に使用している場合の調整係数
        eap_use (bool): 電気を家電設備に使用しているかの有無
        eap_coeff (float): 電気を家電設備に使用している場合の調整係数
        ckg_use (bool): 電気を調理に使用しているかの有無
        ckg_coeff (float): 電気を調理に使用している場合の調整係数
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/m³

    Returns:
        tuple: 月別の電気の一次エネルギー消費量

    """
    # 各月が中間月か否かの値
    IM = get_IM(ele_htg_use, ele_clg_use)

    # 各設備の調整係数
    C_V = ele.get_C_V(vnt_use, vnt_coeff)
    C_L = ele.get_C_L(ltg_use, ltg_coeff)
    C_HW = ele.get_C_HW(hws_use, hws_coeff)
    C_AP = ele.get_C_AP(eap_use, eap_coeff)
    C_CC = ele.get_C_CC(ckg_use, ckg_coeff)

    E_V_ref, E_L_ref, E_HW_ref, E_AP_ref, E_CC_ref, E_exHC_ref \
        = energy.get_E_ref(p, region, A_MR, A_OR, A_A,
                      C_V, C_L, C_HW, C_AP, C_CC)

    # 月別消費量
    S = np.array([ele.get_S_m(S_E_m) for (S_E_m) in ele_cos])

    # 暖冷房設備以外の用途の消費量
    S_exHC = energy.get_S_exHC(E_exHC_ref, IM, S)

    # 電気の暖房設備の一次エネルギー消費量
    E_p_E_H = np.array([ele.get_E_p_E_H_m(S_m, S_exHC_m, U_E_H_m, f_PE_E)
                       for (S_m, S_exHC_m, U_E_H_m) in zip(S, S_exHC, ele_htg_use)])

    # 電気の冷房設備の一次エネルギー消費量
    E_p_E_C = np.array([ele.get_E_p_E_C_m(S_m, S_exHC_m, U_E_C_m, f_PE_E)
                       for (S_m, S_exHC_m, U_E_C_m) in zip(S, S_exHC, ele_clg_use)])

    # 電気の換気設備の一次エネルギー消費量
    r_s_V = np.array([energy.get_r_S_V_m(E_V_ref_m, E_exHC_ref_m)
                     for (E_V_ref_m, E_exHC_ref_m) in zip(E_V_ref, E_exHC_ref)])
    E_p_E_V = np.array([ele.get_E_p_E_V_m(S_exHC_m, r_s_V_m, f_PE_E)
                       for (S_exHC_m, r_s_V_m) in zip(S_exHC, r_s_V)])

    # 電気の照明設備の一次エネルギー消費量
    r_s_L = np.array([energy.get_r_S_L_m(E_L_ref_m, E_exHC_ref_m)
                     for (E_L_ref_m, E_exHC_ref_m) in zip(E_L_ref, E_exHC_ref)])
    E_p_E_L = np.array([ele.get_E_p_E_L_m(S_exHC_m, r_s_L_m, f_PE_E)
                       for (S_exHC_m, r_s_L_m) in zip(S_exHC, r_s_L)])

    # 電気の給湯設備の一次エネルギー消費量
    r_s_HW = np.array([energy.get_r_S_HW_m(E_HW_ref_m, E_exHC_ref_m)
                      for (E_HW_ref_m, E_exHC_ref_m) in zip(E_HW_ref, E_exHC_ref)])
    E_p_E_HW = np.array([ele.get_E_p_E_HW_m(S_exHC_m, r_s_HW_m, f_PE_E)
                        for (S_exHC_m, r_s_HW_m) in zip(S_exHC, r_s_HW)])

    # 電気の家電設備の一次エネルギー消費量
    r_s_AP = np.array([energy.get_r_S_AP_m(E_AP_ref_m, E_exHC_ref_m)
                      for (E_AP_ref_m, E_exHC_ref_m) in zip(E_AP_ref, E_exHC_ref)])
    E_p_E_AP = np.array([ele.get_E_p_E_AP_m(S_exHC_m, r_s_AP_m, f_PE_E)
                        for (S_exHC_m, r_s_AP_m) in zip(S_exHC, r_s_AP)])

    # 電気の調理設備の一次エネルギー消費量
    r_s_CC = np.array([energy.get_r_S_CC_m(E_CC_ref_m, E_exHC_ref_m)
                      for (E_CC_ref_m, E_exHC_ref_m) in zip(E_CC_ref, E_exHC_ref)])
    E_p_E_CC = np.array([ele.get_E_p_E_CC_m(S_exHC_m, r_s_CC_m, f_PE_E)
                        for (S_exHC_m, r_s_CC_m) in zip(S_exHC, r_s_CC)])

    return E_p_E_H, E_p_E_C, E_p_E_V, E_p_E_L, E_p_E_HW, E_p_E_AP, E_p_E_CC


def get_E_p_G(p, region, A_MR, A_OR, A_A, gas_cos,
              gas_htg_use, gas_clg_use, hws_use, hws_coeff,
              ckg_use, ckg_coeff, f_PE_G):
    """月別のガスの一次エネルギー消費量

    Args:
        p (int): 世帯の人数
        region (int): 地域の区分
        A_MR (float): 主たる居室の床面積
        A_OR (float): その他の居室の床面積
        A_A (float): 床面積の合計
        gas_cos (np.array): ガスの月別消費量
        gas_htg_use (np.array): 暖房を使用しているかの有無
        gas_clg_use (np.array): 冷房を使用しているかの有無
        hws_use (bool): ガスを給湯設備に使用しているかの有無
        hws_coeff (float): ガスを給湯設備に使用している場合の調整係数
        ckg_use (bool): ガスを調理に使用しているかの有無
        ckg_coeff (float): ガスを調理に使用している場合の調整係数
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        tuple: 月別のガスの一次エネルギー消費量

    """
    # 各月が中間月か否かの値
    IM = get_IM(gas_htg_use, gas_clg_use)

    # 各設備の調整係数
    C_V = gas.get_C_V()
    C_L = gas.get_C_L()
    C_HW = gas.get_C_HW(hws_use, hws_coeff)
    C_AP = gas.get_C_AP()
    C_CC = gas.get_C_CC(ckg_use, ckg_coeff)

    E_V_ref, E_L_ref, E_HW_ref, E_AP_ref, E_CC_ref, E_exHC_ref \
        = energy.get_E_ref(p, region, A_MR, A_OR, A_A,
                      C_V, C_L, C_HW, C_AP, C_CC)

    # 月別消費量
    S = np.array([gas.get_S_m(S_E_m) for (S_E_m) in gas_cos])

    # 暖冷房設備以外の用途の消費量
    S_exHC = energy.get_S_exHC(E_exHC_ref, IM, S)

    # ガスの暖房設備の一次エネルギー消費量
    E_p_G_H = np.array([gas.get_E_p_G_H_m(S_m, S_exHC_m, U_G_H_m, f_PE_G)
                       for (S_m, S_exHC_m, U_G_H_m) in zip(S, S_exHC, gas_htg_use)])

    # ガスの冷房設備の一次エネルギー消費量
    E_p_G_C = np.array([gas.get_E_p_G_C_m(S_m, S_exHC_m, f_PE_G)
                       for (S_m, S_exHC_m) in zip(S, S_exHC)])

    # ガスの換気設備の一次エネルギー消費量
    r_s_V = np.array([energy.get_r_S_V_m(E_V_ref_m, E_exHC_ref_m)
                     for (E_V_ref_m, E_exHC_ref_m) in zip(E_V_ref, E_exHC_ref)])
    E_p_G_V = np.array([gas.get_E_p_G_V_m(S_exHC_m, r_s_V_m, f_PE_G)
                       for (S_exHC_m, r_s_V_m) in zip(S_exHC, r_s_V)])

    # ガスの照明設備の一次エネルギー消費量
    r_s_L = np.array([energy.get_r_S_L_m(E_L_ref_m, E_exHC_ref_m)
                     for (E_L_ref_m, E_exHC_ref_m) in zip(E_L_ref, E_exHC_ref)])
    E_p_G_L = np.array([gas.get_E_p_G_L_m(S_exHC_m, r_s_L_m, f_PE_G)
                       for (S_exHC_m, r_s_L_m) in zip(S_exHC, r_s_L)])

    # ガスの給湯設備の一次エネルギー消費量
    r_s_HW = np.array([energy.get_r_S_L_m(E_HW_ref_m, E_exHC_ref_m)
                      for (E_HW_ref_m, E_exHC_ref_m) in zip(E_HW_ref, E_exHC_ref)])
    E_p_G_HW = np.array([gas.get_E_p_G_HW_m(S_exHC_m, r_s_HW_m, f_PE_G)
                        for (S_exHC_m, r_s_HW_m) in zip(S_exHC, r_s_HW)])

    # ガスの家電設備の一次エネルギー消費量
    r_s_AP = np.array([energy.get_r_S_AP_m(E_AP_ref_m, E_exHC_ref_m)
                      for (E_AP_ref_m, E_exHC_ref_m) in zip(E_AP_ref, E_exHC_ref)])
    E_p_G_AP = np.array([gas.get_E_p_G_AP_m(S_exHC_m, r_s_AP_m, f_PE_G)
                        for (S_exHC_m, r_s_AP_m) in zip(S_exHC, r_s_AP)])

    # ガスの調理設備の一次エネルギー消費量
    r_s_CC = np.array([energy.get_r_S_CC_m(E_CC_ref_m, E_exHC_ref_m)
                      for (E_CC_ref_m, E_exHC_ref_m) in zip(E_CC_ref, E_exHC_ref)])
    E_p_G_CC = np.array([gas.get_E_p_G_CC_m(S_exHC_m, r_s_CC_m, f_PE_G)
                        for (S_exHC_m, r_s_CC_m) in zip(S_exHC, r_s_CC)])

    return E_p_G_H, E_p_G_C, E_p_G_V, E_p_G_L, E_p_G_HW, E_p_G_AP, E_p_G_CC


def get_E_p_K(p, region, A_MR, A_OR, A_A, k_cos,
              k_htg_use, k_clg_use, hws_use, hws_coeff, f_PE_K):
    """月別の灯油の一次エネルギー消費量

    Args:
        p (int): 世帯の人数
        region (int): 地域の区分
        A_MR (float): 主たる居室の床面積
        A_OR (float): その他の居室の床面積
        A_A (float): 床面積の合計
        k_cos (np.array): 灯油の月別消費量
        k_htg_use (np.array): 暖房を使用しているかの有無
        k_clg_use (np.array): 冷房を使用しているかの有無
        hws_use (bool): 灯油を給湯設備に使用しているかの有無
        hws_coeff (float): 灯油を給湯設備に使用している場合の調整係数
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/m³

    Returns:
        tuple: 月別の灯油の一次エネルギー消費量

    """
    # 各月が中間月か否かの値
    IM = get_IM(k_htg_use, k_clg_use)

    # 各設備の調整係数
    C_V = k.get_C_V()
    C_L = k.get_C_L()
    C_HW = k.get_C_HW(hws_use, hws_coeff)
    C_AP = k.get_C_AP()
    C_CC = k.get_C_CC()

    E_V_ref, E_L_ref, E_HW_ref, E_AP_ref, E_CC_ref, E_exHC_ref \
        = energy.get_E_ref(p, region, A_MR, A_OR, A_A,
                      C_V, C_L, C_HW, C_AP, C_CC)

    # 月別消費量
    S = np.array([k.get_S_m(S_K_m) for (S_K_m) in k_cos])

    # 暖冷房設備以外の用途の消費量
    S_exHC = energy.get_S_exHC(E_exHC_ref, IM, S)

    # 灯油の暖房設備の一次エネルギー消費量
    E_p_K_H = np.array([k.get_E_p_K_H_m(S_m, S_exHC_m, U_E_H_m, f_PE_K)
                       for (S_m, S_exHC_m, U_E_H_m) in zip(S, S_exHC, k_htg_use)])

    # 灯油の冷房設備の一次エネルギー消費量
    E_p_K_C = np.array([k.get_E_p_K_C_m(S_m, S_exHC_m, f_PE_K)
                       for (S_m, S_exHC_m) in zip(S, S_exHC)])

    # 灯油の換気設備の一次エネルギー消費量
    r_s_V = np.array([energy.get_r_S_V_m(E_V_ref_m, E_exHC_ref_m)
                     for (E_V_ref_m, E_exHC_ref_m) in zip(E_V_ref, E_exHC_ref)])
    E_p_K_V = np.array([k.get_E_p_K_V_m(S_exHC_m, r_s_V_m, f_PE_K)
                       for (S_exHC_m, r_s_V_m) in zip(S_exHC, r_s_V)])

    # 灯油の照明設備の一次エネルギー消費量
    r_s_L = np.array([energy.get_r_S_L_m(E_L_ref_m, E_exHC_ref_m)
                     for (E_L_ref_m, E_exHC_ref_m) in zip(E_L_ref, E_exHC_ref)])
    E_p_K_L = np.array([k.get_E_p_K_L_m(S_exHC_m, r_s_L_m, f_PE_K)
                       for (S_exHC_m, r_s_L_m) in zip(S_exHC, r_s_L)])

    # 灯油の給湯設備の一次エネルギー消費量
    r_s_HW = np.array([energy.get_r_S_HW_m(E_HW_ref_m, E_exHC_ref_m)
                      for (E_HW_ref_m, E_exHC_ref_m) in zip(E_HW_ref, E_exHC_ref)])
    E_p_K_HW = np.array([k.get_E_p_K_HW_m(S_exHC_m, r_s_HW_m, f_PE_K)
                        for (S_exHC_m, r_s_HW_m) in zip(S_exHC, r_s_HW)])

    # 灯油の家電設備の一次エネルギー消費量
    r_s_AP = np.array([energy.get_r_S_AP_m(E_AP_ref_m, E_exHC_ref_m)
                      for (E_AP_ref_m, E_exHC_ref_m) in zip(E_AP_ref, E_exHC_ref)])
    E_p_K_AP = np.array([k.get_E_p_K_AP_m(S_exHC_m, r_s_AP_m, f_PE_K)
                        for (S_exHC_m, r_s_AP_m) in zip(S_exHC, r_s_AP)])

    # 灯油の調理設備の一次エネルギー消費量
    r_s_CC = np.array([energy.get_r_S_CC_m(E_CC_ref_m, E_exHC_ref_m)
                      for (E_CC_ref_m, E_exHC_ref_m) in zip(E_CC_ref, E_exHC_ref)])
    E_p_K_CC = np.array([k.get_E_p_K_CC_m(S_exHC_m, r_s_CC_m, f_PE_K)
                        for (S_exHC_m, r_s_CC_m) in zip(S_exHC, r_s_CC)])

    return E_p_K_H, E_p_K_C, E_p_K_V, E_p_K_L, E_p_K_HW, E_p_K_AP, E_p_K_CC


def get_IM(
    htg_use: np.array,
    clg_use: np.array
):
    """各月が中間月か否かの値

    Args:
        U_H_m (bool): 暖房を使用しているかの有無
        U_C_m (bool): 冷房を使用しているかの有無

    Returns:
        List: 各月が中間月か否かの値
    """
    return [get_IM_m(U_H_m, U_C_m) for (U_H_m, U_C_m) in zip(htg_use, clg_use)]


def get_IM_m(
    U_H_m: bool,
    U_C_m: bool
) -> bool:
    """月mが中間月か否か, bool値

    Args:
        U_H_m (bool): 暖房を使用しているかの有無
        U_C_m (bool): 冷房を使用しているかの有無

    Returns:
        bool: 月mが中間月か否か

    """
    return U_H_m == False and U_C_m == False
