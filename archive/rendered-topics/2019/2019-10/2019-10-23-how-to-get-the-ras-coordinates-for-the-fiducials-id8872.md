---
topic_id: 8872
title: "How To Get The Ras Coordinates For The Fiducials"
date: 2019-10-23
url: https://discourse.slicer.org/t/8872
---

# How to get the RAS coordinates for the fiducials

**Topic ID**: 8872
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/how-to-get-the-ras-coordinates-for-the-fiducials/8872

---

## Post #1 by @Saima (2019-10-23 06:34 UTC)

<p>How to get the right coordinates for the data points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acbee68a2022666db83a9045ac41a001f08d23f.png" data-download-href="/uploads/short-url/hwjaFLyF7Qw4kbQtOPwzI4db2vZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7acbee68a2022666db83a9045ac41a001f08d23f_2_690x429.png" alt="image" data-base62-sha1="hwjaFLyF7Qw4kbQtOPwzI4db2vZ" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7acbee68a2022666db83a9045ac41a001f08d23f_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acbee68a2022666db83a9045ac41a001f08d23f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7acbee68a2022666db83a9045ac41a001f08d23f.png 2x" data-dominant-color="9C9ED4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">937×583 16.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-10-23 13:31 UTC)

<p>You can get markups fiducial point positions by calling <code>GetNthFiducialPosition</code> method. See many examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">script repository</a>.</p>

---

## Post #3 by @Saima (2019-10-24 07:33 UTC)

<p>Hi Andras,<br>
How can I get the fiducials inside the box. Why they are outside</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2019-10-24 15:22 UTC)

<p>Click the small box icon (“Center the 3D view on the scene”) in the top-left corner of the slice view to reset the box boundaries to current view content.</p>

---
