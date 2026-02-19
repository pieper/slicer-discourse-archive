---
topic_id: 27951
title: "Release Of Slicer 5 2 2 In Progress"
date: 2023-02-21
url: https://discourse.slicer.org/t/27951
---

# Release of Slicer 5.2.2 in progress

**Topic ID**: 27951
**Date**: 2023-02-21
**URL**: https://discourse.slicer.org/t/release-of-slicer-5-2-2-in-progress/27951

---

## Post #1 by @jcfr (2023-02-21 14:32 UTC)

<p>This evening, regular preview and stable builds of Slicer and associated extensions will be disabled in favor of a <strong>patch</strong> release.</p>
<p>Fixes to be integrated in the <a href="https://github.com/Slicer/Slicer/tree/5.2">Slicer@5.2</a> maintenance branch are associated with <a href="https://github.com/Slicer/Slicer/pull/6782">PR-6782</a>.</p>
<p>To track the progress, see <a href="https://github.com/Slicer/Slicer/issues/6832" class="inline-onebox">Patch Release Slicer v5.2.2 · Issue #6832 · Slicer/Slicer · GitHub</a></p>

---

## Post #2 by @jcfr (2023-02-21 15:06 UTC)

<p><a href="https://discourse.slicer.org/t/release-of-slicer-5-2-2-in-progress/27951:" class="onebox" target="_blank" rel="noopener">https://discourse.slicer.org/t/release-of-slicer-5-2-2-in-progress/27951:</a></p>
<ul>
<li>Backports
<ul>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/pull/6831">PR-6831</a> <code>Update dicom.md typo</code>
</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/pull/6803">PR-6803</a> <code>COMP: Update python packages to latest</code>
<ul>
<li>with/without numpy update ? <a class="mention" href="/u/jamesobutler">@jamesobutler</a>
<ul>
<li>
<strong>Update</strong>: Will ignore numpy update</li>
</ul>
</li>
</ul>
</li>
<li>
<span class="chcklst-box fa fa-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/pull/6814">PR-6814</a> <code>BUG: Make loading of legacy annotation fiducial, line, ROI nodes more robust</code> <a class="mention" href="/u/lassoan">@lassoan</a> ?
<ul>
<li>
<strong>Update</strong>: This will not be backported as it depends on <a href="https://github.com/Slicer/Slicer/pull/6524">PR-6524</a> <code>ENH: Remove Annotations module</code> not included in the 5.2 branch.</li>
</ul>
</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/pull/6822">PR-6822</a> <code>BUG: Fixes default progress callback raises user warning in send() function</code> <a class="mention" href="/u/lassoan">@lassoan</a> ?</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/pull/6824">PR-6824</a> <code>BUG: Free notifier after request handling</code>  <a class="mention" href="/u/pieper">@pieper</a> ?</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/commit/9506e42834364ad528f5e26c0150ca25e4c44999">Slicer@9506e4283</a> <code>BUG: Adding missing null-pointer checks to qMRMLSegmentEditorWidget </code> <a class="mention" href="/u/lassoan">@lassoan</a> ?</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> <a href="https://github.com/Slicer/Slicer/pull/6810">PR-6810</a> <code>Fix welcome module translation</code>
</li>
</ul>
</li>
</ul>

---

## Post #3 by @jcfr (2023-02-21 18:57 UTC)

<p>All changes have been backported to the <a href="https://github.com/Slicer/Slicer/commits/5.2">Slicer@5.2</a> branch.</p>
<p>Local build and testing initiated to confirm no obvious regressions were introduced.</p>

---

## Post #4 by @jcfr (2023-02-22 06:14 UTC)

<p>Update:</p>
<ul>
<li>Slicer 5.2.2 are being generated<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ae9d9b90645ef8ebe13be51315ce97e74ee4c5.png" data-download-href="/uploads/short-url/jDZwB2Yq5enm7EX8hw6jUWfQ3lj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ae9d9b90645ef8ebe13be51315ce97e74ee4c5_2_517x43.png" alt="image" data-base62-sha1="jDZwB2Yq5enm7EX8hw6jUWfQ3lj" width="517" height="43" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ae9d9b90645ef8ebe13be51315ce97e74ee4c5_2_517x43.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ae9d9b90645ef8ebe13be51315ce97e74ee4c5_2_775x64.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89ae9d9b90645ef8ebe13be51315ce97e74ee4c5_2_1034x86.png 2x" data-dominant-color="B8C7D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3625×305 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
<em>Source: <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2023-02-22">https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2023-02-22</a></em>
</li>
</ul>

---

## Post #5 by @jcfr (2023-02-22 14:17 UTC)

<p>Update:</p>
<ul>
<li>Packages for all platform have been successfully generated. They are currently being signed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d4943ea9b5a393ff106766a4b612b346153b9e.png" data-download-href="/uploads/short-url/heUKbUE2hsLeAF4rRtxd6hjWlJA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d4943ea9b5a393ff106766a4b612b346153b9e_2_517x45.png" alt="image" data-base62-sha1="heUKbUE2hsLeAF4rRtxd6hjWlJA" width="517" height="45" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d4943ea9b5a393ff106766a4b612b346153b9e_2_517x45.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d4943ea9b5a393ff106766a4b612b346153b9e_2_775x67.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d4943ea9b5a393ff106766a4b612b346153b9e_2_1034x90.png 2x" data-dominant-color="B4C3C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3626×319 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
<em>Source: <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2023-02-22">https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2023-02-22</a></em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd03e4f1b7da44bcfe9e352e51564915d39d8018.png" data-download-href="/uploads/short-url/tfEdWMCvDIF02HDdA8N1elKsLJm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd03e4f1b7da44bcfe9e352e51564915d39d8018_2_517x164.png" alt="image" data-base62-sha1="tfEdWMCvDIF02HDdA8N1elKsLJm" width="517" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd03e4f1b7da44bcfe9e352e51564915d39d8018_2_517x164.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd03e4f1b7da44bcfe9e352e51564915d39d8018_2_775x246.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd03e4f1b7da44bcfe9e352e51564915d39d8018_2_1034x328.png 2x" data-dominant-color="F4F6F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1675×532 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
<em>Source: <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/63f5a1888939577d9867aba0">slicer-packages.kitware.com / Applications / packages / Slicer / 5.2.2</a></em>
</li>
</ul>

---

## Post #6 by @jcfr (2023-02-22 23:08 UTC)

<p>Update:</p>
<ul>
<li>Slicer 5.2.2 packages are now available for download.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af0d38abf80e5b2a221e9b4baa4563e7d013cf0.png" data-download-href="/uploads/short-url/m6FuUd75xjGeKyyjykLqFR5xcR2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af0d38abf80e5b2a221e9b4baa4563e7d013cf0_2_517x149.png" alt="image" data-base62-sha1="m6FuUd75xjGeKyyjykLqFR5xcR2" width="517" height="149" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af0d38abf80e5b2a221e9b4baa4563e7d013cf0_2_517x149.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af0d38abf80e5b2a221e9b4baa4563e7d013cf0_2_775x223.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af0d38abf80e5b2a221e9b4baa4563e7d013cf0_2_1034x298.png 2x" data-dominant-color="EDF3F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1782×514 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>Regular builds are resumed and expected to be published tomorrrow</li>
</ul>
<p>Next:</p>
<ul>
<li>We will soon publish <a href="https://discourse.slicer.org/c/announcements/release-notes/18">release notes</a>
</li>
</ul>

---
