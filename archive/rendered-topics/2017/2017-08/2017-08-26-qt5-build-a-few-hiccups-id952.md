# Qt5 build : a few hiccups

**Topic ID**: 952
**Date**: 2017-08-26
**URL**: https://discourse.slicer.org/t/qt5-build-a-few-hiccups/952

---

## Post #1 by @chir.set (2017-08-26 11:26 UTC)

<p>After using the Qt5 build for one week, here are some minor problems.</p>
<ol>
<li>
<p>Whenever an item is selected in the Fiducial/ROI/Ruler tool, the items get duplicated to an certain number of items that I didn’t count.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa89445d8ab2550bf6afb8aa8a380eced2c674b.png" alt="Screenshot_20170826_130740" data-base62-sha1="AtEVV7AEqftFeWtX4oHegU9tXE7" width="132" height="345"></p>
</li>
<li>
<p>In Volume Rending module, the items of the ‘View’ combobox are no longer checkable.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f53338b31288eca77f18452a785b3a736ff594f.png" alt="Screenshot_20170826_130856" data-base62-sha1="2bzq2UgZ4AWVQObE4Hfp7PtQf03" width="454" height="184"></p>
</li>
<li>
<p>Switching to module ‘SceneViews’ crashes Slicer :</p>
</li>
</ol>
<ul>
<li><em>Switch to module:  “SceneViews”</em></li>
<li><em>qSlicerSceneViewsModuleWidgetPrivate::setupUi - Capture link not implemented with Qt5</em></li>
<li><em>qSlicerSceneViewsModuleWidgetPrivate::setupUi - Restore scroll bar position not implemented with Qt5</em><br>
As it says, it has yet to be implemented.</li>
</ul>
<p>All these are found on today’s build after ‘git pull’ (2017-08-26).</p>
<p>I think developers might be interested in this post.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2017-08-27 00:02 UTC)

<p>Thanks a lot for reporting - it’s very useful. I’ve added these issues to the <a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Slicer">Qt5 migration lab page</a>.</p>

---

## Post #3 by @chir.set (2017-09-23 15:14 UTC)

<p>May I report one more crash source with the QT5/VTK8 build:</p>
<p>Any tool in the <em>new</em> segment editor crashes Slicer as soon as the corresponding button is pressed. The old segment editor is still functional.</p>
<p>Best.</p>

---

## Post #4 by @lassoan (2017-09-23 18:57 UTC)

<p>Thanks, we’ll look into this! What operating system do you use?</p>

---

## Post #5 by @chir.set (2017-09-24 08:06 UTC)

<p>I use ArchLinux to build and run.</p>

---

## Post #6 by @cpinter (2017-10-12 14:43 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> The issue has been fixed just now in <a href="https://github.com/Slicer/Slicer/commit/7de0d6a6e71694ac808a2e73da3fd3c3300f708c">https://github.com/Slicer/Slicer/commit/7de0d6a6e71694ac808a2e73da3fd3c3300f708c</a></p>

---

## Post #7 by @chir.set (2017-10-16 09:03 UTC)

<p>Thanks. But when I click on ‘Show details’ as per attached image, Slicer crashes immediately.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b689d74f3748a75e410a3fc80cd18adbb036daa6.png" alt="Screenshot_20171016_105921" data-base62-sha1="q2OdO78ObgDWPtLpR55gHvDJ3Mi" width="571" height="255"></p>

---

## Post #8 by @cpinter (2017-10-16 14:13 UTC)

<p>Thanks for testing! Unfortunately I cannot reproduce this, as I only have a Windows build with Qt5. I’m building one on Mac now and see if it can be reproduced there. In the meantime <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> Can you please try to see if this is as easy to fix as the previous one? Thanks a lot!</p>

---

## Post #9 by @Davide_Punzo (2017-10-16 14:47 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/819" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/819</a> should fix it</p>

---

## Post #10 by @cpinter (2017-10-16 15:01 UTC)

<p>Thanks a lot, <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>! I integrated the pull request in <a href="https://github.com/Slicer/Slicer/commit/0c3f2cca8d11ed49d55724bca9ca166b08309d0d">https://github.com/Slicer/Slicer/commit/0c3f2cca8d11ed49d55724bca9ca166b08309d0d</a></p>
<p><a class="mention" href="/u/chir.set">@chir.set</a> Please don’t get discourdaged and keep sending us any issues you find <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #11 by @chir.set (2018-01-12 20:08 UTC)

<p>Slicer crashes in Threshold Scalar Volume on ‘Apply’, if ‘Below’ a threshold value is selected. It doesn’t crash if ‘Above’ or ‘Outside’ is chosen. Using Qt5/VTK9 build on Linux.</p>

---

## Post #12 by @chir.set (2018-01-12 20:12 UTC)

<p>Slicer will crash on application exit if the ‘Standard Quantitative’ pane has been shown, whether it is shown or not on exit. Using Qt5/VTK9 build on Linux.</p>

---

## Post #13 by @hherhold (2018-01-14 15:35 UTC)

<p>Qt5 build failing on OS X 10.12.6. Was working a few days ago, sorry I can’t be more specific than that.</p>
<p>Configured with:</p>
<p>/Applications/CMake.app/Contents/MacOS/CMake -DQt5_DIR:PATH=/usr/local/opt/qt</p>
<p>First errors:</p>
<ul>
<li>Skipping extension packaging: DataStore - Slicer_SOURCE_DIR is defined.</li>
</ul>
<hr>
<p>– Configuring remote module: CompareVolumes<br>
– Configuring Scripted module: CompareVolumes</p>
<hr>
<p>– Configuring remote module: LandmarkRegistration<br>
– Configuring Scripted module: LandmarkRegistration<br>
CMake Warning at Utilities/Scripts/SlicerWizard/doc/CMakeLists.txt:41 (message):<br>
Warning: sphinx-build not found: Python documentation will not be created</p>
<p>– Setting ‘CTEST_MODEL’ variable with default value ‘Experimental’<br>
– Setting ‘MIDAS_PACKAGE_URL’ variable with default value ‘<a href="http://slicer.kitware.com/midas3" rel="nofollow noopener">http://slicer.kitware.com/midas3</a>’<br>
– Setting ‘MIDAS_PACKAGE_EMAIL’ variable with default value ‘OBFUSCATED’<br>
– Setting ‘MIDAS_PACKAGE_API_KEY’ variable with default value ‘OBFUSCATED’<br>
– Setting CPACK_PACKAGE_NAME to ‘Slicer’<br>
– Setting CPACK_PACKAGE_VENDOR to ‘NA-MIC’<br>
– Setting CPACK_PACKAGE_VERSION_MAJOR to ‘4’<br>
– Setting CPACK_PACKAGE_VERSION_MINOR to ‘9’<br>
– Setting CPACK_PACKAGE_VERSION_PATCH to ‘0’<br>
– Setting CPACK_PACKAGE_VERSION to ‘4.9.0-2018-01-13’<br>
– Setting CPACK_PACKAGE_INSTALL_DIRECTORY to ‘Slicer 4.9.0-2018-01-13’<br>
– Setting CPACK_PACKAGE_DESCRIPTION_FILE to ‘/Users/hherhold/Development/slicer/Slicer/README.txt’<br>
– Setting CPACK_RESOURCE_FILE_LICENSE to ‘/Users/hherhold/Development/slicer/Slicer/License.txt’<br>
– Setting CPACK_PACKAGE_DESCRIPTION_SUMMARY to ‘Medical Visualization and Processing Environment for Research’<br>
– Setting CPACK_PACKAGE_ICON to ‘/Users/hherhold/Development/slicer/Slicer/Applications/SlicerApp/Resources/Slicer.icns’<br>
– Configuring done<br>
CMake Error at Libs/vtkAddon/CMakeLists.txt:94 (add_library):<br>
Cannot find source file:</p>
<pre><code>/Users/hherhold/Development/slicer/build-qt5/Slicer-build/Libs/vtkAddon/vtkAddonHierarchy.stamp.txt
</code></pre>
<p>Tried extensions .c .C .c++ .cc .cpp .cxx .m .M .mm .h .hh .h++ .hm .hpp<br>
.hxx .in .txx</p>
<p>CMake Error at Libs/vtkTeem/CMakeLists.txt:87 (add_library):<br>
Cannot find source file:</p>
<pre><code>/Users/hherhold/Development/slicer/build-qt5/Slicer-build/Libs/vtkTeem/vtkTeemHierarchy.stamp.txt
</code></pre>
<p>Tried extensions .c .C .c++ .cc .cpp .cxx .m .M .mm .h .hh .h++ .hm .hpp<br>
.hxx .in .txx</p>

---

## Post #14 by @cpinter (2018-01-14 16:48 UTC)

<p>Thanks! I will check out both issues on Monday.</p>

---

## Post #15 by @cpinter (2018-01-16 15:23 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a>  I’ve started a Mac build (although it’s 10.13.1), will let you know how it went.</p>
<p><a class="mention" href="/u/chir.set">@chir.set</a> I wasn’t able to reproduce the crash with either way, but I tried on Windows. If anyone uses Linux for development, please test this one. <a class="mention" href="/u/jcfr">@jcfr</a> could you try? Otherwise I’ll need to do a build on a VM. Thanks!</p>

---

## Post #16 by @jcfr (2018-01-16 15:30 UTC)

<blockquote>
<p>Qt5 build failing on OS X 10.12.6. Was working a few days ago, sorry I can’t be more specific than that<br>
Cannot find source file: … Libs/vtkTeem/vtkTeemHierarchy.stamp.txt</p>
</blockquote>
<p>Thanks to <a class="mention" href="/u/adamrankin">@adamrankin</a>, the issue related to VTK hierarchy stamps file should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26834">r26834</a></p>
<blockquote>
<p>ArchLinux … Any tool in the new segment editor crashes Slicer as soon as the corresponding button is pressed.</p>
</blockquote>
<p>I am not able to reproduce the crash.</p>
<p>If this is still an issue, setting up a VM may be the best way forward.</p>

---

## Post #17 by @Davide_Punzo (2018-01-16 22:57 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="16" data-topic="952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Any tool in the new segment editor crashes Slicer as soon as the corresponding button is pressed.</p>
</blockquote>
</aside>
<p>this was fixed in the past in <a href="https://github.com/Slicer/Slicer/pull/819" class="inline-onebox" rel="noopener nofollow ugc">Dual 3D mode: loading a scene with a single view node, second view is uninitialised · Issue #819 · Slicer/Slicer · GitHub</a> and <a href="https://github.com/Slicer/Slicer/commit/0c3f2cca8d11ed49d55724bca9ca166b08309d0d" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/commit/0c3f2cca8d11ed49d55724bca9ca166b08309d0d</a></p>
<p>Instead I confirm this one:</p>
<aside class="quote no-group" data-username="chir.set" data-post="12" data-topic="952" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Slicer will crash on application exit if the ‘Standard Quantitative’ pane has been shown, whether it is shown or not on exit. Using Qt5/VTK9 build on Linux.</p>
</blockquote>
</aside>
<p>Sorry, but I didn’t understand this other one:</p>
<aside class="quote no-group" data-username="chir.set" data-post="11" data-topic="952" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Slicer crashes in Threshold Scalar Volume on ‘Apply’, if ‘Below’ a threshold value is selected. It doesn’t crash if ‘Above’ or ‘Outside’ is chosen. Using Qt5/VTK9 build on Linux.</p>
</blockquote>
</aside>

---

## Post #18 by @Davide_Punzo (2018-01-16 23:01 UTC)

<p>In addition the linux version (at least my build)</p>
<ol>
<li>some &amp; still appear in the comboboxes and icons in modules and views seems much smaller<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2542091231050f85e26ae6f524fdd4c39f5f086f.jpeg" data-download-href="/uploads/short-url/5jB95NPolfXwM1zroqigyU04qrt.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2542091231050f85e26ae6f524fdd4c39f5f086f_2_690x375.jpg" alt="image" data-base62-sha1="5jB95NPolfXwM1zroqigyU04qrt" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2542091231050f85e26ae6f524fdd4c39f5f086f_2_690x375.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2542091231050f85e26ae6f524fdd4c39f5f086f_2_1035x562.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2542091231050f85e26ae6f524fdd4c39f5f086f_2_1380x750.jpg 2x" data-dominant-color="8B8B8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1854×1009 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
2)some menu have some misalignment. E.g. settings and data module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59159746568065e24b2c5aa8cd1bd94452a20e38.jpeg" data-download-href="/uploads/short-url/cI4KHhMeb80tYy5u3NjHtYA1g6c.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59159746568065e24b2c5aa8cd1bd94452a20e38_2_690x388.jpg" alt="image" data-base62-sha1="cI4KHhMeb80tYy5u3NjHtYA1g6c" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59159746568065e24b2c5aa8cd1bd94452a20e38_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59159746568065e24b2c5aa8cd1bd94452a20e38_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59159746568065e24b2c5aa8cd1bd94452a20e38_2_1380x776.jpg 2x" data-dominant-color="BCBCBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f33fe030c2057c3552ddd3ac985e9efffebeb1.jpeg" data-download-href="/uploads/short-url/jGmzx7Eos7vsweatEJarE3uZulb.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89f33fe030c2057c3552ddd3ac985e9efffebeb1_2_690x388.jpg" alt="image" data-base62-sha1="jGmzx7Eos7vsweatEJarE3uZulb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89f33fe030c2057c3552ddd3ac985e9efffebeb1_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89f33fe030c2057c3552ddd3ac985e9efffebeb1_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89f33fe030c2057c3552ddd3ac985e9efffebeb1_2_1380x776.jpg 2x" data-dominant-color="9697A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 497 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>

---

## Post #19 by @cpinter (2018-01-16 23:58 UTC)

<p>Thanks Davide! Was the module name in the module selector like this before (“Se&amp;gment Editor”)?<br>
Update: Nevermind I see the marking on the first screenshot.</p>

---

## Post #20 by @Davide_Punzo (2018-01-17 08:44 UTC)

<p>you are welcome! the &amp; issue (it shows in many places like the module menu, titles in plotting views, etc. ) was present before <a href="https://github.com/Slicer/Slicer/pull/864" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/864</a></p>
<p>The smaller icons (?), menu misalignment (ctkCollapsiblegroupbox?) and smaller ctkCollapsibleButton are a result of the new style set in <a href="https://github.com/Slicer/Slicer/pull/864" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/864</a>.</p>

---

## Post #21 by @chir.set (2018-01-17 10:05 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="17" data-topic="952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>Sorry, but I didn’t understand this other one:</p>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/621b81a378e7cb7d41819032327167ba0e5bebc4.png" alt="Screenshot_20180117_105350" data-base62-sha1="dZTIUbUUKHnOPxL3w5rnkAvKKzi" width="534" height="491"></p>
<p>In ‘Filtering/Threshold  scalar volume’ module : If ‘Threshold Type’ is set to ‘Below’, Slicer crashes when the ‘Apply’ button is clicked.</p>

---

## Post #22 by @Davide_Punzo (2018-01-17 10:47 UTC)

<p>ah ok, I thought you meant the threshold segmentation editor effect. At the moment I don’t have the filters in my build so I can’t check/fix.</p>
<p>asap I’ll try to fix the other one:</p>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="17" data-topic="952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>Slicer will crash on application exit if the ‘Standard Quantitative’ pane has been shown, whether it is shown or not on exit. Using Qt5/VTK9 build on Linux.</p>
</blockquote>
</aside>
<p>It will also be nice to report all these in an ordered manner in the mantis bug tracker</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/Slicer/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/issues" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/5a584ccb9ffdd30f33742e9a755ab2f6b404c8fc63533dc59482aa0b02778ef7/Slicer/Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/Slicer/issues" target="_blank" rel="noopener nofollow ugc">Issues · Slicer/Slicer</a></h3>

  <p>Multi-platform, free open source software for visualization and image computing. - Issues · Slicer/Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #23 by @Davide_Punzo (2018-01-17 11:09 UTC)

<p>reported in:<br>
<a href="https://issues.slicer.org/view.php?id=4494" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4494</a><br>
<a href="https://issues.slicer.org/view.php?id=4493" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4493</a><br>
<a href="https://issues.slicer.org/view.php?id=4492" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4492</a><br>
<a href="https://issues.slicer.org/view.php?id=4495" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4495</a></p>
<p>and for reference:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/Qt5Integration/" target="_blank" rel="nofollow noopener">ProjectWeek</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/Qt5Integration/" target="_blank" rel="nofollow noopener">ProjectWeek</a></h3>

<p>Website for NA-MIC Project Weeks</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<a href="https://issues.slicer.org/view_all_bug_page.php" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view_all_bug_page.php</a></p>

---

## Post #24 by @lassoan (2018-01-17 21:19 UTC)

<p>I’ve noticed that with the new OpenGL2 backend/VTK9/Qt5, slice browsing speed can be much slower: it is always at least 20% slower than using OpenGL backend/VTK7.1/Qt4, but sometimes it is 5-10FPS instead of the normal 50FPS. It seems to be related to how many synchronous OpenGL calls are used and if NVidia threaded optimization is enabled. I’ve added a ticket to track this issue: <a href="https://issues.slicer.org/view.php?id=4496">https://issues.slicer.org/view.php?id=4496</a>.</p>

---

## Post #26 by @chir.set (2018-01-18 13:41 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="21" data-topic="952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>In ‘Filtering/Threshold  scalar volume’ module : If ‘Threshold Type’ is set to ‘Below’, Slicer crashes when the ‘Apply’ button is clicked.</p>
</blockquote>
</aside>
<p>I could not reproduce it in the 20180116 build where there are no errors.<br>
A build from 20180107 gives the following errors with all default values :</p>
<blockquote>
<p>Threshold Scalar Volume standard error:</p>
<p>PARSE ERROR: Argument: (–thresholdtype)<br>
Value ‘&amp;Below’ does not meet constraint: Below|Above|Outside</p>
<p>Brief USAGE:</p>
<p>For complete USAGE and HELP type:<br>
/home/user/programs/Slicer-4.9.0-2018-01-07-linux-amd64/lib/Slicer-4.9/cli-modules/ThresholdScalarVolume --help</p>
</blockquote>
<p>I probably noticed that in an older build and its has since been fixed by the many recent changes.</p>

---

## Post #27 by @lassoan (2018-01-18 14:22 UTC)

<p>This seems to be the same bug as the extra <strong><em>&amp;</em></strong> characters appearing in the GUI, which is most likely caused by this <a href="https://bugs.kde.org/show_bug.cgi?id=337491">extremely ugly KDE bug</a> (which is intended to be a feature and it seems it has not been removed yet). In the bug report there are many links to duplicate reports, with lots of additional information.</p>
<p>Probably the same bug causes the duplication of tools in the toolbar.</p>

---

## Post #28 by @lassoan (2018-01-18 16:04 UTC)

<p>I’ve implemented a <a href="https://github.com/Slicer/Slicer/commit/cea9dcfd94bc1b670126c60a06a6950e5ead1c01">fix</a> for <a href="https://issues.slicer.org/view.php?id=4493">Threshold volume</a> and <a href="https://issues.slicer.org/view.php?id=4495">duplicated mouse mode icons</a> issues. The fixes do not address the issue of KDE altering text in the application, just changes Slicer to not rely on exact GUI text match in these specific cases. The KDE bug may cause other issues, so we should keep in mind that it is always a possible root cause for errors.</p>

---

## Post #29 by @jcfr (2018-01-24 00:05 UTC)

<p>2 posts were split to a new topic: <a href="/t/support-designer-launcher-argument-for-qt5-build/1917">Support --designer launcher argument for Qt5 build</a></p>

---
