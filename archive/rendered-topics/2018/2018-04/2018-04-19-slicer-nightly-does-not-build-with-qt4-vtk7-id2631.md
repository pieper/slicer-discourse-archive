# Slicer nightly does not build with Qt4/VTK7

**Topic ID**: 2631
**Date**: 2018-04-19
**URL**: https://discourse.slicer.org/t/slicer-nightly-does-not-build-with-qt4-vtk7/2631

---

## Post #1 by @Eloise (2018-04-19 09:57 UTC)

<p>Hello,</p>
<p>I am trying to build Slicer (developper mode) on Mac osX running Sierra (version 10.12). I’ve downloaded the latest sources (April 17 2018) with git and I am currently getting this error message below when building with cmake (3.11.1). I am using CMAKE_BUILD_TYPE set to Release,  CMAKE_OSX_DEPLOYMENT_TARGET set to 10.12 (tried 10.9 but got the same error), and Xcode version 8.3.3.</p>
<p>The build fails on “VTKITKVectorReader” target with the following error :</p>
<p>‘vtkDiscreteFlyingEdges3D.h’ file not found</p>
<p>Is there any compatibility problem with the latest sources (in particular VTK, I use VTK7) and Sierra? Did anyone have successfully built the latest Slicer on Sierra?</p>
<p>Thanks.</p>

---

## Post #2 by @ihnorton (2018-04-19 13:12 UTC)

<p>Which qt version, and from where did you download or build?</p>

---

## Post #3 by @Eloise (2018-04-19 13:48 UTC)

<p>Hi,</p>
<p>I have qt 4.7.4 and I download the sources from git repository (command : git clone <a href="https://github.com/Slicer/Slicer.git" rel="nofollow noopener">https://github.com/Slicer/Slicer.git</a>, version 4.9)<br>
Actually, the problem mentioned in my previous post is solved, I guess it came from git/https protocol I used. But I have another building issue, I get different errors referring to "use of undeclared identifier " from DCMTK, it seems that the building of this version of Slicer requires C++11 ?</p>
<p>Thanks for your help</p>

---

## Post #4 by @ihnorton (2018-04-19 14:04 UTC)

<p>I’ve seen some discussion of the <code>undeclared identifier</code> problem, but I thought that had been fixed with a DCMTK update.</p>
<p>If you don’t have a reason to use Qt4, I would suggest starting with Qt5, because that is the most maintained/tested now, and will build everything with C++11. I am successfully building on macOS 10.12 against Qt 5.10.1 from <a href="http://download.qt.io/official_releases/qt/5.10/5.10.1/">http://download.qt.io/official_releases/qt/5.10/5.10.1/</a></p>
<p>If you do need Qt4 then somebody can try to debug, but otherwise please try Qt5 using <a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status">these instructions</a>. eg on my computer:</p>
<pre><code class="lang-auto">cd /opt/bld/r/r5nj
ccmake -DQt5_DIR=/opt/sw/Qt_ol/5.10.1/clang_64/lib/cmake/Qt5 ~/git/s5
</code></pre>
<p>note that the base path for your build should be a relatively short path, in order to avoid errors described <a href="https://discourse.slicer.org/t/macos-sierra-10-12-6-dynamic-linker-errors/2339">here</a>. I would suggest staying under about 20 characters or so.</p>

---

## Post #5 by @Eloise (2018-04-20 14:15 UTC)

<p>Thanks for your reply.<br>
I followed your suggestions, since I don’t specifically need Qt4, I tried building Slicer using Qt5, I got a new error during the SVN checkout of EMSegment  :</p>
<p>svn: E000060: Operation timed out</p>
<p>I have svn version 1.9.4, I can’t find where the error comes from ?</p>

---

## Post #6 by @ihnorton (2018-04-20 16:29 UTC)

<p>I saw that issue yesterday, and turned off building EMSegment off with <code>-DSlicer_BUILD_EMSegment:BOOL=OFF</code> (or setting it in the CMake GUI, under Advanced options). I normally do turn it off because I don’t need it, but forgot for that build.</p>
<p>There may be an intermittent network issue with the SVN server, however I just now tried it again (<code>svn co http://svn.slicer.org/Slicer3/branches/Slicer4-EMSegment</code>) and it worked.</p>

---

## Post #7 by @lassoan (2018-04-21 19:17 UTC)

<aside class="quote no-group" data-username="Eloise" data-post="1" data-topic="2631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eloise/48/3948_2.png" class="avatar"> Eloise:</div>
<blockquote>
<p>‘vtkDiscreteFlyingEdges3D.h’ file not found</p>
</blockquote>
</aside>
<p>I’ve recently made some changes in the Slicer trunk that require VTK9. if you build with Qt4/VTK7?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you still need VTK7/Qt4 compatibility in the trunk?</p>

---

## Post #8 by @jcfr (2018-04-21 19:29 UTC)

<p>Later this week, I will check with our team and report back.</p>
<p>Note that I will have limited access to internet until Wed evening (pacific time)</p>

---

## Post #9 by @Eloise (2018-04-23 09:50 UTC)

<p>Hi,</p>
<p>I turned off building of EMSegment as suggested by Isaiah and the compilation worked finally !!<br>
Thank you very much!</p>

---

## Post #10 by @wpgao (2018-04-26 06:42 UTC)

<p>Hi guys,</p>
<p>Recently, I builded Slicer on Window 10 with qt 4.8.7 and got following error.<br>
Slicer\Libs\vtkSegmentationCore\vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx(28): fatal error C1083: Cannot open include file: ‘vtkDiscreteFlyingEdges3D.h’: No such file or directory [F:\S4R\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] It seems that it is related to vtk version. Can anybody give any advice. Thanks!</p>
<p>Operating system: Win 10<br>
Slicer version: 4.9<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #11 by @lassoan (2018-04-26 12:42 UTC)

<p><a class="mention" href="/u/wpgao">@wpgao</a> I’ve moved your post here, as it is a duplicate of this report.</p>

---

## Post #12 by @lassoan (2018-04-26 19:31 UTC)

<p>I have <a href="https://github.com/Slicer/Slicer/commit/ea976db9beaa7ca1774b97f6d77769237fb0775a">updated code in the trunk</a> to allow building with both Qt5/VTK9 and Qt4/VTK7. Note that VTK7/Qt4 support will be dropped latest after the next stable build (Slicer-4.10) will be released, probably in a couple of weeks.</p>

---

## Post #13 by @wpgao (2018-04-27 13:37 UTC)

<p>Hi Andras,</p>
<p>Thanks for you information. I have a question about Qt5: whether it should be build with openssl? Since 3D slicer is updated frequently, the module developed using c++ under the older version can not work in the new version. Is there any way to let the module work in the new version easily? I’m not good at this. Forgive me , if the question is too simple!</p>
<p>Thanks again!</p>
<p>Best,</p>
<p>Wenpeng</p>

---

## Post #14 by @lassoan (2018-04-27 17:33 UTC)

<p>You should be able to still build Slicer with VTK7/Qt4 (I’ve made breaking changes conditional, based on the VTK version), so in the short term you can still build using Qt4.</p>
<p>Qt5 build: SSL is not required, but if you don’t use a Qt that has been built with OpenSSL then downloads through https protocol will fail (sample data, extension manager, etc. uses https for most downloads).</p>

---

## Post #15 by @jcfr (2018-04-28 06:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="2631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that VTK7/Qt4 support will be dropped latest after the next stable build (Slicer-4.10) will be released</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="2631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You should be able to still build Slicer with VTK7/Qt4 (I’ve made breaking changes conditional, based on the VTK version), so in the short term you can still build using Qt4.</p>
</blockquote>
</aside>
<p>Thanks for implementing the fixes.</p>

---
