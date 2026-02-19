---
topic_id: 1696
title: "Extension Configuration Failing"
date: 2017-12-20
url: https://discourse.slicer.org/t/1696
---

# Extension configuration failing

**Topic ID**: 1696
**Date**: 2017-12-20
**URL**: https://discourse.slicer.org/t/extension-configuration-failing/1696

---

## Post #1 by @dzenanz (2017-12-20 23:13 UTC)

<p>When trying to configure <a href="https://github.com/BrainMeasurement/MultiAtlas" rel="nofollow noopener">this</a> extension, I run into the below errors. While the extension is a few years old, the errors don’t seem overly related to it, cropping up in VTK’s CMake code. Any ideas how to resolve this?</p>
<pre><code class="lang-auto">Found PythonLibs: optimized;C:/Dev/S3/python-install/libs/python27.lib;debug;C:/Dev/S3//python-install/libs/python27.lib (found version "2.7.13") 
Trying to find DCMTK expecting DCMTKConfig.cmake
Trying to find DCMTK expecting DCMTKConfig.cmake - ok
Found CURL: C:/Dev/S3/curl-install/lib/libcurl.lib (found version "7.34.0-DEV") 
RapidJSON found. Headers: ./include/Slicer-4.9
Found JsonCpp: C:/Dev/S3/JsonCpp-build/src/lib_json/Release/jsoncpp.lib  
Trying to find DCMTK expecting DCMTKConfig.cmake
Trying to find DCMTK expecting DCMTKConfig.cmake - ok
CMake Error at C:/Dev/S3/VTKv9/CMake/FindPythonLibs.cmake:126 (get_filename_component):
  get_filename_component unknown component
  C:/Dev/S3/python-install/libs/python27.lib
Call Stack (most recent call first):
  C:/Dev/S3/Slicer-build/SlicerConfig.cmake:956 (find_package)
  CMakeLists.txt:16 (find_package)


CMake Error at C:/Dev/S3/VTKv9/CMake/FindPythonLibs.cmake:127 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  C:/Dev/S3/Slicer-build/SlicerConfig.cmake:956 (find_package)
  CMakeLists.txt:16 (find_package)


Found PythonLibs: optimized;C:/Dev/S3/python-install/libs/python27.lib;debug;C:/Dev/S3//python-install/libs/python27.lib  
Found PythonInterp: C:/Dev/S3/python-install/bin/SlicerPython.exe (found version "2.7.13") 
Configuring Project with Qt 5.9.3 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, Script, Test, )
Setting QT_PLUGINS_DIR: C:/Libs/Qt/5.9.3/msvc2015_64/plugins
Setting QT_BINARY_DIR: C:/Libs/Qt/5.9.3/msvc2015_64/bin
Checking EXTENSION_NAME variable
Checking EXTENSION_NAME variable - MABMIS
CMake Error at C:/Dev/S3/VTKv9/CMake/FindPythonLibs.cmake:126 (get_filename_component):
  get_filename_component unknown component
  C:/Dev/S3/python-install/libs/python27.lib
Call Stack (most recent call first):
  C:/Dev/S3/CTK/Utilities/CMake/FindPythonQt.cmake:7 (find_package)
  C:/Dev/S3/Slicer-build/UseSlicer.cmake:148 (find_package)
  CMakeLists.txt:17 (include)


CMake Error at C:/Dev/S3/VTKv9/CMake/FindPythonLibs.cmake:127 (get_filename_component):
  get_filename_component called with incorrect number of arguments
Call Stack (most recent call first):
  C:/Dev/S3/CTK/Utilities/CMake/FindPythonQt.cmake:7 (find_package)
  C:/Dev/S3/Slicer-build/UseSlicer.cmake:148 (find_package)
  CMakeLists.txt:17 (include)


Checking to see if CXX compiler accepts flag -features=no%anachronisms
Checking to see if CXX compiler accepts flag -features=no%anachronisms - No
Adding ConfigureAdditionalLauncherSettings target
Adding ConfigureAdditionalLauncherSettings target - yes
Setting EXTENSION_SOURCE_DIR ................: C:/Dev/RPTdose/MultiAtlasSegmentation/Mabmis/MultiAtlas
Setting EXTENSION_SUPERBUILD_BINARY_DIR .....: C:/_/MAS
Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
Setting MIDAS_PACKAGE_URL ...................: http://slicer.kitware.com/midas3
Setting MIDAS_PACKAGE_EMAIL .................: OBFUSCATED
Setting MIDAS_PACKAGE_API_KEY ...............: OBFUSCATED
Setting EXTENSION_SVNUSERNAME ...............: NOT DEFINED
Setting EXTENSION_SVNPASSWORD ...............: NOT DEFINED
Setting EXTENSION_DEPENDS ...................: NA
Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
Setting EXTENSION_HOMEPAGE ..................: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensi [...]
Setting EXTENSION_CONTRIBUTORS ..............: Xiaofeng Liu (GE GLobal Research), Minjeong Kim (UNC), Dinggang Shen (UNC [...]
Setting EXTENSION_CATEGORY ..................: Segmentation
Setting EXTENSION_ICONURL ...................: http://wiki.slicer.org/slicerWiki/images/e/e2/MABMIS_Icon.png
Setting EXTENSION_DESCRIPTION ...............: Multi-Atlas Based Group Segmentation
Setting EXTENSION_SCREENSHOTURLS ............: http://wiki.slicer.org/slicerWiki/images/2/2c/MABMIS_trainning_GUI.png ht [...]
Setting EXTENSION_ENABLED ...................: 1
Setting EXTENSION_STATUS ....................: NOT DEFINED
Setting default for EXTENSION_STATUS ........: 
Found Git: C:/Program Files/Git/bin/git.exe  
Found Subversion: C:/Program Files/TortoiseSVN/bin/svn.exe (found version "1.9.5") 
Configuring SEM CLI module: IGR3D_MABMIS_Training
ITKCommonitksysitkvnl_algoitkvnlitkv3p_netlibitknetlibitkvclITKIOXMLITKIOImageBaseITKEXPAT
Configuring SEM CLI module: IGR3D_MABMIS_Testing
C:/_/MAS/Testing
C:/Dev/RPTdose/MultiAtlasSegmentation/Mabmis/MultiAtlas/Testing
Configuring directory C:/_/MAS/Testing/../Testing/Temporary/
Configuring file AA_cbq_000.nii.gz
Configuring file AA_seg_000.nii.gz
Configuring file AB_cbq_000.nii.gz
Configuring file AB_seg_000.nii.gz
Configuring file AC_cbq_000.nii.gz
Configuring file AC_seg_000.nii.gz
Configuring file AD_cbq_000.nii.gz
Configuring file AD_seg_000.nii.gz
Configuring file TrainingData.xml
Configuring directory C:/_/MAS/Testing/../Testing/Temporary/TrainedAtlas/
Configuring file 000_to_003_cbq_reg.nii.gz
Configuring file 000_to_003_deform_000.ni_sub.nii.gz
Configuring file 000_to_003_deform_000.nii.gz
Configuring file 001_to_003_cbq_reg.nii.gz
Configuring file 001_to_003_deform_000.ni_sub.nii.gz
Configuring file 001_to_003_deform_000.nii.gz
Configuring file 002_to_003_cbq_reg.nii.gz
Configuring file 002_to_003_deform_000.ni_sub.nii.gz
Configuring file 002_to_003_deform_000.nii.gz
Configuring file 003_to_000_cbq_000.nii.gz
Configuring file 003_to_000_cbq_reg.nii.gz
Configuring file 003_to_000_deform_000.nii.gz
Configuring file 003_to_001_cbq_000.nii.gz
Configuring file 003_to_001_cbq_reg.nii.gz
Configuring file 003_to_001_deform_000.nii.gz
Configuring file 003_to_002_cbq_000.nii.gz
Configuring file 003_to_002_cbq_reg.nii.gz
Configuring file 003_to_002_deform_000.nii.gz
Configuring file AA_cbq_000.nii.gz
Configuring file AA_seg_000.nii.gz
Configuring file AB_cbq_000.nii.gz
Configuring file AB_seg_000.nii.gz
Configuring file AC_cbq_000.nii.gz
Configuring file AC_seg_000.nii.gz
Configuring file AD_cbq_000.nii.gz
Configuring file AD_seg_000.nii.gz
Configuring file simulated_cbq_000.nii.gz
Configuring file simulated_cbq_001.nii.gz
Configuring file simulated_cbq_002.nii.gz
Configuring file simulated_cbq_003.nii.gz
Configuring file simulated_cbq_004.nii.gz
Configuring file simulated_cbq_005.nii.gz
Configuring file simulated_cbq_006.nii.gz
Configuring file simulated_cbq_007.nii.gz
Configuring file simulated_deform_000.nii.gz
Configuring file simulated_deform_001.nii.gz
Configuring file simulated_deform_002.nii.gz
Configuring file simulated_deform_003.nii.gz
Configuring file simulated_deform_004.nii.gz
Configuring file simulated_deform_005.nii.gz
Configuring file simulated_deform_006.nii.gz
Configuring file simulated_deform_007.nii.gz
Configuring directory C:/_/MAS/Testing/../Testing/Temporary/TestData/
Configuring file .gitignore
Configuring file TestData.xml
Configuring file UA_cbq_000.nii.gz
Configuring file UB_cbq_000.nii.gz
Configuring file VA_cbq_000.nii.gz
Configuring file VB_cbq_000.nii.gz
Extension description has been written to: C:/_/MAS/MABMIS.s4ext
Checking if extension type is SuperBuild
Checking if extension type is SuperBuild - false
Setting 'CTEST_MODEL' variable with default value 'Experimental'
Configuring incomplete, errors occurred!
See also "C:/_/MAS/CMakeFiles/CMakeOutput.log".
See also "C:/_/MAS/CMakeFiles/CMakeError.log".
</code></pre>

---

## Post #2 by @dzenanz (2017-12-20 23:24 UTC)

<p>This might be due to some issues with git-python. I will do a clean build overnight.</p>

---

## Post #3 by @dzenanz (2017-12-21 14:58 UTC)

<p>Doing a clean build using visual studio gets rid of the error.</p>

---
