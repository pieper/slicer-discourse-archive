---
topic_id: 22457
title: "No Downloaded Modules Are Loading Into Slicer"
date: 2022-03-11
url: https://discourse.slicer.org/t/22457
---

# No downloaded modules are loading into Slicer

**Topic ID**: 22457
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/no-downloaded-modules-are-loading-into-slicer/22457

---

## Post #1 by @Steven_A (2022-03-11 16:32 UTC)

<p>Slicer 4.13.0. I am trying to load up modules from the installation path, but for some reason I am getting the folowing errors:<br>
Error <span class="hashtag">#1</span> while writing setting “Modules/AdditionalPaths”</p>
<p>Error <span class="hashtag">#1</span> while writing setting “Modules/IgnoreModules”</p>
<p>Error <span class="hashtag">#1</span> while writing setting “Extensions/ManagerEnabled”</p>
<p>Error <span class="hashtag">#1</span> while writing setting “Extensions/ServerUrl”</p>
<p>Error <span class="hashtag">#1</span> while writing setting “Extensions/FrontendServerUrl”</p>
<p>Error <span class="hashtag">#1</span> while writing setting “Extensions/InstallPath”</p>
<p>In addition, when I search through the extensions manager, I cannot find SlicerMorph or SlicerRadiomics.</p>

---

## Post #2 by @pieper (2022-03-11 17:56 UTC)

<p>Those errors would indicate something wrong with the directory where your settings are stored, like maybe it’s not writable.</p>

---

## Post #3 by @Steven_A (2022-03-11 18:12 UTC)

<p>So, I have figured out the problem. I am installing 3D Slicer onto our department annotation station computers for the med students, and they installed it into a general account for the office use to have everyone have access. Unfortunately, this also means that in order to install packages and have everyone have access, I have to install them through the general account as well. Now the main problem is that I cannot install the modules I need from the Extension Manager. So I cannot install SlicerMorph and SlicerRadiomics from this preview build (4.13.0).</p>

---

## Post #4 by @lassoan (2022-03-14 02:40 UTC)

<p>The easiest solution is to unpack Slicer into your own user folder. Recent Slicer Preview Releases are fully portable, no installation is needed at all, it runs the same way from any location (even from a USB stick).</p>

---

## Post #5 by @Steven_A (2022-03-14 17:50 UTC)

<p>So, this may be a stupid question, but is there a way to copy a folder containing a module of SlicerRadiomics onto a USB stick with Slicer and add that to the path in order to access it, because I have the installation on my personal laptop and my school desktop, but I need to have access to it on different computers, and the extension manager isn’t showing SlicerRadiomics still. It is showing SlicerMorph now though.</p>

---

## Post #6 by @rbumm (2022-03-14 18:35 UTC)

<p>Yes, that should be possible by clicking here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5513d1bd1fe912caf0de00fed6f541d3018b1438.png" data-download-href="/uploads/short-url/c8D2X4vyK9bu5cexyUtTn8Q7ACI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5513d1bd1fe912caf0de00fed6f541d3018b1438_2_677x500.png" alt="image" data-base62-sha1="c8D2X4vyK9bu5cexyUtTn8Q7ACI" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5513d1bd1fe912caf0de00fed6f541d3018b1438_2_677x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5513d1bd1fe912caf0de00fed6f541d3018b1438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5513d1bd1fe912caf0de00fed6f541d3018b1438.png 2x" data-dominant-color="D4D5D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×643 66.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then adding the path to the extension here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b926b671b129e0a3cd6cee350ca2833ae9f6e044.png" data-download-href="/uploads/short-url/qpVgXwQVbGqazO8clzLl4QkcdKc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b926b671b129e0a3cd6cee350ca2833ae9f6e044_2_612x500.png" alt="image" data-base62-sha1="qpVgXwQVbGqazO8clzLl4QkcdKc" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b926b671b129e0a3cd6cee350ca2833ae9f6e044_2_612x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b926b671b129e0a3cd6cee350ca2833ae9f6e044.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b926b671b129e0a3cd6cee350ca2833ae9f6e044.png 2x" data-dominant-color="CCCDD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×697 70.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All this is in “Application settings”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/133f378ec9d20d1e9e0a70933d135b9561c6069e.png" alt="image" data-base62-sha1="2KgvQZgyPk0Fwz6CFfatz4raglE" width="353" height="160"></p>

---

## Post #7 by @Steven_A (2022-03-14 18:41 UTC)

<p>The issue is, when I do that, it gives me the error previously reported, saying that it cannot load said module.</p>

---

## Post #8 by @rbumm (2022-03-14 18:46 UTC)

<p>On your hospital network?</p>

---

## Post #9 by @rbumm (2022-03-14 18:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="22457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>your settings</p>
</blockquote>
</aside>
<p>As <a class="mention" href="/u/pieper">@pieper</a> said, the error probably indicates that you do not have write access to the Slicer installation folder, usually C:\Users\Yourname\AppData\Local\NA-MIC\</p>

---

## Post #10 by @rbumm (2022-03-14 19:21 UTC)

<p>Can you try the following:</p>
<p>Start Slicer and install the extensions you need on your private laptop.<br>
Exit Slicer.<br>
The installation folder on C:\Users\Yourname\AppData\Local\NA-MIC\Slicer4.13.0-xxx-xx-xx now contains the extensions you need.<br>
Then copy the Slicer installation directory to a USB stick like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6423086adb4f89ccac9cb7a0fe2955d829dd3489.png" data-download-href="/uploads/short-url/ehQNT3uadZG0BfHt6MgcARYXOad.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6423086adb4f89ccac9cb7a0fe2955d829dd3489.png" alt="image" data-base62-sha1="ehQNT3uadZG0BfHt6MgcARYXOad" width="663" height="500" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">815×614 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Run Slicer.exe from the USB on your hospital system.</p>

---

## Post #11 by @Steven_A (2022-03-17 07:10 UTC)

<p>That seems to have worked, thank you.</p>

---

## Post #12 by @tbillah (2024-01-16 23:07 UTC)

<p>Steven, I worked out this solution with Slicer developers a few years back. Would this be helpful to you?</p>
<aside class="quote quote-modified" data-post="2" data-topic="7511">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/installing-extensions-in-binary-distribution-of-slicer/7511/2">Installing extensions in binary distribution of Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Assuming the user where Slicer and the extensions are installed is called slicer, the idea is to create a script called SlicerWithExtensions.sh along side the Slicer launcher in your shared installation. 
The script only need to be updated with the name of the user under which Slicer  is installed on the cluster: 
#!/bin/bash -e

# This is the username associated with the Slicer installation to share between users.
slicer_user=jcfr # TODO: Update this line

script_dir=$(cd $(dirname $0) || exit …
  </blockquote>
</aside>


---

## Post #13 by @baderstine (2025-02-10 18:40 UTC)

<p>I’m getting this same set of errors on a new clean install of 5.8.0 on windows machine on which 5.6.2 works perfectly fine.  Is there some reason why 5.8.0 would not work the same as 5.6.2 on the same machine?  As far as I can tell they are using essentially the same installation paths with the same permissions - the only difference being that one uses the /Slicer 5.6.2/ folder and the other uses the /Slicer 5.8.0/ folder.</p>
<pre><code class="lang-auto">Python 3.9.10 (main, Jan 23 2025, 23:04:06) [MSC v.1942 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
[Qt] Error #1 while writing setting "Modules/AdditionalPaths"
[Qt] Error #1 while writing setting "Modules/IgnoreModules"
[Qt] Error #1 while writing setting "Extensions/ManagerEnabled"
[Qt] Error #1 while writing setting "Extensions/ServerUrl"
[Qt] Error #1 while writing setting "Extensions/FrontendServerUrl"
[Qt] Error #1 while writing setting "Extensions/InstallPath"
</code></pre>

---

## Post #14 by @baderstine (2025-08-07 21:17 UTC)

<p>The answer I discovered was that I had installed 5.6.2 “As Administrator” which worked fine.  But did not work fine for 5.8.0/1.  It “just works” if I install 5.8.1 as a regular user.</p>

---

## Post #15 by @lassoan (2025-09-02 12:16 UTC)

<p>Since 2021 Slicer install tree has been fully portable: it can store all settings and extensions in the installation folder and the application can be launched from anywhere, without installation, by any user. This has the side effect that the installation folder has to be writable. See some more information here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="15410">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-is-now-fully-portable/15410">Slicer is now fully portable</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Slicer can now be run from a portable drive (external drive, USB stick), along with all extensions, Python packages, settings, DICOM database, etc. - without installation. This can be used for easy distribution of Slicer to users, for example to be used as a free DICOM viewer for a folder full of DICOM files, or handing out preconfigured Slicer instance for a training course (see <a href="https://discourse.slicer.org/t/portable-installation-of-slicer-with-extension-on-usb/8582">this related request</a>). Since cache directory can be made local, too, the cache can be prepopulated with sample data s…
  </blockquote>
</aside>

<p>Slicer can be built with <code>Slicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR=OFF</code> to store settings and extensions in the user profile by default, but extensions that need to install additional Python packages must be installed by a user that has write access to the installation folder.</p>

---
