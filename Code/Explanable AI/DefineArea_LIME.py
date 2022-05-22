# -*- coding: utf-8 -*-
"""
Author: LiGorden
Email: likehao1006@gmail.com
URL: https://www.linkedin.com/in/kehao-li-06a9a2235/
ResearchGate: https://www.researchgate.net/profile/Gorden-Li

Use disorder np map generated by  LIME to create explanatory area serve as robustness check
"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读取canvas高维数组
    canvas_array = np.load(file="canvas_data_150samples.npy")
    final_canvas = np.zeros([224, 224])
    for i in range(canvas_array.shape[2]):  # 找到每个区域最大prob归属(D1~D10)
        candidate_array = np.ones([224, 224])
        for j in range(canvas_array.shape[2]):
            if i == j:
                continue
            candidate_array = candidate_array * (canvas_array[:, :, i] > canvas_array[:, :, j])
        final_canvas += candidate_array * (i + 1)
    final_canvas = final_canvas.astype(int)

    # 绘制区域
    plt.figure()
    plt.xticks(np.arange(0, 230, 10))
    plt.yticks(np.arange(0, 230, 10))
    plt.axis('off')
    i = 0
    while i < 224:
        j = 0
        while j < 224:
            num = final_canvas[i][j]
            if num in []:
                num_color = 'b'
            elif num in [5]:
                num_color = 'r'
            elif num in []:
                num_color = 'y'
            else:
                num_color = 'w'
            plt.annotate(final_canvas[i][j], fontsize=15, xy=(j, 223 - i), xytext=(j, 223 - i), color=num_color)
            j += 15
        i += 15
    plt.show()

