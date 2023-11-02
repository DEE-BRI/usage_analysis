"""5.月別の灯油の一次エネルギー消費量"""

def get_E_p_K_H_m(
    S_m: float,
    S_exHC_m: float,
    U_K_H_m: bool,
    f_PE_K: float,
) -> float:
    """月mにおける灯油の暖房設備の一次エネルギー消費量 式(42)

    Args:
        S_H_m (float): 月mにおける暖房設備の用途の消費量, L
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月mにおける灯油の暖房設備の一次エネルギー消費量, MJ
    """
    U_H_m = get_U_H_m(U_K_H_m)

    S_H_m = get_S_H_m(S_exHC_m, S_m, U_H_m)

    return S_H_m * f_PE_K


def get_E_p_K_C_m(
    S_m: float,
    S_exHC_m: float,
    f_PE_K: float,
) -> float:
    """月mにおける灯油の冷房設備の一次エネルギー消費量 式(43)

    Args:
        S_m (float): 月mにおける月別消費量, L
        S_exHC_m (float): 月mにおける月別消費量
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月mにおける灯油の冷房設備の一次エネルギー消費量, MJ
    """
    # 冷房設備を使用しているかの有無
    U_C_m = get_U_C_m()

    # 冷房設備の用途の消費量
    S_C_m = get_S_C_m(S_exHC_m, S_m, U_C_m)

    return S_C_m * f_PE_K


def get_E_p_K_V_m(
    S_exHC_m: float,
    r_s_V_m: float,
    f_PE_K: float,
) -> float:
    """月mにおける灯油の換気設備の一次エネルギー消費量 式(44)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, L
        r_s_V_m (float): 月mにおける換気設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月mにおける灯油の換気設備の一次エネルギー消費量, MJ
    """
    # 換気設備の用途の消費量
    S_V_m = get_S_V_m(S_exHC_m, r_s_V_m)
    return S_V_m * f_PE_K


def get_E_p_K_L_m(
    S_exHC_m: float,
    r_s_L_m: float,
    f_PE_K: float,
) -> float:
    """月mにおける灯油の照明設備の一次エネルギー消費量 式(45)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, L
        r_s_L_m (float): 月mにおける照明設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月mにおける灯油の照明設備の一次エネルギー消費量, MJ
    """
    # 照明設備の用途の消費量
    S_L_m = get_S_L_m(S_exHC_m, r_s_L_m)
    return S_L_m * f_PE_K


def get_E_p_K_HW_m(
    S_exHC_m: float,
    r_s_HW_m: float,
    f_PE_K: float,
) -> float:
    """月における灯油の給湯設備の一次エネルギー消費量 式(46)

    Args:
        S_HW_m (float): 月における給湯設備の用途の消費量, L
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月における灯油の給湯設備の一次エネルギー消費量, MJ
    """
    # 給湯設備の用途の消費量
    S_HW_m = get_S_HW_m(S_exHC_m, r_s_HW_m)
    return S_HW_m * f_PE_K


def get_E_p_K_AP_m(
    S_exHC_m: float,
    r_s_HW_m: float,
    f_PE_K: float,
) -> float:
    """月mにおける灯油の家電の一次エネルギー消費量 式(47)

    Args:
        S_AP_m (float): 月mにおける家電の用途の消費量, L
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月mにおける灯油の家電の一次エネルギー消費量, MJ
    """
    # 家電設備の用途の消費量
    S_AP_m = get_S_AP_m(S_exHC_m, r_s_HW_m)
    return S_AP_m * f_PE_K


def get_E_p_K_CC_m(
    S_exHC_m: float,
    r_s_CC_m: float,
    f_PE_K: float,
) -> float:
    """月mにおける灯油の調理の一次エネルギー消費量 式(48)

    Args:
        S_CC_m (float): 月mにおける調理の用途の消費量, L
        f_PE_K (float): 灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 月mにおける灯油の調理の一次エネルギー消費量, MJ
    """
    # 調理設備の用途の消費量
    S_CC_m = get_S_CC_m(S_exHC_m, r_s_CC_m)
    return S_CC_m * f_PE_K


def get_f_PE_K(
    use_specified_f_PE_K: str,
    f_PE_K: float
) -> float:
    """計算に用いる灯油の一次エネルギー換算係数, MJ/L

    Args:
        use_specified_f_PE_K (str): 灯油の一次エネルギー換算係数の規定値の使用 ('使用する' or '使用しない')
        f_PE_K (float): 指定された灯油の一次エネルギー換算係数, MJ/L

    Returns:
        float: 灯油の一次エネルギー換算係数, MJ/L
    """
    if use_specified_f_PE_K == '使用する':
        return 37.0
    elif use_specified_f_PE_K == '使用しない':
        return f_PE_K
    else:
        raise ValueError(use_specified_f_PE_K)


def get_U_H_m(
    U_K_H_m: bool
) -> bool:
    """月mにおいて暖房設備を使用しているかの有無 式(49)

    Args:
        U_K_H_m (bool): 月mにおける灯油を暖房設備に使用しているかの有無

    Returns:
        bool: 月mにおいて暖房設備を使用しているかの有無
    """
    return U_K_H_m


def get_U_C_m() -> bool:
    """月mにおいて冷房設備を使用しているかの有無, bool 式(50)

    Args:

    Returns:
        bool: 月mにおいて冷房設備を使用しているかの有無, bool
    """
    return False


def get_C_V() -> float:
    """換気設備の調整係数 式(51)

    Args:

    Returns:
        float: 換気設備の調整係数
    """
    return 0.0


def get_C_L() -> float:
    """照明設備の調整係数 式(52)

    Args:

    Returns:
        float: 照明設備の調整係数
    """
    return 0.0


def get_C_HW(
    U_K_HW: bool,
    C_K_HW: float
) -> float:
    """給湯設備の調整係数 式(53)

    Args:
        U_K_HW (bool): 灯油を給湯設備に使用しているかの有無
        C_K_HW (float): 灯油を給湯設備に使用している場合の調整係数

    Returns:
        float: 給湯設備の調整係数
    """
    if U_K_HW:
        return C_K_HW
    else:
        return 0.0


def get_C_AP() -> float:
    """家電の調整係数 式(54)

    Args:

    Returns:
        float: 家電の調整係数
    """
    return 0.0


def get_C_CC() -> float:
    """調理の調整係数 式(55)

    Args:
        C_G_CC (float): 電気を調理に使用している場合の調整係数
        U_G_CC (bool): 電気を調理に使用しているかの有無

    Returns:
        float: 調理の調整係数
    """
    return 0.0


def get_S_m(
    S_K_m: float,
) -> float:
    """月mにおける月別消費量 (L) 式(56)

    Args:
        S_K_m (float): 月mにおける灯油の月別消費量 (L)

    Returns:
        float: 月mにおける月別消費量 (L)
    """
    return S_K_m


def get_S_H_m(
    S_exHC_m: float,
    S_m: float,
    U_H_m: bool,
) -> float:
    """月mにおける暖房設備の用途の消費量 (L) 式(57)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        U_H_m (bool): 月mにおいて暖房設備を使用しているかの有無

    Returns:
        float: 月mにおける暖房設備の用途の消費量 (L)
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
    """月mにおける冷房設備の用途の消費量 (L) 式(58)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        S_m (float): 月mにおける月別消費量
        U_C_m (bool): 月mにおいて冷房設備を使用しているかの有無

    Returns:
        float: 月mにおける冷房設備の用途の消費量 (L)
    """
    if U_C_m:
        return S_m - S_exHC_m
    else:
        return 0.0


def get_S_V_m(
    S_exHC_m: float,
    r_s_V_m: float,
) -> float:
    """月mにおける換気設備の用途の消費量 (L) 式(59)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        r_s_V_m (float): 月mにおける換気設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける換気設備の用途の消費量 (L)
    """
    return r_s_V_m * S_exHC_m


def get_S_L_m(
    S_exHC_m: float,
    r_s_L_m: float,
) -> float:
    """月mにおける照明設備の用途の消費量 (L) 式(60)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        r_s_L_m (float): 月mにおける照明設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける照明設備の用途の消費量 (L)
    """
    return r_s_L_m * S_exHC_m


def get_S_HW_m(
    S_exHC_m: float,
    r_s_HW_m: float,

) -> float:
    """月mにおける給湯設備の用途の消費量 (L) 式(61)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        r_s_HW_m (float): 月mにおける給湯設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける給湯設備の用途の消費量 (L)
    """
    return r_s_HW_m * S_exHC_m


def get_S_AP_m(
    S_exHC_m: float,
    r_s_AP_m: float,

) -> float:
    """月mにおける家電設備の用途の消費量 (L) 式(62)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        r_s_AP_m (float): 月mにおける家電設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける家電設備の用途の消費量 (L)
    """
    return r_s_AP_m * S_exHC_m


def get_S_CC_m(
    S_exHC_m: float,
    r_s_CC_m: float,
) -> float:
    """月mにおける調理設備の用途の消費量 (L) 式(63)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量
        r_s_CC_m (float): 月mにおける調理設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける調理設備の用途の消費量 (L)
    """
    return r_s_CC_m * S_exHC_m
