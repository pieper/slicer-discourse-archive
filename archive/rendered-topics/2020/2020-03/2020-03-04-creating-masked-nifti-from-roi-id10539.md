# Creating masked nifti from ROI

**Topic ID**: 10539
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/creating-masked-nifti-from-roi/10539

---

## Post #1 by @joelyss (2020-03-04 13:22 UTC)

<p>Software version: 3D Slicer 4.10.2</p>
<p>I would like to draw an ROI on a ACPC transformed dataset, then create a binary mask of that ROI whee everything inside has a value of 1 and zeroes outside, and to have the same dimensions as the original nifti T1 dataset i.e. possibly requiring an invert transform. So I can take this nifti mask out of 3D slicer and use it in our current mrtrix3 processing pipeline.</p>
<p>I’m having a few issues doing this and following previous similar threads and online tutorials have not managed to figure this out.</p>
<p>My workflow currently:</p>
<ul>
<li>load in data &amp; create models</li>
<li>perform ACPC transform to data</li>
<li>draw an ROI (that measures 4x4x6 mm3 in the ACPC transformed plane)</li>
</ul>
<p>Then I get stuck. I have tried using the crop volume module and the mask scalar volume modules but I cannot seem to get what I am after.</p>
<p>Any help appreciated, many thanks,<br>
Joely</p>

---

## Post #2 by @lassoan (2020-03-05 05:26 UTC)

<p>You can draw ROI on an image using Segment Editor module (for example, using scissors or paint effects,or any of the automated tools), convert it to labelmap (by right-clicking on the segmentation in Data module), and save the labelmap as nifti.</p>
<p>If you want to draw an ROI with a specific shape and size then you can write a very simple scripted module, which takes markup points/lines as inputs to position a model node, then on the click of a button, it converts it to segmentation node, and then exports it as a labelmap. The module can also launch mrtrix3 processing and visualize the results in Slicer - all by a single click. The programming effort is probably a few hours for someone who is already familiar Slicer programming and maybe a few days for someone who is familiar with VTK, Python, and Qt but does not know anything about Slicer yet. See this <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">tutorial</a> to get started - and feel free to ask here if you have any questions.</p>

---

## Post #3 by @joelyss (2020-03-12 13:53 UTC)

<p>Thank you for getting back to me !</p>
<p>I struggled to get it to work following the segmentation editor module. But I did figure out a way to do what I needed, so here it is if this helps future visitors:</p>
<p>I drew my ROI, in whichever way would work for you, as mine is based off of distances from landmarks and specific measurements (in mm) I found it easiest using the <strong>‘Annotations’</strong> module and using the ruler, fudicial and ROI tools.</p>
<p>Then to convert this to a model I used the <strong>‘Markups to Model’</strong> module.</p>
<p>This was possible as my ROI was a simple cuboid. I could locate the base slice, use the fudicial tool to mark out each corner of the ROI, scroll to the top slice of the ROI and draw fudicials on the 4 corners again.</p>
<p>Then I opened the <strong>‘Data’</strong> module, right clicked on the new ROI model and saved the model as a nii file.</p>
<p>Then checking the result in ImageJ I could see that even though I had performed an ACPC transform on the data in Slicer, it wasn’t ‘hardened’ and therefore the ROI was in the correct (original) space and I did not need to perform an invert transform.</p>
<p>Thanks for the tips on automation. This is something I will look into and go through the tutorial as this will really streamline my process.</p>
<p>Many thanks for the help,<br>
Joely</p>

---
