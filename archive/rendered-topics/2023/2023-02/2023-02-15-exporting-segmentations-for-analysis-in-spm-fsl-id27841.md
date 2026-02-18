# Exporting segmentations for analysis in SPM/FSL

**Topic ID**: 27841
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/exporting-segmentations-for-analysis-in-spm-fsl/27841

---

## Post #1 by @jok (2023-02-15 21:02 UTC)

<p>Hello,<br>
I have been segmenting lesions on brain MRIs. My brain MRIs are in .nii format. I have saved my manually drawn segmentation labels as nrrd files. When I open my subject’s MRI in 3dslicer, and then add the segmentation label files to the scene, as long as I click “Centered” for both the MRI and the label files in the “add data into the scene” options, I am able to see the labels correctly aligned to the MRI. If I do not click “centered” the label files are slightly displaced from where the lesions are on the MRI.<br>
I am now interested in exporting them to be using in FSL and SPM. I have tried to save them as nifti files, but when I open the nifti file on top of the MRI, the labels are not in the same space as the MRI, and are instead misaligned somewhere else.<br>
How do I make sure that my lesion masks remain spatially registered to my MRI when I save them? It does not seem to be an exclusively nifti problem as I have similar problems with nrrd too.<br>
Thanks,<br>
Josh</p>

---

## Post #2 by @lassoan (2023-02-15 21:06 UTC)

<aside class="quote no-group" data-username="jok" data-post="1" data-topic="27841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ba9def/48.png" class="avatar"> jok:</div>
<blockquote>
<p>as long as I click “Centered” for both the MRI and the label files in the “add data into the scene” options</p>
</blockquote>
</aside>
<p>I would not recommend clicking “Centered”, as it discards the image origin information.</p>
<p>You may find <a href="https://github.com/PerkLab/SlicerFreeSurfer#slicerfreesurfer">SlicerFreeSurfer extension</a> useful for importing images, segmentations, and overlays from FreeSurfer.</p>

---

## Post #3 by @jok (2023-02-16 15:22 UTC)

<p>Thanks for the suggestion.<br>
It sound like they are in the wrong space, so I am assuming that I will have to manually realign them using a linear transformation and then save them in the correct space.<br>
Is this what others would do?<br>
The problem is that this is very cumbersome and clearly slicer is able to have them perfectly aligned if I do the centering. Surely there is a better way?<br>
Thanks</p>

---
