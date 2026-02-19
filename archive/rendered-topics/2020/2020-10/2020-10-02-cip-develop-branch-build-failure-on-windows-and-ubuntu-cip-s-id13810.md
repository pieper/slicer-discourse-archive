---
topic_id: 13810
title: "Cip Develop Branch Build Failure On Windows And Ubuntu Cip S"
date: 2020-10-02
url: https://discourse.slicer.org/t/13810
---

# CIP develop branch build failure on windows and ubuntu(CIP, slicer)

**Topic ID**: 13810
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/cip-develop-branch-build-failure-on-windows-and-ubuntu-cip-slicer/13810

---

## Post #1 by @akshay_pillai (2020-10-02 01:07 UTC)

<p>Hello,</p>
<p>I have been trying to build CIP on my windows computer with the develop branch. I have tried different versions of cmake including 3.5.2, 3.5, 3.15, and also tried different versions of gcc such as gcc 5.4, 7.4, 8.1. But I have not been able to successfully build it. I have also tried using the ubuntu WSL with ubuntu 18.04, 16.04 also with different cmake and gcc versions. It always keeps erroring out. Please let me know what I can do to solve this. Here is the error that I get:</p>
<p>HEAD is now at 31dc6a08b8 BUG: Ensure VTK_PYTHON_SITE_PACKAGES_SUFFIX is set in vtkInitializeWrapPython<br>
Submodule ‘VTK-m’ (<a href="https://gitlab.kitware.com/vtk/vtk-m.git" rel="noopener nofollow ugc">https://gitlab.kitware.com/vtk/vtk-m.git</a>) registered for path ‘ThirdParty/vtkm/vtk-m’<br>
Cloning into ‘C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/vtkm/vtk-m’…<br>
Updating files: 100% (8/8), done.<br>
Already on ‘master’<br>
process_begin: CreateProcess(NULL, CIPPython-install\Scripts\conda install --yes -c conda-forge nipype==0.12.1, …) failed.<br>
make (e=2): The system cannot find the file specified.<br>
make[2]: *** [CIPPython-prefix/src/CIPPython-stamp/CIPPython-installnipype] Error 2<br>
make[1]: *** [CMakeFiles/CIPPython.dir/all] Error 2<br>
make[1]: *** Waiting for unfinished jobs…<br>
In file included from C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/lzma/vtklzma/src/liblzma/common/common.h:19:0,<br>
from C:\Users\pilht4\Desktop\CIP\ChestImagingPlatform-build\VTKv8\ThirdParty\lzma\vtklzma\src\liblzma\check\check.h:16,<br>
from C:\Users\pilht4\Desktop\CIP\ChestImagingPlatform-build\VTKv8\ThirdParty\lzma\vtklzma\src\liblzma\check\check.c:13:<br>
C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/lzma/vtklzma/src/common/mythread.h:138:33: error: unknown type name ‘sigset_t’<br>
mythread_sigmask(int how, const sigset_t *restrict set,<br>
^<br>
C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/lzma/vtklzma/src/common/mythread.h:139:3: error: unknown type name ‘sigset_t’<br>
sigset_t *restrict oset)<br>
^<br>
C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/lzma/vtklzma/src/common/mythread.h: In function ‘mythread_create’:<br>
C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/lzma/vtklzma/src/common/mythread.h:158:2: error: unknown type name ‘sigset_t’<br>
sigset_t old;<br>
^<br>
C:/Users/pilht4/Desktop/CIP/ChestImagingPlatform-build/VTKv8/ThirdParty/lzma/vtklzma/src/common/mythread.h:159:2: error: unknown type name ‘sigset_t’<br>
sigset_t all;<br>
^<br>
make[5]: *** [ThirdParty/lzma/vtklzma/CMakeFiles/vtklzma.dir/src/liblzma/check/check.c.obj] Error 1<br>
make[4]: *** [ThirdParty/lzma/vtklzma/CMakeFiles/vtklzma.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…<br>
CMakeFiles\vtkglew.dir/objects.a(glew.c.obj):glew.c:(.text+0x16ea0): multiple definition of `DllMainCRTStartup’<br>
C:/ProgramData/chocolatey/lib/mingw/tools/install/mingw64/bin/…/lib/gcc/x86_64-w64-mingw32/5.4.0/…/…/…/…/x86_64-w64-mingw32/lib/…/lib/dllcrt2.o:crtdll.c:(.text+0x3e0): first defined here<br>
collect2.exe: error: ld returned 1 exit status<br>
make[5]: *** [bin/libvtkglew-8.2.dll] Error 1<br>
make[4]: *** [ThirdParty/glew/vtkglew/CMakeFiles/vtkglew.dir/all] Error 2<br>
make[3]: *** [all] Error 2<br>
make[2]: *** [VTKv8-prefix/src/VTKv8-stamp/VTKv8-build] Error 2<br>
make[1]: *** [CMakeFiles/VTKv8.dir/all] Error 2<br>
make: *** [all] Error 2</p>
<p>Also attached is the cmakeOutputLog.<br>
<a href="https://github.com/acil-bwh/ChestImagingPlatform/files/5313175/CMakeOutput.log" rel="noopener nofollow ugc">cmakeoutput file</a></p>
<p>Please let me know if there are any solutions to this issue. Any help is appreciated. If anyone has built on windows please let me know what steps to follow. Thank you.</p>

---

## Post #2 by @lassoan (2020-10-02 23:52 UTC)

<p>We are switching to a new VTK version and build errors are expected on the master. You can either wait a few days until we resolve the issues or you build master from a few days ago (Sep 29 or so should work).</p>

---
