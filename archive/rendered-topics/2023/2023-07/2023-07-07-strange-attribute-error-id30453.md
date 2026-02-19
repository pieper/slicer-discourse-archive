---
topic_id: 30453
title: "Strange Attribute Error"
date: 2023-07-07
url: https://discourse.slicer.org/t/30453
---

# Strange attribute error

**Topic ID**: 30453
**Date**: 2023-07-07
**URL**: https://discourse.slicer.org/t/strange-attribute-error/30453

---

## Post #1 by @Patrick_Li (2023-07-07 14:37 UTC)

<p>When testing out the WriteXML() function, I keep getting this error. It seems the node type name is too long, or something like that. Any way to resolve?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/318e00f2406542ed50b5cc15351ad1dbe49b82c6.png" data-download-href="/uploads/short-url/74nDwOqSd4q7R2UKPoF5fTVFbRs.png?dl=1" title="Screenshot 2023-07-07 103618" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/318e00f2406542ed50b5cc15351ad1dbe49b82c6.png" alt="Screenshot 2023-07-07 103618" data-base62-sha1="74nDwOqSd4q7R2UKPoF5fTVFbRs" width="690" height="58" data-dominant-color="2B2020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-07 103618</span><span class="informations">907×77 3.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-07-08 04:02 UTC)

<p>The <code>WriteXML</code> method is not exposed on the Python interface because it is for internal use only (to be able to save the scene). If you want to write the content of a node to XML then you can save the scene.</p>

---
