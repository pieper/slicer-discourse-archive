---
topic_id: 2482
title: "Why Do I Get Build Error Class Vtkobjexporter Has No Member"
date: 2018-03-30
url: https://discourse.slicer.org/t/2482
---

# Why do I get build error "class vtkOBJExporter has no member named SetOBJFileComment" when building Slicer against Qt4?

**Topic ID**: 2482
**Date**: 2018-03-30
**URL**: https://discourse.slicer.org/t/why-do-i-get-build-error-class-vtkobjexporter-has-no-member-named-setobjfilecomment-when-building-slicer-against-qt4/2482

---

## Post #1 by @gaoyi.cn (2018-03-30 23:00 UTC)

<p>On linux mint/ubuntu 16.04, GCC 5.4.0</p>
<p>I got error:</p>
<p>[ 24%] Building CXX object Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLProceduralColorNode.cxx.o<br>
/home/gaoyi/usr/work/namic/rls20180330/Slicer/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx: In member function ‘virtual int vtkMRMLModelStorageNode::WriteDataInternal(vtkMRMLNode*)’:<br>
/home/gaoyi/usr/work/namic/rls20180330/Slicer/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx:504:15: error: ‘class vtkOBJExporter’ has no member named ‘SetOBJFileComment’<br>
exporter-&gt;SetOBJFileComment(header.c_str());<br>
^<br>
[ 24%] Building CXX object Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLProceduralColorStorageNode.cxx.o<br>
[ 24%] Building CXX object Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLROIListNode.cxx.o<br>
Libs/MRML/Core/CMakeFiles/MRMLCore.dir/build.make:998: recipe for target ‘Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLModelStorageNode.cxx.o’ failed<br>
make[5]: *** [Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLModelStorageNode.cxx.o] Error 1<br>
make[5]: *** Waiting for unfinished jobs…<br>
CMakeFiles/Makefile2:1275: recipe for target ‘Libs/MRML/Core/CMakeFiles/MRMLCore.dir/all’ failed<br>
make[4]: *** [Libs/MRML/Core/CMakeFiles/MRMLCore.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…<br>
[ 24%] Linking CXX static library …/…/…/lib/Slicer-4.9/libBRAINSDemonWarpTemplatesLIB.a<br>
[ 24%] Built target BRAINSDemonWarpTemplatesLIB<br>
Makefile:149: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/Slicer.dir/build.make:142: recipe for target ‘Slicer-prefix/src/Slicer-stamp/Slicer-build’ failed<br>
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2<br>
CMakeFiles/Makefile2:96: recipe for target ‘CMakeFiles/Slicer.dir/all’ failed<br>
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2<br>
Makefile:83: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>
<p>Yesterday it was fine so I checked the git log, seems there are some major changes with VTK in 4ac140217b2b564c7fed7226706616d8523bb4b1</p>
<p>Thanks for any hint!</p>
<p>Best,<br>
yi</p>

---

## Post #2 by @jcfr (2018-03-30 23:14 UTC)

<p>This happens because you build Slicer against Qt4 + VTK7.</p>
<p>I suggest you build against Qt5. Simply doing a clean build passing <code>-DQt5_DIR:PATH=/path/to/lib/cmake/Qt5</code> should be sufficient.</p>
<p>That said, I will fix the error because code up to the next release (Slicer 4.10.0) that will be cut tonight or tomorrow will be the last one to support compiling against both Qt4/VTK7 and Qt5/VTK9.</p>

---

## Post #3 by @jcfr (2018-03-30 23:36 UTC)

<p>2 posts were split to a new topic: <a href="/t/should-i-build-qt-5-10-from-source-on-linux/2484">Should I build Qt 5.10 from source on Linux?</a></p>

---
