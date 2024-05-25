import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1017890038 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha=0.04
    control_conversion = 1.0*x_success/x_cnt
    test_conversion = 1.0*y_success/y_cnt
               
    count = np.array([control_sales, test_sales])
    nobs = np.array([control_leads, test_leads])   
               
    z_stat, p_value = proportions_ztest(count, nobs, alternative = 'smaller')
    ans = p_value < alpha
               
    return ans # Ваш ответ, True или False
