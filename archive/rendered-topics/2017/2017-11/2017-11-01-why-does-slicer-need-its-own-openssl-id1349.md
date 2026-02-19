---
topic_id: 1349
title: "Why Does Slicer Need Its Own Openssl"
date: 2017-11-01
url: https://discourse.slicer.org/t/1349
---

# Why does Slicer need its own OpenSSL?

**Topic ID**: 1349
**Date**: 2017-11-01
**URL**: https://discourse.slicer.org/t/why-does-slicer-need-its-own-openssl/1349

---

## Post #1 by @gcsharp (2017-11-01 19:00 UTC)

<p>I’m looking into fixing this irritating bug:<br>
<a href="https://issues.slicer.org/view.php?id=4125" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4125</a></p>
<p>But first I have a question.  Why does Slicer need its own OpenSSL?  Could it work using the one my OS provides?</p>

---

## Post #2 by @jcfr (2017-11-01 20:23 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="1" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Why does Slicer need its own OpenSSL?</p>
</blockquote>
</aside>
<p>This was motivated to have a consistent environment on Linux, macOS and Windows.</p>
<aside class="quote no-group" data-username="gcsharp" data-post="1" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Could it work using the one my OS provides?</p>
</blockquote>
</aside>
<p>Since different Os ship if different version, it would be hard to ensure the distributed binaries works everywhere.</p>
<aside class="quote no-group quote-modified" data-username="gcsharp" data-post="1" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>I’m looking into fixing this irritating bug: <a href="https://issues.slicer.org/view.php?id=4125" class="inline-onebox">Linux crash at startup on fresh build · Issue #4125 · Slicer/Slicer · GitHub</a></p>
</blockquote>
</aside>
<p>We are also overdue for an OpenSSL update.</p>
<p>When I have some cycle, I will setup a VM to debut this</p>

---

## Post #3 by @gcsharp (2017-11-02 13:28 UTC)

<p>Thank you Jc.</p>
<p>Just to clarify, this is not about distributed binaries.  Those are fine.</p>
<p>I will try the OpenSSL update and report back.</p>

---

## Post #4 by @jcfr (2017-11-02 13:42 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="3" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>I will try the OpenSSL update and report back.</p>
</blockquote>
</aside>
<p>Great. In that case, I suggest you focus on Qt5 + VTK8. OpenSSL requirements for Qt 4.8 are different from the one of Qt5.</p>

---

## Post #5 by @gcsharp (2017-11-02 18:36 UTC)

<p>Confirm that Super-build upgrade to OpenSSL 1.0.2l resolves issue with<br>
Debian stable.  Slicer launches without crashing.  This test was<br>
performed with VTK 8 and Qt 5.7.1.</p>
<p>Older linux install may supply Qt linked against 1.0.1.  Possibly<br>
these will crash.</p>
<p>Would the next step be the below to generate windows?</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/jcfr/6030240" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/jcfr/6030240" target="_blank" rel="nofollow noopener">https://gist.github.com/jcfr/6030240</a></h4>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jcfr (2017-11-02 21:26 UTC)

<p>The good news is that the script has been updated (see <a href="https://gist.github.com/jamesobutler/f29a8edfe70cbdf7c3d94d25c20e1dce">here</a> and <a href="https://github.com/jcfr/qt-easy-build/pull/28">PR jcfr/qt-easy-build#28</a>).</p>
<p>We need to consolidate the windows OpenSSL build scripts and generate windows openssl archives</p>

---

## Post #7 by @gcsharp (2017-11-02 22:35 UTC)

<p>Wow, outstanding!  Is there anything I can do to help?</p>

---

## Post #8 by @gcsharp (2017-11-16 14:56 UTC)

<p>I tried to upload the new OpenSSL to midas, so I can create a pull<br>
request.  I don’t have permission to push to the OpenSSL community.<br>
Would a download from the midas personal folder be acceptable?</p>

---

## Post #9 by @jcfr (2017-11-16 15:11 UTC)

<p>Thanks Greg</p>
<p>Are you talking about generating OpenSSL build for windows ?</p>
<p>Which version of script did you use (a link to it would be great). I would then make sure the jcfr/qt-easy-build is up-to-date first.</p>

---

## Post #10 by @gcsharp (2017-11-16 15:26 UTC)

<p>First I was going to address linux by uploading the tarball.  That is the highest priority because of the build failure.</p>
<p>But yes, I did plan to proceed with windows after that.</p>

---

## Post #11 by @jcfr (2017-11-16 15:44 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="10" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>First I was going to address linux by uploading the tarball.</p>
</blockquote>
</aside>
<p>All set. See <a href="https://packages.kitware.com/item/10336">https://packages.kitware.com/item/10336</a></p>
<p>Soon we will transition away from <a href="http://packages.kitware.com">packages.kitware.com</a> and host the OpenSSL build artifacts in a project like <a href="https://github.com/Slicer/Slicer-OpenSSL" class="inline-onebox">GitHub - Slicer/Slicer-OpenSSL: OpenSSL sources and builds used in Slicer-based projects.</a></p>

---

## Post #12 by @chir.set (2017-11-16 16:13 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="5" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Confirm that Super-build upgrade to OpenSSL 1.0.2l resolves issue with</p>
<p>Debian stable.  Slicer launches without crashing.</p>
</blockquote>
</aside>
<p>Please note thta Arch Linux ships with openssl 1.1.0.g. Version 1.0.2.l is optional. If Slicer does not ship its own OpenSSL libs, it won’t run on all distros.</p>

---

## Post #13 by @gcsharp (2017-11-16 16:51 UTC)

<p>If Arch ships 1.1.0g, presumably it links Qt against 1.1.0g as well.</p>
<p>Are you saying this version not supported by PythonQt or curl or some other Slicer-provided dependency?</p>

---

## Post #14 by @gcsharp (2017-11-16 17:56 UTC)

<p>You’re the best Jc.  Pull request submitted.</p>

---

## Post #15 by @jcfr (2018-01-19 21:06 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> OpenSSL version used on Unix has been updated to <code>1.0.2n</code>. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26841">r26841</a></p>
<p>As a side note, your authorship will be restored when we transition to GitHub. See <a href="https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit#Authorship">https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit#Authorship</a></p>

---

## Post #16 by @jcfr (2018-02-01 14:21 UTC)

<p>To follow up on this, pre-built archive of OpenSSL 1.0.2n for VS2013 and VS2015 are now available. See <a href="https://github.com/Slicer/Slicer-OpenSSL">https://github.com/Slicer/Slicer-OpenSSL</a></p>

---

## Post #17 by @fedorov (2018-06-25 18:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> can you confirm - is Slicer supposed to build in Debug mode with binary-installed Qt5 on Mac with OpenSSL enabled</p>
<p>or</p>
<p>we need to compile Qt5 from source with SSL enabled to be able to enable SSL in Slicer?</p>
<p>I ran into a problem compiling Slicer on Mac, which seem to have disappeared after disabling SSL, but I could not find the answer in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instruction">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instruction</a> on whether I am supposed to do this or not.</p>

---

## Post #18 by @ihnorton (2018-06-25 19:34 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="17" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>is Slicer supposed to build in Debug mode with binary-installed Qt5 on Mac with OpenSSL enabled</p>
</blockquote>
</aside>
<p>FWIW, this is my primary build configuration, so I can confirm Debug build with PythonQt+SSL enabled works (aside from stepping in to upstream Qt library code, as expected). I’m using Qt 5.9.3 from the online installer, on macOS 10.12.</p>

---

## Post #19 by @fedorov (2018-06-25 20:46 UTC)

<p>Thanks <a class="mention" href="/u/ihnorton">@ihnorton</a>! I think that issue was related to command line tools being uninstalled/inaccessible as a result of Xcode update. I discovered this while looking for a solution to PCRE build issue. After installing the command line tools and restarting, I no longer had SSL problem.</p>
<p>Just one thing I didn’t understand: what did you mean by “aside from stepping in to upstream Qt library code, as expected”?</p>

---

## Post #20 by @ihnorton (2018-06-25 21:10 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="19" data-topic="1349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Just one thing I didn’t understand: what did you mean by “aside from stepping in to upstream Qt library code, as expected”?</p>
</blockquote>
</aside>
<p>I mean in the debugger: if you put a breakpoint in Slicer-build libraries then you can single-step through the file because they are built in debug mode. But you won’t be able to set a breakpoint in to a Qt library (QtCore.dylib etc.), and if you step in to one from Slicer you will just see assembly – because the Qt library is built in release mode, and doesn’t include mach-o symbols with location information for the debugger.</p>

---
