# -*- coding: utf-8 -*-

"""
@date: 2020/11/25 下午6:49
@file: model.py
@author: zj
@description: 
"""

from yacs.config import CfgNode as CN


def add_config(_C):
    # ---------------------------------------------------------------------------- #
    # Model
    # ---------------------------------------------------------------------------- #
    _C.MODEL = CN()

    # ---------------------------------------------------------------------------- #
    # Convolution
    # ---------------------------------------------------------------------------- #
    _C.MODEL.CONV = CN()
    _C.MODEL.CONV.TYPE = 'Conv2d'

    # ---------------------------------------------------------------------------- #
    # Normalization
    # ---------------------------------------------------------------------------- #
    _C.MODEL.NORM = CN()
    _C.MODEL.NORM.TYPE = 'BatchNorm2d'
    # for BN
    _C.MODEL.NORM.SYNC_BN = False
    _C.MODEL.NORM.FIX_BN = False
    _C.MODEL.NORM.PARTIAL_BN = False
    # Precise BN stats.
    _C.MODEL.NORM.PRECISE_BN = False
    # Number of samples use to compute precise bn.
    _C.MODEL.NORM.NUM_BATCHES_PRECISE = 200
    # for GN
    _C.MODEL.NORM.GROUPS = 32

    # ---------------------------------------------------------------------------- #
    # activation
    # ---------------------------------------------------------------------------- #
    _C.MODEL.ACT = CN()
    _C.MODEL.ACT.TYPE = 'ReLU'

    # ---------------------------------------------------------------------------- #
    # compression
    # ---------------------------------------------------------------------------- #
    _C.MODEL.COMPRESSION = CN()
    _C.MODEL.COMPRESSION.WIDTH_MULTIPLIER = 1.0

    # ---------------------------------------------------------------------------- #
    # attention
    # ---------------------------------------------------------------------------- #
    _C.MODEL.ATTENTION = CN()
    _C.MODEL.ATTENTION.WITH_ATTENTION = (1, 1, 1, 1)
    _C.MODEL.ATTENTION.REDUCTION = 16
    _C.MODEL.ATTENTION.ATTENTION_TYPE = 'GlobalContextBlock2D'

    # ---------------------------------------------------------------------------- #
    # backbone
    # ---------------------------------------------------------------------------- #
    _C.MODEL.BACKBONE = CN()
    # 输入通道数
    _C.MODEL.BACKBONE.IN_PLANES = 3
    # for ResNet series
    _C.MODEL.BACKBONE.ARCH = 'resnet18'
    # stem通道数,
    _C.MODEL.BACKBONE.BASE_PLANES = 64
    # 每一层基础通道数
    _C.MODEL.BACKBONE.LAYER_PLANES = (64, 128, 256, 512)
    # 是否执行空间下采样
    _C.MODEL.BACKBONE.DOWN_SAMPLES = (0, 1, 1, 1)
    # cardinality
    _C.MODEL.BACKBONE.GROUPS = 1
    # 每组的宽度
    _C.MODEL.BACKBONE.WIDTH_PER_GROUP = 64

    # ---------------------------------------------------------------------------- #
    # head
    # ---------------------------------------------------------------------------- #
    _C.MODEL.HEAD = CN()
    _C.MODEL.HEAD.NUM_CLASSES = 1000

    # ---------------------------------------------------------------------------- #
    # recognizer
    # ---------------------------------------------------------------------------- #
    _C.MODEL.RECOGNIZER = CN()
    _C.MODEL.RECOGNIZER.TYPE = 'ResNet'
    _C.MODEL.RECOGNIZER.NAME = 'CustomResNet'
    # zcls框架训练的模型，用于训练阶段
    _C.MODEL.RECOGNIZER.PRELOADED = ""
    # zcls框架训练的模型，用于训练阶段
    _C.MODEL.RECOGNIZER.PRETRAINED = ""
    # torchvision训练的模型，用于训练阶段
    _C.MODEL.RECOGNIZER.TORCHVISION_PRETRAINED = False
    # 预训练模型类别数
    _C.MODEL.RECOGNIZER.PRETRAINED_NUM_CLASSES = 1000
    # 零初始化残差连接
    _C.MODEL.RECOGNIZER.ZERO_INIT_RESIDUAL = False

    # ---------------------------------------------------------------------------- #
    # criterion
    # ---------------------------------------------------------------------------- #
    _C.MODEL.CRITERION = CN()
    _C.MODEL.CRITERION.NAME = 'CrossEntropyLoss'
