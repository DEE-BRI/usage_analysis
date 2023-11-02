"""5.月別の電気の一次エネルギー消費量"""

def get_E_p_E_H_m(
    S_m: float,
    S_exHC_m: float,
    U_E_H_m: bool,
    f_PE_E: float,
) -> float:
    """月mにおける電気の暖房設備の一次エネルギー消費量 式(12)

    Args:
        S_m (float): 月mにおける月別消費量, kWh
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        U_E_H_m (float): 月mにおける電気を暖房設備に使用しているかの有無
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける電気の暖房設備の一次エネルギー消費量, MJ
    """
    # 月mにおいて暖房設備を使用しているかの有無
    U_H_m = get_U_H_m(U_E_H_m)

    # 月mにおける暖房設備の用途の消費量
    S_H_m = get_S_H_m(S_exHC_m, S_m, U_H_m)

    return S_H_m * f_PE_E


def get_E_p_E_C_m(
    S_m: float,
    S_exHC_m: float,
    U_E_C_m: bool,
    f_PE_E: float,
) -> float:
    """月mにおける電気の冷房設備の一次エネルギー消費量 式(13)

    Args:
        S_m (float): 月mにおける月別消費量, kWh
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        U_E_C_m (float): 月mにおける電気を冷房設備に使用しているかの有無
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける電気の暖房設備の一次エネルギー消費量, MJ
    """
    # 冷房設備を使用しているかの有無
    U_C_m = get_U_C_m(U_E_C_m)

    # 冷房設備の用途の消費量
    S_C_m = get_S_C_m(S_exHC_m, S_m, U_C_m)

    return S_C_m * f_PE_E


def get_E_p_E_V_m(
    S_exHC_m: float,
    r_s_V_m: float,
    f_PE_E: float,
) -> float:
    """月mにおける電気の換気設備の一次エネルギー消費量 式(14)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_V_m (float): 月mにおける換気設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける電気の換気設備の一次エネルギー消費量, MJ
    """
    # 換気設備の用途の消費量
    S_V_m = get_S_V_m(S_exHC_m, r_s_V_m)
    return S_V_m * f_PE_E


def get_E_p_E_L_m(
    S_exHC_m: float,
    r_s_L_m: float,
    f_PE_E: float,
) -> float:
    """月mにおける電気の照明設備の一次エネルギー消費量 式(15)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_L_m (float): 月mにおける照明設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける電気の照明設備の一次エネルギー消費量, MJ
    """
    # 照明設備の用途の消費量
    S_L_m = get_S_L_m(S_exHC_m, r_s_L_m)
    return S_L_m * f_PE_E


def get_E_p_E_HW_m(
    S_exHC_m: float,
    r_s_HW_m: float,
    f_PE_E: float,
) -> float:
    """月mにおける電気の給湯設備の一次エネルギー消費量 式(16)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_HW_m (float): 月mにおける給湯設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける電気の給湯設備の一次エネルギー消費量, MJ
    """
    # 給湯設備の用途の消費量
    S_HW_m = get_S_HW_m(S_exHC_m, r_s_HW_m)
    return S_HW_m * f_PE_E


def get_E_p_E_AP_m(
    S_exHC_m: float,
    r_s_AP_m: float,
    f_PE_E: float,
) -> float:
    """月mにおける家電設備の一次エネルギー消費量 式(17)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_AP_m (float): 月mにおける家電設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける家電設備の一次エネルギー消費量, MJ
    """
    # 家電設備の用途の消費量
    S_AP_m = get_S_AP_m(S_exHC_m, r_s_AP_m)
    return S_AP_m * f_PE_E


def get_E_p_E_CC_m(
    S_exHC_m: float,
    r_s_CC_m: float,
    f_PE_E: float,
) -> float:
    """月mにおける電気の調理の一次エネルギー消費量 式(18)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_CC_m (float): 月mにおける調理設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_E (float): 電気の一次エネルギー換算係数, MJ/kWh

    Returns:
        float: 月mにおける電気の調理の一次エネルギー消費量, MJ
    """
    # 調理設備の用途の消費量
    S_CC_m = get_S_CC_m(S_exHC_m, r_s_CC_m)
    return S_CC_m * f_PE_E


def get_U_H_m(
    U_E_H_m
) -> bool:
    """月mにおいて暖房設備を使用しているかの有無 式(19)

    Args:
        U_E_H_m (bool): 月mにおける電気を暖房設備に使用しているかの有無

    Returns:
        bool: 月mにおいて暖房設備を使用しているかの有無
    """
    return U_E_H_m


def get_U_C_m(
    U_E_C_m: bool
) -> bool:
    """月mにおいて冷房設備を使用しているかの有無 式(20)

    Args:
        U_E_C_m (bool): 月mにおける電気を冷房設備に使用しているかの有無

    Returns:
        bool: 月mにおいて冷房設備を使用しているかの有無
    """
    return U_E_C_m


def get_C_V(
    U_E_V: bool,
    C_E_V: float,
) -> float:
    """換気設備の調整係数 式(21)

    Args:
        C_E_V (float): 電気を換気設備に使用している場合の調整係数
        U_E_V (bool): 電気を換気設備に使用しているかの有無

    Returns:
        float: 換気設備の調整係数
    """
    if U_E_V:
        return C_E_V
    else:
        return 0.0


def get_C_L(
    U_E_L: bool,
    C_E_L: float,
) -> float:
    """照明設備の調整係数 式(22)

    Args:
        C_E_L (float): 電気を照明設備に使用している場合の調整係数
        U_E_L (bool): 電気を照明設備に使用しているかの有無

    Returns:
        float: 照明設備の調整係数
    """
    if U_E_L:
        return C_E_L
    else:
        return 0.0


def get_C_HW(
    U_E_HW: bool,
    C_E_HW: float,
) -> float:
    """給湯設備の調整係数 式(23)

    Args:
        C_E_HW (float): 電気を給湯設備に使用している場合の調整係数
        C_E_HW (bool): 電気を給湯設備に使用しているかの有無

    Returns:
        float: 給湯設備の調整係数
    """
    if U_E_HW:
        return C_E_HW
    else:
        return 0.0


def get_C_AP(
    U_E_AP: bool,
    C_E_AP: float,
) -> float:
    """家電の調整係数 式(24)

    Args:
        C_E_HW (float): 電気を給湯設備に使用している場合の調整係数
        C_E_HW (bool): 電気を給湯設備に使用しているかの有無

    Returns:
        float: 家電の調整係数
    """
    if U_E_AP:
        return C_E_AP
    else:
        return 0.0


def get_C_CC(
    U_E_CC: bool,
    C_E_CC: float,
) -> float:
    """調理の調整係数 式(25)

    Args:
        U_E_CC (float): 電気を調理に使用している場合の調整係数
        C_E_CC (bool): 電気を調理に使用しているかの有無

    Returns:
        float: 調理の調整係数
    """
    if U_E_CC:
        return C_E_CC
    else:
        return 0.0


def get_S_m(
    S_E_m: float
) -> float:
    """月における月別消費量 (kWh) 式(26)

    Args:
        S_E_m (float): 月における電気の月別消費量 (kWh)

    Returns:
        float: 月における月別消費量 (kWh)
    """
    return S_E_m


def get_S_H_m(
    S_exHC_m: float,
    S_m: float,
    U_H_m: bool,

) -> float:
    """月mにおける暖房設備の用途の消費量 (kWh) 式(57)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        U_H_m (bool): 月mにおいて暖房設備を使用しているかの有無

    Returns:
        float: 月mにおける暖房設備の用途の消費量 (kWh)
    """
    if U_H_m:
        return S_m - S_exHC_m
    else:
        return 0.0


def get_S_C_m(
    S_exHC_m: float,
    S_m: float,
    U_C_m: bool,

) -> float:
    """月mにおける冷房設備の用途の消費量 (kWh) 式(58)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        S_m (float): 月mににおける月別消費量
        U_C_m (bool): 月mにおいて冷房設備を使用しているかの有無

    Returns:
        float: 月mにおける冷房設備の用途の消費量 (kWh)
    """
    if U_C_m:
        return S_m - S_exHC_m
    else:
        return 0.0


def get_S_V_m(
    S_exHC_m: float,
    r_s_V_m: float,

) -> float:
    """月mにおける換気設備の用途の消費量 (kWh) 式(59)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_V_m (float): 月mにおける換気設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける換気設備の用途の消費量 (kWh)
    """
    return r_s_V_m * S_exHC_m


def get_S_L_m(
    S_exHC_m: float,
    r_s_L_m: float,

) -> float:
    """月mにおける照明設備の用途の消費量 (kWh) 式(60)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        r_s_L_m (float): 月mにおける照明設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける照明設備の用途の消費量 (kWh)
    """
    return r_s_L_m * S_exHC_m


def get_S_HW_m(
    S_exHC_m: float,
    r_s_HW_m: float,

) -> float:
    """月mにおける給湯設備の用途の消費量 (kWh) 式(61)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_HW_m (float): 月mにおける給湯設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける給湯設備の用途の消費量 (kWh)
    """
    return r_s_HW_m * S_exHC_m


def get_S_AP_m(
    S_exHC_m: float,
    r_s_AP_m: float,

) -> float:
    """月mにおける家電設備の用途の消費量 (kWh) 式(62)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_AP_m (float): 月mにおける家電設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける家電設備の用途の消費量 (kWh)
    """
    return r_s_AP_m * S_exHC_m


def get_S_CC_m(
    S_exHC_m: float,
    r_s_CC_m: float,
) -> float:
    """月mにおける調理設備の用途の消費量 (kWh) 式(63)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, kWh
        r_s_CC_m (float): 月mにおける調理設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける調理設備の用途の消費量 (kWh)
    """
    return r_s_CC_m * S_exHC_m
