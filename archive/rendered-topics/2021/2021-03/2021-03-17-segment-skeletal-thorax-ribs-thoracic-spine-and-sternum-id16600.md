---
topic_id: 16600
title: "Segment Skeletal Thorax Ribs Thoracic Spine And Sternum"
date: 2021-03-17
url: https://discourse.slicer.org/t/16600
---

# Segment Skeletal thorax (Ribs, Thoracic spine and sternum)

**Topic ID**: 16600
**Date**: 2021-03-17
**URL**: https://discourse.slicer.org/t/segment-skeletal-thorax-ribs-thoracic-spine-and-sternum/16600

---

## Post #1 by @colabwarrior (2021-03-17 18:20 UTC)

<p>Hi,</p>
<p>I am trying to use slicer to isolate the skeletal thorax from DICOMS. I am working with threshold, islands and scissors tool but I am not able to isolate the bones cleanly. Soft  tissue, organs, scan bed shows up in the segmented image. Plus same threshold range captures different stuff for different DICOMS. I have two questions:</p>
<ol>
<li>Is there a way to cleanly segment the bones?</li>
<li>I have over 600 DICOMS from which I need to isolate the skeletal thorax (bones). How can   I do this using Python script?</li>
</ol>
<p>Thanks,<br>
Vik</p>

---

## Post #2 by @rbumm (2021-03-18 17:18 UTC)

<p>Hi Vik,</p>
<p>My personal preference for segmentation of thoracic skeletal bones is using the new  “local threshold” function of the “Segment Editor”, but this requires a few mouseclicks for each dataset. Another option would be the involvement of  “Grow from Seeds” as described in this thread: <a href="https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960" class="inline-onebox">Bone segmentation to create 3D-printable STL</a></p>
<p>Once you have defined a good workflow you can try to integrate it into a python script that loads the DICOM dataset, then lets you do the manually assisted segmentation, automatically saves the results, and switches to the next patient.</p>
<p>Regards,<br>
Rudolf</p>

---

## Post #3 by @rbumm (2021-03-19 08:19 UTC)

<p>PS for detailed and almost instant overviews of the thoracic bone structures you can use “Volume Rendering” and the “CT-AAA”  preset.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dfd13a782229cf6af16be25708797a798b5ad70.jpeg" data-download-href="/uploads/short-url/kg5xlo9VrEG9l06jscz2DyL850I.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dfd13a782229cf6af16be25708797a798b5ad70_2_690x228.jpeg" alt="image" data-base62-sha1="kg5xlo9VrEG9l06jscz2DyL850I" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dfd13a782229cf6af16be25708797a798b5ad70_2_690x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dfd13a782229cf6af16be25708797a798b5ad70_2_1035x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dfd13a782229cf6af16be25708797a798b5ad70_2_1380x456.jpeg 2x" data-dominant-color="99999D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1908×633 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @colabwarrior (2021-03-19 14:24 UTC)

<p>Thanks Rudolf. I have the latest version 4.11 but I do not see any “local threshold” function. Is it in v5.0 and is there any tutorial on it?</p>

---

## Post #5 by @colabwarrior (2021-03-19 14:33 UTC)

<p>Thanks Rudolf. If I use the “CT-AAA” preset, can I save the displayed parts directly. Also in “CT-AAA” preset, scan bed shows up with some other noise. So it is still not a clean bone segmentation.  <a href="/uploads/short-url/4tX1DVWQA9xOPn2t48diw6UVN8N.jpeg">Annotation 2021-03-19 102944|400x347</a> . Any suggestion is highly appreciated. Thanks again.</p>

---

## Post #6 by @rbumm (2021-03-19 14:38 UTC)

<p>You will find it after installing the “Segment Editor Extra Effects” extension from the extensions manager.</p>
<p>More information on the effect see here: <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233/7" class="inline-onebox">New Segment Editor effect: Local threshold - #7 by sfglio</a></p>
<p>It is important to remember that - after selection of a “bone” threshold - you need to left click into one of the slices (onto the bone) to add to the new segmentation.</p>

---

## Post #7 by @rbumm (2021-03-19 14:43 UTC)

<p>CT-AAA: Adjust the “shift” slider a bit right or left to remove or include unwanted areas</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70ab2c2d9c55ef4e03f48af376b3cf369cb7393e.png" alt="image" data-base62-sha1="g4Id9OSyItdUNby6DUSTDZuUfds" width="634" height="91"></p>
<p>Please remember, that you are working with volume rendering here, you will not get any kind of 3D printable segment or segment statistics, it is is just a  quick visual 3D representation of the volume.</p>

---

## Post #8 by @colabwarrior (2021-03-19 14:44 UTC)

<p>Thanks Rudolf. I was looking at the “CT-AAA” preset and if I move the shift parameter it does help a lot but these lines from the scan bed show up. Not sure how to eliminate those. Also can I save only the displayed parts from this “CT-AAA” preset to a new file (DICOM, NIFTI etc.)</p>

---

## Post #9 by @rbumm (2021-03-19 14:56 UTC)

<p>Sure, enable Crop and check ROI as shown here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cab45f8fbd7f4f11e4e6ae4d2bee4ac3fcc88c9b.png" alt="image" data-base62-sha1="sVcTC80THGlTvVItdbzoMi4WN6P" width="642" height="94"></p>
<p>then you can crop away the table artefact by moving the ROI box markers around</p>

---

## Post #10 by @colabwarrior (2021-03-19 15:04 UTC)

<p>Thanks. Is there a way to save this rendered volume only?</p>

---

## Post #11 by @rbumm (2021-03-19 15:43 UTC)

<p>As no “real” 3D segmentation is generated in volume rendering, you would just save (“File” → “Save”)  the scene into a directory of your choice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/410630d43e953f9df485ffaf56d0e13c894bf869.png" data-download-href="/uploads/short-url/9heiy1T1WbdfM34N80j45s9QrCp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/410630d43e953f9df485ffaf56d0e13c894bf869_2_690x388.png" alt="image" data-base62-sha1="9heiy1T1WbdfM34N80j45s9QrCp" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/410630d43e953f9df485ffaf56d0e13c894bf869_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/410630d43e953f9df485ffaf56d0e13c894bf869_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/410630d43e953f9df485ffaf56d0e13c894bf869_2_1380x776.png 2x" data-dominant-color="D2D2DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 369 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Calling the “*.mrml” file later will reopen your volume rendering exactly as you have left it.</p>
<p>Also have a look at saving from 3D Slicer into a “*.mrb” bundle - this will save the complete data set into one single file.</p>

---

## Post #12 by @colabwarrior (2021-03-23 16:28 UTC)

<p>Hello Rudolf,</p>
<p>I saved the file as a *.mrb file. Is there a way to extract the 3D array of the CT-AAA preset. I want to use the array for machine learning. Thanks</p>

---

## Post #13 by @rbumm (2021-03-23 17:11 UTC)

<p>That sounds very interesting.</p>
<p>A quick google search revealed this thread:</p>
<aside class="quote quote-modified" data-post="2" data-topic="3063">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063/2">How to set volume rendering preset using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi Oliver, 
There have been some improvements since 4.8.1 that makes it easier for us to do this. So if you use the latest nightly, then this is what you can do: 
Easier setup of volume rendering (no need to create the display node and update it from the logic): 
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)

This is not very clean, because it uses widgets from the volume rendering module, but you can apply a shift li…
  </blockquote>
</aside>

<p>which may get you started …<br>
What is the goal of your trial in the end, what do you need to see?</p>
<p>Best regards<br>
Rudolf</p>

---

## Post #14 by @mikebind (2021-03-23 17:16 UTC)

<p>The CT-AAA preset is pretty close to a straight threshold. You can see the transfer function in the Volume Rendering module, under Advanced…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e2d63386fdc8ed7e38074fdc9d189d75113bdb.png" data-download-href="/uploads/short-url/gXIkTf9gRd3fmRGljAi6wfatenV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76e2d63386fdc8ed7e38074fdc9d189d75113bdb_2_615x500.png" alt="image" data-base62-sha1="gXIkTf9gRd3fmRGljAi6wfatenV" width="615" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76e2d63386fdc8ed7e38074fdc9d189d75113bdb_2_615x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e2d63386fdc8ed7e38074fdc9d189d75113bdb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e2d63386fdc8ed7e38074fdc9d189d75113bdb.png 2x" data-dominant-color="F3F3F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×599 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The effective threshold is where Point 2 is in the transfer function.  Note that this slides back and forth with the “Shift” slider, so you want to identify the value of Point 2 when you like how the volume rendering looks.</p>
<p>If you want a volume output, you can generate a thresholded volume easily in a couple different ways (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a> for an example).  However, if this is good enough training data for your ML project, then essentially all you are doing is teaching it to apply a binary threshold, which you hardly need machine learning for…</p>
<p>If you need to do something more complex, then you basically need to figure out a workflow that works well on some of your example images, and if you are lucky and it requires no manual decisions on a per-image basis, then you can fully automate it and try it on the rest of your 600 images.  If it still requires user judgement on every image, you can still create a facilitated workflow which will speed your processing of the remaining images, but that’s the best you can do.</p>

---

## Post #15 by @colabwarrior (2021-03-23 17:20 UTC)

<p>I am developing computational Human models and need to come up with an average thorax geometry for males and females for injury analysis.</p>
<p>Also in the link you sent, it does not say how to store the CT-AAA preset as a 3D array, which can be opened with Numpy and not Slicer. Is that possible? Thanks</p>

---

## Post #16 by @mikebind (2021-03-23 17:38 UTC)

<pre><code>import numpy as np
imageVolumeNode = getNode('ThoraxImage') # replace with the name of your volume
thresholdValue = 350 # whatever threshold value you want
imageNumpyArray = slicer.util.arrayFromVolume(imageVolumeNode)
threshIm = imageNumpyArray &gt; thresholdValue
with open('numpyOutput.npy', 'wb') as file_handle:
  np.save(file_handle, threshIm)
</code></pre>
<p>This will threshold your entire volume at 350 HU, and save the output logical numpy array to “numpyOutput.npy” (which can be loaded into numpy using numpy.load()).  Note that this will not crop out the table, as you might have in the volume rendering.  To do that, you can use the CropVolume module using the same ROI as you used in the volume rendering module.  Then, in the code snippet above, use the name of the cropped volume node rather than the original volume (or you can just have the cropped volume replace the original volume by selecting it as the output volume in “CropVolume” instead of “Create new volume”.</p>

---

## Post #17 by @colabwarrior (2021-03-23 17:41 UTC)

<p>Thanks Mike. This is really helpful.</p>

---
