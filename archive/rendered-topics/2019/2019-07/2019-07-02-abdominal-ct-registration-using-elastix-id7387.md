# Abdominal CT registration using Elastix

**Topic ID**: 7387
**Date**: 2019-07-02
**URL**: https://discourse.slicer.org/t/abdominal-ct-registration-using-elastix/7387

---

## Post #1 by @AVLguru (2019-07-02 07:52 UTC)

<p>He! Currently I am trying to use Elastix during registration in 3D Slicer. However, I am hoping to gain some tips and tricks for the registration of abdominal CT scans. I would like to use a ROI, however I could only use a volumeclip to register with the other image instead of the registration with the original image. Could you help me out with this?</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2019-07-02 19:19 UTC)

<p>You can crop volume to the desired region rectangular region of interest using “Crop Volume” module, and you can specify arbitrarily shaped masks in “General registration (Elastix)” module. You can apply the registration result to the original (non-clipped, non-masked) volume.</p>

---

## Post #3 by @AVLguru (2019-07-03 13:32 UTC)

<p>Thank you. If I’m understanding right I could try two things:</p>
<ol>
<li>crop an ROI, register this with a fixed volume and then use the transform to register the non-cropped image in ‘Transform’.</li>
<li>create or specify a mask by for example using ‘Foreground Masking (BRAINS)’ and apply this mask in Elastix as mask. Or are there any other options to create a mask for registration?</li>
</ol>

---

## Post #4 by @lassoan (2019-07-04 00:31 UTC)

<p>You can create a mask by using Segment Editor . You can use any effect, such as simple paint with a large brush, or scissors (fill in from one viewpoint then cut the two ends from another viewpoint), or using Surface Cut effect (provided by SegmentEditorExtraEffects extension). Then you can export the segment to a labelmap by right-clicking on the segmentation in Data module and choosing export to labelmap volume.</p>

---

## Post #5 by @AVLguru (2019-07-05 13:24 UTC)

<p>I’ve tried using scissors and surface cut as a mask (in fixed as well as moving volume mask), however I get these two errors:</p>
<p>‘Could not find enough image samples within reasonable time. Probably the mask is too small’<br>
‘Too many samples map outside moving image buffer: 265 / 32768’</p>
<p>I’m not sure what I’m doing wrong considering I’ve done as what you suggested me to do.<br>
If I’m right you tell me to do it in these steps: create mask --&gt; save as labelmap --&gt; use this mask in Elastix (fixed/moving volume mask) --&gt; Save Transform --&gt; Apply transform to non-clipped/masked volume. What I do not get is that Elastix seems not to accept my masks to apply for registration…</p>

---

## Post #6 by @lassoan (2019-07-05 16:39 UTC)

<p>This happens if the mask is much smaller than the entire image. You can either to crop the volume to make it approximately same size as the masked area, or use a different sampler as suggested <a href="https://github.com/SuperElastix/elastix/wiki/FAQ#i-am-getting-the-error-message-could-not-find-enough-image-samples-within-reasonable-time-probably-the-mask-is-too-small-what-can-i-do-about-it" rel="nofollow noopener">here</a>.</p>

---

## Post #7 by @AVLguru (2019-07-10 06:55 UTC)

<p>I think I solved the problem by adding the suggested sampler. However I am still not sure if I’m doing it right compared to the ROI volume that I clip. So I’ll address it in the steps I’ve made:</p>
<ol>
<li>clipping volume ROI of moving volume (Second Volume)</li>
<li>Elastix registration with ROI volume as moving volume over the original fixed volume (First Volume)</li>
<li>Save Transform</li>
<li>Go to Transform Module and apply the given Transform on the original Second Volume.</li>
<li>Check registration between First and Second volume.</li>
</ol>
<p>However if I do this the only registration that appears to happen is within the boundaries of the ROI in the Second Volume plus a small region around the ROI border. Maybe I’m not clear but it means only a volume within the Second Volume that is slightly greater compared to the ROI that I’ve used. Two questions:</p>
<ol>
<li>Are the steps I’m taking right?</li>
<li>Does Slicer only apply the Transform around the ROI in the Second image?</li>
</ol>

---

## Post #8 by @AVLguru (2019-07-19 11:51 UTC)

<p>Dear Andras Lasso,</p>
<p>Could you reply my question if you are able to?<br>
In addition, is it possible to change the script and for example let Elastix do an easier threshold registration? Can we modify the parameter files to accomplish this?</p>
<p>And does Elastix always present the transform symbol as a deformable transform in the Data module? Because if an rigid registration is applied, the symbol of an deformed transform is visible if we apply this on the volume, is this correct although the transform is basically rigid?</p>
<p>Sincerely</p>

---
