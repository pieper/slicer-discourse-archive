---
topic_id: 21902
title: "Slicer Modules Markups Logic Addnewfiducialnode Does Not Wor"
date: 2022-02-10
url: https://discourse.slicer.org/t/21902
---

# slicer.modules.markups.logic().AddNewFiducialNode() does not work in preview release

**Topic ID**: 21902
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/slicer-modules-markups-logic-addnewfiducialnode-does-not-work-in-preview-release/21902

---

## Post #1 by @koeglfryderyk (2022-02-10 22:02 UTC)

<p>slicer.modules.markups.logic().AddNewFiducialNode(“test_fid_node”) does not work in the nightly build 4.13.0-2022-02-06. When this line of code is executed ‘’ (empty string) is returned.</p>
<p>It works in the stable release 4.11.20210226</p>

---

## Post #2 by @smrolfe (2022-02-10 23:09 UTC)

<p>This is working for me using the most recent Windows preview 4.13.0-2022-02-09. Could you try updating to that version and let us know your OS?</p>

---

## Post #3 by @jamesobutler (2022-02-10 23:17 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="21902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>licer.modules.markups.logic().AddNewFiducialNode(“test_fid_node”)</p>
</blockquote>
</aside>
<p>This specific method was broken on this one day (4.13.0-2022-02-06) due to a typo error in <a href="https://github.com/Slicer/Slicer/commit/c8daef472497776cb9db67487c2664c384407d31" class="inline-onebox" rel="noopener nofollow ugc">BUG: Adds varying colors to ROIs added as a single node · Slicer/Slicer@c8daef4 · GitHub</a>. It was fixed the next day in <a href="https://github.com/Slicer/Slicer/commit/6db0afbb7d29a9fc7e8340a862f7346241647383" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix vtkSlicerMarkupsLogic::AddNewFiducialNode · Slicer/Slicer@6db0afb · GitHub</a> which would’ve been (4.13.0-2022-02-07).</p>

---

## Post #4 by @koeglfryderyk (2022-02-11 00:42 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="21902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>slicer.modules.markups.logic().AddNewFiducialNode(“test_fid_node”)</p>
</blockquote>
</aside>
<p>Thanks! It works with the current preview build (2022-02-09) I somehow didn’t think of trying it on the newest version, I’ll make sure to do this in the future</p>

---
