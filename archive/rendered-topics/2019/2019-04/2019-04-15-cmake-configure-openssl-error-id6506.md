# CMake Configure OpenSSL Error

**Topic ID**: 6506
**Date**: 2019-04-15
**URL**: https://discourse.slicer.org/t/cmake-configure-openssl-error/6506

---

## Post #1 by @marcmclean (2019-04-15 15:43 UTC)

<p>When generating Slicer solution files, I get the following error:</p>
<p>CMake Error at SuperBuild/External_OpenSSL.cmake:241 (message):<br>
There is no pre-compiled version of OpenSSL 1.0.1h available for</p>
<p>this version of visual studio [1916].  You could either:</p>
<p>(1) disable SSL support configuring with option Slicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=OFF<br>
or<br>
(2) configure Slicer providing your own version of OpenSSL that matches the version<br>
of OpenSSL also used to compile Qt library.<br>
The options to specify are OPENSSL_INCLUDE_DIR, LIB_EAY_DEBUG, LIB_EAY_RELEASE,<br>
SSL_EAY_DEBUG and SSL_EAY_RELEASE.<br>
Call Stack (most recent call first):<br>
CMake/ExternalProjectDependency.cmake:842 (include)<br>
SuperBuild/External_curl.cmake:15 (ExternalProject_Include_Dependencies)<br>
CMake/ExternalProjectDependency.cmake:842 (include)<br>
CMake/ExternalProjectDependency.cmake:916 (ExternalProject_Include_Dependencies)<br>
SuperBuild.cmake:458 (ExternalProject_Include_Dependencies)<br>
CMakeLists.txt:670 (include)</p>
<p>I’m using:<br>
Current Generator: Visual Studio 15 2017<br>
Qt 5.12.2 msvc2017_64</p>
<p>I’ve never compiled Slicer from source before so maybe my configuration is not correct. Also, if I specify “v140” as the optional toolset, I get another set of errors but I have the VC++ 2015.3 v14.00(v140) toolset for desktop installed.</p>
<p>Any help would be appreciated.</p>
<p>Thank you,<br>
Marc McLean</p>

---

## Post #2 by @lassoan (2019-04-15 16:54 UTC)

<p>Officially supported compiler is VS2015 (this is what Python3.6 uses, so we cannot upgrade if we want to remain binary compatible). VS2015 toolset with VS2017 works (that’s what most of developers use). Make sure you use a 64-bit generator. If you have problems then post the error message that you get.</p>

---

## Post #3 by @marcmclean (2019-04-15 18:33 UTC)

<p>Hello Andras,</p>
<p>I’m sorry I don’t understand what you’re suggesting I should change.<br>
I’m using:<br>
Current Generator: Visual Studio 15 2017 (with VC++ 2015.3 v14.00(v140) installed)<br>
Qt 5.12.2 msvc2017_64</p>
<p>Is that not correct?<br>
A youtube video showing how to compile 3DSlicer would be very helpful.</p>
<p>Marc</p>

---

## Post #4 by @jcfr (2019-04-15 18:48 UTC)

<p>Selecting <code>Visual Studio 15 2017 (with VC++ 2015.3 v14.00(v140) installed)</code> means that Qt compiled for vs2015 should be used.</p>

---

## Post #5 by @lassoan (2019-04-15 19:07 UTC)

<p>Also, as described in the build instructions, you may need to use Qt-5.10 or older.</p>
<p>I think the easiest is to specify CMake arguments on the command-line, as shown here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows</a></p>

---

## Post #6 by @jamesobutler (2019-04-15 22:38 UTC)

<p>I think the Windows build instructions should probably be clarified to indicate the VS2015 toolset is required.</p>
<p>Currently it states the following below which seems to suggest building with VS2015(the toolset) is just an option and not a requirement.</p>
<blockquote>
<p>For building with VS2015, Qt version 5.10.x or older is required.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites_2" rel="noopener nofollow ugc">source</a></p>
</blockquote>
<p>Could someone update the wiki with an edit? I think you could just remove the “For building with VS2015” part of that sentence and make it clearer to understand.</p>

---

## Post #7 by @marcmclean (2019-04-15 22:53 UTC)

<p>Looking at the command-line code, the documentation states the following assumes the source is in c:\S4</p>
<p>“C:\Program Files\CMake\bin\cmake.exe” -G “Visual Studio 15 2017 Win64” -T “v140” -DQt5_DIR:PATH=C:\Qt\5.10.0\msvc2015_64\lib\cmake\Qt5 C:\D\S4</p>
<p>What is the last argument c:\D\S4? Where is the source c:\S4 specified? Per the cmake documentation, should the last argument be the source?</p>

---

## Post #8 by @jcfr (2019-04-15 23:00 UTC)

<blockquote>
<p>the documentation states the following assumes the source is in c:\S4</p>
</blockquote>
<p>Thanks pointing this out. I also just updated the wiki page to consistently use <code>C:\D\S4</code> and <code>C:\D\S4R</code></p>
<p>The motivation for using short paths is explained in the checkout section, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files" class="inline-onebox">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a></p>

---

## Post #9 by @marcmclean (2019-04-15 23:51 UTC)

<p>Using cmake from the command prompt or gui and using Qt 5.9.7 msvc2015_64 or Qt 5.12.2 msvc2015_64 and specifying the generator as Visual Studio 15 2017:<br>
if I specify the v140 toolset, I get the error:<br>
CMake Error at CMakeLists.txt:51 (project):<br>
No CMAKE_C_COMPILER could be found.</p>
<p>if I don’t specify the v140 toolset, I get the error:<br>
CMake Error at SuperBuild/External_OpenSSL.cmake:241 (message):<br>
There is no pre-compiled version of OpenSSL 1.0.1h available for<br>
this version of visual studio [1916].</p>
<p>What should I try next?<br>
Is the OpenSSL error related to the v140 toolset?</p>
<p>The reason I want to compile from source is to test 3DSlicer running in a browser like this simple demo I created in C#: <a href="http://3.16.153.64:6580/Cybele_Test_App/" rel="nofollow noopener">http://3.16.153.64:6580/Cybele_Test_App/</a></p>

---

## Post #10 by @jcfr (2019-04-15 23:55 UTC)

<aside class="quote no-group" data-username="marcmclean" data-post="9" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png" class="avatar"> marcmclean:</div>
<blockquote>
<p>if I specify the v140 toolset, I get the error:<br>
CMake Error at CMakeLists.txt:51 (project):<br>
No CMAKE_C_COMPILER could be found.</p>
</blockquote>
</aside>
<p>Could you confirm that the components <code>VC++ 2015.3 v14.00 (v140) toolset for desktop</code>  is installed ?</p>
<p>For more details, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Experimental.2Fdeprecated_build_environments" class="inline-onebox">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a></p>

---

## Post #11 by @jcfr (2019-04-15 23:58 UTC)

<aside class="quote no-group" data-username="marcmclean" data-post="9" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png" class="avatar"> marcmclean:</div>
<blockquote>
<p>Is the OpenSSL error related to the v140 toolset?</p>
</blockquote>
</aside>
<p>Yes. We do not have pre-compiled binaries of OpenSSL for this version of Visual Studio.</p>
<blockquote>
<p>I want to compile from source is to test 3DSlicer running in a browser like this simple demo I created</p>
</blockquote>
<p>Are you planning to build Slicer with webassembly or emscripten ? Or deploy it using amazon appstream ?</p>

---

## Post #12 by @marcmclean (2019-04-16 00:31 UTC)

<p>Yes, v140 toolset is installed<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9aa8063c73f144189a7481c2b2faeb4d366486d5.jpeg" data-download-href="/uploads/short-url/m49wiE8srCsPvSoscRPXMKx7wUJ.jpeg?dl=1" title="v140_install" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa8063c73f144189a7481c2b2faeb4d366486d5_2_517x294.jpeg" alt="v140_install" data-base62-sha1="m49wiE8srCsPvSoscRPXMKx7wUJ" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa8063c73f144189a7481c2b2faeb4d366486d5_2_517x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa8063c73f144189a7481c2b2faeb4d366486d5_2_775x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa8063c73f144189a7481c2b2faeb4d366486d5_2_1034x588.jpeg 2x" data-dominant-color="EBEBEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">v140_install</span><span class="informations">1319×752 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @marcmclean (2019-04-16 00:33 UTC)

<p>I planned on testing it with Cybele Thinfinity VirtualUI: <a href="https://www.cybelesoft.com/thinfinity/virtualui/" rel="nofollow noopener">https://www.cybelesoft.com/thinfinity/virtualui/</a></p>

---

## Post #14 by @marcmclean (2019-04-16 00:58 UTC)

<p>Do you know of anyone using Slicer on Amazon Appstream? I would not need to re-compile but the cost could be higher than using Cybele depending on the amount on time used.</p>
<p>With Cybele you have to re-compile including their libraries, but the cost is $69 USD per concurrent user, one time charge.</p>

---

## Post #15 by @lassoan (2019-04-16 01:00 UTC)

<aside class="quote no-group" data-username="marcmclean" data-post="9" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png" class="avatar"> marcmclean:</div>
<blockquote>
<p>No CMAKE_C_COMPILER could be found.</p>
</blockquote>
</aside>
<p>You might have multiple Visual Studio versions installed, installed in non-default location, or for some reason the installation may be corrupted.</p>
<p>Try restarting your computer, launch Visual Studio, start CMake from Visual Studio command prompt.</p>
<p>You may also try building a project using the v140 toolset: create a new project in desktop x64 project in Visual Studio, without CMake; right-click on the project (not the solution), choose Properties / General / Platform Toolset: “Visual Studio 2015 (v140)” - you may get a more meaningful error message if something is off.</p>
<aside class="quote no-group" data-username="marcmclean" data-post="13" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png" class="avatar"> marcmclean:</div>
<blockquote>
<p>I planned on testing it with Cybele Thinfinity VirtualUI</p>
</blockquote>
</aside>
<p>I had a quick look at Thinfinity VIrtualUI and it does not seem that it could run a Qt-based application. Slicer runs quite nicely in Docker, would that be an option for you?</p>

---

## Post #16 by @marcmclean (2019-04-16 01:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You might have multiple Visual Studio versions installed</p>
</blockquote>
</aside>
<p>Yes, I have both VS2015 and VS2017 installed. Do you know if that is a problem for CMake?</p>

---

## Post #17 by @marcmclean (2019-04-16 01:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer runs quite nicely in Docker, would that be an option for you?</p>
</blockquote>
</aside>
<p>The end users must be able to access Slicer through a browser. Is that possible using Docker?</p>

---

## Post #18 by @lassoan (2019-04-16 01:37 UTC)

<aside class="quote no-group" data-username="marcmclean" data-post="16" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png" class="avatar"> marcmclean:</div>
<blockquote>
<p>Yes, I have both VS2015 and VS2017 installed. Do you know if that is a problem for CMake?</p>
</blockquote>
</aside>
<p>This is most likely not a CMake error (the error indicates that CMake fails to build a simple test project with v140 toolset). If you install Visual Studio versions out of order (VS2017 first then VS2015) then it may corrupt the installation and uninstalling both and reinstalling in VS2015, VS2017 order might fix it. Were you be able to build a project with v140 without CMake as I described above?</p>
<aside class="quote no-group" data-username="marcmclean" data-post="17" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png" class="avatar"> marcmclean:</div>
<blockquote>
<p>The end users must be able to access Slicer through a browser. Is that possible using Docker?</p>
</blockquote>
</aside>
<p>Yes. Slicer runs in your browser with full GUI.</p>
<p>There is <a href="https://hub.docker.com/r/dit4c/dit4c-container-slicer">Slicer image with GUI available via web browser</a> but it’s quite old; and there are the <a href="https://discourse.slicer.org/t/slicer-docker-images/508">regularly updated images</a> but I don’t think any of them is configured to show the GUI in the browser.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> Is there a docker image of recent version of Slicer that has web-accessible GUI configured?</p>

---

## Post #19 by @pieper (2019-04-16 12:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="6506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> Is there a docker image of recent version of Slicer that has web-accessible GUI configured?</p>
</blockquote>
</aside>
<p>Yes, this version has 4.10.1:</p>
<pre><code class="lang-auto">docker run -d -p 8080:8080 --name slicer stevepieper/slicer
</code></pre>
<p>then open your browser to <a href="http://localhost:8080">http://localhost:8080</a> and click the X11 button (or you can use <a href="http://localhost:8080/x11/vnc.html?autoconnect=true&amp;path=x11/websockify">the direct link</a>).</p>
<p>I’ve been using this approach for a while and I find the performance to be good.  I’ve tested it on AWS, Google Cloud and other systems that support docker and it very reliable.</p>
<p>In the README there’s also info on how to use this for batch jobs.  I plan to use this quite a bit for some batch analysis jobs, for example using SlicerDMRI.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerDockers">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/dc2f796837ddaa3aa9b98e294f96a6623868cb0cc7a42b465625e6b04d840dc0/pieper/SlicerDockers" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers: docker config files for slicer</a></h3>

  <p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #20 by @lassoan (2019-04-16 16:07 UTC)

<p>Thanks a lot, this image works very well!</p>

---

## Post #21 by @marcmclean (2019-04-16 21:13 UTC)

<p>Steve, your container is really good. This could be very useful in environments where IT department’s policies make loading software difficult. This simplifies that significantly.</p>

---

## Post #22 by @jcfr (2019-04-16 21:32 UTC)

<p>That is great, we will look into updating the <a href="https://github.com/thewtex/SlicerDocker" rel="nofollow noopener">SlicerDocker</a> project so that up-to-date images are published daily.</p>
<p>Note that images used for Continuous integration are already published there daily.</p>

---

## Post #23 by @pieper (2019-04-17 14:18 UTC)

<p>Yes, having a dockerized version of each nighty build work be great for testing, especially for extensions.</p>

---
