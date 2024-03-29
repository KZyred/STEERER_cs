# ------------------------------------------------------------------------------
# Copyright (c) Microsoft
# Licensed under the MIT License.
# Create by Bin Xiao (Bin.Xiao@microsoft.com)
# Modified by Ke Sun (sunk@mail.ustc.edu.cn), Rainbowsecret (yuyua@microsoft.com)
# ------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yacs.config import CfgNode as CN

# configs for HRNet64
HRNET_64 = CN()
HRNET_64.STEM_INPLANES = 64
HRNET_64.FINAL_CONV_KERNEL = 1
HRNET_64.WITH_HEAD = True

HRNET_64.STAGE2 = CN()
HRNET_64.STAGE2.NUM_MODULES = 1
HRNET_64.STAGE2.NUM_BRANCHES = 2
HRNET_64.STAGE2.NUM_BLOCKS = [4, 4]
HRNET_64.STAGE2.NUM_CHANNELS = [64, 128]
HRNET_64.STAGE2.BLOCK = "BASIC"
HRNET_64.STAGE2.FUSE_METHOD = "SUM"

HRNET_64.STAGE3 = CN()
HRNET_64.STAGE3.NUM_MODULES = 4
HRNET_64.STAGE3.NUM_BRANCHES = 3
HRNET_64.STAGE3.NUM_BLOCKS = [4, 4, 4]
HRNET_64.STAGE3.NUM_CHANNELS = [64, 128, 256]
HRNET_64.STAGE3.BLOCK = "BASIC"
HRNET_64.STAGE3.FUSE_METHOD = "SUM"

HRNET_64.STAGE4 = CN()
HRNET_64.STAGE4.NUM_MODULES = 3
HRNET_64.STAGE4.NUM_BRANCHES = 4
HRNET_64.STAGE4.NUM_BLOCKS = [4, 4, 4, 4]
HRNET_64.STAGE4.NUM_CHANNELS = [64, 128, 256, 512]
HRNET_64.STAGE4.BLOCK = "BASIC"
HRNET_64.STAGE4.FUSE_METHOD = "SUM"


# configs for HRNet48
MOC_SMALL = CN()
MOC_SMALL.WITH_HEAD = True
MOC_SMALL.DROP_PATH_RATE = 0.
MOC_SMALL.NORM = "BN"
MOC_SMALL.ACTIVATION = "ReLU"
MOC_SMALL.FINAL_CONV_KERNEL = 1

MOC_SMALL.STEM_INPLANES = 64
MOC_SMALL.STEM_EXPANSION = 2
MOC_SMALL.STEM_BLOCK = "BOTTLENECK"


MOC_SMALL.STAGE2 = CN()
MOC_SMALL.STAGE2.NUM_MODULES = 1
MOC_SMALL.STAGE2.NUM_BRANCHES = 2
MOC_SMALL.STAGE2.NUM_BLOCKS = [4, 4]

MOC_SMALL.STAGE2.EXPANSION = [1,1]
MOC_SMALL.STAGE2.NUM_CHANNELS = [32, 128]
MOC_SMALL.STAGE2.BLOCK = "HRNetBASIC"
MOC_SMALL.STAGE2.FUSE_METHOD = "SUM"


MOC_SMALL.STAGE3 = CN()
MOC_SMALL.STAGE3.NUM_MODULES = 4
MOC_SMALL.STAGE3.NUM_BRANCHES = 3
MOC_SMALL.STAGE3.NUM_BLOCKS = [ 4, 4, 4]

MOC_SMALL.STAGE3.EXPANSION = [1,1,1]
MOC_SMALL.STAGE3.NUM_CHANNELS = [32, 128, 256]
MOC_SMALL.STAGE3.BLOCK = "HRNetBASIC"
MOC_SMALL.STAGE3.FUSE_METHOD = "SUM"

MOC_SMALL.STAGE4 = CN()
MOC_SMALL.STAGE4.NUM_MODULES = 3
MOC_SMALL.STAGE4.NUM_BRANCHES = 4
MOC_SMALL.STAGE4.NUM_BLOCKS = [ 4, 4, 4,4]

MOC_SMALL.STAGE4.EXPANSION = [1,1,1,1]
MOC_SMALL.STAGE4.NUM_CHANNELS = [32, 128, 256,256]
MOC_SMALL.STAGE4.BLOCK = "HRNetBASIC"
MOC_SMALL.STAGE4.FUSE_METHOD = "SUM"


MOC_BASE = MOC_SMALL.clone()
MOC_BASE.STAGE2.NUM_CHANNELS = [64, 256, 512, 512]
MOC_BASE.STAGE2.EXPANSION = [2,3,4,4]
MOC_BASE.STAGE2.NUM_BLOCKS = [5, 5, 5, 5]

MOCT_SMALL = MOC_SMALL.clone()
MOCT_SMALL.STAGE2.BLOCK = "TRANSFORMER_BLOCK"
MOCT_SMALL.STAGE2.NUM_HEADS = [2,4,8,8]
MOCT_SMALL.STAGE2.NUM_WINDOW_SIZES = [7, 5, 3, 3]

MOCT_SMALL.STAGE2.NUM_MLP_RATIOS = [2,3,4,4]




MODEL_CONFIGS = {
    "moc_small": MOC_SMALL,
    "moc_base": MOC_BASE,
    "moct_small": MOCT_SMALL,
}
