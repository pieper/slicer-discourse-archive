# Build error: class vtkCellPicker has no member named Pick3DPoint

**Topic ID**: 4141
**Date**: 2018-09-18
**URL**: https://discourse.slicer.org/t/build-error-class-vtkcellpicker-has-no-member-named-pick3dpoint/4141

---

## Post #1 by @zhaobingshuai (2018-09-18 12:59 UTC)

<p><strong>make -j4</strong>        when i use this command,i meet the following error:</p>
<p>[ 33%] Linking CXX shared library …/…/bin/libSlicerBaseLogicPythonD.so<br>
Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/build.make:75: recipe for target ‘Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/vtkMRMLModelDisplayableManager.cxx.o’ failed<br>
make[5]: *** [Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/vtkMRMLModelDisplayableManager.cxx.o] Error 1<br>
CMakeFiles/Makefile2:1725: recipe for target ‘Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/all’ failed<br>
make[4]: *** [Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…<br>
[ 34%] Built target SlicerBaseLogicPythonD<br>
Copying XML file ‘PETStandardUptakeValueComputation.xml’ along side the executable<br>
[ 34%] Built target PETStandardUptakeValueComputation<br>
[ 34%] Built target ModelMakerLib<br>
Makefile:151: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/Slicer.dir/build.make:143: recipe for target ‘Slicer-prefix/src/Slicer-stamp/Slicer-build’ failed<br>
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2<br>
CMakeFiles/Makefile2:103: recipe for target ‘CMakeFiles/Slicer.dir/all’ failed<br>
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2<br>
Makefile:83: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>
<p><strong>make</strong>         when i use this command,i meet the following error:</p>
<p>[ 28%] Building CXX object Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/vtkMRMLModelDisplayableManager.cxx.o<br>
/home/zbs/Slicer/Libs/MRML/DisplayableManager/vtkMRMLModelDisplayableManager.cxx: In member function ‘virtual int vtkMRMLModelDisplayableManager::Pick3D(double*)’:<br>
/home/zbs/Slicer/Libs/MRML/DisplayableManager/vtkMRMLModelDisplayableManager.cxx:1881:35: error: ‘class vtkCellPicker’ has no member named ‘Pick3DPoint’<br>
if (this-&gt;Internal-&gt;CellPicker-&gt;Pick3DPoint(ras, ren))<br>
^<br>
Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/build.make:75: recipe for target ‘Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/vtkMRMLModelDisplayableManager.cxx.o’ failed<br>
make[5]: *** [Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/vtkMRMLModelDisplayableManager.cxx.o] Error 1<br>
CMakeFiles/Makefile2:1725: recipe for target ‘Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/all’ failed<br>
make[4]: *** [Libs/MRML/DisplayableManager/CMakeFiles/MRMLDisplayableManager.dir/all] Error 2<br>
Makefile:151: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/Slicer.dir/build.make:143: recipe for target ‘Slicer-prefix/src/Slicer-stamp/Slicer-build’ failed<br>
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2<br>
CMakeFiles/Makefile2:103: recipe for target ‘CMakeFiles/Slicer.dir/all’ failed<br>
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2<br>
Makefile:83: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>
<p>i have repeat many times, i can’t find solution via intertet . so ,i need help, who can tell me what should i do ?  please!!!</p>

---

## Post #2 by @lassoan (2018-09-18 13:13 UTC)

<p>Thanks for reporting this. It seems that you’ve forced Slicer to build with an old VTK version (or you have a build tree that was created before Slicer switched VTK version).</p>
<p>Slicer master requires Q5/VTK9 as described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build instructions</a>.</p>
<p>Occasionally we still fix build errors with VTK7/Qt4 to make transition easier, but after release of Slicer-4.10 (within a few weeks), master version will not be compatible VTK7/Qt4 anymore. Therefore, it is recommended to update your build environment as soon as you can.</p>

---
