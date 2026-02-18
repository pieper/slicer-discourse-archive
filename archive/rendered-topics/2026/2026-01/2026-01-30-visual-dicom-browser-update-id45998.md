# Visual DICOM browser update

**Topic ID**: 45998
**Date**: 2026-01-30
**URL**: https://discourse.slicer.org/t/visual-dicom-browser-update/45998

---

## Post #1 by @Davide_Punzo (2026-01-30 13:07 UTC)

<p>Hey everyone, I have been working on major improvements to the visual DICOM browser:</p>
<h2><a name="p-131649-whats-new-1" class="anchor" href="#p-131649-whats-new-1" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/bullseye.png?v=15" title=":bullseye:" class="emoji" alt=":bullseye:" loading="lazy" width="20" height="20"> What’s New</h2>
<p><strong>Performance for large datasets (both remote and local)</strong></p>
<ul>
<li>
<p>Optimized for &gt;100GB databases</p>
</li>
<li>
<p>Lazy thumbnail generation in background</p>
</li>
<li>
<p>Use of model/views → batch model updates → less UI flickering and interactive filtering on local database</p>
</li>
</ul>
<p><strong>Better Slicer Integration</strong></p>
<ul>
<li>
<p>New/cleaner UI with visual operation status</p>
</li>
<li>
<p>Studies auto-sort by date (most recent first)</p>
</li>
<li>
<p>Smart query prioritization (top 2 studies get high priority)</p>
</li>
</ul>
<p><strong>and bug fixes</strong></p>
<p>See full list in links <a href="https://discourse.slicer.org/t/visual-dicom-browser-update/45998#p-131649-links-4">section</a> below</p>
<h2><a name="p-131649-videos-2" class="anchor" href="#p-131649-videos-2" aria-label="Heading link"></a><strong><img src="https://emoji.discourse-cdn.com/twitter/video_camera.png?v=15" title=":video_camera:" class="emoji" alt=":video_camera:" loading="lazy" width="20" height="20"> Videos</strong></h2>
<p>Part 1 (below part 2, 3 and 4):</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a66dc403ada285de3e190a7d5f9fae4e43b39846.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f2f0b09222e84cf828a281481cd12c5ef6a7b1.jpeg" data-video-base62-sha1="nKiqMxlxpkBsfFHRsYsTEBxoKGO.mp4">
  </div><p></p>
<h2><a name="p-131649-links-3" class="anchor" href="#p-131649-links-3" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/link.png?v=15" title=":link:" class="emoji" alt=":link:" loading="lazy" width="20" height="20"> Links</h2>
<p><strong>PRs:</strong> CTK <a href="https://github.com/commontk/CTK/pull/1326" rel="noopener nofollow ugc">#1326</a>, <a href="https://github.com/commontk/CTK/pull/1343" rel="noopener nofollow ugc">#1343</a>, <a href="https://github.com/commontk/CTK/pull/1345" rel="noopener nofollow ugc">#1345</a> | Slicer <a href="https://github.com/Slicer/Slicer/pull/8866" rel="noopener nofollow ugc">#8866</a>, <a href="https://github.com/Slicer/Slicer/pull/8982" rel="noopener nofollow ugc">#8982</a></p>
<p><strong>Roadmap:</strong> <a href="https://github.com/commontk/CTK/issues/1230" rel="noopener nofollow ugc">CTK #1230</a></p>
<p><strong>Known Issues:</strong> <a href="https://github.com/commontk/CTK/issues/1344" rel="noopener nofollow ugc">#1344</a>, <a href="https://github.com/commontk/CTK/issues/1341" rel="noopener nofollow ugc">#1341</a>, <a href="https://github.com/commontk/CTK/issues/1340" rel="noopener nofollow ugc">#1340</a></p>
<p><strong>Documentation</strong>: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#visual-dicom-browser" class="inline-onebox" rel="noopener nofollow ugc">DICOM — 3D Slicer documentation</a></p>
<h2><a name="p-131649-testing-4" class="anchor" href="#p-131649-testing-4" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/test_tube.png?v=15" title=":test_tube:" class="emoji" alt=":test_tube:" loading="lazy" width="20" height="20"> Testing</h2>
<p>Available in latest Slicer preview.</p>
<p>Feedback is very welcome! <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/ungi">@ungi</a> <a class="mention" href="/u/tina_kapur">@Tina_Kapur</a></p>
<p>Davide</p>

---

## Post #2 by @Davide_Punzo (2026-01-30 13:09 UTC)

<p>I had to split the video, follow part 2, 3 and 4:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329ad350548d7070f38661cf02f5c749c7479b85.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ac1b267b7c4d472c2dbea3baaa40406dea39afa.jpeg" data-video-base62-sha1="7dFAiGOEwZ3eVx0pLHV4CaSHd09.mp4">
  </div><p></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f81fe1626e99e2141cbf722f44d9e23a312991fb.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed6a2813be4fdd92a57a1c9b178ccd1d1f2adeee.jpeg" data-video-base62-sha1="zp0IoO3ekO6NR9GDCcvWyIQr06v.mp4">
  </div><p></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f349e7f0f39b0874dcce77178f4d9cd258116845.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b33cd362ef71a7243ac088fb0415cb0a2679874.jpeg" data-video-base62-sha1="yIemPvjdDFVtJWmgRkFrVwf2CRT.mp4">
  </div><p></p>

---
