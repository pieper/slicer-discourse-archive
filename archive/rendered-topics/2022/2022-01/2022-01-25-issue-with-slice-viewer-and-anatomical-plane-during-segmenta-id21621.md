# Issue with Slice viewer and anatomical plane during segmentations

**Topic ID**: 21621
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/issue-with-slice-viewer-and-anatomical-plane-during-segmentations/21621

---

## Post #1 by @yvonnew (2022-01-25 13:50 UTC)

<p>Hi,<br>
I have some issues managing the slice views during segmentation, could you let me know if my workflow should be changed:</p>
<ul>
<li>open an MRI scan (brain) to analyze</li>
<li>transform it to be symetrical in all 3 views (axial, coronal and sagittal) in order to identify the left and right structures easily for later segmentation</li>
<li>harden transform</li>
<li>create a segmentation in the segment editor</li>
<li>warning appears that my segment is not align with the volume: I click the warning icon to align and avoid artifact, but then my master volume (MRI scan) is ``randomly` moved to a position (especially the axial axis) that makes it difficult to precisely delineation my structures of interest.</li>
</ul>
<p>I would like to be able to segment on the transformed volume, am i missing a step or doing it wrong all the way ? any input would be really helpful, thank you!</p>

---

## Post #2 by @lassoan (2022-01-25 13:52 UTC)

<p>Segmentation on oblique slices can indeed be confusing at first. See detailed description of your options <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments">here</a>.</p>

---

## Post #3 by @yvonnew (2022-01-25 15:06 UTC)

<p>Hi,<br>
Thanks for the quick feedback!<br>
Yes, very confusing to me indeed! <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"><br>
I have tried to crop my volume, but that option is limited since I am segmenting structures throughout the brain, and similar change of orientation happens when I have to click again on the warning icon.<br>
The artifacts are a concern for me since I do see them if I try to segment on the volume plane.<br>
Would you have any other idea ?</p>

---

## Post #4 by @lassoan (2022-01-25 18:45 UTC)

<p>If there is no single orientation that works for all structures then you cannot rely on resampling, as each resampling could slightly deteriorate your segmentation.</p>
<p>Instead, you can paint in oblique slices. You can use sphere brush, which should mostly take care of the stripe artifacts. People doing high-accuracy manual brain segmentations also often adjust the editable intensity range (using Threshold effect). They also reported that for segmentations tasks Local thresholding effect (provided by SegmentEditorExtraEffects extension) was also very useful.</p>
<p><a class="mention" href="/u/jarrett-rushmore">@jarrett-rushmore</a> do you have any advice for this? Do you ever segment in oblique planes?</p>

---

## Post #5 by @jarrett-rushmore (2022-01-26 19:10 UTC)

<p>I don’t segment in oblique planes, but threshold tool should work.  With respect to the artifacts, this (rather excellent) article may shed some light on the issue.  Good luck!</p>

---

## Post #6 by @jarrett-rushmore (2022-01-26 19:11 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">
  <header class="source">

      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener nofollow ugc">3D Slicer segmentation recipes</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener nofollow ugc">Overview</a></h3>

  <p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
