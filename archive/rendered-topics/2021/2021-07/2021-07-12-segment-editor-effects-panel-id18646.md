---
topic_id: 18646
title: "Segment Editor Effects Panel"
date: 2021-07-12
url: https://discourse.slicer.org/t/18646
---

# Segment Editor "Effects" Panel

**Topic ID**: 18646
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/segment-editor-effects-panel/18646

---

## Post #1 by @OpenSource_Contri (2021-07-12 17:11 UTC)

<p>I wanted to change the state of icons present in “Effects” panel of Segment Editor when clicked.<br>
When we click any icon in effects panel the we do not able to differentiate which icon is currently in use.</p>
<p>For example - if we click on Threshold icon then icon should change from colored “Threshold” icon to lets say Uncolored “Threshold” icon.<br>
<strong>Screenshot is attached</strong></p>
<p>How can I do that? What code should I use?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d20ef853b032d9e50155b436c0d2b3a422c574.png" data-download-href="/uploads/short-url/enTNiXFs0Ir3D4hXidLNLFfvJnm.png?dl=1" title="Screenshot (309)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d20ef853b032d9e50155b436c0d2b3a422c574_2_320x500.png" alt="Screenshot (309)" data-base62-sha1="enTNiXFs0Ir3D4hXidLNLFfvJnm" width="320" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d20ef853b032d9e50155b436c0d2b3a422c574_2_320x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d20ef853b032d9e50155b436c0d2b3a422c574_2_480x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d20ef853b032d9e50155b436c0d2b3a422c574.png 2x" data-dominant-color="343638"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (309)</span><span class="informations">623×971 40.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2021-07-12 18:28 UTC)

<p>The active effect has a darker gray look (it looks pressed down) in light Slicer theme (see below). Same effect works in dark slicer theme (e.g., in your screenshot active effect is None), but much less pronounced.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80e74bb5eba7a1c00508262937c4fa8db856c2ef.png" data-download-href="/uploads/short-url/iokFevAFyIGYNzmHHcv60WHfmzB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e74bb5eba7a1c00508262937c4fa8db856c2ef_2_334x250.png" alt="image" data-base62-sha1="iokFevAFyIGYNzmHHcv60WHfmzB" width="334" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e74bb5eba7a1c00508262937c4fa8db856c2ef_2_334x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e74bb5eba7a1c00508262937c4fa8db856c2ef_2_501x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e74bb5eba7a1c00508262937c4fa8db856c2ef_2_668x500.png 2x" data-dominant-color="EDF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1183×884 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @OpenSource_Contri (2021-07-12 18:35 UTC)

<p>Thanks, You are right. <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>I have one more query. I also wanted to use another Uncolored “Threshold” icon when click on particular icon and when it is not clicked then It is always colored.<br>
Please Guide.</p>

---

## Post #4 by @lassoan (2021-07-12 19:38 UTC)

<p>You can do very thorough customization of all styles, colors, and icons if you create a custom build of Slicer: <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" class="inline-onebox">SlicerCAT: Creating custom applications based on 3D Slicer - Kitware Blog</a></p>

---
