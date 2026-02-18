# Cannot find libraries when loading custom loadable extension because of versioning

**Topic ID**: 43582
**Date**: 2025-07-02
**URL**: https://discourse.slicer.org/t/cannot-find-libraries-when-loading-custom-loadable-extension-because-of-versioning/43582

---

## Post #1 by @glso (2025-07-02 16:09 UTC)

<p>Hi,</p>
<p>I built a loadable extension which builds and runs successfully on my Slicer-Release (5.9), built from source code on x86_64 architecture on MacOS. My CMake version is 3.22.6.</p>
<p>I wanted to package the extension so that it can be loaded via <code>Extension Manager &gt; Install from file...</code> on a pre-built version of Slicer (5.8.1, Slicer_REVISION 33241).</p>
<p>I executed <code>export Slicer_REVISION=33241</code> followed by the typical <code>cmake</code>, <code>make</code>, and <code>make package</code> commands. On a pre-built version of Slicer (5.8.1), I uploaded the tar.gz file and added the path <code>/Applications/Slicer 5.8.1.app/Contents/Extensions-33241/MyExtension/lib/Slicer-5.9/qt-loadable-modules</code> to Settings &gt; Additional Module Paths. When I restarted Slicer, I get the following error:</p>
<pre><code class="lang-auto">[Qt] Error(s):
[Qt] Cannot load library /Applications/Slicer 5.8.1.app/Contents/Extensions-33241/MyExtension/lib/Slicer-5.9/qt-loadable-modules/libqSlicerMyExtensionModule.dylib:
     (dlopen(/Applications/Slicer 5.8.1.app/Contents/Extensions-33241/MyExtension/lib/Slicer-5.9/qt-loadable-modules/libqSlicerMyExtensionModule.dylib, 0x0085):
     Library not loaded: @rpath/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib
[Qt] Referenced from: &lt;46F9E511-7BE0-3A9B-AA9D-279AE8C37AC2&gt; /Applications/Slicer 5.8.1.app/Contents/Extensions-33241/MyExtension/lib/Slicer-5.9/qt-loadable-modules/libqSlicerMyExtensionModule.dylib
[Qt] Reason: tried: '/Users/myname/Slicer/Slicer-Release/teem-build/bin/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/System/Volumes/Preboot/Cryptexes/OS/Users/myname/Slicer/Slicer-Release/teem-build/bin/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/Users/myname/Slicer/Slicer-Release/qRestAPI-build/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/System/Volumes/Preboot/Cryptexes/OS/Users/myname/Slicer/Slicer-Release/qRestAPI-build/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/Users/myname/Slicer/Slicer-Release/teem-build/bin/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/System/Volumes/Preboot/Cryptexes/OS/Users/myname/Slicer/Slicer-Release/teem-build/bin/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/Users/myname/Slicer/Slicer-Release/qRestAPI-build/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/System/Volumes/Preboot/Cryptexes/OS/Users/myname/Slicer/Slicer-Release/qRestAPI-build/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file), 
 '/Applications/Slicer 5.8.1.app/Contents/Frameworks/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/Applications/Slicer 5.8.1.app/Contents/Frameworks/QtCore.framework/Versions/5/Frameworks/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/Applications/Slicer 5.8.1.app/Contents/MacOS/../lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file), 
 '/Users/svc-dashboard/D/S/A/CTK-build/CMakeExternals/Install/lib/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/CTK-build/CMakeExternals/Install/lib/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file), 
 '/Users/svc-dashboard/D/S/A/teem-build/bin/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file),
 '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/S/A/teem-build/bin/lib/Slicer-5.9/qt-loadable-modules/libvtkSlicerVolumesModuleLogic.dylib' (no such file))
</code></pre>
<p>I know that <code>libvtkSlicerVolumesModuleLogic.dylib</code> and my other linker files exists here:</p>
<pre><code class="lang-auto">/Applications/Slicer 5.8.1.app/Contents/lib/Slicer-5.8/qt-loadable-modules
</code></pre>
<p>For some reason it wasn’t even looking into the <code>/Applications/Slicer 5.8.1.app/Contents/lib</code> folder so I added it to rpath via <code>install_name_tool -add_rpath /Applications/Slicer\ 5.8.1.app/Contents libqSlicerVESCLModule.dylib</code>.</p>
<p>Slicer then looks in the right directory, but still can’t find the files because it looks in <code>Contents/lib/Slicer-5.9</code> instead of <code>Contents/lib/Slicer-5.8</code>. Also, Slicer 5.9 and 5.8.1 use different versions of some linker files (e.g.<code>libvtkWrappingTools-9.4.1.dylib</code> instead of <code>libvtkWrappingTools-9.2.1.dylib</code>) so they still can’t be found.</p>
<p>If I run <code>export Slicer_REVISION=33241</code> before building the extension (as per <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" rel="noopener nofollow ugc">link</a>), shouldn’t that be enough to avoid version issues? Or do I need to build the extension using the same version of Slicer that I plan to deploy it with (meaning, rebuilding my Slicer-Release from 3.8.1 source code)?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @pieper (2025-07-02 17:00 UTC)

<p>As a general rule, mixing C++ libraries across builds is not going to work.  Things like compiler versions, compile flags, exact dependencies, installation and packaging modifications, etc can all vary in ways that make the libraries incompatible.  That’s why the factory machines we use to make extension packages build against a Slicer build tree using the exact same build environment.</p>
<p>To simplify development and distribution of custom code you have two reasonable options.  If it’s public and ready for broader use you can submit a pull request to the extension manager and factories will make compatible builds for you (for all platform) and it’ll run the tests and post to the dashboard.  This can help track down platform-specific build and packaging issues.</p>
<p>But if you are just testing with a smaller group you can package your local Slicer build (i.e. <code>make package</code>) and give that to your testers a long with your extension.  In fact, you can install your package and your extension on your local machine, zip up the slicer install directory, and make the zip available for people to test.  You should be able to update your extension easily this way during development.</p>

---
