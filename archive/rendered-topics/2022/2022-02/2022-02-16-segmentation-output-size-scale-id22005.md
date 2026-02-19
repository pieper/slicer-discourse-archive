---
topic_id: 22005
title: "Segmentation Output Size Scale"
date: 2022-02-16
url: https://discourse.slicer.org/t/22005
---

# Segmentation Output Size Scale

**Topic ID**: 22005
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/segmentation-output-size-scale/22005

---

## Post #1 by @Ed_Hopkins (2022-02-16 20:52 UTC)

<p>Hi there!</p>
<p>New 3D Slicer user.</p>
<p>Just wondering if anyone knows if I am going wrong anywhere, I have hundreds of CT scan images, similar to the one below. I have been able to generate a segmentation/reconstructed CAD geometry (STL File) from these images.</p>
<p>However, when I look at the size of the STL model, it is not comparable to the sample that I have CT images for, in terms of size. So I am wondering if it is at all possible to use the known the image separation distance (~6 um) to then generate an STL file with the correct dimensions? Or rather use the image separation distance and image size (x by y number of pixels)?</p>
<p>Any suggestions would be greatly appreciated,<br>
Ed</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb48d0d79d09fa8e582f248b1ee3472a6cf52ee0.png" alt="image" data-base62-sha1="zQXQPPwoa9GMwiOq4QmXLb63MVG" width="316" height="324"></p>

---

## Post #2 by @muratmaga (2022-02-16 21:56 UTC)

<p>I suspect your issue is similar to this thread <a href="https://discourse.slicer.org/t/ruler-in-orthographic-3d-view/4656/23" class="inline-onebox">Ruler in (orthographic) 3D view - #23 by muratmaga</a></p>
<p>Probaby the imported image has incorrect physical scale, hence all downstream objects carried this over.<br>
Can you check what the image spacing is reported for your volumes and that they are correct?</p>

---

## Post #3 by @Ed_Hopkins (2022-02-18 13:28 UTC)

<p>Hi Muratmaga,</p>
<p>The link link you supplied was extremely useful!</p>
<p>For anyone with the same issue, the following, is the process required to use generate a 3D CAD/STL file segmentation that can be exported using a 2D image stack (multiple CT scan images), with a known pixel spacing.</p>
<ol>
<li>
<p>Download 3D Slicer and have it installed.</p>
</li>
<li>
<p>At the top of 3D Slicer, use View —&gt; Extension Manager and search (in the top right) for SliceMorph.</p>
</li>
<li>
<p>Download and install and accept all of the required toolboxes (initially 5 and an extra 1 will popup).</p>
</li>
<li>
<p>Modules: SlicerMorph (bottom of dropdown) —&gt; Input and Output —&gt; ImageStacks. Or search for imagestacks using the magnifying glass.</p>
</li>
<li>
<p>Using the Input Files — &gt; Filename pattern: Select the first image in the sequence.</p>
</li>
<li>
<p>In the spacing: update this to the correct Image Pixel Size, in my case this was ~6um but I input this as 0.006 mm.</p>
</li>
<li>
<p>For a high quality CAD model, ensure that full model is selected in the Quality section.</p>
</li>
<li>
<p>Click Load Files.</p>
</li>
<li>
<p>Modules: Segmentation Editor —&gt; Add.</p>
</li>
<li>
<p>Threshold (select appropriate). REMEMBER TO CLICK APPLY.</p>
</li>
<li>
<p>In my case, I used the Island tab to remove small islands. Again remember to click apply.</p>
</li>
<li>
<p>Modules: Segmentations.</p>
</li>
<li>
<p>Representations —&gt; Click Create next to Closed Surface.</p>
</li>
<li>
<p>Expand the Export to files.</p>
</li>
<li>
<p>Select the export destination folder.</p>
</li>
<li>
<p>Click Export… and Enjoy!</p>
</li>
</ol>
<p>Kind regards,<br>
Ed</p>

---

## Post #4 by @Ed_Hopkins (2022-02-21 13:53 UTC)

<p>Just as a final edit, at step 6. the Image Pixel Size should be input into all 3 of the Spacing: boxes. As seen in the attached image.</p>
<p>Kind regards,<br>
Ed</p>
<p>P.S. This is done as the pixel is based on a voxel and is the same in all 3 dimensions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/829dccab1d35850f7c2db037131f4e223b2c75b7.png" data-download-href="/uploads/short-url/iDu9BOkWB1aB0tI9HOgjnctw6xh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/829dccab1d35850f7c2db037131f4e223b2c75b7.png" alt="image" data-base62-sha1="iDu9BOkWB1aB0tI9HOgjnctw6xh" width="531" height="500" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">547×515 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
