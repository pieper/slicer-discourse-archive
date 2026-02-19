---
topic_id: 7721
title: "How To Hide The Default 3D Slicer Gui With Slicelet Module"
date: 2019-07-23
url: https://discourse.slicer.org/t/7721
---

# How to hide the default 3D Slicer GUI with Slicelet module?

**Topic ID**: 7721
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/how-to-hide-the-default-3d-slicer-gui-with-slicelet-module/7721

---

## Post #1 by @Zhao_Su (2019-07-23 08:39 UTC)

<p>like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e25b4ea25b69120b6b6d7a37d29fa368c8ab9467.png" data-download-href="/uploads/short-url/wirx2VAOr6qo9QYDyOaQXKhnLyn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25b4ea25b69120b6b6d7a37d29fa368c8ab9467_2_690x373.png" alt="image" data-base62-sha1="wirx2VAOr6qo9QYDyOaQXKhnLyn" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25b4ea25b69120b6b6d7a37d29fa368c8ab9467_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25b4ea25b69120b6b6d7a37d29fa368c8ab9467_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25b4ea25b69120b6b6d7a37d29fa368c8ab9467_2_1380x746.png 2x" data-dominant-color="C5C5C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1637×885 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Zhao_Su (2019-07-23 09:03 UTC)

<p>I add the slicelet example by"select Extension", am i right?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc66c7d1dbbca8e1377e6c5bd722df7f29490c91.png" alt="image" data-base62-sha1="A0QwMVulu6VLoRZmczVcS4d7RBL" width="566" height="391"><br>
but it didn’t hide the disable slicer GUI</p>

---

## Post #3 by @jamesobutler (2019-07-23 10:38 UTC)

<p>For Slicer 4.11 nightly, I think the encouraged method for running modules with reduced interface is to hide elements of the main GUI specifically instead of using the previously used method of specifying the <code>--no-main-window</code> command line argument and adding GUI elements.</p>
<blockquote>
<p>Slicelets are regular modules, which hide user interface elements that are not necessary for the particular workflow and provide all required widgets on their module panel.</p>
<p>Hiding of user interface elements can be implemented in the setup method of the module widget class, using a combination of set…Visibility methods implemented in <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1853" rel="noopener nofollow ugc">slicer.util</a>.</p>
</blockquote>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="noopener nofollow ugc">source</a></p>
<p>The specific methods in slicer.util to use can be found here:<br>
<a href="https://github.com/Slicer/Slicer/blob/e2096cc2210d0fb47da4bfa9f311e8c05149714e/Base/Python/slicer/util.py#L2025-L2094" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/e2096cc2210d0fb47da4bfa9f311e8c05149714e/Base/Python/slicer/util.py#L2025-L2094</a></p>

---

## Post #4 by @cpinter (2019-07-23 13:57 UTC)

<p>Hi! What you are doing seems useful for the community, as many people have asked about a simplified segmentation tool based on Slicer. Are you planning to make yours openly accessible? I think a lot of researchers would appreciate that. Thanks!</p>

---

## Post #5 by @Zhao_Su (2019-07-25 11:35 UTC)

<p>Thanks for your reply. I am not a professional developer. I just want to make some of work more custom friendly. And if I could, I would love to make my work openly accessible.</p>

---
