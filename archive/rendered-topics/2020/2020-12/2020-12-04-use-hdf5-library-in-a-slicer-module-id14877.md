# Use HDF5 library in a Slicer module

**Topic ID**: 14877
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/use-hdf5-library-in-a-slicer-module/14877

---

## Post #1 by @keri (2020-12-04 02:11 UTC)

<p>Hi,</p>
<p>Is it possible to build Slicer with custom HDF5 library? I mean I would like to build HDF5 separetely from SLicer<br>
I can see that VTK and ITK somehow use it but there is no <code>hdf5_D.lib</code> or <code>hdf5_hl_D.lib</code> in Slicer build dir (<code>VTK-build</code> and <code>ITK-build</code> folders)</p>
<p>For now when I try to use my custom HDF5 lib in my loadable module I get link errors like:<br>
<strong>h5core.obj:-1: error: LNK2019: unresolved external symbol itk_H5open referenced in function “public: __cdecl HighFive::AtomicType::AtomicType(void)” (??0?$AtomicType@H@HighFive@<span class="mention">@QEAA</span>@XZ) [C:\S\extensions\build-MSV-Qt_msvc2019_64-Debug\MSVCore\msvcore.vcxproj]</strong></p>
<p>I use HighFive C++ wrapper for HDF5</p>

---

## Post #2 by @lassoan (2020-12-04 03:04 UTC)

<p>Slicer does not use HDF5 directly, only via its dependent libraries - ITK and VTK. You should be able to pass down your custom HDF5 library the same way as it is done for zlib (check out *.cmake files in the SuperBuild folder), but you would only need to do this if you wanted ITK and VTK to use your custom HDF5, which is probably not what you need.</p>
<p>If you want your module to use custom HDF5 then you can build your custom HDF5 along with other modules and libraries in your extension (you can use the superbuild extension template). Both ITK and VTK use name mangling when building HDF, so there will be no conflicts.</p>
<p>I’m just curious, why do you need to use a custom HDF5 library?</p>

---

## Post #3 by @keri (2020-12-04 04:03 UTC)

<p>Thank you for explaination</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m just curious, why do you need to use a custom HDF5 library?</p>
</blockquote>
</aside>
<p>I’m sorry I confused you. The word <strong>custom</strong> is inapropriate.<br>
I need HDF5 library configured with almost any CMake settings. I would like to try to use the same HDF5 library that VTK or ITK uses but I didn’t find HDF5 library with names something like <code>hdf5_D.lib</code> in VTK-build and ITK-build subfolders.</p>
<p>I have written some small <strong>core</strong> shared lib that uses HDF5 via <a href="https://github.com/BlueBrain/HighFive" rel="noopener nofollow ugc">HighFive wrapper header only C++ library</a>. As I’m not going to display this <strong>core</strong> in <strong>Slicer app</strong> and in the same time many of my loadable modules use this <strong>core</strong>, I decided to make this <strong>core</strong> as a subfolder in my extension and <strong>not to make</strong> a module from this <strong>core</strong>. And modules of this extension simply links to this <strong>core</strong>.<br>
When I build this I get many errors like this:<br>
<strong>h5core.obj:-1: error: LNK2019: unresolved external symbol itk_H5open referenced in function “public: __cdecl HighFive::AtomicType::AtomicType(void)” (??0?$AtomicType@H@HighFive@<span class="mention">@QEAA</span>@XZ) [C:\S\extensions\build-MSV-Qt_msvc2019_64-Debug\MSVCore\msvcore.vcxproj]</strong></p>
<p>I decided that the problem is that VTK and ITK uses HDF5 libs and I also include <strong>static</strong> <code>libhdf5_D.lib</code> and <code>libhdf5_hl_D.lib</code></p>
<p>Well the problem is that I can’t link HDF5 to my <strong>core</strong> shared lib which is subfolder of extension and there is some custom HDF5, probably I would like to use one of the latest HDF5 lib</p>

---

## Post #4 by @lassoan (2020-12-04 05:32 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="14877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>modules of this extension simply links to this <strong>core</strong> .<br>
When I build this I get many errors like this:<br>
<strong>h5core.obj:-1: error: LNK2019: unresolved external symbol itk_H5open referenced in function “public: __cdecl HighFive::AtomicType::AtomicType(void)” (??0?$AtomicType@H@HighFive@<span class="mention">@QEAA</span>@XZ) [C:\S\extensions\build-MSV-Qt_msvc2019_64-Debug\MSVCore\msvcore.vcxproj]</strong></p>
</blockquote>
</aside>
<p>Probably you just need to link ITK’s HDF5 library to your target. In general, if you use ITK’s or VTK’s name-mangled HDF5 then you need to link the corresponding ITK/VTK library.</p>
<p>If ITK/VTK is built so that HDF5 library is not exported as a publicly usable target outside ITK/VTK then you can build any HDF5 library implementation yourself, as part of your extension superbuild, and use that. See for example <a href="https://github.com/Slicer/SlicerJupyter/tree/master/SuperBuild">SlicerJupyter extension</a>, which builds and uses several third-party libraries.</p>

---

## Post #5 by @keri (2020-12-05 19:43 UTC)

<p>Thank you for information.</p>
<p>As I’m studying Slicer I’m trying now to simply build HDF5 lib with SuperBuild. So to do this I guess I should work only with CMake. Is there the simplest example showing how to build third party C++ external library with Slicer superbuild?<br>
I tried to follow the example you gave with Slicer Jupiter but somehow my code doesn’t launch build step for HDF5 even if in general build is succesfull.</p>

---

## Post #6 by @lassoan (2020-12-05 20:33 UTC)

<p>SlicerRT extension is a simpler example: <a href="https://github.com/SlicerRt/SlicerRT/tree/master/SuperBuild">https://github.com/SlicerRt/SlicerRT/tree/master/SuperBuild</a></p>

---

## Post #7 by @keri (2020-12-06 05:35 UTC)

<p>Thank you. I’ve found my mistake. I should have been look more precisely at <code>ExternalProject_Add(...)</code> CMake parameters.</p>
<p>Now inside my module the command <code>find_package(hdf5 REQUIRED)</code> fails with error:</p>
<p><em>CMake Error at C:/S/extensions/Proba-build/HDF5-build/hdf5-config.cmake:25 (message):    File or directory C:/S/extensions/bin referenced by variable HDF5_TOOLS_DIR    does not exist !</em></p>
<p>Here <em>C:/S/extensions/bin</em> should be <em>C:\S\extensions\Proba-build\HDF5-build\tools</em> but I can’t understand why it points to wrong directory. If you had some experience of superbuild <code>HDF5</code> did you encounter similar error?<br>
I use <code>hdf5-1_12_0</code> git tag, tomorrow I will try some other tag</p>

---

## Post #8 by @lassoan (2020-12-06 05:52 UTC)

<p>If you send a link to your repository then somebody can have a look.</p>

---

## Post #9 by @keri (2020-12-06 06:53 UTC)

<p>Here it is the repository: <a href="https://github.com/KerimMatlab/Proba/tree/main" rel="noopener nofollow ugc">https://github.com/KerimMatlab/Proba/tree/main</a><br>
I’m ashamed that it has strange name. I just started exploring slicer and didnt think that I would create repo from this test extension</p>

---

## Post #10 by @lassoan (2020-12-06 14:33 UTC)

<p>I’ve had a look. You need to use hdf5 instead of HDF5 (this is how the library calls itself in its CMake config file) and not specify NO_MODULE when you find the package: <a href="https://github.com/KerimMatlab/Proba/pull/1/files">https://github.com/KerimMatlab/Proba/pull/1/files</a></p>

---

## Post #11 by @keri (2020-12-06 18:04 UTC)

<p>Thank you very much!</p>
<p>Now I can compile hdf5 and I’m trying to link this hdf5 to my <code>KKK</code> module.<br>
Like in the Jupiter example I tried to add <code>hdf5</code> in:</p>
<pre><code>set(MODULE_TARGET_LIBRARIES
  vtkSlicer${MODULE_NAME}ModuleLogic
  qSlicer${MODULE_NAME}ModuleWidgets
  hdf5
  )
</code></pre>
<p>But I get link error:</p>
<p><code>:- 1: error: LNK1104: cannot open file 'hdf5.lib' [C:\S\extensions\Proba_fixed\Proba-build\inner-build\KKK\qSlicerKKKModule.vcxproj] [C:\S\extensions\Proba_fixed\Proba-build\inner.vcxproj]</code></p>
<p>Probably this is beacause there no such <code>hdf5.lib</code> library (even if I flagged cmake <code>-DBUILD_SHARED_LIBS=ON</code> and <code>-DBUILD_STATIC_LIBS=ON</code>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33efb45a1e7e0d03cf4f80fc86cf3606576b4df0.png" data-download-href="/uploads/short-url/7prULf3Op4tuOoPkpU1hoToLfxe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33efb45a1e7e0d03cf4f80fc86cf3606576b4df0.png" alt="image" data-base62-sha1="7prULf3Op4tuOoPkpU1hoToLfxe" width="690" height="166" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×192 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I commited git repository</p>

---

## Post #12 by @keri (2020-12-06 20:11 UTC)

<p>I ve figured out that this error is the result of the fact that <code>find_package(hdf5 REQUIRED)</code> produces the message:</p>
<p>RUNNING KKK<br>
CMake Warning (dev) at C:/Qt/Tools/CMake_64/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:424 (message):<br>
The package name passed to <code>find_package_handle_standard_args</code> (HDF5) does<br>
not match the name of the calling package (hdf5).  This can lead to<br>
problems in calling code that expects <code>find_package</code> result variables<br>
(e.g., <code>_FOUND</code>) to follow a certain pattern.<br>
Call Stack (most recent call first):<br>
C:/Qt/Tools/CMake_64/share/cmake-3.19/Modules/FindHDF5.cmake:975 (find_package_handle_standard_args)<br>
C:/S/d/VTK/CMake/FindHDF5.cmake:9 (include)<br>
KKK/CMakeLists.txt:10 (find_package)<br>
This warning is for project developers.  Use -Wno-dev to suppress it.</p>
<p>– Could NOT find HDF5 (missing: HDF5_LIBRARIES HDF5_INCLUDE_DIRS) (found version “”)</p>
<p>In my code now there no upper case variables <code>HDF5</code> only smaller <code>hdf5</code></p>

---
