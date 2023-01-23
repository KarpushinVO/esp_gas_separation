import math

class Lepkov:
    def __init__(self):
        self.fvf_oil = 0.89
        self.fvf_water = 1
        self.diameter_casing = 100
        self.diameter_sn = 55
    #Здесь надо прописать исходные данные для констант.100


    # Методика Ляпкова расчета коэффициента естественной, искуственной и общей сепарации
    # fvf - formation volume factor - объёмный коэффициент
    # stc - stock-tank conditions - стандартные условия
    # z - коэффициент сверхсжимаемости на глубине спуска насоса
    # w_pr - приведенная скорость жидкости


    # Расчет приведенной скорости жидкости w_pr:
    def liquid_velocity(qliquid_stc, fvf_oil, fvf_water, betta_vsu, diameter_casing, diameter_sn):
        w_pr = (4 * qliquid_stc * (fvf_water * betta_vsu + fvf_oil * (1 - betta_vsu))) / (
                86400 * 3.14 * (diameter_casing ** 2 - diameter_sn ** 2))
        return w_pr

    # Расчет коэффициента естественной сепарации газа
    def natural_gas_separation_ratio(w_drg, betta_gas_input, w_pr):
        k_s = 1 / (1 + ((0.52 * w_pr) / (w_drg * (1 - 0.06 * betta_gas_input))))
        return k_s

    #Расчет расход газа на глубине спуска насоса до сепарации

    def gas_flow_input(q_g_input, pressure_input, temprature_stc, pressure_stc, z):
        q_g_input_stc = q_g_input * (pressure_input * temprature_stc)/(pressure_stc * pressure_input * z)
        return q_g_input_stc
    #Расход газа при отжиме

    def q_g_otjim(H_max, p_max, p_min, H_min, Diameter_casing_inside, Diameter_tubing_outside, pressure_stc, t_otjim):
        q_g_otjim = (360 * math.pi * (H_max * p_max - H_min * p_min) * (Diameter_casing_inside ** 2 - Diameter_tubing_outside ** 2)) / (pressure_stc * t_otjim)
        return q_g_otjim
# Расчет общего коэффициента сепарации проводится по результатам отжима динамического уровня и определяется по формуле
    def overall_separation_ratio_after_lapping(q_g_otj_stc, q_g_input_stc):
        k_sep = q_g_otj_stc / q_g_input_stc
        return k_sep

    #Расчет коэффициента искусственной сепарации производится по формуле
    def sintetic_separation_ratio(k_sep, k_s):
        k_sgs = (k_sep - k_s)/(1 - k_s)
        return k_sgs