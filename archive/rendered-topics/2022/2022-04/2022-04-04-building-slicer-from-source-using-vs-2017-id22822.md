# Building Slicer from source using VS 2017

**Topic ID**: 22822
**Date**: 2022-04-04
**URL**: https://discourse.slicer.org/t/building-slicer-from-source-using-vs-2017/22822

---

## Post #1 by @cay18 (2022-04-04 15:02 UTC)

<p>Hello, I am a beginner programmer and need to build Slicer from source using VS 2017 for my project. The build instructions mention:</p>
<p>“ Visual Studio 2017 (v141) toolset is not tested anymore but probably still works. Qt-5.15.2 requires v142 redistributables, so either these extra DLL files need to be added to the installation package or each user may need to install “Microsoft Visual C++ Redistributable” package.”</p>
<p>Could someone explain what these DLL files are and how I could include them? How do I use v142 toolset for VS 2017?</p>
<p>Thank you!</p>

---

## Post #2 by @jamesobutler (2022-04-04 15:20 UTC)

<p>Redistributables are available for download at <a href="https://visualstudio.microsoft.com/downloads/" class="inline-onebox" rel="noopener nofollow ugc">Download Visual Studio Tools - Install Free for Windows, Mac, Linux</a> or <a href="https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170" class="inline-onebox" rel="noopener nofollow ugc">Latest supported Visual C++ Redistributable downloads | Microsoft Learn</a>.</p>
<blockquote>
<p>Visual Studio versions since Visual Studio 2015 share the same redistributable files. For example, any apps built by the Visual Studio 2015, 2017, 2019, or 2022 toolsets can use the latest Microsoft Visual C++ Redistributable. However, the version of the Microsoft Visual C++ redistributable installed on the machine must be the same or higher than the version of the Visual C++ toolset used to create your application.</p>
</blockquote>
<p>However, why do you need to build from source using VS 2017? If you have binaries compiled with the VS 2017 v141 toolset you can still compile the application built with later versions of the toolset such as for 2019 or 2022. Visual Studio 2022 has install options that lets you use either the v143 toolset corresponding to 2022 or even the v141 toolset to build it as though it was Visual Studio 2017. See <a href="https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-170" class="inline-onebox" rel="noopener nofollow ugc">C++ binary compatibility 2015-2022 | Microsoft Learn</a>.</p>
<blockquote>
<p>(The toolset version is v140 for Visual Studio 2015, v141 for 2017, v142 for 2019, and v143 for 2022). Say you have third-party libraries built by Visual Studio 2015. You can still use them in an application built by Visual Studio 2017, 2019, or 2022. There’s no need to recompile with a matching toolset.</p>
</blockquote>

---

## Post #3 by @cay18 (2022-04-05 06:06 UTC)

<p>Thanks for your help. I downloaded the redistributables and tried building using command line:</p>
<pre><code class="lang-auto">cd /d C:\D\S4R
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 15 2017" -A x64 -DQt5_DIR:PATH=C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 C:\D\S4\Slicer
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release

</code></pre>
<p>I get these errors with VTK:</p>
<pre><code class="lang-auto">C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(328): error C2065: 'max': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(328): error C2275: 'vtkIdType': illegal use of this type as an expression [C
:\D\S4R\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    c:\d\s4r\vtk\common\core\vtkType.h(315): note: see declaration of 'vtkIdType'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(328): error C2039: 'min': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(328): error C2065: 'min': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(331): error C2039: 'max': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(331): error C2065: 'max': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(331): error C2275: 'vtkIdType': illegal use of this type as an expression [C
:\D\S4R\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    c:\d\s4r\vtk\common\core\vtkType.h(315): note: see declaration of 'vtkIdType'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(425): error C2039: 'max': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(425): error C2065: 'max': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(425): error C2275: 'vtkIdType': illegal use of this type as an expression [C
:\D\S4R\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    c:\d\s4r\vtk\common\core\vtkType.h(315): note: see declaration of 'vtkIdType'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(425): error C2039: 'min': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(425): error C2065: 'min': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(426): error C2039: 'max': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(426): error C2065: 'max': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(426): error C2275: 'vtkIdType': illegal use of this type as an expression [C
:\D\S4R\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    c:\d\s4r\vtk\common\core\vtkType.h(315): note: see declaration of 'vtkIdType'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(491): error C2039: 'max': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(491): error C2065: 'max': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(491): error C2275: 'vtkIdType': illegal use of this type as an expression [C
:\D\S4R\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    c:\d\s4r\vtk\common\core\vtkType.h(315): note: see declaration of 'vtkIdType'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(491): error C2039: 'min': is not a member of 'std' [C:\D\S4R\VTK-build\Commo
n\DataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\functional(23): not
  e: see declaration of 'std'
C:\D\S4R\VTK\Common\DataModel\vtkTable.cxx(491): error C2065: 'min': undeclared identifier [C:\D\S4R\VTK-build\Common\D
ataModel\CommonDataModel-objects.vcxproj] [C:\D\S4R\VTK.vcxproj]
</code></pre>
<p>Is there a way to resolve these errors without upgrading to VS 2019 or 2022? I am using VS 2017 as it is required for the project by my supervisor. Thanks!</p>

---

## Post #4 by @lassoan (2022-04-05 21:30 UTC)

<p>Are you trying to build the latest Slicer master version? If not, then try that.</p>
<p>If that does not help then please try to fix these build errors on your computer.</p>
<ul>
<li>If adding a few <code>#include</code>s fix everything then let’s just do that (we may even integrate those changes int Slicer master).</li>
<li>If you run into more complicated errors due to unsupported C++ features then it may worth discussing the VS2017 requirement with your supervisor. You can invite him to this discussion.</li>
</ul>

---

## Post #5 by @cay18 (2022-04-11 02:44 UTC)

<p>Yes, I am trying to build the latest slicer version. It works after adding #include&lt; algorithm &gt; to vtkDatatable.cxx. Thank you for your help!</p>

---
