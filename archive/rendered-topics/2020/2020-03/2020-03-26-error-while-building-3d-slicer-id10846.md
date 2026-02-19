---
topic_id: 10846
title: "Error While Building 3D Slicer"
date: 2020-03-26
url: https://discourse.slicer.org/t/10846
---

# Error while building 3D Slicer

**Topic ID**: 10846
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/error-while-building-3d-slicer/10846

---

## Post #1 by @alankrutha (2020-03-26 13:20 UTC)

<p>Hi Team,</p>
<p>I’m facing issue while compiling 3d Slicer source code.</p>
<p>Gave make and below are last 30 lines of compilation log.</p>
<p>[ 81%] Built target SimpleITK_ITKImageFunction<br>
[ 81%] Building CXX object Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKImageGrid.dir/sitkResampleImageFilter.cxx.o<br>
c++: internal compiler error: Killed (program cc1plus)<br>
Please submit a full bug report,<br>
with preprocessed source if appropriate.<br>
See &lt;file:///usr/share/doc/gcc-5/README.Bugs&gt; for instructions.<br>
Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKImageGrid.dir/build.make:192: recipe for target ‘Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKImageGrid.dir/sitkResampleImageFilter.cxx.o’ failed<br>
make[8]: *** [Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKImageGrid.dir/sitkResampleImageFilter.cxx.o] Error 4<br>
CMakeFiles/Makefile2:1721: recipe for target ‘Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKImageGrid.dir/all’ failed<br>
make[7]: *** [Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKImageGrid.dir/all] Error 2<br>
Makefile:151: recipe for target ‘all’ failed<br>
make[6]: *** [all] Error 2<br>
CMakeFiles/SimpleITK.dir/build.make:114: recipe for target ‘SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-build’ failed<br>
make[5]: *** [SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-build] Error 2<br>
CMakeFiles/Makefile2:209: recipe for target ‘CMakeFiles/SimpleITK.dir/all’ failed<br>
make[4]: *** [CMakeFiles/SimpleITK.dir/all] Error 2<br>
Makefile:83: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/SimpleITK.dir/build.make:115: recipe for target ‘SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-build’ failed<br>
make[2]: *** [SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-build] Error 2<br>
CMakeFiles/Makefile2:1621: recipe for target ‘CMakeFiles/SimpleITK.dir/all’ failed<br>
make[1]: *** [CMakeFiles/SimpleITK.dir/all] Error 2<br>
Makefile:94: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>
<p>Kindly do the needful.</p>
<p>Thanks,<br>
Alankrutha</p>

---

## Post #2 by @gcsharp (2020-03-26 13:47 UTC)

<p>You might have ran out of RAM.  Assuming you are running a parallel make, you might try using fewer parallel processes.</p>

---
