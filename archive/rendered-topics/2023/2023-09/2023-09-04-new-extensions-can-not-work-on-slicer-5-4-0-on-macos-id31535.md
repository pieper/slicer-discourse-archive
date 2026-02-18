# New extensions can not work on Slicer 5.4.0 on MacOS

**Topic ID**: 31535
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/new-extensions-can-not-work-on-slicer-5-4-0-on-macos/31535

---

## Post #1 by @wrc (2023-09-04 06:01 UTC)

<p>Hello, I have just updated Slicer VMTK to 144582e (2023-08-22). It showed the following error:</p>
<pre><code class="lang-auto">dlopen(/Applications/Slicer 5.4.0.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-loadable-modules/qSlicerBranchClipperModuleWidgetsPythonQt.so, 0x0002): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib
  Referenced from: &lt;8228E9E9-AE1B-31B6-BEEB-4F916BF21B91&gt; /Applications/Slicer 5.4.0.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/libitkgdcmMSFF-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/usr/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file, not in dyld cache)
</code></pre>
<p>This version of Slicer VMTK works well on Slicer 5.4.0 on Windows PC.<br>
The old version of Slicer VMTK also works well on Slicer 5.4.0 on MacOS.<br>
Other extensions like SlicerIGT also has the same problem.</p>
<p>Do you know how to install old version of the extensions of Slicer?<br>
Thank you.</p>

---

## Post #2 by @chir.set (2023-09-04 06:53 UTC)

<aside class="quote no-group" data-username="wrc" data-post="1" data-topic="31535">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/6de8d8/48.png" class="avatar"> wrc:</div>
<blockquote>
<p>Slicer VMTK to 144582e</p>
</blockquote>
</aside>
<p>Just reporting that there are no such issues with Slicer 5.4.0 on Linux.</p>

---

## Post #3 by @pieper (2023-09-04 14:03 UTC)

<p>Thanks for the reports.  I’m able to replicate the issue - there appears to be an issue fixing up the shared libraries for the VMTK extension on mac.</p>
<p>I guess it needs something like this: <a href="https://github.com/Slicer/Slicer/commit/858c19515f5e4eb69145f0b8c38aa8525b56521f" class="inline-onebox">COMP: Fix extension packaging on macOS accounting for synthetic firmlink · Slicer/Slicer@858c195 · GitHub</a></p>
<p>Probably something similar or more extensive is needed for VMTK due to its structure.  It would be great if someone has a chance to dig in to this.</p>
<p>For now maybe use older slicer or build from source.</p>

---

## Post #4 by @jcfr (2023-09-12 22:09 UTC)

<p>To follow up on this issue as well as the one discussed in <a href="https://discourse.slicer.org/t/fiducial-registration-wizard-module-not-loading/31513/5" class="inline-onebox">Fiducial Registration Wizard Module not loading - #5 by Jayme_Goodrum</a>, the root cause of the problem has been identified and fixed.</p>
<p>The patch locally integrated in the build machine source tree was not the one effectively tested and contributed through <a href="https://github.com/Slicer/Slicer/pull/7181">PR-7181</a> in <code>main</code>, and <a href="https://github.com/Slicer/Slicer/pull/7182">PR-7182</a> in <code>5.4</code> maintenance branch.</p>
<p>This has now been addressed <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>
<p>Valid stable extensions are expected to be uploaded in the next 12 hours <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=15" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<h3><a name="p-100349-details-1" class="anchor" href="#p-100349-details-1" aria-label="Heading link"></a>Details</h3>
<p>It was an hard-coded version expected to work only for the <em>Preview</em> source tree and not the <em>Stable</em> source tree.</p>
<pre data-code-wrap="diff"><code class="lang-diff">diff --git a/CMake/SlicerExtensionCPack.cmake b/CMake/SlicerExtensionCPack.cmake
index 842abbb6ff..b65b312d5a 100644
--- a/CMake/SlicerExtensionCPack.cmake
+++ b/CMake/SlicerExtensionCPack.cmake
@@ -193,6 +193,7 @@ if(APPLE)
   set(EXTENSION_BINARY_DIR ${EXTENSION_SUPERBUILD_BINARY_DIR}/${EXTENSION_BUILD_SUBDIRECTORY})
   set(EXTENSION_SUPERBUILD_DIR ${EXTENSION_SUPERBUILD_BINARY_DIR})
   get_filename_component(Slicer_SUPERBUILD_DIR ${Slicer_DIR}/.. ABSOLUTE)
+  set(Slicer_SUPERBUILD_DIR "/Users/svc-dashboard/D/P/A")
 
   #------------------------------------------------------------------------------
   # &lt;ExtensionName&gt;_FIXUP_BUNDLE_LIBRARY_DIRECTORIES
</code></pre>
<p>instead the following patch was added:</p>
<pre data-code-wrap="diff"><code class="lang-diff">diff --git a/CMake/SlicerExtensionCPack.cmake b/CMake/SlicerExtensionCPack.cmake
index 842abbb6ff..6adec7bcac 100644
--- a/CMake/SlicerExtensionCPack.cmake
+++ b/CMake/SlicerExtensionCPack.cmake
@@ -194,6 +194,14 @@ if(APPLE)
   set(EXTENSION_SUPERBUILD_DIR ${EXTENSION_SUPERBUILD_BINARY_DIR})
   get_filename_component(Slicer_SUPERBUILD_DIR ${Slicer_DIR}/.. ABSOLUTE)
 
+  # If any, resolve synthetic firmlink  (e.g from "/D/P/A" to "/Users/svc-dashboard/D/P/A")
+  #
+  # Since the output of "otool -L" reports paths with synthetic firmlinks resolved
+  # (see GetPrerequisitesWithRPath), we are using REAL_PATH below to also resolve
+  # Slicer_SUPERBUILD_DIR and ensure that the test in "SlicerExtensionCPackBundleFixup.cmake.in"
+  # checking if "${key}_ITEM" is a library built in Slicer itself work as expected.
+  file(REAL_PATH ${Slicer_SUPERBUILD_DIR} Slicer_SUPERBUILD_DIR)
+
   #------------------------------------------------------------------------------
   # &lt;ExtensionName&gt;_FIXUP_BUNDLE_LIBRARY_DIRECTORIES
   #------------------------------------------------------------------------------

</code></pre>

---

## Post #5 by @jcfr (2023-09-12 22:47 UTC)

<blockquote>
<p>Valid stable extensions are expected to be uploaded in the next 12 hour</p>
</blockquote>
<p>Since the regular build process would have skip the update (no metadata change detected), existing macOS extensions have been manually removed and are currently being re-packaged and re-uploaded.</p>
<p>This should be completed in the next hour.</p>

---

## Post #6 by @jcfr (2023-09-13 13:09 UTC)

<p>And for future reference, the steps were the following:</p>
<p><strong>Delete macos extension packages:</strong></p>
<ul>
<li>Go to <a href="https://slicer-packages.kitware.com">https://slicer-packages.kitware.com</a></li>
<li>Browse  to <code>Applications / packages  / Slicer 5.4.0 / extensions</code><sup class="footnote-ref"><a href="#footnote-100380-1" id="footnote-ref-100380-1">[1]</a></sup></li>
<li>Select all <code>macos</code> extension packages</li>
<li>Click on <code>Delete checked resources</code></li>
</ul>
<p><strong>Re-upload packages:</strong></p>
<ul>
<li>SSH into macOS build server</li>
<li>Go to <code>/path/to/S/S-0-E-b</code></li>
<li>Set env. variable <code>SLICER_PACKAGE_UPLOAD_SKIP_PACKAGING_TARGET</code></li>
<li>Set env. variables <code>SLICER_EXTENSION_MANAGER_*</code> for client executable, url and api key</li>
</ul>
<pre><code class="lang-auto">export SLICER_PACKAGE_UPLOAD_SKIP_PACKAGING_TARGET=1

cd /path/to/S/S-0-E-b

for extension_build_dir in $(ls -1 | grep "\-build"); do
  subdir=""
  # Assume SuperBuild extensions are all using the same inner build directory
  if [ -d "${extension_build_dir}/inner-build" ]; then
    subdir=inner-build
  fi
  echo "extension_build_dir [${extension_build_dir}/${subdir}]"
  (cd ${extension_build_dir}/${subdir}; make packageupload/fast)
done
</code></pre>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-100380-1" class="footnote-item"><p><a href="https://slicer-packages.kitware.com/#folder/64e0bcf706a93d6cff363ad0">https://slicer-packages.kitware.com/#folder/64e0bcf706a93d6cff363ad0</a> <a href="#footnote-ref-100380-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #7 by @lassoan (2023-09-18 02:19 UTC)

<p>A post was split to a new topic: <a href="/t/slicertms-extension-does-not-work-in-slicer-5-4-on-macos/31763">SlicerTMS extension does not work in Slicer-5.4 on macOS</a></p>

---

## Post #9 by @lassoan (2023-09-18 13:15 UTC)

<p>Maybe the fix from last week did not fully work.</p>
<p>Can someone (<a class="mention" href="/u/pieper">@pieper</a> maybe?) test if Surface Cut effect in SegmentEditorExtraEffects extension works on macOS in a freshly installed Slicer-5.4?</p>

---

## Post #10 by @AKue (2023-09-18 13:48 UTC)

<p>It worked last week (I think it was Friday). In the meantime I downloaded some extensions. Could that be the reason why it doesn’t work anymore?</p>

---

## Post #11 by @lassoan (2023-09-18 13:55 UTC)

<p>Installing additional extensions should not break existing extensions but anything is possible in software.</p>
<p>What extensions are installed now? (the application log that you shared only showed MarkupsToModel and SegmentEditorExtraEffects extensions)</p>
<p>Can you reproduce the behavior on a fresh Slicer install (that you install SegmentEditorExtraEffects extension and Surface Cut effects works and then you install some additional extensions and the Surface Cut effect does not work anymore)?</p>

---

## Post #12 by @AKue (2023-09-19 11:11 UTC)

<p>I did download “NvidiaAIAssistedAnnotation” and after that the “Surface cut” didn’t work anymore (I can’t the fiducial points as it’s greyed out).<br>
Maybe it’s just a coincidence but after I realized that I doesn’t work anymore I firstly deinstalled and installed the extensions and secondly also deinstalled and installed 3D Slicer software, without solving the problem.</p>
<p>Many thanks for your help!</p>

---

## Post #13 by @pieper (2023-09-19 13:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="31535">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can someone (<a class="mention" href="/u/pieper">@pieper</a> maybe?) test if Surface Cut effect in SegmentEditorExtraEffects extension works on macOS in a freshly installed Slicer-5.4?</p>
</blockquote>
</aside>
<p>I can confirm that there’s still a shared library path issue on MacOS with 5.4.  Here’s the result of a fresh 5.4 installation with the extra effects extension installed.  Looks like an issue with the ITK IO shared libraries.</p>
<pre><code class="lang-auto">(base) pieper@hive ~ % /tmp/Slicer.app/Contents/MacOS/Slicer 
  Error(s):
    Cannot load library /private/tmp/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib: (dlopen(/private/tmp/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib, 0x0085): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib
  Referenced from: &lt;8228E9E9-AE1B-31B6-BEEB-4F916BF21B91&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/libitkgdcmMSFF-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file), '/usr/lib/libitkgdcmjpeg8-5.3.1.dylib' (no such file, not in dyld cache))
dlopen(/private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-loadable-modules/vtkSlicerSegmentEditorFastMarchingModuleLogicPython.so, 0x0002): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib
  Referenced from: &lt;249C14A3-922A-3ACF-A049-3F2D2DEDC62A&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKCommon-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib' (no such file), '/usr/lib/libitkdouble-conversion-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmMSFF-5.3.1.dylib
  Referenced from: &lt;560159FD-BA27-3CB8-99E1-A270AADA946D&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOGDCM-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmMSFF-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmMSFF-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmMSFF-5.3.1.dylib' (no such file), '/usr/lib/libitkgdcmMSFF-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkjpeg-5.3.1.dylib
  Referenced from: &lt;F70DCEE4-1D80-3987-BC57-2EEF23E16F18&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOJPEG-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkjpeg-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkjpeg-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkjpeg-5.3.1.dylib' (no such file), '/usr/lib/libitkjpeg-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib
  Referenced from: &lt;97F92774-CA75-3F14-B0C4-D7F4CA49AD41&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOLSM-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib' (no such file), '/usr/lib/libitktiff-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib
  Referenced from: &lt;0FDE7828-E821-3811-8AAF-CD0AF44ED2D2&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOTIFF-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib' (no such file), '/usr/lib/libitktiff-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkpng-5.3.1.dylib
  Referenced from: &lt;428379DB-772D-34CE-9CDB-54428A4B439A&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOPNG-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkpng-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkpng-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkpng-5.3.1.dylib' (no such file), '/usr/lib/libitkpng-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libITKniftiio-5.3.1.dylib
  Referenced from: &lt;8055E7CC-11BB-3C0C-A3AE-25FE5DDDAE98&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIONIFTI-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKniftiio-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKniftiio-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKniftiio-5.3.1.dylib' (no such file), '/usr/lib/libITKniftiio-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libITKNrrdIO-5.3.1.dylib
  Referenced from: &lt;49E409EA-EF87-3221-B7A2-CAA30301DE84&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIONRRD-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKNrrdIO-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKNrrdIO-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKNrrdIO-5.3.1.dylib' (no such file), '/usr/lib/libITKNrrdIO-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkhdf5_cpp-shared-5.3.1.dylib
  Referenced from: &lt;EFD52745-B6CC-3C26-AF09-663C61E2CA1B&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOTransformHDF5-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkhdf5_cpp-shared-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkhdf5_cpp-shared-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkhdf5_cpp-shared-5.3.1.dylib' (no such file), '/usr/lib/libitkhdf5_cpp-shared-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib
  Referenced from: &lt;1DF364A2-DEE6-3CF5-854E-3A34C7485ADA&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOTransformInsightLegacy-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib' (no such file), '/usr/lib/libitkdouble-conversion-5.3.1.dylib' (no such file, not in dyld cache)Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkminc2-5.3.1.dylib
  Referenced from: &lt;6482C254-2F9C-30EE-A8A9-7A27F36C0215&gt; /private/tmp/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOMINC-5.3.1.dylib
  Reason: tried: '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkminc2-5.3.1.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkminc2-5.3.1.dylib' (no such file), '/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkminc2-5.3.1.dylib' (no such file), '/usr/lib/libitkminc2-5.3.1.dylib' (no such file, not in dyld cache)
Switch to module:  "Welcome"
Populating font family aliases took 104 ms. Replace uses of missing font family ".AppleSystemUIFont" with one that exists to avoid this cost. 
Loading Slicer RC file [/Users/pieper/.slicerrc.py]

</code></pre>

---

## Post #14 by @Sam_Horvath (2023-09-19 14:23 UTC)

<p>Due to some (probably unrelated) factory issues, the extensions might not have been rebuilt yet to take into effect now changes.</p>

---

## Post #15 by @AKue (2023-09-20 09:09 UTC)

<p>Is there a way I can fix the problem? Or is it a general problem, that still needs to be fixed?</p>

---

## Post #16 by @lassoan (2023-09-20 13:54 UTC)

<p>Please try the uninstall and install the extensions today. If there are still problems then let us know. Thank you!</p>

---

## Post #17 by @Su_So (2023-09-20 21:41 UTC)

<p>As a new user who downloaded 3D Slicer and these 2 extensions just today, I can confirm that the issue still exists.</p>

---

## Post #18 by @lassoan (2023-09-20 21:48 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could you please check what’s happening?</p>

---

## Post #19 by @AKue (2023-09-21 14:49 UTC)

<p>I unistallend and reinstalled both extensions and there are no more extensions installed right now but I still can’t set the fiducial points with “Surface cut”.</p>

---

## Post #20 by @lassoan (2023-09-21 15:09 UTC)

<p>“Surface cut” effect is provided by an extension, so if you don’t have any extensions installed then the “Surface cut” effect should not be visible at all in the Extensions Manager. Can you upload somewhere the application log (menu: Help / Report a bug) and post the link here?</p>

---

## Post #21 by @AKue (2023-09-21 15:13 UTC)

<p>Sorry. I wasn’t precise enough. I’ve only installed the two extensions I need for “Surface cut” (no more).</p>
<details>
<summary>
Logs</summary>
<p>[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-09-21 16:44:39<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.4.0 (revision 31938 / 311cb26) macosx-amd64 - installed release<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: macOS / 12.6.4 / 21G526 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16384 MB physical, 3072 MB virtual<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i7-5557U CPU @ 3.10GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.8, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 21.09.2023 16:44:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules<br>
[CRITICAL][Qt] 21.09.2023 16:44:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib, 0x0085): Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib’<br>
Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/libitkgdcmMSFF-5.3.1.dylib’<br>
Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkgdcmjpeg8-5.3.1.dylib’ (no such file))<br>
[DEBUG][Python] 21.09.2023 16:44:53 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.4/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - dlopen(/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-loadable-modules/vtkSlicerSegmentEditorFastMarchingModuleLogicPython.so, 0x0002): Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKCommon-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkdouble-conversion-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmMSFF-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOGDCM-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmMSFF-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkgdcmMSFF-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkjpeg-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOJPEG-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkjpeg-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkjpeg-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOLSM-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib’ (no such file), ‘/usr/lib/libitktiff-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOTIFF-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitktiff-5.3.1.dylib’ (no such file), ‘/usr/lib/libitktiff-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkpng-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOPNG-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkpng-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkpng-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKniftiio-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIONIFTI-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKniftiio-5.3.1.dylib’ (no such file), ‘/usr/lib/libITKniftiio-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKNrrdIO-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIONRRD-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libITKNrrdIO-5.3.1.dylib’ (no such file), ‘/usr/lib/libITKNrrdIO-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkhdf5_cpp-shared-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOTransformHDF5-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkhdf5_cpp-shared-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkhdf5_cpp-shared-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOTransformInsightLegacy-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkdouble-conversion-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkdouble-conversion-5.3.1.dylib’ (no such file)Library not loaded: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkminc2-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Referenced from: ‘/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/libITKIOMINC-5.3.1.dylib’<br>
[CRITICAL][Stream] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Reason: tried: ‘/Users/svc-dashboard/D/S/A/ITK-build/lib/libitkminc2-5.3.1.dylib’ (no such file), ‘/usr/lib/libitkminc2-5.3.1.dylib’ (no such file)<br>
[DEBUG][Python] 21.09.2023 16:45:03 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.4/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 21.09.2023 16:45:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Populating font family aliases took 257 ms. Replace uses of missing font family “.AppleSystemUIFont” with one that exists to avoid this cost.<br>
[CRITICAL][FD] 21.09.2023 16:45:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - [49065:89859:0921/164527.159831:ERROR:gl_context_cgl.cc(118)] Error creating context.<br>
[WARNING][Qt] 21.09.2023 16:45:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e8/MatlabBridgeLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/31938/macosx</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/3/34/PkModeling.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/f/f2/SkullStripper.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png" rel="noopener nofollow ugc">http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png" rel="noopener nofollow ugc">http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269" rel="noopener nofollow ugc">http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 21.09.2023 16:45:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31938/macosx" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png</a>’. This content should also be served over HTTPS.<br>
[DEBUG][Qt] 21.09.2023 16:45:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Python] 21.09.2023 16:45:50 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - </p><p>Status: <i>Idle</i></p><br>
[DEBUG][Python] 21.09.2023 16:45:53 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>Verifying checksum</b><br>
[DEBUG][Python] 21.09.2023 16:45:53 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>File already exists and checksum is OK - reusing it.</b><br>
[DEBUG][Python] 21.09.2023 16:45:53 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>Requesting load</b> <i>PreDentalSurgery</i> from /Users/Aud/Library/Caches/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz …<br>
[DEBUG][Qt] 21.09.2023 16:45:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/Aud/Library/Caches/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz” “[0.57s]”<br>
[DEBUG][Python] 21.09.2023 16:45:54 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>Load finished</b><br>
[DEBUG][Python] 21.09.2023 16:45:54 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>Verifying checksum</b><br>
[DEBUG][Python] 21.09.2023 16:45:54 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>File already exists and checksum is OK - reusing it.</b><br>
[DEBUG][Python] 21.09.2023 16:45:54 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>Requesting load</b> <i>PostDentalSurgery</i> from /Users/Aud/Library/Caches/slicer.org/Slicer/SlicerIO/PostDentalSurgery.gipl.gz …<br>
[DEBUG][Qt] 21.09.2023 16:45:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/Aud/Library/Caches/slicer.org/Slicer/SlicerIO/PostDentalSurgery.gipl.gz” “[0.55s]”<br>
[DEBUG][Python] 21.09.2023 16:45:54 [Python] (/Applications/Slicer.app/Contents/bin/…/lib/Slicer-5.4/qt-scripted-modules/SampleData.py:385) - <b>Load finished</b><br>
[DEBUG][Qt] 21.09.2023 16:45:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 21.09.2023 16:46:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 21.09.2023 16:46:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 138, in activate<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.createNewMarkupNode()<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 352, in createNewMarkupNode<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.setAndObserveSegmentMarkupNode(self.segmentMarkupNode)<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 374, in setAndObserveSegmentMarkupNode<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.updateModelFromSegmentMarkupNode()<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 413, in updateModelFromSegmentMarkupNode<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.logic.updateModelFromMarkup(self.segmentMarkupNode, self.segmentModel, smoothing)<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 447, in updateModelFromMarkup<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     markupsToModel = slicer.modules.markupstomodel.logic()<br>
[CRITICAL][Stream] 21.09.2023 16:46:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: module ‘modules’ has no attribute ‘markupstomodel’<p></p>
</details>

---

## Post #22 by @lassoan (2023-09-21 15:17 UTC)

<p>Thank you for the additonal information. As the <code>AttributeError: module ‘modules’ has no attribute ‘markupstomodel’</code> error message indicates, <code>Surface Cut</code> effect requires the MarkupsToModel extension. You need to install it for the effect to work.</p>
<p>Let us know if the effect does not work after installing MarkupsToModel extension. That would mean there are still problems with macOS that <a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> needs to look into.</p>

---

## Post #23 by @AKue (2023-09-21 15:21 UTC)

<p>MarkupsToModel is already installed<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/738f76856e9b07054a9e41bff5cba4faf4a014ac.png" data-download-href="/uploads/short-url/guihbbPYLFKrwjh9rmgyC9l800Y.png?dl=1" title="Bildschirmfoto 2023-09-21 um 17.20.05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738f76856e9b07054a9e41bff5cba4faf4a014ac_2_690x105.png" alt="Bildschirmfoto 2023-09-21 um 17.20.05" data-base62-sha1="guihbbPYLFKrwjh9rmgyC9l800Y" width="690" height="105" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738f76856e9b07054a9e41bff5cba4faf4a014ac_2_690x105.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738f76856e9b07054a9e41bff5cba4faf4a014ac_2_1035x157.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738f76856e9b07054a9e41bff5cba4faf4a014ac_2_1380x210.png 2x" data-dominant-color="F0F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-09-21 um 17.20.05</span><span class="informations">2526×388 82.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @jcfr (2023-09-21 15:25 UTC)

<blockquote>
<p>That would mean there are still problems with macOS</p>
</blockquote>
<p>We will look into this later this week after we are done teaching the Slicer advanced training.</p>

---

## Post #25 by @AKue (2023-09-25 11:36 UTC)

<p>Is there any news with the current problem? Thank you!!</p>

---

## Post #26 by @jcfr (2023-09-26 02:58 UTC)

<h3><a name="p-101020-macos-1" class="anchor" href="#p-101020-macos-1" aria-label="Heading link"></a>macOS</h3>
<p>The issue seems to be specific to the macOS build of <code>MarkupsToModel</code>, a new package failed to be re-generated due to the following error:</p>
<pre><code class="lang-auto">[  9%] Building CXX object MarkupsToModel/MRML/CMakeFiles/vtkSlicerMarkupsToModelModuleMRML.dir/vtkMRMLMarkupsToModelNode.cxx.o
In file included from /Users/svc-dashboard/D/S/S-0-E-b/MarkupsToModel/MarkupsToModel/MRML/vtkMRMLMarkupsToModelNode.cxx:6:
In file included from /D/S/S-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.h:30:
In file included from /D/S/S-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h:23:
/Users/svc-dashboard/D/S/A/vtkAddon/vtkCurveGenerator.h:24:10: fatal error: 'vtkParametricFunction.h' file not found
#include &lt;vtkParametricFunction.h&gt;
         ^~~~~~~~~~~~~~~~~~~~~~~~~
</code></pre>
<p>After checking that the file <code>vtkParametricFunction.h</code> exists on the filesystem:</p>
<pre><code class="lang-auto">% pwd
/D/S/A/VTK

% find . | grep vtkParametricFunction\.h
./Common/ComputationalGeometry/vtkParametricFunction.h
</code></pre>
<p>we looked at the parameters being passed to the compiler, and it looks like not all VTK include directories are being passed.</p>
<p><strong>Next steps:</strong> Since the Preview build seems to happen without issues, we will compare the Stable and Preview one once today’s round of preview (aka nightly) builds is completed.</p>
<h3><a name="p-101020-windows-2" class="anchor" href="#p-101020-windows-2" aria-label="Heading link"></a>Windows</h3>
<p>On Windows, the expected VTK paths are being associated with the corresponding  target:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7beca016b8be9513681bda8ce6ee6ed10878140a.png" data-download-href="/uploads/short-url/hGhHaHw6kNd19Yy8lZ3YShBnX4K.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca016b8be9513681bda8ce6ee6ed10878140a_2_517x269.png" alt="image" data-base62-sha1="hGhHaHw6kNd19Yy8lZ3YShBnX4K" width="517" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca016b8be9513681bda8ce6ee6ed10878140a_2_517x269.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca016b8be9513681bda8ce6ee6ed10878140a_2_775x403.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca016b8be9513681bda8ce6ee6ed10878140a_2_1034x538.png 2x" data-dominant-color="E1DEDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1530×798 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #27 by @jcfr (2023-09-27 00:38 UTC)

<p>Since the release was created, the XCode version on the build machine went through a minor update that lead to the removal of</p>
<pre><code class="lang-auto">/Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX13.3.sdk
</code></pre>
<p>and the introduction of</p>
<pre><code class="lang-auto">/Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk
</code></pre>
<p>As a side effect, some of the extensions failed to build and instead of uploading a newly generated package, the older &amp; invalid package that were left over have been re-uploaded.</p>
<p>To address this, the string <code>13.3.sdk</code> was replaced with <code>14.0.sdk</code> in the relevant files:</p>
<pre><code class="lang-auto">./VTK-build/CMakeFiles/Export/lib/cmake/vtk-9.2/VTK-targets.cmake
./VTK-build/lib/cmake/vtk-9.2/VTK-targets.cmake
./ITK-build/CMakeFiles/Export/lib/cmake/ITK-5.3/ITKTargets.cmake
./ITK-build/ITKTargets.cmake
./Slicer-build/SlicerTargets.cmake
</code></pre>
<p>and the following macos extensions have been removed and have already been re-generated <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> or are in the process of being re-generated <img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=12" title=":hourglass_flowing_sand:" class="emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto">AirwaySegmentation
BoneTextureExtension
BrainVolumeRefinement
CarreraSlice
ChangeTracker
CleverSeg
CMFreg
DRRGenerator
DSCMRIAnalysis
ErodeDilateLabel
GelDosimetryAnalysis
ImageMaker
MarkupsToModel
MatlabBridge
MedialSkeleton
MeshToLabelMap
ModelClip
ModelToModelDistance
OsteotomyPlanner
PathReconstruction
PBNRR
PerkTutor
PETCPhantom
PETDICOMExtension
PET-IndiC
PETTumorSegmentation
Sandbox
ScatteredTransform
SegmentationAidedRegistration
SegmentEditorExtraEffects
SegmentMesher
ShapePopulationViewer
ShapeVariationAnalyzer
SkeletalRepresentation
SkullStripper
SlicerANTs
SlicerDMRI
SlicerElastix
SlicerFreeSurfer
SlicerIGSIO
SlicerJupyter
SlicerLookingGlass
SlicerNeuro
SlicerOpenCV
SlicerOpenIGTLink
SlicerProstate
SlicerRT
SlicerVMTK
SNRMeasurement
SurfaceMarkup
SwissSkullStripper
T1Mapping
UKFTractography
VASSTAlgorithms
ZFrameRegistration
</code></pre>
<aside class="quote no-group" data-username="AKue" data-post="25" data-topic="31535" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> AKue:</div>
<blockquote>
<p>Is there any news with the current problem? Thank you!!</p>
</blockquote>
</aside>
<p>The <code>MarkupsToModel</code>  has already been re-generated and re-uploaded. Let us know if you still have issue.</p>

---

## Post #28 by @AKue (2023-09-27 09:45 UTC)

<p>Now I can’t download the SegmentEditorExtraEffets Extension any more <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe63a09ce81f43697d09889e2bb655d7e2cbf36.jpeg" data-download-href="/uploads/short-url/vnjP7jFMlvwLZXpIjh4KRiJx1CS.jpeg?dl=1" title="Bildschirmfoto 2023-09-27 um 11.42.57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe63a09ce81f43697d09889e2bb655d7e2cbf36_2_690x431.jpeg" alt="Bildschirmfoto 2023-09-27 um 11.42.57" data-base62-sha1="vnjP7jFMlvwLZXpIjh4KRiJx1CS" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe63a09ce81f43697d09889e2bb655d7e2cbf36_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe63a09ce81f43697d09889e2bb655d7e2cbf36_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe63a09ce81f43697d09889e2bb655d7e2cbf36_2_1380x862.jpeg 2x" data-dominant-color="F7F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-09-27 um 11.42.57</span><span class="informations">2560×1600 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #29 by @muratmaga (2023-09-27 16:51 UTC)

<p>Probably it was building right around the time you tried. it should be available now.<br>
<a href="https://slicer.cdash.org/build/3159382" rel="noopener nofollow ugc">Build Summary (cdash.org)</a></p>

---

## Post #30 by @AKue (2023-09-28 07:21 UTC)

<p>It`s working again!!! Many thanks for your help!</p>

---
