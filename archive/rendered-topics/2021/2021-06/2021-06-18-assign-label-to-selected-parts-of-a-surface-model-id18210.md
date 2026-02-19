---
topic_id: 18210
title: "Assign Label To Selected Parts Of A Surface Model"
date: 2021-06-18
url: https://discourse.slicer.org/t/18210
---

# Assign label to selected parts of a surface model

**Topic ID**: 18210
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/assign-label-to-selected-parts-of-a-surface-model/18210

---

## Post #1 by @Aep93 (2021-06-18 15:22 UTC)

<p>Hello all,<br>
I have a surface model (.vtk format). I want to choose some of the elements of this model (interactively) and assign a different label to them. How can I do this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ac40cb87a0bb9513cce244c005c0794dbd87674.png" data-download-href="/uploads/short-url/3OMrP0TZmnMol8T2RcDVqqieZp2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ac40cb87a0bb9513cce244c005c0794dbd87674.png" alt="image" data-base62-sha1="3OMrP0TZmnMol8T2RcDVqqieZp2" width="690" height="447" data-dominant-color="6A6059"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×689 60.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-06-18 20:25 UTC)

<p>You can select individual cells as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#select-cells-of-a-model-using-markups-fiducial-points">here</a>. You can also select entire regions by placing a closed curve on the surface, as shown in the beginning of this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="nLva95ZF4ko" data-video-title="Extract one side of a closed surface mesh" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=nLva95ZF4ko" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/nLva95ZF4ko/maxresdefault.jpg" title="Extract one side of a closed surface mesh" width="" height="">
  </a>
</div>


---
