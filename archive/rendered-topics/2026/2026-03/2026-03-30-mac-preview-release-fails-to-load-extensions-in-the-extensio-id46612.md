---
topic_id: 46612
title: "Mac Preview Release Fails To Load Extensions In The Extensio"
date: 2026-03-30
url: https://discourse.slicer.org/t/46612
---

# Mac preview release fails to load extensions in the Extension Manager

**Topic ID**: 46612
**Date**: 2026-03-30
**URL**: https://discourse.slicer.org/t/mac-preview-release-fails-to-load-extensions-in-the-extension-manager/46612

---

## Post #1 by @DeepaKrishnaswamy (2026-03-30 14:25 UTC)

<p>Hi,</p>
<p>I installed the latest Slicer Preview Release 2026-03-29 (Slicer 5.11.0 revision 34472) on Mac. I noticed that the extensions are not loading in the Extensions Manager:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe7fa605345d83456b24fba2d0b65bda54632fdd.png" data-download-href="/uploads/short-url/AjoLjFdLEOgGSqRViruw1AXQjA9.png?dl=1" title="Screenshot 2026-03-30 at 10.24.34 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe7fa605345d83456b24fba2d0b65bda54632fdd_2_690x388.png" alt="Screenshot 2026-03-30 at 10.24.34 AM" data-base62-sha1="AjoLjFdLEOgGSqRViruw1AXQjA9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe7fa605345d83456b24fba2d0b65bda54632fdd_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe7fa605345d83456b24fba2d0b65bda54632fdd_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe7fa605345d83456b24fba2d0b65bda54632fdd_2_1380x776.png 2x" data-dominant-color="FDFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-03-30 at 10.24.34 AM</span><span class="informations">1506×848 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I checked cdash and noticed many errors, even for extensions that should work like SlicerRT.</p>
<p>Thanks!</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
</table>
</div>

---

## Post #2 by @pieper (2026-03-30 15:10 UTC)

<p>Thanks for reporting.</p>
<p>Yes, it looks like pretty much <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">everything</a> is failing on the preview, while the stable look more normal.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95cee1a5acd2c1cdf35d68d00ac294c452763f3d.jpeg" data-download-href="/uploads/short-url/lngnQ7deRUhDzGoeJsCRggrPiqh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95cee1a5acd2c1cdf35d68d00ac294c452763f3d_2_479x500.jpeg" alt="image" data-base62-sha1="lngnQ7deRUhDzGoeJsCRggrPiqh" width="479" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95cee1a5acd2c1cdf35d68d00ac294c452763f3d_2_479x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95cee1a5acd2c1cdf35d68d00ac294c452763f3d_2_718x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95cee1a5acd2c1cdf35d68d00ac294c452763f3d_2_958x1000.jpeg 2x" data-dominant-color="D9D1C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×1668 708 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @fedorov (2026-03-30 21:59 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="46612">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it looks like pretty much <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">everything</a> is failing on the preview</p>
</blockquote>
</aside>
<p>AND it seems that pretty much <a href="https://slicer.cdash.org/viewBuildGroup.php?project=SlicerPreview&amp;buildgroup=Extensions-Nightly&amp;date=2026-03-30&amp;">everything</a> has been failing since March 22!</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> this can’t be related to the Girder work you’ve been doing, right?…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a577a794d3fa8a50456f6c4509ed6b46e85073f.png" data-download-href="/uploads/short-url/hshFJ8as7MKOs5MwT12E8MIyrpl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a577a794d3fa8a50456f6c4509ed6b46e85073f_2_690x104.png" alt="image" data-base62-sha1="hshFJ8as7MKOs5MwT12E8MIyrpl" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a577a794d3fa8a50456f6c4509ed6b46e85073f_2_690x104.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a577a794d3fa8a50456f6c4509ed6b46e85073f_2_1035x156.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a577a794d3fa8a50456f6c4509ed6b46e85073f.png 2x" data-dominant-color="EFE3CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1257×191 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
