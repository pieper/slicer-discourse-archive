---
topic_id: 14050
title: "Failed To Build 3D Slicer In Ubuntu 18 04"
date: 2020-10-15
url: https://discourse.slicer.org/t/14050
---

# failed to build 3D Slicer in Ubuntu 18.04

**Topic ID**: 14050
**Date**: 2020-10-15
**URL**: https://discourse.slicer.org/t/failed-to-build-3d-slicer-in-ubuntu-18-04/14050

---

## Post #1 by @Shun_Yao (2020-10-15 03:37 UTC)

<p>Dear experts in Slicer community,<br>
I am a doctor and a fun of Slicer (not too much background of computer science). I am trying to build Slicer in my new PC for the convenience of working on a large data set using streamline code.<br>
However, I got errors and can’t figure it out when I am building Slicer according the steps from here <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa</a>.<br>
Any comments are appreciated.</p>
<p>My PC configurations:<br>
system: Ubuntu 18.04<br>
CPU: Intel® Core™ i9-9900 CPU @ 3.10GHz<br>
Memory: 32 G<br>
Python 3.7.9</p>
<p><strong>ERROR shows below:</strong></p>
<p>[ 10%] Python Wrapping - generating vtkOpenGLShaderComputationPython.cxx<br>
Scanning dependencies of target vtkTeemPythonD<br>
Scanning dependencies of target vtkAddonPythonD<br>
/usr/lib/x86_64-linux-gnu/libSM.so: undefined reference to <code>uuid_generate@UUID_1.0' /usr/lib/x86_64-linux-gnu/libSM.so: undefined reference to </code>uuid_unparse_lower@UUID_1.0’<br>
collect2: error: ld returned 1 exit status<br>
Libs/vtkTeem/Testing/CMakeFiles/vtkTeemCxxTests.dir/build.make:200: recipe for target ‘bin/vtkTeemCxxTests’ failed<br>
make[5]: *** [bin/vtkTeemCxxTests] Error 1<br>
CMakeFiles/Makefile2:9178: recipe for target ‘Libs/vtkTeem/Testing/CMakeFiles/vtkTeemCxxTests.dir/all’ failed<br>
make[4]: *** [Libs/vtkTeem/Testing/CMakeFiles/vtkTeemCxxTests.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…<br>
[ 10%] Building CXX object Libs/vtkTeem/CMakeFiles/vtkTeemPythonD.dir/vtkDiffusionTensorGlyphPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkTeem/CMakeFiles/vtkTeemPythonD.dir/vtkDiffusionTensorMathematicsPython.cxx.o<br>
[ 10%] Linking CXX shared library …/…/…/lib/Slicer-4.13/cli-modules/libResampleScalarVolumeLib.so<br>
[ 10%] Linking CXX executable …/…/…/bin/vtkAddonCxxTests<br>
[ 10%] Building CXX object Libs/vtkTeem/CMakeFiles/vtkTeemPythonD.dir/vtkTeemNRRDReaderPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkTeem/CMakeFiles/vtkTeemPythonD.dir/vtkTeemNRRDWriterPython.cxx.o<br>
/usr/lib/x86_64-linux-gnu/libSM.so: undefined reference to <code>uuid_generate@UUID_1.0' /usr/lib/x86_64-linux-gnu/libSM.so: undefined reference to </code>uuid_unparse_lower@UUID_1.0’<br>
collect2: error: ld returned 1 exit status<br>
Libs/vtkAddon/Testing/CMakeFiles/vtkAddonCxxTests.dir/build.make:239: recipe for target ‘bin/vtkAddonCxxTests’ failed<br>
make[5]: *** [bin/vtkAddonCxxTests] Error 1<br>
CMakeFiles/Makefile2:9041: recipe for target ‘Libs/vtkAddon/Testing/CMakeFiles/vtkAddonCxxTests.dir/all’ failed<br>
make[4]: *** [Libs/vtkAddon/Testing/CMakeFiles/vtkAddonCxxTests.dir/all] Error 2<br>
[ 10%] Building CXX object Libs/vtkTeem/CMakeFiles/vtkTeemPythonD.dir/vtkImageLabelCombinePython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkAddonTestingUtilitiesPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkErrorSinkPython.cxx.o<br>
[ 10%] Built target ResampleScalarVolumeLib<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkLoggingMacrosPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkTestingOutputWindowPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkTeem/CMakeFiles/vtkTeemPythonD.dir/vtkTeemPythonInitImpl.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkOrientedBSplineTransformPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkOrientedGridTransformPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkPersonInformationPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkAddonMathUtilitiesPython.cxx.o<br>
[ 10%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkAddonSetGetPython.cxx.o<br>
[ 11%] Linking CXX shared library …/…/bin/libvtkTeemPythonD.so<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkStreamingVolumeCodecPython.cxx.o<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkStreamingVolumeFramePython.cxx.o<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkStreamingVolumeCodecFactoryPython.cxx.o<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkRawRGBVolumeCodecPython.cxx.o<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkOpenGLTextureImagePython.cxx.o<br>
[ 11%] Built target vtkTeemPythonD<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkOpenGLShaderComputationPython.cxx.o<br>
[ 11%] Building CXX object Libs/vtkAddon/CMakeFiles/vtkAddonPythonD.dir/vtkAddonPythonInitImpl.cxx.o<br>
[ 11%] Linking CXX shared library …/…/bin/libvtkAddonPythonD.so<br>
[ 11%] Built target vtkAddonPythonD<br>
[ 11%] Linking CXX shared library …/…/…/lib/Slicer-4.13/cli-modules/libExpertAutomatedRegistrationLib.so<br>
[ 11%] Built target ExpertAutomatedRegistrationLib<br>
[ 11%] Linking CXX static library …/…/…/lib/Slicer-4.13/libBRAINSCommonLib.a<br>
[ 11%] Built target BRAINSCommonLib<br>
Makefile:181: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/Slicer.dir/build.make:162: recipe for target ‘Slicer-prefix/src/Slicer-stamp/Slicer-build’ failed<br>
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2<br>
CMakeFiles/Makefile2:454: recipe for target ‘CMakeFiles/Slicer.dir/all’ failed<br>
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2<br>
Makefile:113: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>

---

## Post #2 by @lassoan (2020-10-15 03:40 UTC)

<p>You don’t need to build Slicer to use it, customize, or extend it. See more information here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html</a></p>
<p>Anyway, these build instructions should work: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html</a> (I’ve tried Ubuntu 20.04 build instructions a couple of weeks ago).</p>

---

## Post #3 by @Shun_Yao (2020-10-15 04:03 UTC)

<p>Hi Lassoan,<br>
Many thanks for your flash reply!<br>
Best,<br>
SY</p>

---
