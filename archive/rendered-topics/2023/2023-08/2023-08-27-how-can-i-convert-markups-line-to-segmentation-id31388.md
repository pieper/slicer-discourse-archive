---
topic_id: 31388
title: "How Can I Convert Markups Line To Segmentation"
date: 2023-08-27
url: https://discourse.slicer.org/t/31388
---

# How can i convert markups line to segmentation?

**Topic ID**: 31388
**Date**: 2023-08-27
**URL**: https://discourse.slicer.org/t/how-can-i-convert-markups-line-to-segmentation/31388

---

## Post #1 by @yeong9316 (2023-08-27 15:16 UTC)

<p>hello. I found this community today and am posting my first question.<br>
Currently I am working on how to mark the spine with a specific trajectory for the pedicle screw.<br>
This trajectory was displayed in a cylinder shape using the line of the Markups function, but I want to convert this cylinder-shaped line into a segment and export it as an STL file together with the spine model.<br>
I would appreciate it if you could tell me how to merge the markups into the spine model.</p>
<p>P.S I am a very inexperienced beginner in handling 3d slicer. I would be very grateful if you could give me a little detail.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb9860ac2a1545c6e00567ea299e1fa98c71e09b.jpeg" data-download-href="/uploads/short-url/t35oqLRAH1spICmAi6jziUqyP59.jpeg?dl=1" title="스크린샷 2023-08-28 000318" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9860ac2a1545c6e00567ea299e1fa98c71e09b_2_690x451.jpeg" alt="스크린샷 2023-08-28 000318" data-base62-sha1="t35oqLRAH1spICmAi6jziUqyP59" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9860ac2a1545c6e00567ea299e1fa98c71e09b_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9860ac2a1545c6e00567ea299e1fa98c71e09b_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9860ac2a1545c6e00567ea299e1fa98c71e09b_2_1380x902.jpeg 2x" data-dominant-color="3E3D43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2023-08-28 000318</span><span class="informations">1402×917 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2023-08-27 18:38 UTC)

<p>If all you need is to convert these markup lines to 3D model, then you can use the MarkupsToModel extension, and save the resultant model as STL.</p>

---

## Post #3 by @cpinter (2023-08-28 09:41 UTC)

<p>Or if you insist on doing it from within Segment Editor, we have an effect called DrawTube that is in the SlicerSegmentEditorExtraEffects extension.</p>
<p>But if your goal is just to export them to STL and you don’t need to do other editing, then the way suggested by <a class="mention" href="/u/muratmaga">@muratmaga</a> is simpler.</p>

---
