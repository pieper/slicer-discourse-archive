---
topic_id: 41791
title: "SlicerJupyter not available for latest version?"
date: 2025-02-20
url: https://discourse.slicer.org/t/41791
last_bumped: 2026-04-27T14:41:57.558Z
---

# SlicerJupyter not available for latest version?

**Topic ID**: 41791
**Date**: 2025-02-20
**URL**: https://discourse.slicer.org/t/slicerjupyter-not-available-for-latest-version/41791

---

## Post #1 by @Juergen (2025-02-20 18:38 UTC)

<p>Hello,<br>
I just noticed that SlicerJupyter was not available as an extension for both the latest stable version and the latest unstable version.<br>
What are the plans moving forward? Will SlicerJupyter work? SlicerJupyter is mission critical for my work.<br>
Thanks, Juergen</p>

---

## Post #2 by @jamesobutler (2025-02-20 19:06 UTC)

<p>Please see the following recent response on this topic:</p>
<aside class="quote" data-post="5" data-topic="41463">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerjupyter-not-found-in-slicer-5-7-and-5-8/41463/5">SlicerJupyter Not Found in Slicer 5.7 and 5.8</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for the report <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title="pray" alt="pray" class="emoji"> 
Looking at CDash associated with both the Stable (see <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-16&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=jupyter" rel="noopener nofollow ugc">here</a>) and the Preview build (see <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-18&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=jupyter" rel="noopener nofollow ugc">here</a>), the extension is packaged and available on Linux and macOS but not on Windows. 
For example, corresponding Windows error can be reviewed <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3693507" rel="noopener nofollow ugc">here</a> 
A dedicated issue has been created: <a href="https://github.com/Slicer/SlicerJupyter/issues/78" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerJupyter/issues/78</a> 
<a class="mention" href="/u/matteboo">@Matteboo</a>  Let us know if you would like to either work on the issue or if you would have resources to help support its resolution <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title="pray" alt="pray" class="emoji">
  </blockquote>
</aside>


---

## Post #3 by @Juergen (2025-02-20 19:27 UTC)

<p>Ok, thanks for the quick response. I’ve been using 5.7.0-2024-02-08 with SlicerJupyter without a problem though, but I’m not sure about newer versions. For sure it didn’t work with the latest 5.9.</p>

---

## Post #4 by @Juergen (2025-11-14 15:35 UTC)

<p>Is there still hope and desire to bring SlicerJupyter back into operation or has this extension been abandoned?</p>

---

## Post #5 by @lassoan (2025-11-15 20:48 UTC)

<p>No, it’s not abandoned, but we don’t hear a lot from users and there are many other priorities to juggle with. I’ll have a look if it’s easy to update to recent package versions that are compatible with Slicer. What operating system do you use?</p>

---

## Post #6 by @Juergen (2025-11-15 21:22 UTC)

<p>Thanks, Andras, that’s encouraging. I understand that there are many other priorities. Unfortunately, I don’t have the skills to fix this, but I completely rely on SlicerJupyter because I scripted my entire workflow with it as a way to codify and document my process for repeatability. I would like to upgrade Slicer for a newer vtk etc but I’m stuck with 5.7.</p>
<p>I’m on Windows. Thanks</p>

---

## Post #7 by @cmr0807 (2025-11-20 17:34 UTC)

<p>Dear Andras,</p>
<p>please let me chime in - actually, our working group, too, relies heavily (if not entirely) on SlicerJupyter regarding development of an electrophysiological, real-time fully MR-guided interventional procedure with 3DSlicer for visualization. This project runs together with ETH Zurich (Switzerland) funded by a Swiss National Fund.</p>
<p>Our main motivations to kindly ask for your setting priority higher for SlicerJupyter are:</p>
<ul>
<li>Upgrading to 3DSlicer version &gt;/= 5.9 and hence, Python3.12 (rendering Slicer code “future proof”)</li>
<li>Further improvements regarding Xeus-Python kernel integration in Jupyter to benefit from</li>
</ul>
<p>We are mainly developing on Windows and Linux.</p>
<p>Many thanks in advance for considering to set SlicerJupyter to a higher priority - we very much appreciate the amazing work you have invested over all those years and cannot thank you enough for such dedication and perseverance</p>
<p>Warmest regards</p>

---

## Post #8 by @Matteboo (2025-11-21 12:25 UTC)

<p>Same here, we use SlicerJupyter a lot to study microwave ablation.<br>
It would be a huge help if the extension was available in the latest realease</p>

---

## Post #9 by @refelix (2025-11-25 14:53 UTC)

<p>Hi, just wanted to let you know that we used SlicerJupiter a lot for analysis of clinical CT data as well as for a prototyping and debugging tool for surgery planning. For someone with a Data Analysis background I struggle to imagine developing something more complex without it. Having problems with the installation on MacOS since Slicer 5.2, we kind of got stuck on this Slicer release.  I always check if new Versions fixed the issue, now seeing it gone completely from the Extension manager is a bit of a downer. I hope someone finds time to look into it.<br>
That being said, thanks a lot for all the development you are doing, also I wouldn’t know how I would have fixed problems without all the information I found in this forum mostly by Andras himself.</p>

---

## Post #10 by @ebrahim (2026-04-22 04:44 UTC)

<p>For those watching this thread, we just merged a set of fixes/upgrades to SlicerJupyter that at least worked for me on linux. It looked like there was a possibly independent set of issues on windows so IDK about that, but at least on linux it should work now!</p>

---

## Post #11 by @Juergen (2026-04-24 21:34 UTC)

<p>Thanks for working on a fix for the Linux version. Unfortunately, I’m on Windows and I don’t know how to fix it. I hope somebody can help this along. I had to set up a new computer and just copied the old Slicer directory and hope this old version still works. Otherwise I would be locked out of my SlicerJupyter code.</p>

---

## Post #12 by @ebrahim (2026-04-27 14:41 UTC)

<aside class="quote no-group" data-username="Juergen" data-post="11" data-topic="41791">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/juergen/48/66870_2.png" class="avatar"> Juergen:</div>
<blockquote>
<p>I had to set up a new computer and just copied the old Slicer directory and hope this old version still works. Otherwise I would be locked out of my SlicerJupyter code.</p>
</blockquote>
</aside>
<p>In case you need to download an older version of Slicer to make something work, older versions are always available. See this link on <a href="http://download.slicer.org">download.slicer.org</a>:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e88a4123145e4316f987bc3d2975096fceda9665.png" data-download-href="/uploads/short-url/xb8YSuNF63Vpkbm1hAg985ZC7MF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e88a4123145e4316f987bc3d2975096fceda9665_2_690x244.png" alt="image" data-base62-sha1="xb8YSuNF63Vpkbm1hAg985ZC7MF" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e88a4123145e4316f987bc3d2975096fceda9665_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e88a4123145e4316f987bc3d2975096fceda9665.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e88a4123145e4316f987bc3d2975096fceda9665.png 2x" data-dominant-color="EEF4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">853×302 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
