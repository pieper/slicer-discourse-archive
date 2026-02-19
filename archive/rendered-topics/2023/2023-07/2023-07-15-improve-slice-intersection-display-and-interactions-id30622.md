---
topic_id: 30622
title: "Improve Slice Intersection Display And Interactions"
date: 2023-07-15
url: https://discourse.slicer.org/t/30622
---

# Improve slice intersection display and interactions

**Topic ID**: 30622
**Date**: 2023-07-15
**URL**: https://discourse.slicer.org/t/improve-slice-intersection-display-and-interactions/30622

---

## Post #1 by @slicer365 (2023-07-15 16:44 UTC)

<p>I suggest that when the user clicks this icon, this option should be selected by default, or how to keep it selected through the script.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea9072410d78875647950289e57aede4fbb6a4d.png" data-download-href="/uploads/short-url/8WjK710bIeQ8122pTSqv86NHSB7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea9072410d78875647950289e57aede4fbb6a4d_2_690x324.png" alt="image" data-base62-sha1="8WjK710bIeQ8122pTSqv86NHSB7" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea9072410d78875647950289e57aede4fbb6a4d_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea9072410d78875647950289e57aede4fbb6a4d_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea9072410d78875647950289e57aede4fbb6a4d.png 2x" data-dominant-color="807F91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×512 31.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2023-07-15 17:07 UTC)

<p>Some people like me prefer to reslice using ‘CTRL + ALT + MouseMove’ though, rather than using the handles.</p>
<p>May I suggest that ‘Skip line crossings’ become available even without ‘Interaction’ enabled. The same reasoning may apply to line thickness.</p>

---

## Post #3 by @slicer365 (2023-07-15 17:14 UTC)

<p>In fact ,it won’t affect the “CTRL + ALT + MouseMove”</p>

---

## Post #4 by @chir.set (2023-07-15 17:18 UTC)

<p>True, if it is enabled by default, all the rest will be enabled.</p>
<p>It’s still not clear why ‘Skip line crossings’ and ‘Line thickness’ should depend on ‘Interaction’. Now it’s a minor thing in itself.</p>

---

## Post #5 by @lassoan (2023-07-16 01:28 UTC)

<p>Slice intersections were reimplemented from scratch. It supports interactions and new visualization options. That new implementation is used when you enable “Interaction” mode. We will not add new features to the old implementation, such as adding thickness adjustment or skipping line crossings.</p>
<p>Unfortunately, the new implementation was not completed. It has some significant bugs and limitations (sometimes the slice intersections appear as angled lines; it interferes with the Segment Editor, etc.) so we could not switch to it completely, but we kept the old implementation around (and enabled by default) until these issue are sorted out. It is a very complex component (computations, rendering, interactions, …) and right now there is no funded project that would require improvements in it, so I’m not sure when the problems with the new implementation will be fixed.</p>

---
