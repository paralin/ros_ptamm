## *********************************************************
## 
## File autogenerated for the ptamm package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 259, 'description': 'Scale', 'max': 30.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'Scale', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 259, 'description': 'selects the source for the motion model.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MotionModelSource', 'edit_method': "{'enum_description': 'An enum to set wich input to use for the motion model.', 'enum': [{'srcline': 28, 'description': 'use constant motion model.', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'CONSTANT', 'ctype': 'std::string', 'type': 'str', 'name': 'MM_CONSTANT'}, {'srcline': 29, 'description': 'use imu orientation for the motion model.', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'IMU', 'ctype': 'std::string', 'type': 'str', 'name': 'MM_IMU'}, {'srcline': 30, 'description': 'use full pose estimated externally for motion model.', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'FULL_POSE', 'ctype': 'std::string', 'type': 'str', 'name': 'MM_FULL_POSE'}]}", 'default': 'CONSTANT', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'max features per frame', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MaxPatchesPerFrame', 'edit_method': '', 'default': 500.0, 'level': 0, 'min': 10.0, 'type': 'double'}, {'srcline': 259, 'description': "'distance' after which a new kf is requested", 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MaxKFDistWiggleMult', 'edit_method': '', 'default': 3.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 259, 'description': 'use AutoInitPixel as new KF request criteria', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'UseKFPixelDist', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'do not add map points at level zero', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'NoLevelZeroMapPoints', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'depth variance to search for features', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'EpiDepthSearchMaxRange', 'edit_method': '', 'default': 100.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 259, 'description': 'min number of features for coarse tracking', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'CoarseMin', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 259, 'description': 'max number of features for coarse tracking', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'CoarseMax', 'edit_method': '', 'default': 60.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 259, 'description': 'Pixel search radius for coarse features', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'CoarseRange', 'edit_method': '', 'default': 30.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 259, 'description': 'coarse tracking sub-pixel iterations', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'CoarseSubPixIts', 'edit_method': '', 'default': 8.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 259, 'description': 'enable/disable coarse tracking', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'DisableCoarse', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'speed above which coarse stage is used', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'CoarseMinVelocity', 'edit_method': '', 'default': 0.006, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 259, 'description': 'min ratio features visible/features found for good tracking', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'TrackingQualityGood', 'edit_method': '', 'default': 0.3, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 259, 'description': 'max ratio features visible/features found before lost', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'TrackingQualityLost', 'edit_method': '', 'default': 0.13, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 259, 'description': 'min pixels to be found for good tracking', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'TrackingQualityFoundPixels', 'edit_method': '', 'default': 100, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 259, 'description': 'max iterations for bundle adjustment', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MaxIterations', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 259, 'description': 'number of keyframes kept in the map (0 or 1 = inf)', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MaxKF', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'bundleadjustment method', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'BundleMethod', 'edit_method': "{'enum_description': 'An enum to set the bundle adjustment mode.', 'enum': [{'srcline': 14, 'description': 'local and global bundle adjustment', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'LOCAL_GLOBAL', 'ctype': 'std::string', 'type': 'str', 'name': 'LOCAL_GLOBAL'}, {'srcline': 15, 'description': 'local bundle adjustment only', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'LOCAL', 'ctype': 'std::string', 'type': 'str', 'name': 'LOCAL'}, {'srcline': 16, 'description': 'global bundle adjustment only', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'GLOBAL', 'ctype': 'std::string', 'type': 'str', 'name': 'GLOBAL'}]}", 'default': 'LOCAL_GLOBAL', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'limit for convergence in bundle adjustment', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'UpdateSquaredConvergenceLimit', 'edit_method': '', 'default': 1e-06, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 259, 'description': 'print bundle debug messages', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'BundleDebugMessages', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'FAST corner method', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'FASTMethod', 'edit_method': "{'enum_description': 'An enum to set the FAST corner extraction method.', 'enum': [{'srcline': 20, 'description': 'FAST 9', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'FAST9', 'ctype': 'std::string', 'type': 'str', 'name': 'FAST9'}, {'srcline': 21, 'description': 'FAST 10', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'FAST10', 'ctype': 'std::string', 'type': 'str', 'name': 'FAST10'}, {'srcline': 22, 'description': 'FAST 9 with nonmax suppression', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'FAST9_nonmax', 'ctype': 'std::string', 'type': 'str', 'name': 'FAST9_nonmax'}, {'srcline': 23, 'description': 'AGAST 12 pixel diamond', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'AGAST12d', 'ctype': 'std::string', 'type': 'str', 'name': 'AGAST12d'}, {'srcline': 24, 'description': 'AGAST 16 pixel circular', 'srcfile': '../cfg/PtamParams.cfg', 'cconsttype': 'const char * const', 'value': 'OAST16', 'ctype': 'std::string', 'type': 'str', 'name': 'OAST16'}]}", 'default': 'FAST9_nonmax', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'threshold for FAST features on level 0', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'Thres_lvl0', 'edit_method': '', 'default': 10, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'threshold for FAST features on level 1', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'Thres_lvl1', 'edit_method': '', 'default': 15, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'threshold for FAST features on level 2', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'Thres_lvl2', 'edit_method': '', 'default': 15, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'threshold for FAST features on level 3', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'Thres_lvl3', 'edit_method': '', 'default': 10, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'adaptive threshold for corner extraction', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'AdaptiveThrs', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'controls adaptive threshold to MaxPatches*N corners', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'AdaptiveThrsMult', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.5, 'type': 'double'}, {'srcline': 259, 'description': 'small images for the rotation estimator blur', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'RotationEstimatorBlur', 'edit_method': '', 'default': 0.75, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 259, 'description': 'small images for the rotation estimator enable/disable', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'UseRotationEstimator', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'MiniPatch tracking threshhold', 'max': 10000000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MiniPatchMaxSSD', 'edit_method': '', 'default': 100000, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'number of dominant plane RANSACs', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'PlaneAlignerRansacs', 'edit_method': '', 'default': 100, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'score for relocalization', 'max': 90000000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'RelocMaxScore', 'edit_method': '', 'default': 9000000, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'enable auto initialization', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'AutoInit', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'check map point variance for initial map', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'CheckInitMapVar', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'min pixel distance for auto initialization', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'AutoInitPixel', 'edit_method': '', 'default': 20, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 259, 'description': 'max # of loops for stereo initialization', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'MaxStereoInitLoops', 'edit_method': '', 'default': 10, 'level': 0, 'min': 1, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

PtamParams_LOCAL_GLOBAL = 'LOCAL_GLOBAL'
PtamParams_LOCAL = 'LOCAL'
PtamParams_GLOBAL = 'GLOBAL'
PtamParams_FAST9 = 'FAST9'
PtamParams_FAST10 = 'FAST10'
PtamParams_FAST9_nonmax = 'FAST9_nonmax'
PtamParams_AGAST12d = 'AGAST12d'
PtamParams_OAST16 = 'OAST16'
PtamParams_MM_CONSTANT = 'CONSTANT'
PtamParams_MM_IMU = 'IMU'
PtamParams_MM_FULL_POSE = 'FULL_POSE'
PtamParams_SEND_PARAMETERS = 1
