# -*- coding: utf-8 -*-

"""
@date: 2020/12/3 下午8:19
@file: test_mobilenetv1_head.py
@author: zj
@description: 
"""

import torch
from zcls.model.heads.mobilenetv1_head import MobileNetV1Head


def test_mobilenet_v1_head():
    data = torch.randn(1, 1024, 7, 7)

    feature_dims = 1024
    num_classes = 1000
    model = MobileNetV1Head(feature_dims=feature_dims, num_classes=num_classes)

    outputs = model(data)
    print(outputs.shape)

    assert outputs.shape == (1, 1000)


if __name__ == '__main__':
    test_mobilenet_v1_head()
