---
topic_id: 12480
title: "Locking The Slider For A Slice"
date: 2020-07-10
url: https://discourse.slicer.org/t/12480
---

# "Locking" the slider for a slice

**Topic ID**: 12480
**Date**: 2020-07-10
**URL**: https://discourse.slicer.org/t/locking-the-slider-for-a-slice/12480

---

## Post #1 by @rohan_n (2020-07-10 17:01 UTC)

<p>Is there a way to restrict which slices the user can view? For example, configure the red slice’s slider (lock it in place) so that the user cannot view anything other than the center axial slice of the image. If so, what is the syntax for this configuration, and also for undoing this configuration so that the user can once again view all axial slices?</p>

---

## Post #2 by @lassoan (2020-07-10 17:32 UTC)

<p>Yes, you can disable all kinds of interactions (slice browsing, zooming, rotating, blending, setting crosshair position, etc.):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Libs/MRML/DisplayableManager/vtkMRMLSliceViewInteractorStyle.h#L69-L82" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Libs/MRML/DisplayableManager/vtkMRMLSliceViewInteractorStyle.h#L69-L82" target="_blank">Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Libs/MRML/DisplayableManager/vtkMRMLSliceViewInteractorStyle.h#L69-L82</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="69" style="counter-reset: li-counter 68 ;">
<li>Translate = 1,</li>
<li>Zoom = 2,</li>
<li>Rotate = 4, /* Rotate not currently used */</li>
<li>Blend = 8, /* fg to bg, labelmap to bg */</li>
<li>AdjustWindowLevelBackground = 16,</li>
<li>AdjustWindowLevelForeground = 32,</li>
<li>BrowseSlice = 64,</li>
<li>ShowSlice = 128,</li>
<li>AdjustLightbox = 256, /* not used */</li>
<li>SelectVolume = 512,</li>
<li>SetCursorPosition = 1024, /* adjust cursor position in crosshair node as mouse is moved */</li>
<li>SetCrosshairPosition = 2048,</li>
<li>TranslateSliceIntersection = 4096,</li>
<li>RotateSliceIntersection = 8192,</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>See example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views</a></p>

---

## Post #3 by @rohan_n (2020-07-10 18:38 UTC)

<p>Thanks, I got the result I wanted by using the syntax in link at the bottom of your post to prevent mouse scrolling through slices and removing slider from view.</p>

---
