---
topic_id: 23345
title: "Error During Generation With Visual Studio"
date: 2022-05-09
url: https://discourse.slicer.org/t/23345
---

# Error during generation with Visual Studio

**Topic ID**: 23345
**Date**: 2022-05-09
**URL**: https://discourse.slicer.org/t/error-during-generation-with-visual-studio/23345

---

## Post #1 by @Shoshoda (2022-05-09 13:02 UTC)

<p>Hello everyone,<br>
I’m new to 3d slicer so maybe I’m doing it wrong but this is the error I get :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a08308c5fe634fd87522884c4d181004fe342564.png" data-download-href="/uploads/short-url/mTX8mzajtB4NKkBTEBNl7Z4a7Mo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a08308c5fe634fd87522884c4d181004fe342564.png" alt="image" data-base62-sha1="mTX8mzajtB4NKkBTEBNl7Z4a7Mo" width="690" height="106" data-dominant-color="323233"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1363×210 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried several time to build the project with CMAKE and Visual Studio on two differents computers(Windows 10 and 11)</p>
<p>Regards,<br>
Michael</p>

---

## Post #2 by @Shoshoda (2022-05-09 13:04 UTC)

<p>Hello everyone,<br>
I’m new to 3d slicer so maybe I’m doing it wrong but this is the error I get :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdb23b282de8fe6b8ad5dce99b3e8de284992660.png" data-download-href="/uploads/short-url/r486dlzp0FWLHOvhMd4gAC24Ryg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdb23b282de8fe6b8ad5dce99b3e8de284992660.png" alt="image" data-base62-sha1="r486dlzp0FWLHOvhMd4gAC24Ryg" width="690" height="40" data-dominant-color="464646"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1471×86 4.96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried several time to build the project with CMAKE and Visual Studio on two differents computers(Windows 10 and 11)</p>
<p>Regards,<br>
Michael</p>

---

## Post #3 by @Dwij_Mistry (2022-05-09 15:52 UTC)

<p><a class="mention" href="/u/shoshoda">@Shoshoda</a> are you getting only, this ONE error?</p>

---

## Post #4 by @Shoshoda (2022-05-09 16:29 UTC)

<p>Yes only this one, on both computer</p>

---

## Post #5 by @cpinter (2022-05-10 08:50 UTC)

<p>Still, this is very little information. A full log would definitely help.</p>
<p>Has the build otherwise succeed btw? Because I have seen similar errors (although I don’t speak French and from your screenshot I cannot copy-paste, so cannot say if the message itself is the same or not) in otherwise successful builds that then allowed running and debugging Slicer without problems.</p>

---

## Post #6 by @Shoshoda (2022-05-10 12:45 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="23345">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Has the build otherwise succeed btw? Because I have seen similar errors (although I don’t speak French and from your screenshot I cannot copy-paste, so cannot say if the message itself is the same or not) in otherwise successful builds that then allowed running and debugging Slicer without problems.</p>
</blockquote>
</aside>
<p>Yes sorry I didn’t notice that my screenshot was in french. There is copy-paste of the screenshot :</p>
<p>|Erreur|MSB8066|la build personnalisée de ‘C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-configure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-build.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-forceconfigure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\Slicer-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\Slicer.rule’ s’est arrêtée. Code 1.|Slicer|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|245||</p>
<hr>
<p>And here are the logs I get :</p>
<p>Performing configure step for ‘Slicer’<br>
loading initial cache file C:/D/S4R/Slicer-prefix/tmp/Slicer-cache-Release.cmake<br>
– Setting C++ standard<br>
– Setting C++ standard - C++14<br>
– Selecting Windows SDK version 10.0.22000.0 to target Windows 10.0.19043.</p>
<p>Slicer should not be configured &amp; built in the Slicer source directory<br>
You must run cmake in a build directory.<br>
For example:<br>
mkdir Slicer-sandbox ; cd Slicer-sandbox<br>
git clone <a href="https://github.com/Slicer/Slicer.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a> # or download &amp; unpack the source tarball<br>
mkdir Slicer-SuperBuild<br>
this will create the following directory structure</p>
<p>Slicer-sandbox<br>
±-Slicer<br>
±-Slicer-SuperBuild</p>
<p>Then you can proceed to configure and build<br>
by using the following commands</p>
<p>cd Slicer-SuperBuild<br>
cmake …/Slicer # or ccmake, or cmake-gui<br>
make</p>
<p>NOTE: Given that you already tried to make an in-source build<br>
CMake have already created several files &amp; directories<br>
in your source tree. run ‘git status’ to find them and<br>
remove them by doing:</p>
<pre><code>    cd Slicer-sandbox/Slicer
    git clean -n -d
    git clean -f -d
    git checkout --
</code></pre>
<p>CMake Error at CMake/PreventInSourceBuilds.cmake:42 (message):<br>
Quitting configuration<br>
Call Stack (most recent call first):<br>
CMake/PreventInSourceBuilds.cmake:46 (AssureOutOfSourceBuilds)<br>
CMakeLists.txt:93 (include)</p>
<p>– Configuring incomplete, errors occurred!<br>
See also “C:/D/S4/CMakeFiles/CMakeOutput.log”.<br>
C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(245,5): error MSB8066: la build personnalisée de ‘C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-configure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-build.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-forceconfigure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\Slicer-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\Slicer.rule’ s’est arrêtée. Code 1.</p>

---

## Post #7 by @cpinter (2022-05-10 15:45 UTC)

<aside class="quote no-group" data-username="Shoshoda" data-post="6" data-topic="23345">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/df705f/48.png" class="avatar"> Shoshoda:</div>
<blockquote>
<p>Slicer should not be configured &amp; built in the Slicer source directory</p>
</blockquote>
</aside>
<p>This looks like a good next point of attention.</p>

---

## Post #8 by @Shoshoda (2022-05-11 15:31 UTC)

<p>So it’s now working !<br>
I was working on two different folder like the doc say :  C:\D\S4 and C:\D\S4R<br>
but It’s wasn’t working.<br>
So I tried C:\D\S4\Slicer with the sources code and it’s finaly working fine.</p>
<p>Thanks for your help</p>
<p>Michael</p>

---

## Post #9 by @lassoan (2022-05-12 03:43 UTC)

<aside class="quote no-group" data-username="Shoshoda" data-post="8" data-topic="23345">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/df705f/48.png" class="avatar"> Shoshoda:</div>
<blockquote>
<p>C:\D\S4 and C:\D\S4R<br>
but It’s wasn’t working.<br>
So I tried C:\D\S4\Slicer with the sources code and it’s finaly working fine.</p>
</blockquote>
</aside>
<p>It is great to hear this!</p>
<p>It seems that the problem was that you checked out the source code into <code>C:\D\S4\Slicer</code> instead of <code>C:\D\S4</code>. This most likely happened because you have forgot the <code>.</code> from the command that was described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#set-up-source-and-build-folders">build instructions</a>: <code>git clone https://github.com/Slicer/Slicer.git .</code> (if you don’t have the <code>.</code> in the end then a <code>Slicer</code> subfolder is created).</p>

---
