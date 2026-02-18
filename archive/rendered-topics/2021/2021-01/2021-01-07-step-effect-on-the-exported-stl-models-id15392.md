# Step effect on the exported STL models

**Topic ID**: 15392
**Date**: 2021-01-07
**URL**: https://discourse.slicer.org/t/step-effect-on-the-exported-stl-models/15392

---

## Post #1 by @Tekk_ya (2021-01-07 15:29 UTC)

<p>Hi,</p>
<p>I have segmented the desired organs in a CT scan, and after applying a different type of smoothing such as median smoothing and joint smoothing I export the models as STL files. However, I see some “step effect” on the exported geometries. You can simply see this effect by disabling the surface smoothing in the show 3D module. Note that, some of the segmented geometries are watertight, so I need an approach that eliminates the undesired effect but keeps the geometries watertight (with no gap/overlapping). I really appreciate it if you could help me with this issue.</p>
<p>Thank you in advance for your help</p>

---

## Post #2 by @pll_llq (2021-01-08 08:11 UTC)

<p>Your source scan might be low resolution or the voxels aren’t isotropic (not cube shaped).<br>
If this is the case you can try to resample the scan to a higher resolution and isotropic voxels using the Crop Volume module and then go through the segmentation and smoothing.</p>

---

## Post #3 by @Tekk_ya (2021-01-08 10:00 UTC)

<p>Hi Theodore,</p>
<p>Thank you for your reply. Would you please let me know which module shows the voxels’ dimension?</p>
<p>Regarding your suggestions, I have done all of them in my geometry reconstruction process. So first, I have cropped the volume with the checked isotropic option. Second, I have segmented the geometries, Third, I have resampled the segmentation in such a way that the spacing is half of the original one. Finally, I have applied the smoothing steps.  I apply the resampling process after the segmentation due to the computational time and slow editing process. However, still, the exported geometries contain those patterns. Do you know if the smoothing surface is only used for visualization purposes or does it actually affect the exported models as well?</p>
<p>Best,<br>
Tekya</p>

---

## Post #4 by @pll_llq (2021-01-08 11:26 UTC)

<p>The spacing is the voxel dimensions.</p>
<p>If I understood you correctly you are doing the following:</p>
<ol>
<li>crop+resample the volume (convert to isotropic voxels)</li>
<li>create segmentation</li>
<li>resample segmentation (upsample)</li>
<li>smooth segmentation</li>
<li>resample segmentation back (downsample)</li>
<li>create and export models</li>
</ol>
<p>I would suggest</p>
<ol>
<li>crop+resample the volume (convert to isotropic voxels and upsample)</li>
<li>create and smooth segmentation</li>
<li>create and export models</li>
</ol>

---

## Post #5 by @cpinter (2021-01-08 11:42 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="15392">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>You can simply see this effect by disabling the surface smoothing in the show 3D module</p>
</blockquote>
</aside>
<p>Surface smoothing is not just a display option, it actually changes the way your segmentation is represented as a 3D surface. So if you turn smoothing off and export the STL, you’ll have the little cubes that originate from the finite resolution of the master labelmap representation. If you enable smoothing and export to STL, then it will be smooth. There is no change in terms of “watertightness”, your surface will be closed.</p>

---

## Post #6 by @Tekk_ya (2021-01-08 13:49 UTC)

<p>In my case, the original scan contains a cube shape voxels.</p>
<p>Yes, I followed all steps in the order you mentioned from 1 to 6 expect the step5. Wouldn’t the downsampling of the segmentation cause a similar issue?</p>
<p>Regarding your suggested approach, I have a few questions:<br>
1 - Should I complete the first step in the Crop Volume module by checking the isotropic option and interpolating option (scaling the spacing)?<br>
2 - what is the difference between the space scaling in the crop volume module and the oversampling option in the below image? Is there any difference between these two approaches? if so, would you please explain them in detail?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e2f27d6fb7086c365ccd1d09550da398e8a63b4.png" alt="image" data-base62-sha1="b9EgW0bByqpXxC8kIJIYJji17Ug" width="606" height="406"></p>
<p>3 - For exporting the segmentations as 3D models, should the segmentation and the scan have the same spacing? what would happen if I do not complete step 5? is it a must to do a thing? should they always match?</p>
<p>4 - As I mentioned, I have done the segmentation step (steps 1 through 4), and I am not planning to redo the segmentation as it is a time-consuming process. Do you have any other suggestions for my current stage?</p>
<p>Thanks</p>

---

## Post #7 by @Tekk_ya (2021-01-08 13:57 UTC)

<p>Hi,</p>
<p>Thanks for your reply. I recall that I had a penetration issue in my segmented geometries using the surface smoothing. However, I will check it once more and will let you know about the results. The amount of the penetrations were relatively small which I was thinking they are coming from marching cubes of flying edges algorithms while exporting the 3D models. Please correct me if I am wrong.</p>

---

## Post #8 by @cpinter (2021-01-08 15:11 UTC)

<p>Can you elaborate on what you mean by penetration? Is it excessive smoothing at certain regions?</p>
<p>You can adjust the amount of smoothing using the <code>Smoothing factor</code> slider in the drop-down menu that appears if you click the small arrow next to <code>Show 3D</code>.</p>

---

## Post #9 by @lassoan (2021-01-08 15:31 UTC)

<p>See this <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#generated-surface-contains-step-artifacts">Segment Editor FAQ</a> for instructions on how to avoid staircase artifacts and overlap (penetration) between segments.</p>

---
