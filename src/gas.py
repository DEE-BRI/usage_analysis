"""5.月別のガスの一次エネルギー消費量"""

def get_E_p_G_H_m(
    S_m: float,
    S_exHC_m: float,
    U_G_H_m: bool,
    f_PE_G: float,
) -> float:
    """月mにおけるガスの暖房設備の一次エネルギー消費量 式(27)

    Args:
        S_m (float): 月mにおける月別消費量, m³
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        U_G_H_m (bool): 月mにおけるガスを暖房設備に使用しているかの有無
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの暖房設備の一次エネルギー消費量, MJ
    """
    # 調理設備の用途の消費量
    U_H_m = get_U_H_m(U_G_H_m)

    # 調理設備の用途の消費量
    S_H_m = get_S_H_m(S_exHC_m, S_m, U_H_m)

    return S_H_m * f_PE_G


def get_E_p_G_C_m(
    S_m: float,
    S_exHC_m: float,
    f_PE_G: float,
) -> float:
    """月mにおけるガスの冷房設備の一次エネルギー消費量 式(28)

    Args:
        S_m (float): 月mにおける月別消費量, m³
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの冷房設備の一次エネルギー消費量, MJ
    """
    # 冷房設備を使用しているかの有無
    U_C_m = get_U_C_m()

    # 冷房設備の用途の消費量
    S_C_m = get_S_C_m(S_exHC_m, S_m, U_C_m)

    return S_C_m * f_PE_G


def get_E_p_G_V_m(
    S_exHC_m: float,
    r_s_V_m: float,
    f_PE_G: float,
) -> float:
    """月mにおけるガスの換気設備の一次エネルギー消費量 式(29)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_V_m (float): 月mにおける換気設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの換気設備の一次エネルギー消費量, MJ
    """
    # 換気設備の用途の消費量
    S_V_m = get_S_V_m(S_exHC_m, r_s_V_m)
    return S_V_m * f_PE_G


def get_E_p_G_L_m(
    S_exHC_m: float,
    r_s_L_m: float,
    f_PE_G: float,
) -> float:
    """月におけるガスの照明設備の一次エネルギー消費量 式(30)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_L_m (float): 月mにおける照明設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの照明設備の一次エネルギー消費量, MJ
    """
    # 照明設備の用途の消費量
    S_L_m = get_S_L_m(S_exHC_m, r_s_L_m)
    return S_L_m * f_PE_G


def get_E_p_G_HW_m(
    S_exHC_m: float,
    r_s_HW_m: float,
    f_PE_G: float,
) -> float:
    """月におけるガスの給湯設備の一次エネルギー消費量 式(31)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_HW_m (float): 月mにおける給湯設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月におけるガスの給湯設備の一次エネルギー消費量, MJ
    """
    # 給湯設備の用途の消費量
    S_HW_m = get_S_HW_m(S_exHC_m, r_s_HW_m)
    return S_HW_m * f_PE_G


def get_E_p_G_AP_m(
    S_exHC_m: float,
    r_s_AP_m: float,
    f_PE_G: float,
) -> float:
    """月mにおけるガスの家電の一次エネルギー消費量 式(32)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_AP_m (float): 月mにおける家電設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの家電の一次エネルギー消費量, MJ
    """
    # 家電設備の用途の消費量
    S_AP_m = get_S_AP_m(S_exHC_m, r_s_AP_m)
    return S_AP_m * f_PE_G


def get_E_p_G_CC_m(
    S_exHC_m: float,
    r_s_CC_m: float,
    f_PE_G: float,
) -> float:
    """月mにおけるガスの調理の一次エネルギー消費量 式(33)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_CC_m (float): 月mにおける調理設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの調理の一次エネルギー消費量, MJ
    """
    # 調理設備の用途の消費量
    S_CC_m = get_S_CC_m(S_exHC_m, r_s_CC_m)
    return S_CC_m * f_PE_G


def get_f_PE_G(
    use_specified_f_PE_G: str,
    gas_type: str,
    f_PE_G: float
) -> float:
    """月mにおけるガスの調理の一次エネルギー消費量

  Args:
        S_CC_m (float): 月mにおける調理の用途の消費量, m³
        f_PE_G (float): ガスの一次エネルギー換算係数, MJ/m³

    Returns:
        float: 月mにおけるガスの調理の一次エネルギー消費量, MJ
    """
    if use_specified_f_PE_G == '使用する':
        if gas_type == '都市ガス':
            return 45.0
        elif gas_type == 'ＬＰガス':
            return 100.0
        raise ValueError(gas_type)
    else:
        return f_PE_G


def get_U_H_m(
    U_G_H_m: bool
) -> bool:
    """月mにおいて暖房設備を使用しているかの有無 式(34)

  Args:
        U_G_H_m (bool): 月mにおけるガスを暖房設備に使用しているかの有無

    Returns:
        bool: 月mにおいて暖房設備を使用しているかの有無
    """
    return U_G_H_m


def get_U_C_m() -> bool:
    """月mにおいて冷房設備を使用しているかの有無, bool 式(35)

    Args:

    Returns:
        bool: 月mにおいて冷房設備を使用しているかの有無, bool
    """
    return False


def get_C_V() -> float:
    """換気設備の調整係数 式(36)

    Args:

    Returns:
        float: 換気設備の調整係数
    """
    return 0.0


def get_C_L() -> float:
    """照明設備の調整係数 式(36)

    Args:

    Returns:
        float: 照明設備の調整係数
    """
    return 0.0


def get_C_HW(
    U_G_HW: bool,
    C_G_HW: float,
) -> float:
    """給湯設備の調整係数 式(38)

    Args:
        U_G_HW (bool): ガスを給湯設備に使用しているかの有無
        C_E_HW (float): ガスを給湯設備に使用している場合の調整係数

    Returns:
        float: 給湯設備の調整係数
    """
    if U_G_HW:
        return C_G_HW
    else:
        return 0.0


def get_C_AP() -> float:
    """家電の調整係数

    Args:

    Returns:
        float: 家電の調整係数 式(39)
    """
    return 0.0


def get_C_CC(
    U_G_CC: bool,
    C_G_CC: float,
) -> float:
    """調理の調整係数 式(40)

    Args:
        C_G_CC (float): ガスを調理に使用している場合の調整係数
        U_G_CC (bool): ガスを調理に使用しているかの有無

    Returns:
        float: 調理の調整係数
    """
    if U_G_CC:
        return C_G_CC
    else:
        return 0.0


def get_S_m(
    S_G_m: float,
) -> float:
    """月mにおける月別消費量 (m³) 式(41)

    Args:
        S_G_m (float): 月mにおけるガスの月別消費量 (m³)

    Returns:
        float: 月mにおける月別消費量 (m³)
    """
    return S_G_m


def get_S_H_m(
    S_exHC_m: float,
    S_m: float,
    U_H_m: bool,

) -> float:
    """月mにおける暖房設備の用途の消費量 (m³) 式(57)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        S_m (float): 月mにおける月別消費量, m³
        U_H_m (bool): 月mにおいて暖房設備を使用しているかの有無

    Returns:
        float: 月mにおける暖房設備の用途の消費量 (m³)
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
    """月mにおける冷房設備の用途の消費量 (m³) 式(58)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        S_m (float): 月mにおける月別消費量, m³
        U_C_m (bool): 月mにおいて冷房設備を使用しているかの有無

    Returns:
        float: 月mにおける冷房設備の用途の消費量 (m³)
    """
    if U_C_m:
        return S_m - S_exHC_m
    else:
        return 0.0


def get_S_V_m(
    S_exHC_m: float,
    r_s_V_m: float,
) -> float:
    """月mにおける換気設備の用途の消費量 (m³) 式(59)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_V_m (float): 月mにおける換気設備の消費量が月mにおける暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける換気設備の用途の消費量 (m³)
    """
    return r_s_V_m * S_exHC_m


def get_S_L_m(
    S_exHC_m: float,
    r_s_L_m: float,
) -> float:
    """月mにおける照明設備の用途の消費量 (m³) 式(60)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_L_m (float): 月mにおける照明設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける照明設備の用途の消費量 (m³)
    """
    return r_s_L_m * S_exHC_m


def get_S_HW_m(
    S_exHC_m: float,
    r_s_HW_m: float,

) -> float:
    """月mにおける給湯設備の用途の消費量 (m³) 式(61)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_HW_m (float): 月mにおける給湯設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける給湯設備の用途の消費量 (m³)
    """
    return r_s_HW_m * S_exHC_m


def get_S_AP_m(
    S_exHC_m: float,
    r_s_AP_m: float,

) -> float:
    """月mにおける家電設備の用途の消費量 (m³) 式(62)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_AP_m (float): 月mにおける家電設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける家電設備の用途の消費量 (m³)
    """
    return r_s_AP_m * S_exHC_m


def get_S_CC_m(
    S_exHC_m: float,
    r_s_CC_m: float,

) -> float:
    """月mにおける調理設備の用途の消費量 (m³) 式(63)

    Args:
        S_exHC_m (float): 月mにおける暖冷房設備以外の用途の消費量, m³
        r_s_CC_m (float): 月mにおける調理設備の消費量が月における暖冷房設備以外の用途の消費量に占める割合

    Returns:
        float: 月mにおける調理設備の用途の消費量 (m³)
    """
    return r_s_CC_m * S_exHC_m
