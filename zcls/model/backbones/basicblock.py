# -*- coding: utf-8 -*-

"""
@date: 2020/11/21 下午2:38
@file: basicblock.py
@author: zj
@description: 
"""
from abc import ABC

import torch.nn as nn


class BasicBlock(nn.Module, ABC):
    """
    使用两个3x3卷积，如果进行下采样，那么使用第一个卷积层对输入空间尺寸进行减半操作
    参考Torchvision实现
    """
    expansion = 1

    def __init__(self,
                 # 输入通道数
                 in_planes,
                 # 输出通道数
                 out_planes,
                 # 步长
                 stride=1,
                 # 下采样
                 down_sample=None,
                 # cardinality
                 groups=1,
                 # 基础宽度
                 base_width=64,
                 # 卷积层类型
                 conv_layer=None,
                 # 归一化层类型
                 norm_layer=None,
                 # 激活层类型
                 act_layer=None
                 ):
        super(BasicBlock, self).__init__()
        if groups != 1 or base_width != 64:
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')

        if conv_layer is None:
            conv_layer = nn.Conv2d
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if act_layer is None:
            act_layer = nn.ReLU

        self.downsample = down_sample

        self.conv1 = conv_layer(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = norm_layer(out_planes)

        self.conv2 = conv_layer(out_planes, out_planes, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = norm_layer(out_planes)

        self.relu = act_layer(inplace=True)

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out
