# SlicerRT built from source cannot start

**Topic ID**: 43792
**Date**: 2025-07-21
**URL**: https://discourse.slicer.org/t/slicerrt-built-from-source-cannot-start/43792

---

## Post #1 by @ferhue (2025-07-21 08:52 UTC)

<p>I’ve built Slicer and then SlicerRT from source several times in the past. I followed the online instructions.</p>
<p>In the same computer, I recently updated (via git pull) the Slicer and SlicerRT repositories to master, and then rebuilt from scratch.</p>
<p>The build of Slicer works fine, and I can start Slicer-build/Slicer without problems. The GUI shows perfectly fine, both directly within the computer as well as via ssh -X.</p>
<p>If I call directly /home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/bin/SlicerApp-real that works fine, too.</p>
<p>The build of SlicerRt works fine, however, when I now start inner-build/SlicerWithSlicerRT, (no difference if locally or via ssh -X), I get the following error:</p>
<pre><code class="lang-auto">SlicerRT_bld/inner-build$ ./SlicerWithSlicerRT 
qt.network.ssl: QSslSocket: cannot resolve SSL_get1_peer_certificate
qt.network.ssl: QSslSocket: cannot resolve EVP_PKEY_get_base_id
qt.network.ssl: QSslSocket: cannot resolve SSL_CTX_load_verify_dir
error: [/home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>so the GUI does not pop up and the program stops.</p>
<p>Note that GLX works fine, glxinfo and glxgears show the right output.</p>
<p>Could you let me know what can I do to debug this issue? Is there a way to get more verbose erro information? Some logfile to check? Any idea why this is happening?</p>

---

## Post #2 by @ferhue (2025-07-21 09:01 UTC)

<p>If I start with --verbose-module-discovery --launcher-verbose I get:</p>
<pre><code class="lang-auto">Loading module "Endoscopy"
Loading module "Markups"
Loading module "EventBroker"
Loading module "ExecutionModelTour"
Loading module "ExtensionWizard"
Loading module "ExternalBeamPlanning"
error: [/home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>I am at git commit d4a3d8ef1ccc76f49b7532b63b6bd456f8d752f0 of SlicerRt and c22540839cb55c206331579fc4757b65a2d2540a of Slicer</p>

---

## Post #3 by @ferhue (2025-07-21 11:12 UTC)

<p>If I run <code>/home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/bin/./SlicerApp-real --additional-module-paths /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-loadable-modules /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/cli-modules --no-splash --verbose-module-discovery</code></p>
<p>the GUI pops up, but with some warnings:</p>
<pre><code class="lang-auto">  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "&lt;string&gt;", line 5, in &lt;module&gt;
ModuleNotFoundError: No module named 'ctk'
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'slicer'
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'slicer'
qSlicerScriptedLoadableModuleFactory - Failed to import module "NA" python extensions
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/lib/Slicer-5.9/qt-scripted-modules/AddManyMarkupsFiducialTest.py", line 3, in &lt;module&gt;
    import ctk
....

Loading module "ExternalBeamPlanning"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules/DoseEngines/__init__.py", line 1, in &lt;module&gt;
    from .AbstractScriptedDoseEngine import *
  File "/opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules/DoseEngines/AbstractScriptedDoseEngine.py", line 2, in &lt;module&gt;
    import vtk, qt, ctk, slicer, logging
ModuleNotFoundError: No module named 'vtk'

....

</code></pre>
<p>and DICOM import and many other things are not working.</p>
<p>This looks very similar to <a href="https://discourse.slicer.org/t/2018-10-15-windows-nightly-build-unable-to-import-vtk/4403" class="inline-onebox">2018-10-15 Windows nightly build "unable to import VTK"</a> so maybe <a class="mention" href="/u/jcfr">@jcfr</a> has an idea on what’s happening.</p>

---

## Post #4 by @jamesobutler (2025-07-21 16:19 UTC)

<aside class="quote no-group" data-username="ferhue" data-post="2" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<p>c22540839cb55c206331579fc4757b65a2d2540a of Slicer</p>
</blockquote>
</aside>
<p>There has been various build issues during this recent period of dependency upgrades.</p>
<p>You may want to actually try latest Slicer <code>main</code> (<a href="https://github.com/Slicer/Slicer/commit/3f4cd76f7ee8f2137d0bf625f1de49d28cd1e36f" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix crashes caused by range-based loops over temporary Qt contai… · Slicer/Slicer@3f4cd76 · GitHub</a>) where the current factory build results are showing it to be successful (<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-07-21" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview</a>).</p>
<p>SlicerRT currently has known build errors with latest Slicer <code>main</code>. See <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3869852" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview - Build Errors</a>. So you may actually want to try latest Slicer Stable 5.8.1 if you are trying to find a configuration that can build SlicerRT successfully. See <a href="https://slicer.cdash.org/index.php?project=SlicerStable" class="inline-onebox" rel="noopener nofollow ugc">SlicerStable</a>.</p>

---

## Post #5 by @ferhue (2025-07-21 16:22 UTC)

<p>Thanks, I was actually just doing that since a couple of hours, but now I see that I get a build error in SlicerRt:</p>
<pre><code class="lang-auto">[ 29%] Building CXX object DicomRtImportExport/ConversionRules/CMakeFiles/vtkSlicerDicomRtImportExportConversionRules.dir/vtkPlanarContourToClosedSurfaceConversionRule.cxx.o
/opt/SlicerRT_src/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx: In member function ‘void vtkPlanarContourToClosedSurfaceConversionRule::TriangulateContourInterior(vtkLine*, vtkCellArray*, bool)’:
/opt/SlicerRT_src/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx:1594:23: error: no matching function for call to ‘vtkPolygon::Triangulate(vtkSmartPointer&lt;vtkIdList&gt;&amp;)’
 1594 |   polygon-&gt;Triangulate(polygonIds);
      |   ~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
In file included from /opt/SlicerRT_src/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx:34:
/opt/Slicer_bld/VTK/Common/DataModel/vtkPolygon.h:182:7: note: candidate: ‘virtual int vtkPolygon::Triangulate(int, vtkIdList*, vtkPoints*)’
  182 |   int Triangulate(int index, vtkIdList* ptIds, vtkPoints* pts) override
      |       ^~~~~~~~~~~
/opt/Slicer_bld/VTK/Common/DataModel/vtkPolygon.h:182:7: note:   candidate expects 3 arguments, 1 provided
make[5]: *** [DicomRtImportExport/ConversionRules/CMakeFiles/vtkSlicerDicomRtImportExportConversionRules.dir/build.make:92: DicomRtImportExport/ConversionRules/CMakeFiles/vtkSlicerDicomRtImportExportConversionRules.dir/vtkPlanarContourToClosedSurfaceConversionRule.cxx.o] Error 1
make[4]: *** [CMakeFiles/Makefile2:3726: DicomRtImportExport/ConversionRules/CMakeFiles/vtkSlicerDicomRtImportExportConversionRules.dir/all] Error 2
make[3]: *** [Makefile:166: all] Error 2
make[2]: *** [CMakeFiles/inner.dir/build.make:87: inner-prefix/src/inner-stamp/inner-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:896: CMakeFiles/inner.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
</code></pre>

---

## Post #6 by @chir.set (2025-07-21 16:51 UTC)

<aside class="quote no-group" data-username="ferhue" data-post="5" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<p><code> 1594 |   polygon-&gt;Triangulate(polygonIds);</code></p>
</blockquote>
</aside>
<p>You could try:</p>
<blockquote>
<p>polygon-&gt;NonDegenerateTriangulate(polygonIds);</p>
</blockquote>
<p>It seems VTK 9.5 has made this incompatible change.</p>

---

## Post #7 by @chir.set (2025-07-21 16:58 UTC)

<aside class="quote no-group" data-username="ferhue" data-post="3" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<pre><code class="lang-auto">  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'slicer'
</code></pre>
</blockquote>
</aside>
<p>I’m having that on Arch Linux too, plus other encoding error messages; I’m using this <code>brute force</code> hack:</p>
<pre><code class="lang-auto">diff --git a/Base/Python/slicer/__init__.py b/Base/Python/slicer/__init__.py
index 1443f9b7f8..fbcb831339 100644
--- a/Base/Python/slicer/__init__.py
+++ b/Base/Python/slicer/__init__.py
@@ -183,6 +183,11 @@ except ImportError as detail:
 
 import os
 import sys
+import locale
+
+# 'ANSI_X3.4-1968' codec is being enforced since july 2025.
+# Dumb but needed. Don't use getlocale(). A literal is good also.
+locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())
 
 standalone_python = "python" in str.lower(os.path.split(sys.executable)[-1])
</code></pre>
<p>If you don’t want to patch the Slicer source tree, you may update <code>__init__.py</code> in your installed tree:</p>
<p><code>./bin/Python/slicer/__init__.py</code></p>

---

## Post #8 by @chir.set (2025-07-21 16:59 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>the current factory build results are showing it to be successful (<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-07-21" rel="noopener nofollow ugc">SlicerPreview</a>).</p>
</blockquote>
</aside>
<p>Unfortunately, still nothing for Linux…</p>

---

## Post #9 by @ferhue (2025-07-21 17:15 UTC)

<p>Thanks a lot! That solved it partly, but I am getting further errors:</p>
<pre><code class="lang-auto">
/opt/SlicerRT_src/DoseComparison/Logic/vtkMRMLDoseComparisonNode.cxx: In member function ‘virtual void vtkMRMLDoseComparisonNode::ReadXMLAttributes(const char**)’:
/opt/SlicerRT_src/DoseComparison/Logic/vtkMRMLDoseComparisonNode.cxx:108:59: error: cannot convert ‘vtkStdString’ to ‘const char*’
  108 |       this-&gt;SetMaskSegmentID(vtkVariant(attValue).ToString());
      |                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~
      |                                                           |
      |                                                           vtkStdString
</code></pre>
<p>I will try adding <code>.c_str()</code></p>

---

## Post #10 by @ferhue (2025-07-21 17:43 UTC)

<p>Ok, I managed to compile now. Still aborts when starting the ExternalBeamPlanning module. Even if I edit by hand the init.py file you mentioned.</p>

---

## Post #11 by @chir.set (2025-07-21 18:17 UTC)

<aside class="quote no-group" data-username="ferhue" data-post="10" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<p>Still aborts when starting the ExternalBeamPlanning module</p>
</blockquote>
</aside>
<p>It’s perhaps time to run in a debugger. The mentioned hack addresses a locale problem in Python, it’s doubtful it would lead to a crash.</p>

---

## Post #12 by @chir.set (2025-07-22 08:26 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p><code>+locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())</code></p>
</blockquote>
</aside>
<p>Update:</p>
<p>With this hack, Slicer starts but files are badly read (NRRD, DICOM…).</p>
<p>This fix yields a functional Slicer:</p>
<p><code>locale.setlocale(locale.LC_ALL, "C.UTF-8")</code></p>
<p><strong>NOTE</strong>: this is just a temporary hack for my Linux build at the moment. It should not be needed at all and things should bet back to normal when the library/toolkit/infrastructure upgrade phase is over.</p>

---

## Post #13 by @cpinter (2025-07-28 13:55 UTC)

<p>I just came back from vacation. I’m planning on working on SlicerRT related stuff later this week, at least fixing the build error. Please note that I’ll not be able to address Mac specific stuff, but hopefully it won’t come up.</p>
<p>Can you give me more information on how to reproduce the crash when entering the EBP module? Thanks!</p>

---

## Post #14 by @ferhue (2025-07-30 09:15 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="13" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Can you give me more information on how to reproduce the crash when entering the EBP module? Thanks!</p>
</blockquote>
</aside>
<p>Hi, thanks!</p>
<p>The crash does not happen when entering the EBP module, but rather when loading it at startup.</p>
<p>In my case, I just do:</p>
<p><code>/opt/SlicerRT_bld/inner-build$ ./SlicerWithSlicerRT</code><br>
the splash screen shows up, and then after a couple of seconds, it crashes.</p>

---

## Post #15 by @cpinter (2025-07-30 12:10 UTC)

<p>Thanks! It may be due to loading the dependencies (especially IECTransformLogic). I have seen this, but since there is <a href="https://discourse.slicer.org/t/build-error-in-windows-in-debug-mode-due-to-python312-d-lib/43781">no working debug build</a> for Slicer I cannot debug it currently.</p>

---

## Post #16 by @ferhue (2025-07-30 12:53 UTC)

<p>Thanks for the info.<br>
By setting LD_DEBUG variable on Linux, I found:</p>
<p><code>1724316:	find library=libvtkIECTransformLogic.so [0]; searching</code><br>
<code>1724316:	 search path=/opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/cli-modules/.:/opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-loadable-modules/.:/opt/SlicerRT_bld/lib/Slicer-5.9/.:/opt/Slicer_bld/Slicer-build/bin/.:/opt/Slicer_bld/Slicer-build/lib/Slicer-5.9/cli-modules/.:/opt/Slicer_bld/Slicer-build/lib/Slicer-5.9/qt-loadable-modules/.		(LD_LIBRARY_PATH)</code><br>
<code>1724316:	  trying file=/opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/cli-modules/./libvtkIECTransformLogic.so</code><br>
<code>1724316:	  trying file=/opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-loadable-modules/./libvtkIECTransformLogic.so</code><br>
<code>1724316:	  trying file=/opt/SlicerRT_bld/lib/Slicer-5.9/./libvtkIECTransformLogic.so</code><br>
<code>1724316:</code></p>
<p>I checked</p>
<p><code>ldd ./lib/Slicer-5.9/libvtkIECTransformLogic.so</code></p>
<p>and it looks fine.</p>

---

## Post #17 by @Davide_Punzo (2025-08-05 12:17 UTC)

<p>I just run the debugger (linux) with latest Slicer and SlicerRT and I got (when loading the EBP module at startup):</p>
<p>(gdb) run</p>
<p>Starting program: /home/davide/Development/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/SlicerApp-realPython Exception &lt;class ‘AttributeError’&gt;: module ‘_thread’ has no attribute ‘_set_sentinel’[Thread debugging using libthread_db enabled]Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.Python Exception &lt;class ‘AttributeError’&gt;: module ‘_thread’ has no attribute ‘_set_sentinel’could not find minimal symbol for typeinfo address 0x5555555db660</p>
<p>Catchpoint 1 (exception caught), Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing0x00007fffc6abfedb in __cxa_begin_catch () from /lib/x86_64-linux-gnu/libstdc++.so.6(gdb) btPython Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missingPython Exception &lt;class ‘AttributeError’&gt;: module ‘_thread’ has no attribute ‘_set_sentinel’<span class="hashtag-raw">#0</span>  0x00007fffc6abfedb in __cxa_begin_catch () from /lib/x86_64-linux-gnu/libstdc++.so.6#1  0x00007fffc6e283e2 in tbb::detail::r1::gcc_rethrow_exception_broken () at /localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/exception.cpp:156Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#2  0x00007fffc6e29455 in tbb::detail::r1::governor::acquire_resources () at /localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/governor.cpp:72Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#3  0x00007fffc6e36423 in tbb::detail::r1::__TBB_InitOnce::add_ref () at /localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/main.cpp:94Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#4  0x00007fffc6e367dd in tbb::detail::r1::__TBB_InitOnce::__TBB_InitOnce (this=0x7fffc70a3460 &lt;_INTERNALcc7d3d25::tbb::detail::r1::__TBB_InitOnceHiddenInstance&gt;)at /localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/main.h:73Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#5  0x00007fffc6e365c6 in __sti___ZN17_INTERNALcc7d3d253tbb6detail2r128__TBB_InitOnceHiddenInstanceE ()at /localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/main.cpp:70Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#6  0x00007fffc6e36593 in sti$E () at /localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/main.cpp:45Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#7  0x00007ffff7fc64af in call_init (Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missingl=, argc=argc@entry=1, argv=argv@entry=0x7fffffffafe8, env=env@entry=0x7fffffffaff8) at ./elf/dl-init.c:74#8  0x00007ffff7fc65c4 in call_init (l=, argc=, argv=, env=) at ./elf/dl-init.c:120#9  _dl_init (Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missingmain_map=0x7ffff7ffe310, argc=1, argv=0x7fffffffafe8, env=0x7fffffffaff8) at ./elf/dl-init.c:121#10 0x00007ffff7fe2760 in _dl_start_user () from /lib64/ld-linux-x86-64.so.2Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#11 0x0000000000000001 in ?? ()Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#12 0x00007fffffffb5c8 in ?? ()Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing#13 0x0000000000000000 in ?? ()Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing</p>
<p>It seems some conflicts with tbb, but I have no further insight</p>
<p>EBP module seems to link to the right tbb Slicer installation:<br>
davide@davide-MS-7C77:~/Development/Slicer/Extensions/SlicerRT-build/inner-build/lib/Slicer-5.9/qt-loadable-modules$ ldd /home/davide/Development/Slicer/Extensions/SlicerRT-build/inner-build/lib/Slicer-5.9/qt-loadable-modules/libqSlicerExternalBeamPlanningModule.so | grep -i tbb<br>
libtbb_debug.so.12 =&gt; /home/davide/Development/Slicer/Slicer-SuperBuild-Debug/tbb-install/lib/intel64/gcc4.8/libtbb_debug.so.12 (0x00007983ffe00000)</p>
<p>commenting out:</p>
<p>add_subdirectory(ExternalBeamPlanning)</p>
<p>add_subdirectory(PlmProtonDoseEngine)</p>
<p>remove the crash</p>

---

## Post #18 by @ferhue (2025-08-05 12:31 UTC)

<p>Thanks for trying!</p>
<p>Sorry, one question, how do you run gdb?<br>
I tried with<br>
<code>gdb --args ./inner-build/SlicerWithSlicerRT --no-splash</code><br>
and then <code>run</code>, but I did not get extra info.</p>
<p>(I could not figure out how to call gdb SlicerAppReal and at the same time initialize the SlicerRT part.)</p>
<p>Just to see if I get the same onetbb error.</p>

---

## Post #19 by @Davide_Punzo (2025-08-05 12:40 UTC)

<p>for running the debbuger, you can use QtCreator as descrived in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/qtcreatorcpp.html" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging with Qt Creator — 3D Slicer documentation</a> (but with latest Slicer I am having issues with both QtCreator 17 and QtCreator 14.0.2: debugger does not start)</p>
<p>using gdb from terminal (from the inner Slicer-build folder):</p>
<p>./Slicer --launch gdb ./bin/SlicerApp-real<br>
(for extensions, you would need to add the modules path manually)</p>
<p>full guide is at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging on GNU/Linux systems — 3D Slicer documentation</a></p>

---

## Post #20 by @ferhue (2025-08-05 12:46 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="19" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>(but with latest Slicer I am having issues with both QtCreator 17 and QtCreator 14.0.2: debugger does not start)</p>
</blockquote>
</aside>
<p>Yes, I was seeing that with QtCreator, too, which is why I was trying instead directly from gdb. Good to see I’m not the only one <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> (I had read the Guide you linked)</p>
<p>Regarding extensions, do you mean adding the following flags after SlicerApp-real? Or do I need to add them in the GUI?</p>
<p><code>–launcher-additional-settings /opt/SlicerRT_bld/inner-build/AdditionalLauncherSettings.ini --additional-module-paths /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-loadable-modules /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/cli-modules</code></p>

---

## Post #21 by @Davide_Punzo (2025-08-05 12:54 UTC)

<aside class="quote no-group" data-username="ferhue" data-post="20" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<p>Yes, I was seeing that with QtCreator, too, which is why I was trying instead directly from gdb. Good to see I’m not the only one <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> (I had read the Guide you linked)</p>
</blockquote>
</aside>
<p>I agree this isn’t optimal. <a class="mention" href="/u/jcfr">@jcfr</a> could you please confirm whether the QtCreator debugger is expected to work with the current latest version of Slicer? I tried with Qtcreator 17 and 14.0.2 (ubuntu 25.04, gcc 14) and the debugger was not starting.</p>
<aside class="quote no-group" data-username="ferhue" data-post="20" data-topic="43792">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/c0e974/48.png" class="avatar"> ferhue:</div>
<blockquote>
<p>Regarding extensions, do you mean adding the following flags after SlicerApp-real? Or do I need to add them in the GUI?</p>
<p><code>–launcher-additional-settings /opt/SlicerRT_bld/inner-build/AdditionalLauncherSettings.ini --additional-module-paths /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/qt-loadable-modules /opt/SlicerRT_bld/inner-build/lib/Slicer-5.9/cli-modules</code></p>
</blockquote>
</aside>
<p>both should work. I used the GUI.</p>

---

## Post #22 by @ferhue (2025-08-05 13:02 UTC)

<p>Awesome, thanks for the help in starting gdb.</p>
<p>I am getting this stacktrace now, which helps us spot the issue:</p>
<p><code>Loading module “ExternalBeamPlanning”</code><br>
<code>Thread 1 “SlicerApp-real” received signal SIGSEGV, Segmentation fault.</code><br>
<code>Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing</code><br>
<code>0x00007fffd8252642 in PyObject_HasAttrString (Python Exception &lt;class ‘NameError’&gt;: Installation error: gdb._execute_unwinders function is missing</code><br>
<code>v=0x7ffefe3f2840, name=0x5555588418c8 “MockPythonDoseEngine”) at /home/user/builds/build-Slicer_src-Desktop-Debug/Python-3.12.10/Objects/object.c:945</code><br>
<code>945	    if (Py_TYPE(v)-&gt;tp_getattr != NULL)</code></p>

---

## Post #23 by @ferhue (2025-08-05 14:47 UTC)

<p>Just git-checked out latest Slicer master, now getting while rebuilding SlicerRT in debug mode (Slicer debug rebuild went fine):</p>
<p><code>[  6%] Linking CXX shared library ../../lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerBeamsModuleMRML.so</code><br>
<code>/usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTPlanNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTPlanNode[_ZTV17vtkMRMLRTPlanNode]+0x158): undefined reference to vtkMRMLNode::GetTypeDisplayName[abi:cxx11]()' /usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTPlanNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTPlanNode[_ZTV17vtkMRMLRTPlanNode]+0x160): undefined reference to vtkMRMLNode::SetTypeDisplayName(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)’</code><br>
<code>/usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTPlanNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTPlanNode[_ZTV17vtkMRMLRTPlanNode]+0x168): undefined reference to vtkMRMLNode::GetDefaultNodeNamePrefix[abi:cxx11]()' /usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTPlanNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTPlanNode[_ZTV17vtkMRMLRTPlanNode]+0x170): undefined reference to vtkMRMLNode::SetDefaultNodeNamePrefix(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)’</code><br>
<code>/usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTBeamNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTBeamNode[_ZTV17vtkMRMLRTBeamNode]+0x158): undefined reference to vtkMRMLNode::GetTypeDisplayName[abi:cxx11]()' /usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTBeamNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTBeamNode[_ZTV17vtkMRMLRTBeamNode]+0x160): undefined reference to vtkMRMLNode::SetTypeDisplayName(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)’</code><br>
<code>/usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTBeamNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTBeamNode[_ZTV17vtkMRMLRTBeamNode]+0x168): undefined reference to vtkMRMLNode::GetDefaultNodeNamePrefix[abi:cxx11]()' /usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTBeamNode.cxx.o:(.data.rel.ro._ZTV17vtkMRMLRTBeamNode[_ZTV17vtkMRMLRTBeamNode]+0x170): undefined reference to vtkMRMLNode::SetDefaultNodeNamePrefix(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)’</code><br>
<code>/usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTIonBeamNode.cxx.o:(.data.rel.ro._ZTV20vtkMRMLRTIonBeamNode[_ZTV20vtkMRMLRTIonBeamNode]+0x158): undefined reference to vtkMRMLNode::GetTypeDisplayName[abi:cxx11]()' /usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTIonBeamNode.cxx.o:(.data.rel.ro._ZTV20vtkMRMLRTIonBeamNode[_ZTV20vtkMRMLRTIonBeamNode]+0x160): undefined reference to vtkMRMLNode::SetTypeDisplayName(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)’</code><br>
<code>/usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTIonBeamNode.cxx.o:(.data.rel.ro._ZTV20vtkMRMLRTIonBeamNode[_ZTV20vtkMRMLRTIonBeamNode]+0x168): undefined reference to vtkMRMLNode::GetDefaultNodeNamePrefix[abi:cxx11]()' /usr/bin/ld: CMakeFiles/vtkSlicerBeamsModuleMRML.dir/vtkMRMLRTIonBeamNode.cxx.o:(.data.rel.ro._ZTV20vtkMRMLRTIonBeamNode[_ZTV20vtkMRMLRTIonBeamNode]+0x170): undefined reference to vtkMRMLNode::SetDefaultNodeNamePrefix(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)’</code><br>
<code>collect2: error: ld returned 1 exit status</code><br>
<code>make[5]: *** [Beams/MRML/CMakeFiles/vtkSlicerBeamsModuleMRML.dir/build.make:167: lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerBeamsModuleMRML.so] Error 1</code><br>
<code>make[4]: *** [CMakeFiles/Makefile2:2819: Beams/MRML/CMakeFiles/vtkSlicerBeamsModuleMRML.dir/all] Error 2</code><br>
<code>make[3]: *** [Makefile:166: all] Error 2</code><br>
<code>make[2]: *** [CMakeFiles/inner.dir/build.make:87: inner-prefix/src/inner-stamp/inner-build] Error 2</code><br>
<code>make[1]: *** [CMakeFiles/Makefile2:896: CMakeFiles/inner.dir/all] Error 2</code></p>

---

## Post #24 by @cpinter (2025-08-05 15:03 UTC)

<p>I just checked quickly and it seems they changed the value of <code>TypeDisplayName</code> from char* to std::string, may be related.</p>

---

## Post #25 by @ferhue (2025-08-05 15:04 UTC)

<p>Hmm could be also that before it was ‘inline’ in the header, and now it’s in the source file? So missing linking to the library?</p>

---

## Post #26 by @ferhue (2025-08-05 15:34 UTC)

<p>It might also be some cache issue, I will try wiping out the build dir and rebuilding from scratch.</p>

---

## Post #27 by @ferhue (2025-08-05 21:20 UTC)

<p>A full rebuild solved this linker error.</p>
<p>I do still get the runtime crash concerning the <code>MockPythonDoseEngine</code></p>

---

## Post #28 by @ferhue (2025-08-06 06:45 UTC)

<p>Alright, with this diff:</p>
<pre><code class="lang-auto">diff --git a/ExternalBeamPlanning/Widgets/Python/CMakeLists.txt b/ExternalBeamPlanning/Widgets/Python/CMakeLists.txt
index 5ce02b92..e4603d84 100644
--- a/ExternalBeamPlanning/Widgets/Python/CMakeLists.txt
+++ b/ExternalBeamPlanning/Widgets/Python/CMakeLists.txt
@@ -7,7 +7,7 @@ configure_file(
 #-----------------------------------------------------------------------------
 set(DoseEngines_PYTHON_SCRIPTS
   AbstractScriptedDoseEngine
-  MockPythonDoseEngine
+  #MockPythonDoseEngine
   EGSnrcUtil
   OrthovoltageDoseEngineUtil
   OrthovoltageDoseEngine
</code></pre>
<pre><code class="lang-auto">diff --git a/ExternalBeamPlanning/Widgets/Python/DoseEngines.__init__.py.in b/ExternalBeamPlanning/Widgets/Python/DoseEngines.__init__.py.in
index 796a2987..31e4eb18 100644
--- a/ExternalBeamPlanning/Widgets/Python/DoseEngines.__init__.py.in
+++ b/ExternalBeamPlanning/Widgets/Python/DoseEngines.__init__.py.in
@@ -11,7 +11,7 @@ except AttributeError:
 import importlib
 import traceback
 engineNames = [
-  "MockPythonDoseEngine",
+  #"MockPythonDoseEngine",
   "OrthovoltageDoseEngine"
   ]
 for engineName in engineNames:
</code></pre>
<p>SlicerRT starts again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I do get the following warning:</p>
<p><code>RuntimeError: qSlicerScriptedDoseEngine::setPythonSource - Failed to load scripted dose engine: class OrthovoltageDoseEngine was not found in /opt/SlicerRT_dbg_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py</code></p>
<p>even if that file is there and contains the mentioned class. Weird.</p>
<p>Anyway, at least now I can start and test SlicerRT again.</p>
<p>For future reference, for debugging, I used:</p>
<p><code>/home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/Slicer --launch gdb --args /home/user/builds/build-Slicer_src-Desktop-Debug/Slicer-build/bin/SlicerApp-real --no-splash --launcher-verbose --verbose-module-discovery --launcher-additional-settings /opt/SlicerRT_dbg_bld/inner-build/AdditionalLauncherSettings.ini --additional-module-paths /opt/SlicerRT_dbg_bld/inner-build/lib/Slicer-5.9/qt-scripted-modules /opt/SlicerRT_dbg_bld/inner-build/lib/Slicer-5.9/qt-loadable-modules /opt/SlicerRT_dbg_bld/inner-build/lib/Slicer-5.9/cli-modules</code></p>

---

## Post #29 by @cpinter (2025-08-06 09:03 UTC)

<p>Thank you very much Fernando! Did you do anything other than commenting out the mock engine to fix the crash? Just to know exactly what worked in the end, because it seems strange that a tbb related crash is resolved by excluding a python script.</p>

---

## Post #30 by @ferhue (2025-08-06 09:13 UTC)

<p>You are welcome. I did nothing else.</p>
<p>In my case, I did not get any warning about tbb when running gdb.<br>
Maybe, that was an artefact related to the fact that the Slicer tbb:<br>
<code>tbb-install/lib/intel64/gcc4.8/libtbb_debug.so.12</code></p>
<p>does not play well with a system onetbb installed. I do not have onetbb installed in my system, which explains why I did not get the tbb warning, but I got directly the MockDoseEngine crash. Whereas Davide had this installed:</p>
<p><code>/localdisk/ci/runner006/intel-innersource/001/_work/libraries.threading.infrastructure.onetbb-ci/libraries.threading.infrastructure.onetbb-ci/onetbb_source_code/src/tbb/exception.cpp</code></p>

---

## Post #31 by @cpinter (2025-08-06 13:47 UTC)

<p>Excluding the mock python engine fixes the crash for me as well. I don’t understand the reason though. I also don’t know why the orthovoltage engine is not loading, but it has not been maintained, and requires some special tools being installed and configured locally, so I am pretty sure nobody uses it currently. Should we commit this workaround to at least have SlicerRT running?</p>

---

## Post #32 by @ferhue (2025-08-06 15:09 UTC)

<p>Sounds good to me! Thanks for checking.</p>

---

## Post #33 by @cpinter (2025-08-06 15:23 UTC)

<p>Change pushed, see <a href="https://github.com/SlicerRt/SlicerRT/commit/80883066fdece55bef5759018671ac1a9416e3b7" class="inline-onebox">BUG: Exclude MockPythonDoseEngine to fix crash on startup · SlicerRt/SlicerRT@8088306 · GitHub</a></p>

---

## Post #34 by @cpinter (2025-08-06 15:37 UTC)

<p>I’m still getting the same crash 4 out of 5 times. I repeat that I don’t think that omitting a Python dose engine that barely does anything makes sense to fix a crash.</p>

---

## Post #35 by @ferhue (2025-08-06 15:52 UTC)

<p>I tried now a couple of times in a row and indeed it sometimes crashes. This is the stack trace:</p>
<pre><code class="lang-auto">Python Exception &lt;class 'NameError'&gt;: Installation error: gdb._execute_unwinders function is missing
0x00007fffd813e642 in PyObject_HasAttrString (Python Exception &lt;class 'NameError'&gt;: Installation error: gdb._execute_unwinders function is missing
v=0x7fff0b338c70, name=0x55555b326ba8 "OrthovoltageDoseEngine")
</code></pre>
<p>After disabling OrthovoltageDoseEngine (and Utils), now it never crashes. Never = 5 times in a row.</p>

---

## Post #36 by @cpinter (2025-08-07 09:28 UTC)

<p>Interesting. Thanks for further looking into it. Could this be related to the Python upgrade? The same thing that causes <a href="https://discourse.slicer.org/t/build-error-in-windows-in-debug-mode-due-to-python312-d-lib/43781/2">this problem</a>. <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #37 by @cpinter (2025-08-07 11:37 UTC)

<p>I pushed a commit with removing the orthovoltage plugin as well.</p>
<p><a class="mention" href="/u/ferhue">@ferhue</a>  Also pushed a commit that is supposed to fix the build errors with the latest Slicer, so you may need to upgdate your Slicer (or I can add more version checks).</p>

---

## Post #38 by @ferhue (2025-08-07 12:45 UTC)

<p>Thanks a lot!</p>
<p>Should I close this PR? <a href="https://github.com/SlicerRt/SlicerRT/pull/276/files" class="inline-onebox" rel="noopener nofollow ugc">FIX: avoid compilation warnings with latest Slicer and VTK9.5 by ferdymercury · Pull Request #276 · SlicerRt/SlicerRT · GitHub</a></p>

---

## Post #39 by @cpinter (2025-08-07 13:01 UTC)

<p>Oh, I missed this. Too many things on my plate lately… OK it seems that most of what your PR did is included in my commit (except for removing the extra spaces from the end of lines).</p>
<p>One difference is that your change fixes the triangulate issue with calling <code>NonDegenerateTriangulate</code> and mine calls <code>EarCutTriangulation</code>. I checked the old VTK code and the new one, and I am pretty sure that what I chose works the same way. Do you have any argument for choosing the one you suggested?</p>
<p>And to your question, I think it can be closed once we discussed this part. Sorry for the confusion about the PR!</p>

---

## Post #40 by @ferhue (2025-08-07 13:04 UTC)

<p>Thanks, no problem!</p>
<p>wrt NonDegenerate: it was a suggestion by <a href="https://discourse.slicer.org/t/slicerrt-built-from-source-cannot-start/43792/6" class="inline-onebox">SlicerRT built from source cannot start - #6 by chir.set</a> so I did not look into the details.</p>

---

## Post #41 by @cpinter (2025-08-07 13:07 UTC)

<p>OK let’s switch to that one. The function I chose does exactly what the old <code>Triangulate</code> function did, but this one may be some improved version of it. I’ll test it a bit though. Please go ahead and close the PR.</p>

---

## Post #42 by @chir.set (2025-08-07 13:54 UTC)

<p>I suggested that because it was a quick solution for me while building VMTK. It’s in a class that’s probably not used in my workflows, so I can’t say which one is the right fix. ‘<em>It builds, I don’t need that class, let’s go</em>’, that was it.</p>

---

## Post #43 by @cpinter (2025-08-07 14:06 UTC)

<p>Thanks a lot for the information! I’ll leave it like it is then, to keep the functionality the same. I just tested DICOM-RT import and it seems to work fine with <code>EarCutTriangulation</code>.</p>

---
