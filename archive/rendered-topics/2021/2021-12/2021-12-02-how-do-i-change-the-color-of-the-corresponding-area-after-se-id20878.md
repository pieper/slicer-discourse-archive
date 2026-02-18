# How do I change the color of the corresponding area after setting the threshold？

**Topic ID**: 20878
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/how-do-i-change-the-color-of-the-corresponding-area-after-setting-the-threshold/20878

---

## Post #1 by @Luke199208 (2021-12-02 07:42 UTC)

<p>Hello Everyone,</p>
<p>I used the method in 3D Slicer Documentation to modify the thresholds in the volume 。<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=threshold#modify-voxels-in-a-volume" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40047f69d9de97b9d8bd08e3834d4aaf46bf3f7.png" data-download-href="/uploads/short-url/wwZsRv3ArD7xG7U8heIKrldWiLJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40047f69d9de97b9d8bd08e3834d4aaf46bf3f7.png" alt="image" data-base62-sha1="wwZsRv3ArD7xG7U8heIKrldWiLJ" width="690" height="175" data-dominant-color="EDF4DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×225 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fb307c63fa7be52c72ff1a6363c6fef8cc9654c.png" alt="image" data-base62-sha1="fW8zl8LhWEHgRHbEcurmPyhvQZu" width="511" height="324"><br>
How do I change the color of the corresponding area after setting the threshold？ Because gray is indistinguishable from the rest of the image.</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @lassoan (2021-12-02 18:27 UTC)

<p>Regardless of what voxel values you set in a volume that is displayed using “gray” colormap then the volume will still always appear as shades of gray.</p>
<p>What are you trying to achieve: show a colored overlay (segmentation, markups, etc.) on the volume for highlighting something, or change the CT volume content? What is the clinical application and your overall goal?</p>

---

## Post #3 by @Luke199208 (2021-12-03 02:13 UTC)

<p>Thank you for your reply！</p>
<p>Functional goals：Multiple markers are affixed to the patient’s skin (markers can be recognized in CT and displayed in CT images) . We want to set the image threshold via the Python script (only marks on the skin will be labeled) .  Automatically creates a segment for each tag and gets the center of mass for each segment  as A,A’,A’',…gets the coordinates of each center of mass</p>
<p>Sample graph:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9691e6cb3c13d32859a5e02ca54cad6e74e357.png" alt="image" data-base62-sha1="4dKrm4rAePxjILNfLBf03vYrKIL" width="278" height="261"></p>

---

## Post #4 by @lassoan (2021-12-03 05:00 UTC)

<p>You can make the marker detection fully automatic quite easily:</p>
<ul>
<li>threshold the image (you can use Segment Editor for these first few steps, first manually, then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-run-segment-editor-effects-from-a-script">automate using Python scripting</a>)</li>
<li>apply some global smoothing (median, maybe Gaussian) if needed</li>
<li>split each island to a separate segment using Island effect; set the minimum size just slightly smaller than the fiducial marker’s volume</li>
<li>use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment statistics module</a> to compute shape and size metrics (this can be scripted, too); by checking oriented bounding box size, flatness, roundness, elongation you can determine which segments correspond to fiducial marker</li>
</ul>
<p>Segment statistics module also provides the centroid of each segment that you can use in the Fiducial registration module to compute the transform between the phantom’s coordinate system and the image coordinate system.</p>
<p>All the steps can be executed using the GUI and I would recommend to start with that. Once you have figured out a robust workflow then you can write a short Python script that automates all the steps. THe <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> is a good starting point, but if you get stuck at any point then you can ask for help here.</p>

---

## Post #5 by @Luke199208 (2021-12-03 05:29 UTC)

<p>Thank you so so so much! I will try it.</p>

---
