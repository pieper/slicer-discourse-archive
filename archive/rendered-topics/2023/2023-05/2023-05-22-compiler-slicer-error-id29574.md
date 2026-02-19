---
topic_id: 29574
title: "Compiler Slicer Error"
date: 2023-05-22
url: https://discourse.slicer.org/t/29574
---

# compiler slicer error

**Topic ID**: 29574
**Date**: 2023-05-22
**URL**: https://discourse.slicer.org/t/compiler-slicer-error/29574

---

## Post #1 by @ma1282029525 (2023-05-22 12:59 UTC)

<pre><code class="lang-auto">46&gt;  moc_qSlicerApplication.cpp
46&gt;E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\moc_qSlicerApplication.cpp(280,20): error C2065: “ctkQtTestingUtility”: 未声明的标识符 [E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj]
46&gt;E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\moc_qSlicerApplication.cpp(280,41): error C2065: “_r”: 未声明的标识符 [E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj]
46&gt;E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\moc_qSlicerApplication.cpp(280,50): error C2039: "testingUtility": 不是 "qSlicerApplication" 的成员 [E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj]
46&gt;E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\../../../../slicersouse/Slicer/Base/QTGUI/qSlicerApplication.h(60,34): message : 参见“qSlicerApplication”的声明 [E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj]
46&gt;E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\moc_qSlicerApplication.cpp(281,43): error C2061: 语法错误: 标识符“ctkQtTestingUtility” [E:\Slicer_all\SlicerBuild\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj]
</code></pre>
<p>I unchecked the compile test program</p>

---

## Post #2 by @jcfr (2023-05-22 13:11 UTC)

<p>To be able to assist you we would need more context about the error.</p>
<p>Scrolling up in the terminal may allows you to find more details.</p>
<p>Additionally, a lot of context is missing: version of Slicer, which compiler,  … ?</p>

---

## Post #3 by @ma1282029525 (2023-05-22 14:01 UTC)

<p>46&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
46&gt;-- Found PythonLibs: E:/Slicer_all/SlicerBuild/python-install/libs/python39.lib (found suitable version “3.9.10”, minimum required is “3.9”)<br>
46&gt;Traceback (most recent call last):<br>
46&gt;  File “”, line 1, in <br>
46&gt;AttributeError: module ‘sys’ has no attribute ‘abiflags’<br>
46&gt;-- Configuring Slicer with python 3.9<br>
46&gt;-- Configuring MRML<br>
46&gt;--   MRML_APPLICATION_NAME is Slicer<br>
46&gt;--   MRML_APPLICATION_VERSION is 0x050300<br>
46&gt;--   MRML_APPLICATION_REVISION is 31756<br>
46&gt;--   MRML_APPLICATION_SUPPORT_VERSION is 0x030000<br>
46&gt;-- Configuring library: ITKFactoryRegistration<br>
46&gt;-- ITK is setting ITKFactoryRegistration’s MSVC_RUNTIME_LIBRARY to dynamic<br>
46&gt;-- Configuring library: vtkAddon [vtkAddon_SOURCE_DIR: E:/Slicer_all/SlicerBuild/vtkAddon]<br>
46&gt;-- Found OpenGL: opengl32</p>
<p>slicer version is I don not konw （but yeastrday git colone <a href="https://github.com/Slicer/Slicer%EF%BC%89" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer）</a>  qt version is 5.15.2</p>

---

## Post #4 by @ma1282029525 (2023-05-22 14:58 UTC)

<p>compiler is visual studio 2022</p>

---

## Post #5 by @ma1282029525 (2023-05-23 11:09 UTC)

<p>What more information do you need.  cmake version is 3.23.3</p>

---

## Post #6 by @ma1282029525 (2023-05-23 14:07 UTC)

<p>Delete line 280 281 of MOC_ qSlicerApplication. CPP to successfully compile, but I want to run it in Slicer and click debug. It will compile again for a long time…, Is there a solution?</p>
<p>/* case 29: { ctkQtTestingUtility* _r = _t-&gt;testingUtility();<br>
if (_a[0]) <em>reinterpret_cast&lt; ctkQtTestingUtility</em>*&gt;(_a[0]) = std::move(_r); }  break;*/</p>

---

## Post #7 by @lassoan (2023-05-23 22:17 UTC)

<p>One build tree can only be used for either debug or release mode. If you have already built Slicer in release mode then you cannot simply switch the build mode, but you need to configure a new build folder from scratch and build in debug mode to begin with.</p>

---
