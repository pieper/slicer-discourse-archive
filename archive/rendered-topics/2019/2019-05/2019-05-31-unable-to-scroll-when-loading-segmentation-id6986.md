---
topic_id: 6986
title: "Unable To Scroll When Loading Segmentation"
date: 2019-05-31
url: https://discourse.slicer.org/t/6986
---

# Unable to scroll when loading segmentation

**Topic ID**: 6986
**Date**: 2019-05-31
**URL**: https://discourse.slicer.org/t/unable-to-scroll-when-loading-segmentation/6986

---

## Post #1 by @fedorov (2019-05-31 22:11 UTC)

<p>I see that users loading segmentations without the corresponding image volume get confused, because it is impossible to scroll through the segmentation volume. Is there a good reason to have this behavior?</p>

---

## Post #2 by @pieper (2019-05-31 22:50 UTC)

<p>Probably because segmentations are not being taken into account when determining the extent/spacing of the slice view UI (e.g. the slider and the scroll wheel).  Probably would be best to generalize the slice viewers so that any displayable node in the slice view can report a preferred bounds and spacing and not just volumes.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/808ec7020d4ac31556bf6c7df3566d11777335ae/Libs/MRML/Logic/vtkMRMLSliceLogic.h#L196-L208" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/808ec7020d4ac31556bf6c7df3566d11777335ae/Libs/MRML/Logic/vtkMRMLSliceLogic.h#L196-L208" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/808ec7020d4ac31556bf6c7df3566d11777335ae/Libs/MRML/Logic/vtkMRMLSliceLogic.h#L196-L208</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="196" style="counter-reset: li-counter 195 ;">
<li>
</li>
<li>///</li>
<li>/// Get the spacing of the volume, transformed to slice space</li>
<li>/// - to be used, for example, to set the slice increment for stepping a single</li>
<li>///   voxel relative to the current slice view</li>
<li>double *GetVolumeSliceSpacing(vtkMRMLVolumeNode *volumeNode);</li>
<li>
</li>
<li>///</li>
<li>/// Get the min/max bounds of the volume</li>
<li>/// - note these are not translated by the current slice offset so they can</li>
<li>///   be used to calculate the range (e.g. of a slider) that operates in slice space</li>
<li>void GetVolumeSliceBounds(vtkMRMLVolumeNode *volumeNode, double sliceBounds[6]);</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
