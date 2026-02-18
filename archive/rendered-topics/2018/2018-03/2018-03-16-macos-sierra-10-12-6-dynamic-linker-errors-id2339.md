# MacOS Sierra (10.12.6) dynamic linker errors

**Topic ID**: 2339
**Date**: 2018-03-16
**URL**: https://discourse.slicer.org/t/macos-sierra-10-12-6-dynamic-linker-errors/2339

---

## Post #1 by @hherhold (2018-03-16 19:54 UTC)

<p>Hey guys,</p>
<p>I’m running into some dynamic linker errors on startup with master built on 10.12.6:</p>
<pre><code>dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerCropVolumeModuleLogicPython.so, 2): no suitable image found.  Did find:
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerCropVolumeModuleLogicPython.so: malformed mach-o: load commands size (32872) &gt; 32768
/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerCropVolumeModuleLogicPython.so: malformed mach-o: load commands size (32872) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerCropVolumeModuleLogicPython.so: malformed mach-o: load commands size (32872) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerCropVolumeModuleLogicPython.so: malformed mach-o: load commands size (32872) &gt; 32768
dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerSegmentationsModuleLogicPython.so, 2): Library not loaded: /Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerSegmentationsModuleLogicPythonD.dylib
  Referenced from: /Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerSegmentationsModuleLogicPython.so
  Reason: no suitable image found.  Did find:
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./libvtkSlicerSegmentationsModuleLogicPythonD.dylib: malformed mach-o: load commands size (33048) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerSegmentationsModuleLogicPythonD.dylib: malformed mach-o: load commands size (33048) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerSegmentationsModuleLogicPythonD.dylib: malformed mach-o: load commands size (33048) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerSegmentationsModuleLogicPythonD.dylib: malformed mach-o: load commands size (33048) &gt; 32768
dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerAnnotationsModuleMRMLDisplayableManagerPython.so, 2): Library not loaded: /Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerAnnotationsModuleMRMLDisplayableManagerPythonD.dylib
  Referenced from: /Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerAnnotationsModuleMRMLDisplayableManagerPython.so
  Reason: no suitable image found.  Did find:
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./libvtkSlicerAnnotationsModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33080) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerAnnotationsModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33080) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerAnnotationsModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33080) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerAnnotationsModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33080) &gt; 32768
dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerMarkupsModuleMRMLDisplayableManagerPython.so, 2): no suitable image found.  Did find:
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerMarkupsModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32904) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerMarkupsModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32904) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerMarkupsModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32904) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerMarkupsModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32904) &gt; 32768
dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so, 2): Library not loaded: /Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPythonD.dylib
  Referenced from: /Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so
  Reason: no suitable image found.  Did find:
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./libvtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33024) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33024) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33024) &gt; 32768
	/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (33024) &gt; 32768
</code></pre>
<p>A while back (May 2017)? I saw a post talking a bit about this, and it sounded like it had something to do with the behavior of the linker being different in 10.12 vs 10.11, and either the symbol table didn’t look right or the pathnames to libraries are too long. (Not sure on either of these.)</p>
<p>Has anybody else run into this? It’s become a bit of a problem with local builds - things like logical operators in the Segmentation Editor fail because it can’t get the segmentations module logic when checking if bypass masking is set. (My guess is because it can’t load the .so that contains the logic, but I’m totally guessinng here.)</p>
<p>Any ideas?</p>
<p>Thanks in advance!!!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2018-03-16 20:04 UTC)

<p>This was the post that talked about it:</p>
<aside class="quote quote-modified" data-post="39" data-topic="1483">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/nightly-build-tests-failing-for-extensions-with-dependencies-to-other-scriptable-modules/1483/39">Nightly build TESTS failing for extensions with dependencies to other scriptable modules</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    This error 
/Users/christian/sources/cpp/Builds/Slicer/Release/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./libvtkSlicerMarkupsModuleMRMLDisplayableManagerPythonD.dylib: malformed mach-o: load commands size (32840) &gt; 32768

seems to be due to the limit on total size of all the load commands in the dynamic library in the MacOS loader. 
I guess using a shorter build directory path would solve the issue. For example, instead of /Users/christian/sources/cpp/Builds/Slicer/Release, you could try…
  </blockquote>
</aside>

<p>I’m doing a build right now with a shorter path - we will see if that fixes it?</p>

---

## Post #3 by @hherhold (2018-03-17 11:53 UTC)

<p>OK, building in a directory tree with shorter initial pathnames seems to fix it. Annoying, but it works.</p>

---

## Post #4 by @lassoan (2018-03-17 20:24 UTC)

<p>Don’t worry, it’s not just a Mac thing. Long base directory path breaks the build on all operating systems.</p>

---

## Post #5 by @mschumaker (2018-04-13 16:37 UTC)

<p>I just built Slicer for the first time, and I get the same errors when I run it. I built Slicer in the directory /Users/michaelschumaker/Packages. How short does the initial pathname need to be?</p>

---

## Post #6 by @ihnorton (2018-04-13 18:00 UTC)

<p>FWIW, I use <code>/opt/bld/s5nj</code> and <code>/opt/bld/r/r5nj</code>.</p>

---
