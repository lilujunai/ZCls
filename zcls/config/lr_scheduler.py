# -*- coding: utf-8 -*-

"""
@date: 2020/11/25 下午6:48
@file: lr_scheduler.py
@author: zj
@description: 
"""

from yacs.config import CfgNode as CN


def add_config(_C):
    # ---------------------------------------------------------------------------- #
    # LR_Scheduler
    # ---------------------------------------------------------------------------- #
    _C.LR_SCHEDULER = CN()
    _C.LR_SCHEDULER.NAME = 'MultiStepLR'
    _C.LR_SCHEDULER.IS_WARMUP = False
    _C.LR_SCHEDULER.GAMMA = 0.1

    # for MultiStepLR
    _C.LR_SCHEDULER.MULTISTEP_LR = CN()
    _C.LR_SCHEDULER.MULTISTEP_LR.MILESTONES = [50, 80]
    # for Warmup
    _C.LR_SCHEDULER.WARMUP = CN()
    _C.LR_SCHEDULER.WARMUP.ITERATION = 5
    _C.LR_SCHEDULER.WARMUP.MULTIPLIER = 1.0
