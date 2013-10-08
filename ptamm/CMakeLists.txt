cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)
rosbuild_init()

add_definitions(-DCVD_HAVE_TOON)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

# Generate dynamic parameters
rosbuild_find_ros_package(dynamic_reconfigure)
include(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake)
gencfg()

find_package(OpenCV REQUIRED)

set(PTAM_SOURCE_FILES         
	src/GLWindow2.cc       
	src/main.cc      
	src/MapViewer.cc 
	src/ATANCamera.cc          
	src/GLWindowMenu.cc    
	src/Map.cc       
	src/MiniPatch.cc    
	src/ShiTomasi.cc         
	src/Tracker.cc
  src/Bundle.cc                 
  src/HomographyInit.cc  
  src/MapMaker.cc  
  src/PatchFinder.cc  
  src/SmallBlurryImage.cc                
  src/KeyFrame.cc        
  src/MapPoint.cc  
  src/Relocaliser.cc  
  src/System.cc     
  src/Params.cpp
  src/OctomapInterface.cc
)

set(PTAM_HEADER_FILES        
  include/ptamm/CameraCalibrator.h  
  include/ptamm/KeyFrame.h      
  include/ptamm/MapViewer.h    
  include/ptamm/Relocaliser.h       
  include/ptamm/TrackerData.h
  include/ptamm/ATANCamera.h         
  include/ptamm/LevelHelpers.h  
  include/ptamm/MEstimator.h   
  include/ptamm/ShiTomasi.h         
  include/ptamm/Tracker.h
  include/ptamm/Bundle.h            
  include/ptamm/GLWindow2.h         
  include/ptamm/Map.h           
  include/ptamm/MiniPatch.h    
  include/ptamm/SmallBlurryImage.h 
  include/ptamm/CalibCornerPatch.h  
  include/ptamm/GLWindowMenu.h      
  include/ptamm/MapMaker.h      
  include/ptamm/OpenGL.h       
  include/ptamm/SmallMatrixOpts.h
  include/ptamm/CalibImage.h        
  include/ptamm/HomographyInit.h    
  include/ptamm/MapPoint.h      
  include/ptamm/PatchFinder.h  
  include/ptamm/System.h  
  include/ptamm/Params.h
)
	
SET(CALIBRATOR_FILES     
  src/CameraCalibrator.cc 
  src/GLWindowMenu.cc 
  src/CalibCornerPatch.cc           
  src/CalibImage.cc            
  src/GLWindow2.cc	
  src/ATANCamera.cc 
  src/Params.cpp 
)	

include_directories(
  ${PROJECT_SOURCE_DIR}/thirdparty/TooN/include 
  ${PROJECT_SOURCE_DIR}/thirdparty/libcvd/include 
  ${PROJECT_SOURCE_DIR}/thirdparty/gvars3/include 
  ${PROJECT_SOURCE_DIR}/thirdparty/agast/include
)  

link_directories(
  ${PROJECT_SOURCE_DIR}/thirdparty/libcvd/lib 
  ${PROJECT_SOURCE_DIR}/thirdparty/gvars3/lib 
  ${PROJECT_SOURCE_DIR}/thirdparty/agast/lib
)

set(PTAM_LIBRARIES GL glut cvd GVars3_headless agast blas lapack)

add_definitions(-DKF_REPROJ)

# PTAM executable
rosbuild_add_executable(ptamm ${PTAM_SOURCE_FILES} ${PTAM_HEADER_FILES})
rosbuild_add_compile_flags(ptamm -D_LINUX -D_REENTRANT -Wall -march=native)
IF(CMAKE_BUILD_TYPE MATCHES Release)
 rosbuild_add_compile_flags(ptamm -O3)
 SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsee -funsafe-loop-optimizations -fno-signed-zeros -fno-math-errno -funroll-loops")
ENDIF(CMAKE_BUILD_TYPE MATCHES Release)

target_link_libraries(ptamm ${PTAM_LIBRARIES} ${OpenCV_LIBS})


# Camera calibrator 
rosbuild_add_executable(cameracalibrator ${CALIBRATOR_FILES})
target_link_libraries(cameracalibrator ${PTAM_LIBRARIES} ${OpenCV_LIBS})

# PTAM remote control
# this is unfortunately neccessary to close app, when opencvwindow gets closed
include(FindPkgConfig)
if (PKG_CONFIG_FOUND AND UNIX AND NOT APPLE)
   pkg_check_modules(GTK gtk+-2.0)
   if (GTK_FOUND)
      include_directories(${GTK_INCLUDE_DIRS})
      link_directories(${GTK_LIBRARY_DIRS})
      add_definitions(-DHAVE_GTK)
      # Hack around gdk-pixbuf move issues for now
      # http://ubuntuforums.org/showthread.php?t=1596930
      include_directories(/usr/include/gdk-pixbuf-2.0)
   endif(GTK_FOUND)
endif(PKG_CONFIG_FOUND AND UNIX AND NOT APPLE)

rosbuild_add_executable(remote_ptamm src/RemotePtam.cpp)
target_link_libraries(remote_ptamm ${GTK_LIBRARIES} ${OpenCV_LIBS})

rosbuild_add_executable(ptamm_visualizer src/PTAMVisualizer.cpp)
