---
topic_id: 25596
title: "Carma Extension Not Installing"
date: 2022-10-07
url: https://discourse.slicer.org/t/25596
---

# CARMA extension not installing

**Topic ID**: 25596
**Date**: 2022-10-07
**URL**: https://discourse.slicer.org/t/carma-extension-not-installing/25596

---

## Post #1 by @Sophie_Liu (2022-10-07 19:14 UTC)

<p>keeps forcing my laptop to shut down and uninstall tons of apps like Firefox, vscode, MATLAB, and more. not sure if it’s a bug in my version of Slicer or I’m just not installing the extension properly.<br>
could I get some help? thanks.</p>

---

## Post #2 by @lassoan (2022-10-07 19:24 UTC)

<p><a href="https://github.com/carma-center/carma_slicer_extension/">CARMA extension</a> was developed about 10 years ago. Many things have changed since then. Several features are now available in Slicer core, while others have not been maintained and so are not available in current Slicer version.</p>
<p>What features are you interested in?</p>

---

## Post #3 by @Sophie_Liu (2022-10-08 00:06 UTC)

<p>Axial dilate. ******</p>

---

## Post #4 by @lassoan (2022-10-08 02:10 UTC)

<p>It seems that Axial dilate filter in CARMA creates a shell from a solid segment. We could port this module to Slicer5, but since we already have this feature implemented in Segment Editor module’s Hollow effect, I would recommend to just use that</p>
<div class="youtube-onebox lazy-video-container" data-video-id="jtDHTaAEilU" data-video-title="Make hollow - new segment editor effect in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jtDHTaAEilU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/jtDHTaAEilU/maxresdefault.jpg" title="Make hollow - new segment editor effect in 3D Slicer" width="" height="">
  </a>
</div>


---
