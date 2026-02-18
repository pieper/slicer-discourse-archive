# How to select the external surface of a model

**Topic ID**: 3917
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/how-to-select-the-external-surface-of-a-model/3917

---

## Post #1 by @giulia29 (2018-08-28 08:23 UTC)

<p>I have a stl model of an arm, I do not have the CT. from this model I have to select only the external surface and give it a thickness to make an orthopedic brace.<br>
I can not figure out how to select only the external surface</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2018-08-28 14:03 UTC)

<p>If you only have mesh data then you can use pure mesh editing software for this, such as MeshMixer, Blender, or Autodesk Fusion 360. However, if you plan to generate orthopedic brace directly from imaging (or you need a thick brace and mesh editing software struggle with creating a non-self-intersecting mesh) then it is worth learning how to do it in Slicer.</p>
<p>To create a shell from an STL file in Slicer:</p>
<ul>
<li>Load the STL file into Slicer</li>
<li>Go to Segmentations module</li>
<li>Create a new segmentation</li>
<li>Import the model into the segmentation (Export/Import… section)</li>
<li>Go to Sample data module and load MRHead sample (this is necessary because currently, Segment editing requires selection of a reference volume, and the simplest way of creating one is to load an existing volume, you can ignore its content)</li>
<li>Go to Segment editor module</li>
<li>Use “Hollow” effect to create a shell</li>
</ul>
<p>You need to use a recent nightly version of Slicer (not older than a few weeks).</p>

---

## Post #3 by @giulia29 (2018-08-28 17:34 UTC)

<p>Thanks for the answer, when I use ‘Hollow’ to create the shell and I click apply I do not see anything on the model, I do not know what I’m doing wrong.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4966e6e0fc2af8fd70e2a133b45b0aa1bf1410de.jpeg" data-download-href="/uploads/short-url/atljWamwzWZhR3jEjG9c5QLy3WC.jpeg?dl=1" title="tutore" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4966e6e0fc2af8fd70e2a133b45b0aa1bf1410de_2_690x387.jpeg" alt="tutore" data-base62-sha1="atljWamwzWZhR3jEjG9c5QLy3WC" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4966e6e0fc2af8fd70e2a133b45b0aa1bf1410de_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4966e6e0fc2af8fd70e2a133b45b0aa1bf1410de_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4966e6e0fc2af8fd70e2a133b45b0aa1bf1410de.jpeg 2x" data-dominant-color="ADAEBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tutore</span><span class="informations">1366×768 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-08-28 22:00 UTC)

<p>Probably the model that you imported is still there and hides the segmentation. Hide or delete the model after you imported it into segmentation. To see the segmentation in 3D, click “Show 3D” button in Segment editor.</p>

---

## Post #5 by @giulia29 (2018-08-29 07:57 UTC)

<p>ok thanks, the model hides the segmentation but what I find is not as hollow as I wanted, but the inside is full</p>

---

## Post #6 by @lassoan (2018-08-29 11:56 UTC)

<p>Apply Hollow effect then cut off the two ends with Scissors effect.</p>

---
