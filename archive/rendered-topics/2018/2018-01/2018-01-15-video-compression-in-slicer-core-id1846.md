---
topic_id: 1846
title: "Video Compression In Slicer Core"
date: 2018-01-15
url: https://discourse.slicer.org/t/1846
---

# Video compression in Slicer core

**Topic ID**: 1846
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/video-compression-in-slicer-core/1846

---

## Post #1 by @Sunderlandkyl (2018-01-15 15:13 UTC)

<p>Hi All,</p>
<p>With the growing desire to have video compression accessible within Slicer, it would be useful to have a discussion regarding how to go about integrating it into the Slicer core.</p>
<ol>
<li>
<p>Adding a video codec interface into the Slicer core:</p>
<ul>
<li>Due to licensing issues, it will be unfeasible to include some codecs within the Slicer core. This is particularly sensitive for commercial applications and Linux <a href="https://discourse.slicer.org/t/building-slicer-offline-for-inclusion-in-fedora/1838">distros</a>.</li>
<li>Several modules (OpenIGTLinkIF, Sequences, Screen Capture, etc.) also need to have access to the same video compression classes.</li>
<li>It may make sense to create a plugin interface in Slicer to register codecs which can be used by any extension.</li>
<li>Codecs could be downloaded individually through the extension manager, combined together in a codec pack, or registered by installed extensions.</li>
<li>This interface could interfere with the codecs in OpenIGTLink. How should these codecs be synchronized between Slicer and OpenIGTLink?</li>
</ul>
</li>
<li>
<p>A related topic is whether we should move OpenIGTLinkIF from the Slicer core to its own extension.</p>
<ul>
<li>This would allow OpenIGTLinkIF to receive more frequent updates, since we currently have no easy way of updating it for fixes and new features.</li>
<li>This is also affected by the video compression integration, due to the codec licensing issue. If OpenIGTLinkIF was moved to its own extension, then this would be less of an issue.</li>
</ul>
</li>
</ol>
<p>What are everyone’s thoughts?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/tokjun">@tokjun</a> (I couldn’t find Longquan’s username)</p>

---

## Post #2 by @leochan2009 (2018-01-15 15:35 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, This is Longquan <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I find it a good idea to move the OpenIGTLinkIF module to the extensions for fixing bugs and adding new features.</p>

---

## Post #3 by @lassoan (2018-01-15 15:35 UTC)

<p>I think topic 1 is quite clear - we would benefit a lot from having video compression infrastructure in the Slicer core, and having it in extensions would allow us greater flexibility and wider choice of codecs.</p>
<p>OpenIGTLinkIF in core/extension: I don’t see much advantage of having OpenIGTLinkIF in the core, other than slightly increased visibility of the feature (but IGT category name is not that welcoming and if people don’t know what the module is for, they cannot figure it out by opening the module), and there are many small disadvantages (we cannot update it in stable builds, we don’t get specific download statistics, the IGT category is not highlighted when we install IGT extensions, …). It seems that using custom codecs would be easier to set up if OpenIGTLinkIF is in a separate extension (OpenIGTLink library could use the codecs directly, there would be no need to create a dynamic codec plugin infrastructure in OpenIGTLink). So, to me it looks like overall it would make more sense to not bundle OpenIGTLinkIF with the Slicer core by default.</p>
<p>Adding <a class="mention" href="/u/ungi">@ungi</a> to the discussion as well.</p>

---

## Post #4 by @pieper (2018-01-15 15:47 UTC)

<p>+1 to moving OpenIGTLinkIF to an extension.</p>

---

## Post #5 by @lassoan (2018-01-15 19:58 UTC)

<p>I talked to <a class="mention" href="/u/ungi">@ungi</a> and he would have no objections to move out OpenIGTLinkIF either (he said he always installed SlicerIGT before doing anything anyway, and we could make SlicerIGT extension to depend on OpenIGTLink extension).</p>

---

## Post #6 by @tokjun (2018-01-16 14:20 UTC)

<p>I agree, moving OpenIGTLinkIF to an extension would make sense.</p>

---

## Post #7 by @tokjun (2018-01-16 14:29 UTC)

<p>As for the IGT category, I remember that we created and kept OpenIGTLinkIF there as a default module because we wanted to make the IGT activities visible in the Slicer community. But that was  when we had a lot more default modules in 3D Slicer. Now the users are expected to install extensions almost any type of research and I think the visibility in the default menu became less important.</p>

---

## Post #8 by @jcfr (2018-01-16 15:01 UTC)

<p>Should the extension be named <code>OpenIGTLink</code> and bundled both <code>OpenIGTLink</code> and <code>OpenIGTLinkIF</code> ?</p>

---

## Post #9 by @lassoan (2018-01-16 15:29 UTC)

<p>I agree, OpenIGTLink as extension name sounds good (maybe SlicerOpenIGTLink? but I think OpenIGTLink is enough). Repository name should be SlicerOpenIGTLink to make it clear in GitHub that this is a Slicer extension.</p>
<p>It would build OpenIGTLink and OpenIGTLinkIO libraries using superbuild.</p>

---

## Post #10 by @jcfr (2018-01-16 15:32 UTC)

<p>Great.</p>
<p>Could someone create the repo <code>SlicerOpenIGTLink</code> in <a href="https://github.com/openigtlink">https://github.com/openigtlink</a>  ?  (Or should it be hosted in the <code>Slicer</code> organization ?)</p>

---

## Post #11 by @leochan2009 (2018-01-16 16:37 UTC)

<p>Hi Jean,</p>
<p>I will make a repo in <a href="https://github.com/openigtlink" rel="nofollow noopener">https://github.com/openigtlink</a>, which i am currently maintaining and have full access to it.<br>
Once the video codec is added into the Slicer core, OpenIGTLink library will be able to link to the codec libraries and video streaming would be available in Slicer.</p>
<p>Best,<br>
Longquan</p>

---

## Post #12 by @jcfr (2018-01-16 18:24 UTC)

<aside class="quote no-group quote-modified" data-username="leochan2009" data-post="11" data-topic="1846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leochan2009/48/519_2.png" class="avatar"> leochan2009:</div>
<blockquote>
<p>I will make a repo in <a href="https://github.com/openigtlink" class="inline-onebox">OpenIGTLink · GitHub</a></p>
</blockquote>
</aside>
<p>Great, the consider giving push access to the following user: <code>@jcfr @lassoan @pieper @ungi</code></p>
<aside class="quote no-group" data-username="leochan2009" data-post="11" data-topic="1846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leochan2009/48/519_2.png" class="avatar"> leochan2009:</div>
<blockquote>
<p>Once the video codec is added into the Slicer core</p>
</blockquote>
</aside>
<p>After we create <code>SlicerOpenIGTLink</code> extension, how would we integrate the video codec ?</p>
<p>Should we also consider a <code>SlicerVideoCodec</code> extension ?</p>

---

## Post #13 by @leochan2009 (2018-01-16 18:56 UTC)

<p>SlicerVideoCodec could be a solution. The OpenH264 codec provides a link for binary download:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/cisco/openh264/releases">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/cisco/openh264/releases" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/ce573446a493621adee93eb79a2009776955f8b92030cf11fd8c2f9de40292f6/cisco/openh264" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/cisco/openh264/releases" target="_blank" rel="noopener nofollow ugc">Releases · cisco/openh264</a></h3>

  <p>Open Source H.264 Codec . Contribute to cisco/openh264 development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
So we should be able to trigger the download in the SlicerVideoCodec extension.<br>
Regarding the other codecs, i am not sure what would be the best method to integrate into slicer.</p>

---

## Post #14 by @lassoan (2018-01-16 20:27 UTC)

<p>We should probably add an abstract interface for video compression (and maybe also a trivial uncompressed storage class) into Slicer core and implement interface to register/unregister codecs, similarly to displayable managers.</p>

---

## Post #15 by @franklinwk (2018-01-18 15:33 UTC)

<p>From a user perspective I think there may be situations where OpenIGTLink is essential and expected despite access to the extension server being limited. Would it make sense to package a Slicer binary with “core extensions” along with a Slicer “Lite” without any?</p>

---

## Post #16 by @ungi (2018-01-19 03:13 UTC)

<p>There are two sides of this issue. If we don’t put OpenIGTLinkIF into an extension, it would be hard to add compressed video support. Not having compressed video is a blocking issue in many projects. On the other hand installing OpenIGTLinkIF from the extension manager or building a custom Slicer packaged with it already is not a impossible thing to do. For the sake of compressed video, I think we should go ahead with the extension plan.</p>

---

## Post #17 by @jcfr (2018-01-19 15:33 UTC)

<aside class="quote no-group" data-username="ungi" data-post="16" data-topic="1846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>think we should go ahead with the extension plan.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/leochan2009">@leochan2009</a> is making good progress. See <a href="https://github.com/openigtlink/SlicerOpenIGTLink" class="inline-onebox">GitHub - openigtlink/SlicerOpenIGTLink: OpenIGTLinkIF module as an Slicer Extension</a></p>
<p><a class="mention" href="/u/leochan2009">@leochan2009</a> Let me know if you need help removing the OpenIGTLink build options from Slicer build system.</p>

---

## Post #18 by @leochan2009 (2018-01-19 16:29 UTC)

<p>Hi All,</p>
<p>I just create a pull request for SlicerOpenIGTLink extension.<br>
As the codec is not available in the Slicer core yet, in the extension, VP9 codec is super-built for linux/Mac, however, it is not easy to superbuild VP9 in windows platform,  so i trigger the download of binary file from this repository for the window platform:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/openigtlink/CodecLibrariesFile">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/openigtlink/CodecLibrariesFile" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/781caf72b11b6366dbe4d05f829f172108fadc1f6dbe270df51c4b998b4ab2ec/openigtlink/CodecLibrariesFile" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/openigtlink/CodecLibrariesFile" target="_blank" rel="noopener nofollow ugc">GitHub - openigtlink/CodecLibrariesFile: Place to stored the compiled codec...</a></h3>

  <p>Place to stored the compiled codec libraries. Contribute to openigtlink/CodecLibrariesFile development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Currently i only uploaded the binary file compiled with “Visual Studio 14 2015”.  I think Slicer nightly build is using “Visual Studio 12 2013”, am i right?  So in windows build Slicer, video streaming will not be available.<br>
unfortunately, i didn’t find binary distributions from webmproject, would be nice if you guys find binary distrubution for other compilers.</p>

---

## Post #19 by @leochan2009 (2018-01-19 16:36 UTC)

<p>Hi Jean,</p>
<p>I just pull another request to remove the OpenIGTLink from the core. I test the build on my Mac machine, it seems working, would be great if you have a double check.</p>
<p>Best,<br>
Longquan</p>

---

## Post #20 by @leochan2009 (2018-01-21 01:53 UTC)

<p>Hi Jean <a class="mention" href="/u/jcfr">@jcfr</a> ,</p>
<p>The build of OpenIGTLinkIF extension failed unfortunately:<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1181930" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1181930</a><br>
The reason is the version of python interpreter. To build VP9, i current set the python version to be 2.7, however, the slicer build system only have 2.6.5 installed. Please refer the above link for more information.<br>
Regarding the windows build, the Slicer is building the extension using “Visual Studio 12 2013 Win64”, <a href="http://slicer.cdash.org/buildSummary.php?buildid=1181801" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1181801</a><br>
So I think once we have the VP9 library available, we should able to make the build successful. I am working with Andras in this issue. Hopefully will fix it soon.</p>
<p>Best,<br>
Longquan</p>

---

## Post #21 by @lassoan (2018-01-21 02:40 UTC)

<p>You can use Slicer’s Python 2.7 interpreter if there is no system Python or if it’s too old.<br>
Why do you need Python for building?</p>

---

## Post #22 by @leochan2009 (2018-01-21 02:52 UTC)

<p>Because the Linux/Mac system built VP9 in OpenIGTlink, which depends on YASM, and YASM is superbuilt too. To  build YASM, a python interpreter is used.</p>

---

## Post #23 by @leochan2009 (2018-01-22 18:39 UTC)

<p>Hi Andras, hi Jean <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Just a short question, i am currently using slicer-build python interpreter to build YASM, however, i try the python interpreter at  following folders:</p>
<pre><code class="lang-auto">Path/To/Slicer-build/python-build/bin/python
Path/To/Slicer-build/python-install/bin/python
Path/To/Slicer-build/python-install/bin/SlicerPython
</code></pre>
<p>the build of YASM was successful. however, when i use the yasm to build VP9, the following error occurred:<br>
<strong>yasm: FATAL: could not load standard modules</strong></p>
<p>Do you possible know the solution to this problem?</p>
<p>Best,<br>
Longquan</p>

---

## Post #24 by @lassoan (2018-01-22 18:48 UTC)

<p>Probably you have to add the folder where yasmstd library is located to Python paths.</p>

---

## Post #25 by @leochan2009 (2018-01-23 22:44 UTC)

<p>Hi All,</p>
<p>I just checked the Slicer nightly build of OpenIGTLinkIF module.<br>
It failed on building vp9 codec. the reason is the compiler “Clang 3.1.0” is too old, do you guys have any suggestion?</p>
<p>Best,<br>
Longquan</p>

---

## Post #26 by @lassoan (2018-01-23 23:26 UTC)

<p>I know that the compiler will be updated on Windows from VS2013 to VS2015 for nightly builds within a couple of days. I’m not sure if compiler update is planned for MacOSX as well (we used an old build toolset for compatibility with old systems).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #27 by @jcfr (2018-01-24 00:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="1846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not sure if compiler update is planned for MacOSX as well</p>
</blockquote>
</aside>
<p>See <a href="https://discourse.slicer.org/t/transition-of-nightly-nuild-to-qt5-vtk9-cmake-3-9-and-c-11/1918" class="inline-onebox">Transition of nightly build to Qt5, VTK9, CMake 3.9 and C++11</a></p>

---

## Post #28 by @leochan2009 (2018-01-24 02:57 UTC)

<p>Great!<br>
I made the vp9 binaries under vs 2015 for 32 bit and 64 bit already. So in the next days we could have the new OpenIGTLink in the nightly build slicer for windows system.<br>
Also the clang version in MacOSX is sufficient for VP9 built. I am looking forward to see the build result!</p>
<p>Best,<br>
Longquan</p>

---
