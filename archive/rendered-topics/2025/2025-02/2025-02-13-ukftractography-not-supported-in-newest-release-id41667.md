---
topic_id: 41667
title: "Ukftractography Not Supported In Newest Release"
date: 2025-02-13
url: https://discourse.slicer.org/t/41667
---

# UKFTractography not supported in newest release

**Topic ID**: 41667
**Date**: 2025-02-13
**URL**: https://discourse.slicer.org/t/ukftractography-not-supported-in-newest-release/41667

---

## Post #1 by @fraslau (2025-02-13 03:33 UTC)

<p>The currently newest stable release 5.8.0 and preview release 5.9.0 for Windows do not support UKFTractography. I downloaded both versions and then downloaded extension SlicerDMRI, but I get the following error message: “slicerDMRI depends on the following extensions, which could not be found.” And there is no UKFTractography extension available.</p>
<p>However, I tried the older release 5.6.2 and this one has both SlicerDMRI and UKFTractography extensions.</p>
<p>Hopefully the new releases can be fixed.</p>

---

## Post #2 by @jamesobutler (2025-02-13 19:42 UTC)

<p>I pinged some of the developers of the extension in another post but they have been unresponsive so far.</p>
<aside class="quote" data-post="2" data-topic="41516">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/ukf-tractography-extension-missing-in-3d-slicer-5-8-0/41516/2">UKF Tractography extension missing in 3D Slicer 5.8.0</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    cc: <a class="mention" href="/u/tbillah">@tbillah</a> <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a>
  </blockquote>
</aside>


---

## Post #3 by @pieper (2025-02-13 19:54 UTC)

<p>As it happens I just proposed a fix earlier today: <a href="https://github.com/pnlbwh/ukftractography/pull/165" class="inline-onebox">COMP: fixes for Slicer 5.8 (cxx 17) by pieper · Pull Request #165 · pnlbwh/ukftractography · GitHub</a></p>
<p>If all goes well it should be in the stable and preview extensions in the next day or so.</p>

---

## Post #4 by @pieper (2025-02-14 15:54 UTC)

<p>Looks like UKF is working again.  It would be great if people could test and report back if there are any issues.  <a class="mention" href="/u/fraslau">@fraslau</a></p>

---
