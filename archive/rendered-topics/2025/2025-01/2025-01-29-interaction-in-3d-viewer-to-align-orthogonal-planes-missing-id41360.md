# "Interaction in 3D Viewer" to align orthogonal planes missing in 5.8.0 update?

**Topic ID**: 41360
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/interaction-in-3d-viewer-to-align-orthogonal-planes-missing-in-5-8-0-update/41360

---

## Post #1 by @sck84 (2025-01-29 15:46 UTC)

<p>Hi everyone,</p>
<p>I used to create a transform and use the “Interaction in 3D Viewer” tool to align structures to the orthogonal planes in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c709f570d4971b3354d9ec48c3193fa843f63dd.png" data-download-href="/uploads/short-url/8CFWjS2gseFjrdtCsRVqZEPIbj7.png?dl=1" title="Screenshot 2025-01-29 at 10.38.23 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c709f570d4971b3354d9ec48c3193fa843f63dd.png" alt="Screenshot 2025-01-29 at 10.38.23 AM" data-base62-sha1="8CFWjS2gseFjrdtCsRVqZEPIbj7" width="648" height="254"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-29 at 10.38.23 AM</span><span class="informations">648×254 33.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Following the most recent update, it appears this function has gone away. When you now click “Interaction,” the white box that used to appear no longer does, and I can’t rotate the object in 3D space to align it to the planes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e0c21fe2f3eb1b09477f00d18e1bb1e4f429cff.png" data-download-href="/uploads/short-url/fHwvZY4rZ33mkS2hbZswys5C6Z1.png?dl=1" title="Screenshot 2025-01-29 at 10.37.50 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e0c21fe2f3eb1b09477f00d18e1bb1e4f429cff_2_690x261.png" alt="Screenshot 2025-01-29 at 10.37.50 AM" data-base62-sha1="fHwvZY4rZ33mkS2hbZswys5C6Z1" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e0c21fe2f3eb1b09477f00d18e1bb1e4f429cff_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e0c21fe2f3eb1b09477f00d18e1bb1e4f429cff_2_1035x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e0c21fe2f3eb1b09477f00d18e1bb1e4f429cff.png 2x" data-dominant-color="23272B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-29 at 10.37.50 AM</span><span class="informations">1140×432 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Am I missing something? Is there a new way to align structures that I am unaware of?</p>

---

## Post #2 by @cpinter (2025-01-29 16:03 UTC)

<p>The feature has been revamped. See details here</p><aside class="quote quote-modified" data-post="1" data-topic="36974">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">New feature: Interactive transformation + adjustable center of rotation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Any nodes can now be translated, rotated, or scaled by interactive handles.  Editing operations can be constrained to specific axes and center of rotation can be freely chosen. The handles are available both in slice and 3D views. 
Transform nodes can be easily added and visualized for any node in 3D Slicer by right-clicking on the node in the Subject hierarchy visibility column and checking “Interaction”. 

  <a href="https://www.youtube.com/watch?v=ielxgJS-6SI" target="_blank" class="video-thumbnail" rel="noopener">
    [Transform Interaction Handles in 3D Slicer]
  </a>


<a name="visualization-options-1" class="anchor" href="#visualization-options-1"></a>Visualization options
Visualiza…
  </blockquote>
</aside>


---
