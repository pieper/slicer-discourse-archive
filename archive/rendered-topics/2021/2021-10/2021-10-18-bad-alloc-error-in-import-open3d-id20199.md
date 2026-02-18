# Bad_alloc error in import open3d

**Topic ID**: 20199
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/bad-alloc-error-in-import-open3d/20199

---

## Post #1 by @muratmaga (2021-10-18 04:43 UTC)

<p>Since r30305, we are getting this error after pip_install(“open3d==0.10.0”). This is on ubuntu 20.04.</p>
<p>I believe Bad allocation is an out of memory error, so I assume real error is something else.  Any suggestions on how to debug this will be great</p>
<pre><code class="lang-auto">import open3d
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/docker/MyData/Slicer-4.13.0-2021-10-14-linux-amd64/lib/Python/lib/python3.6/site-packages/open3d/__init__.py", line 47, in &lt;module&gt;
    from open3d.open3d_pybind import camera
ImportError: std::bad_alloc
</code></pre>
<p><a class="mention" href="/u/agporto">@agporto</a> <a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #2 by @pieper (2021-10-18 11:40 UTC)

<p>I’d suggest testing to see if the same thing happens in a non-slicer python.  Also if you can build a open3d from source in debug mode you could single-step through and see what operation leads to the exception.  Or on linux you can use <code>strace</code> to see what system calls happen before the exception.</p>

---

## Post #3 by @muratmaga (2021-10-18 16:25 UTC)

<p>Can confirm that no such error is triggered on the system python when importing open3d. Although that’s version 3.8.10</p>

---

## Post #4 by @muratmaga (2021-10-27 17:58 UTC)

<p>Anymore suggestions on this?<br>
This error breaks the functionality of ALPACA on linux platforms.</p>

---

## Post #5 by @muratmaga (2021-10-27 18:02 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="20199">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>you can use <code>strace</code> to see what system calls happen before the exception.</p>
</blockquote>
</aside>
<pre><code class="lang-auto">recvmsg(8, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)
recvmsg(8, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\337\0005\5\0\0\373\0\0\0\26\313\37\32\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32
recvmsg(8, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)
recvmsg(8, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)
select(21, [4 8 9 20], [], [], {tv_sec=21, tv_usec=917487}Python console user input: import open3d
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/maga/Downloads/Slicer/lib/Python/lib/python3.6/site-packages/open3d/__init__.py", line 47, in &lt;module&gt;
    from open3d.open3d_pybind import camera
ImportError: std::bad_alloc
) = 1 (in [8], left {tv_sec=6, tv_usec=651769})
recvmsg(8, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\337\0005\5\0\09\1\0\0\270\6 \32\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 64
recvmsg(8, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)
recvmsg(8, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)
</code></pre>

---

## Post #6 by @jamesobutler (2021-10-27 18:19 UTC)

<p>When you use an older Slicer preview version, it begins to work again? Fresh install of that older version.</p>

---

## Post #7 by @muratmaga (2021-10-27 18:29 UTC)

<p>I just tried with a fresh install of r30222 and pip_install and import open3d worked fine.</p>

---

## Post #8 by @jamesobutler (2021-10-27 18:33 UTC)

<p>What’s the date on these two revisions you’ve mentioned?</p>

---

## Post #9 by @jamesobutler (2021-10-27 18:42 UTC)

<p>And does the same error happen if you pip install in Slicer a newer release of Open3D? A new version will force a new download assuming you haven’t done it before and not use any cached wheel.</p>

---

## Post #10 by @muratmaga (2021-10-27 18:45 UTC)

<p>Yes. It does happen with new install.</p>

---

## Post #11 by @muratmaga (2021-10-27 18:45 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="20199" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>What’s the date on these two revisions you’ve mentioned?</p>
</blockquote>
</aside>
<p>We have the problem since r30305. I am not sure how to go back to dates.</p>

---

## Post #12 by @jamesobutler (2021-10-27 18:47 UTC)

<p>When you use the version that is r30305, does it not show the date next to the Slicer version in a window title bar or in Help-&gt;About Slicer?</p>

---

## Post #13 by @muratmaga (2021-10-27 18:51 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="12" data-topic="20199">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>r30305</p>
</blockquote>
</aside>
<p>Sorry, I don’t have the r30305 installed anymore (too many transient versions of slicer confuses my workflows. I download, try and remove it). r30222 (working one) is from 9/18.</p>

---

## Post #14 by @jamesobutler (2021-10-27 18:52 UTC)

<p><code>slicer.app.repositoryRevision</code> should get the same type of information that I want. Just wanting to know the commit hashes so I can compare things that happened between working and not working.</p>

---

## Post #15 by @jamesobutler (2021-10-27 19:19 UTC)

<p>Try the following 2 builds on Linux and see if it works on one or other. If it fails on both I can provide you with another set to test.</p>
<ul>
<li>r30297 - Slicer 4.13.0-2021-10-05<br>
<a href="https://slicer.cdash.org/viewFiles.php?buildid=2425829" class="inline-onebox" rel="noopener nofollow ugc">CDash - View Files</a>
</li>
<li>r30282 - Slicer 4.13.0-2021-10-03<br>
<a href="https://slicer.cdash.org/viewFiles.php?buildid=2423240" class="inline-onebox" rel="noopener nofollow ugc">CDash - View Files</a>
</li>
</ul>

---

## Post #16 by @muratmaga (2021-10-27 19:33 UTC)

<p>Aren’t these prior to r30305?  Those should work.</p>

---

## Post #17 by @jamesobutler (2021-10-27 19:34 UTC)

<p>You tested every version earlier than r30305 to know that it was exactly this version where it broke?</p>

---

## Post #18 by @muratmaga (2021-10-27 19:37 UTC)

<p>r30297 works as well.<br>
And yes I believe <a class="mention" href="/u/agporto">@agporto</a> tested all versions up to r30305, but wasn’t able to find a specific change that might explain the crash.</p>

---

## Post #19 by @jamesobutler (2021-10-27 19:41 UTC)

<p>Ok, r30305 (Sicer 4.13.0-2021-10-07) <a href="https://slicer.cdash.org/viewFiles.php?buildid=2428420" class="inline-onebox" rel="noopener nofollow ugc">CDash - View Files</a>, was the first release from the Slicer Linux Factory build machine that used GCC7 instead of GCC5. It was turned on first for this release as a test (<a href="https://github.com/Slicer/DashboardScripts/commit/c92c2802b15d4b876d943a9fe3f8705af486512f" class="inline-onebox" rel="noopener nofollow ugc">metroplex: Temporarily use gcc7 image for nightly · Slicer/DashboardScripts@c92c280 · GitHub</a>) and then was turned on permanently for all subsequent days. This switch from GCC7 from GCC5 was to fix a long running issue with SlicerJupyter not building correctly on Linux (<a href="https://github.com/Slicer/SlicerJupyter/issues/59#issuecomment-938611809" class="inline-onebox" rel="noopener nofollow ugc">Linux: extension SlicerJupyter not available in 4.13 preview releases · Issue #59 · Slicer/SlicerJupyter · GitHub</a>). Looking at the commits from October 7th and 6th on the Slicer there isn’t something obvious.</p>

---

## Post #20 by @muratmaga (2021-10-27 21:54 UTC)

<p>I am building a py wheel for open3d, and will try to install that. But I am not sure how to do that with the slicer’s pip_install. Can I point out to a file?</p>

---

## Post #21 by @jamesobutler (2021-10-27 22:32 UTC)

<p>Yes, should be able to specify the whl directly.</p>
<p>This worked for me to install this package</p>
<pre><code class="lang-python">slicer.util.pip_install(r"C:\Users\JamesButler\Downloads\pycodestyle-2.8.0-py2.py3-none-any.whl")
</code></pre>

---

## Post #22 by @jamesobutler (2021-11-04 09:57 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> How did the manual whl building go to resolve your issue here?</p>

---

## Post #23 by @muratmaga (2021-11-04 22:59 UTC)

<p>I think it could have worked, if I managed to build open3d 0.10. I can build 0.13 (which doesn’t help us), and install, but unfortunately 0.10 doesn’t seem to work with provided instructions (some external library install is failing).</p>

---

## Post #24 by @jamesobutler (2021-11-05 00:17 UTC)

<p>Can you remind me why you’re unable to update to using the latest version of Open3D?</p>
<p>As a package that includes a large amount of external dependencies, even though you may be specifying a specific version it may not always have the same dependencies.</p>

---

## Post #25 by @muratmaga (2021-11-05 00:52 UTC)

<p>Because almost at every version, they change their API in ways that breaks our functionality. We don’t have the bandwidth to keep updating every 3-4 months. So we are looking in find a way to wean ourselves. Feel free to make comments/suggestion on this thread.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/vtk-point-cloud-and-mesh-filters-for-downsampling-registration-icp-transform/6974">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/vtk-point-cloud-and-mesh-filters-for-downsampling-registration-icp-transform/6974" target="_blank" rel="noopener nofollow ugc" title="07:59PM - 26 October 2021">VTK – 26 Oct 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/493;"><img src="https://discourse.vtk.org/uploads/default/optimized/2X/0/068a62254d1f27783e14636d49ff19173535d4ee_2_1024x732.jpeg" class="thumbnail" width="690" height="493"></div>

<h3><a href="https://discourse.vtk.org/t/vtk-point-cloud-and-mesh-filters-for-downsampling-registration-icp-transform/6974" target="_blank" rel="noopener nofollow ugc">VTK point cloud and mesh filters for downsampling, registration, ICP transform</a></h3>

  <p>In the context of the SlicerMorph project (details below). We are looking to improving existing VTK filters or develop new ones.   Question Following a suggestion of @will.schroeder , I am reaching out to understand which existing filters have been...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #26 by @agporto (2021-11-05 04:56 UTC)

<p>When trying to import individual components, I get a more informative error:</p>
<pre><code>from open3d.cpu.pybind import (camera, geometry, io, pipelines, utility, t)
</code></pre>
<p>ImportError: generic_type: cannot initialize type “VerbosityLevel”: an object with that name is already defined</p>
<p>I am wondering if that is somehow related to the Qt5 update since it also has a ‘VerbosityLevel’ definition</p>

---
