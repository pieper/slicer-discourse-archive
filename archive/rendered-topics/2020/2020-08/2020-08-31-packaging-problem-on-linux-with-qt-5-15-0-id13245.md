# Packaging problem on Linux with Qt 5.15.0

**Topic ID**: 13245
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/packaging-problem-on-linux-with-qt-5-15-0/13245

---

## Post #1 by @cpinter (2020-08-31 10:11 UTC)

<p>I packaged a Slicer using the latest nightly and Ubuntu 18.04, gcc 7.5.0, and Qt 5.15.0, and when unpacking and executing it, Slicer fails to start due to an error<br>
<code>.../Slicer-4.11.0-2020-08-26-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libQt5QmlModels.so.5: cannot open shared object file: No such file or directory</code></p>
<p>When I manually copy the files <code>libQt5QmlModels.so.*</code> to the package, it works without problems.</p>
<p>There is some uncertainty about using Qt on Linux (see <a href="https://discourse.slicer.org/t/linux-build-instructions-lead-to-using-qt-5-9-5-on-ubuntu-18-04/13188">what I posted about it few days ago</a>). Also note that the factory builds still use an older Qt (5.11.2).</p>
<p>So I have two questions:</p>
<ol>
<li>Does anyone has an idea how to make sure the missing files are included in the package?</li>
<li>Are there plans updating the Linux build to 5.15.0? The build instructions (Qt 5.9.5), the actual version used by the factory (5.11.2), and the long-term Slicer plans (5.15.0) don’t seem to match.</li>
</ol>
<p>Thank you!</p>

---

## Post #2 by @jamesobutler (2020-08-31 12:17 UTC)

<p>The Linux build was updated to Qt 5.15 for a short period when the other platforms were being updated. However there were those errors as you explained above and there wasn’t any more effort in resolving those. You can read about the issues in <a href="https://github.com/Slicer/SlicerBuildEnvironment/issues/15" rel="nofollow noopener">https://github.com/Slicer/SlicerBuildEnvironment/issues/15</a></p>

---

## Post #3 by @jamesobutler (2020-08-31 12:21 UTC)

<p>An attempt was tried to update the SlicerBlockInstallQt.cmake but then that broke Windows packaging so it was reverted. <a href="https://github.com/Slicer/Slicer/commit/7da2ff7067218b28111f3c4ea1d6ad76147e0175" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/7da2ff7067218b28111f3c4ea1d6ad76147e0175</a></p>

---

## Post #4 by @cpinter (2020-08-31 13:04 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for the summary! Looking at the topics it seems two different problems. I only encountered one of them. I’ll take a look at the packaging issue in case I find a good solution.</p>

---

## Post #5 by @jcfr (2020-08-31 13:28 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thanks for your help working on this <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #6 by @cpinter (2020-09-01 08:36 UTC)

<p>The only thing that occurred to me so far is adding QmlModels only for Unix-type OS.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> Do you guys remember how <a href="https://github.com/Slicer/Slicer/commit/2a99657052a2cad890f7d1a754ba2ae76496aa76">adding it</a> broke the Windows packaging?</p>

---

## Post #7 by @Davide_Punzo (2020-09-01 08:40 UTC)

<p>Following this configuration <a href="https://github.com/Punzo/SlicerAstroApp#linux" rel="nofollow noopener">https://github.com/Punzo/SlicerAstroApp#linux</a> I had no issues, but it is true that then the binaries (<a href="https://github.com/Punzo/SlicerAstroApp/releases" rel="nofollow noopener">https://github.com/Punzo/SlicerAstroApp/releases</a>), in practise, will work only for other ubuntu 20.04 users.</p>
<p>Addittionally, at the kapteyn they built a working version of SlicerAstroApp on centos 7 (<a href="https://www.astro.rug.nl/~slicerastro/" rel="nofollow noopener">https://www.astro.rug.nl/~slicerastro/</a>) with Qt5.15.0 (I’ll ask all the building info later on and I’ll report), but then users on pretty old linux flavours got this at startup (as for the packing os information, I’ll write the os information asap):</p>
<p><em><strong>qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.</strong></em><br>
<em><strong>This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</strong></em><br>
<em><strong>Available platform plugins are: xcb.</strong></em></p>
<p><a class="mention" href="/u/vdhulst">@vdhulst</a> if you have the packing os info of centos 7, can you post them? thanks!</p>

---

## Post #8 by @Davide_Punzo (2020-09-01 10:01 UTC)

<p>the centos binaries in <a href="https://www.astro.rug.nl/~slicerastro/" rel="nofollow noopener">https://www.astro.rug.nl/~slicerastro/</a> have been compiled and packed with the slicer/buildenv-qt5-centos7:latest in <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="nofollow noopener">https://github.com/Slicer/SlicerBuildEnvironment</a>, i.e.:</p>
<p>centos 7.8<br>
cmake 3.17.1<br>
gcc 5.3.1 (Red Hat 5.3.1-6 from devtoolset 4)<br>
qt 5.15.0</p>
<p>and it seems that the qt plugin error in the previos post was because of the missing of the library libxcb-xinerama0 in the old user machine.</p>
<p>Now they are testing the build using the 4.11-2018.10.17 from <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="nofollow noopener">https://github.com/Slicer/SlicerBuildEnvironment</a></p>

---

## Post #9 by @jamesobutler (2020-09-01 12:20 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="13245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Do you guys remember how <a href="https://github.com/Slicer/Slicer/commit/2a99657052a2cad890f7d1a754ba2ae76496aa76" rel="noopener nofollow ugc">adding it</a> broke the Windows packaging?</p>
</blockquote>
</aside>
<p>It led to the following on Windows:</p>
<aside class="quote no-group" data-username="Lucas_Formighieri" data-post="1" data-topic="11827">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucas_formighieri/48/3266_2.png" class="avatar"><a href="https://discourse.slicer.org/t/latest-nightly-build-won-t-work/11827/1">Latest nightly build won´t work</a></div>
<blockquote>
<p>I kept receiving messages saying a series of dll files were missing (Qt5Core, Qt5Gui, Qt5Network, Qt5WebChannel, Qt5WebEngineWidgets, Qt5Widgets and Qt5Xml).</p>
</blockquote>
</aside>
<p>and on Linux:</p>
<aside class="quote no-group" data-username="Julio_Torres" data-post="1" data-topic="11834">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julio_torres/48/7020_2.png" class="avatar"><a href="https://discourse.slicer.org/t/error-executing-version-slicer-4-11-0-2020-06-01-linux-amd64-tar-gz-on-ubuntu-16-04/11834/1">Error executing version Slicer-4.11.0-2020-06-01-linux-amd64.tar.gz on Ubuntu 16.04</a></div>
<blockquote>
<p>qt.qpa.plugin: Could not load the Qt platform plugin “xcb” in “” even though it was found.<br>
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</p>
</blockquote>
</aside>

---

## Post #10 by @Lucas_Formighieri (2020-09-01 17:12 UTC)

<p>Hello,</p>
<p>I did not find a way around this installation problem. I reinstalled Windows and reinstalled Slicer. Since then, everything is running great.</p>
<p>Regards,</p>
<p>Lucas</p>

---

## Post #11 by @Davide_Punzo (2020-09-03 13:56 UTC)

<p>P.S.: <a class="mention" href="/u/cpinter">@cpinter</a> we tried the following kitware factory machine configuration:</p>
<p>centos 7.6<br>
cmake 3.13.4<br>
5.3.1 (Red Hat 5.3.1-6 from devtoolset 4)<br>
qt 5.11.2</p>
<p>and it produced a version working on all the linux flavours<br>
<a href="https://www.astro.rug.nl/~slicerastro/linux/SlicerAstro-1.1.2-el7-qt5.11.2.tar.gz" class="onebox" target="_blank" rel="nofollow noopener">https://www.astro.rug.nl/~slicerastro/linux/SlicerAstro-1.1.2-el7-qt5.11.2.tar.gz</a></p>
<p>It would be nice to have the Qt5.15.0 version. However, we didn’t manage to make a fully working Qt5.15.0 version on all the linux flavours and os versions. Although it was working on the majority of them, the recent ones at least, on old linux os you can have issues with libxcb-xinerama0 and also require an hack for packing krb5-libs. The configuration is:</p>
<p>centos 7.8<br>
cmake 3.17.1<br>
gcc 5.3.1 (Red Hat 5.3.1-6 from devtoolset 4)<br>
qt 5.15.0</p>
<p>P.S.2: I confirm that the packing wih <a href="https://github.com/Punzo/SlicerAstroApp#linux" rel="nofollow noopener">https://github.com/Punzo/SlicerAstroApp#linux</a>, but then the users need relatively “new” os linux versions.</p>

---

## Post #12 by @cpinter (2020-09-03 14:36 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="11" data-topic="13245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>Although it was working on the majority of them, the recent ones at least</p>
</blockquote>
</aside>
<p>Do you mean that <code>libQt5QmlModels.so.*</code> was successfully added to the package?</p>

---

## Post #13 by @Davide_Punzo (2020-09-03 20:25 UTC)

<p>I didn’t ckecked. I should have done. But we had no issue in running the app (however, I did’t check either if it was using system libraries for eventual missing ones). I’ll check tomorrow and I’ll let you know.</p>

---

## Post #14 by @Davide_Punzo (2020-09-04 08:33 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> so I checked on the version built with <a href="https://github.com/Punzo/SlicerAstroApp#linux" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Punzo/SlicerAstroApp: Astronomy (HI) customization of 3DSlicer with SlicerAstro (https://github.com/Punzo/SlicerAstro)</a> (ubuntu 20.04, gcc9.3, cmake 3.17.3, qt5.15.0). It is true that the libQt5QmlModels libraries are not packed, but from a fast analysis with ldd on SlicerAstroApp-real and few libs in the libs folder, I didn’t see any depedepence from libQt5QmlModels.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca82e0a59c72a6c41d783dd8fcfb90f42aba03dc.png" data-download-href="/uploads/short-url/sTuQSjrRizagL4tSTbBrYtHzc0Q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca82e0a59c72a6c41d783dd8fcfb90f42aba03dc_2_690x197.png" alt="image" data-base62-sha1="sTuQSjrRizagL4tSTbBrYtHzc0Q" width="690" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca82e0a59c72a6c41d783dd8fcfb90f42aba03dc_2_690x197.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca82e0a59c72a6c41d783dd8fcfb90f42aba03dc_2_1035x295.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca82e0a59c72a6c41d783dd8fcfb90f42aba03dc_2_1380x394.png 2x" data-dominant-color="292B41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1541×440 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can you point out which one require libQt5QmlModels?</p>
<p>P.S.: SlicerAstroApp is at Slicer commit 1ed419ef83bebe918cefbf78039cfc9d84967571 (14-08-2020)</p>
<p>P.S.2: I am interested to know, since I told to people that the Qt5.15 version in <a href="https://github.com/Punzo/SlicerAstroApp/releases/tag/1.1.2" class="inline-onebox" rel="noopener nofollow ugc">Release 1.1.2 · Punzo/SlicerAstroApp · GitHub</a> if used on ubuntu 20.04 will work <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> (and at least on 1 another laptop it worked)</p>

---

## Post #15 by @cpinter (2020-09-30 14:25 UTC)

<p>After the recent changes in Slicer CMake, the <code>libQt5QmlModels.so.*</code> files are properly packaged on Linux as well.</p>

---
