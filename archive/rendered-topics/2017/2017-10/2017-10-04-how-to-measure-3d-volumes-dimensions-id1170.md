# How to measure 3D volume's dimensions?

**Topic ID**: 1170
**Date**: 2017-10-04
**URL**: https://discourse.slicer.org/t/how-to-measure-3d-volumes-dimensions/1170

---

## Post #1 by @Mohamed (2017-10-04 10:42 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.7.0-2017-09-21</p>
<p>Hi, I wanted to know how to measure the dimensions of the 3D volume data. For example the perimeter or mass.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2017-10-04 12:30 UTC)

<p>If you segment and make a model you can get volume and surface area.  To get mass you’d need to know the density, which Slicer doesn’t store.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Models" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Models</a></p>
<p>Maybe you can give more details about what you are trying to do and we can give further pointers.</p>

---

## Post #3 by @lassoan (2017-10-04 12:53 UTC)

<p>You can get density (mean intensity of a volume in a selected segment) by Segment Statistics module. Segment Statistics also computes surface, volume, and other properties of segments. You need to use recent nightly version of Slicer and create segments using Segment Editor module.</p>

---

## Post #4 by @pieper (2017-10-04 13:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can get density (mean intensity of a volume in a selected segment)</p>
</blockquote>
</aside>
<p>but to know the overall mass of the segmented volume you’d still need to know the mapping from “signal” density to “mass” density which probably depends on many factors which may not be in the imaging data.</p>

---

## Post #5 by @gcsharp (2017-10-04 13:38 UTC)

<p>For CT, it is reasonable to neglect atomic number and assume all materials are density-scaled water.  Density would be (1000+intensity)/1000 g/cc.</p>

---

## Post #6 by @Mohamed (2017-10-05 11:18 UTC)

<p>Thanks Steve for your answer. Yes i was looking for that data as i want to compare the data size before and after decimation.<br>
Thanks again for referring the doc.<br>
Thanks for everyone’s answer as well.</p>
<p>Regards,</p>

---

## Post #7 by @stevenagl12 (2018-11-09 19:27 UTC)

<p>When using segment statistics, why does it generate 3 different values for volume in mm3 and cm3 per segment? Also, is there a way to compute maximum/minimum 3D diameter with any of the statistics modules? I know radiomics has it, but I guess radiomics is down…</p>

---

## Post #8 by @lassoan (2018-11-09 20:10 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="7" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>why does it generate 3 different values</p>
</blockquote>
</aside>
<p>There are several ways of computing these metrics. The main difference is what is the representation used (surface or volumetric) and if the entire segment is used or only the part that overlaps with the selected scalar volume.</p>
<blockquote>
<p>Also, is there a way to compute maximum/minimum 3D diameter with any of the statistics modules?</p>
</blockquote>
<p>Currently diameter computation is not offered by any of the Segment Statistics plugins.</p>
<p>SimpleITK’s LabelShapeStatisticsImageFilter can compute many kind of diameters and it is already available in Slicer. So, it would be just a matter of adding a few ten lines of code to run the segment’s labelmap representation through this filter and add outputs to the table. Would you be interested in working on this?</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="7" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>radiomics is down</p>
</blockquote>
</aside>
<p>It should be back soon. You can monitor the status <a href="https://github.com/Radiomics/SlicerRadiomics/issues/50">here</a>. Maybe add a note there to show that you would like to get this up and working again (and maybe offer your help, if you can).</p>

---

## Post #9 by @Lottemarijn (2019-05-27 09:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are several ways of computing these metrics. The main difference is what is the representation used (surface or volumetric) and if the entire segment is used or only the part that overlaps with the selected scalar volume.</p>
</blockquote>
</aside>
<p>I want to compare a segmentation from an ultrasound image to that of a CT-image. Which of the three values is most accurate to use for this purpose?<br>
Thanks</p>

---

## Post #10 by @lassoan (2019-05-27 12:30 UTC)

<p>Is there a significant difference between the reported values?</p>

---

## Post #11 by @Lottemarijn (2019-05-27 12:44 UTC)

<p>Thank you Andras for getting back to me so soon.</p>
<p>First of all, the values are very different when I use my segmentation or segmentation preview as input (which I don’t understand).</p>
<p>Secondly, the different volumes (1 and 2, when I use segmentation preview) are respectively 3482,77 mm3 and 3449,25 mm3. Not the biggest difference, but since I will be comparing two different images, I need to make sure that the volume i am using is as accurate as possible and is calculated with the same input as the computed surface area.</p>
<p>Also, I noticed that earlier in this discussion topic, you’ve stated that it was not possible to compute the maximum/minimum 3D diameter. Is this still correct?</p>

---

## Post #12 by @lassoan (2019-05-27 13:22 UTC)

<aside class="quote no-group" data-username="Lottemarijn" data-post="11" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/6de8d8/48.png" class="avatar"> Lottemarijn:</div>
<blockquote>
<p>values are very different when I use my segmentation or segmentation preview as input (which I don’t understand).</p>
</blockquote>
</aside>
<p>Until you apply an auto-complete effect (Grow from seeds, Watershed, etc.) current segmentation stores seeds and preview segmentation stores the final results. Apply the segmentation effect before quantification.</p>
<aside class="quote no-group" data-username="Lottemarijn" data-post="11" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/6de8d8/48.png" class="avatar"> Lottemarijn:</div>
<blockquote>
<p>the different volumes (1 and 2, when I use segmentation preview) are respectively 3482,77 mm3 and 3449,25 mm3.</p>
</blockquote>
</aside>
<p>It does not matter which method you use (the difference is less than 1%), just choose one and use always that. If you primarily work with labelmaps (and use 3D surface for visualization only) then you may prefer labelmap based method; if you mainly work with surfaces then you may choose the volume computed from the generated surface.</p>
<aside class="quote no-group" data-username="Lottemarijn" data-post="11" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/6de8d8/48.png" class="avatar"> Lottemarijn:</div>
<blockquote>
<p>it was not possible to compute the maximum/minimum 3D diameter. Is this still correct?</p>
</blockquote>
</aside>
<p>Correct. It would not be difficult to implement something like this, but for arbitrary shapes, maximum/minimum 3D diameter is not a well-defined metric. How would you define maximum/minimum 3D diameter for your segmented objects?</p>

---

## Post #13 by @Lottemarijn (2019-05-27 13:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Until you apply an auto-complete effect (Grow from seeds, Watershed, etc.) current segmentation stores seeds and preview segmentation stores the final results. Apply the segmentation effect before quantification.</p>
</blockquote>
</aside>
<p>You are right! this worked for me.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It does not matter which method you use (the difference is less than 1%), just choose one and use always that. If you primarily work with labelmaps (and use 3D surface for visualization only) then you may prefer labelmap based method; if you mainly work with surfaces then you may choose the volume computed from the generated surface.</p>
</blockquote>
</aside>
<p>Thank you for your explanation.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="1170">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Correct. It would not be difficult to implement something like this, but for arbitrary shapes, maximum/minimum 3D diameter is not a well-defined metric. How would you define maximum/minimum 3D diameter for your segmented objects?</p>
</blockquote>
</aside>
<p>I understand that it would be difficult for arbitrary shapes. However, it could also be interesting to know the maximum diameter in the three different axes or the average diameter in those three different axes. Is this possible with the current modules and extensions?</p>

---

## Post #14 by @JoostJM (2019-06-17 08:20 UTC)

<p><a class="mention" href="/u/lottemarijn">@Lottemarijn</a>, the SlicerRadiomics extension (based on PyRadiomics) has maximum diameters implemented in the shape feature classes.</p>
<p>For class shape (describing 3D volumes) this is the maximum diameter in row (=saggital), column (=coronal) and slice (=axial) plane, as well as the maximum 3D overall.<br>
These diameters are calculated on the 3D surface mesh, as the other shape features also work with this representation. This mesh is build-up from point that lie half-way between a voxel-center that is part of the segmentation and one that is not. Moreover, this class also implements volume and surface area calculated on the mesh (MeshVolume and SurfaceArea), as well as volum based on counting the voxels (VoxelVolume)</p>
<p>For class shape2D (describing 2D surfaces), equivalent features for 2-dimensional surfaces have been implemented. Instead of MeshVolume and VoxelVolume, there is MeshSurface and PixelSurface, respectively and instead of SurfaceArea, there is Perimeter. This also implements a maximum diameter, but it is just the one (2D).</p>

---

## Post #15 by @Lottemarijn (2019-07-10 12:26 UTC)

<p>Hey Joost,</p>
<p>Thanks for responding to this topic.<br>
I’ve tried to use the SlicerRadiomics extension for calculation these diameters, but the module doesnt function properly. When I press the “Apply” button, after selecting the input image volume and input region, the button changes to “Working…”. After this the program crashes.<br>
Do you have a suggestion on how to solve this problem?</p>

---

## Post #16 by @JoostJM (2019-12-10 06:52 UTC)

<p>My apologies for this late reply,<br>
There have been some updates to the extension, so it may work now. If not, can you share an anonymized image/mask so we can debug the issue?<br>
Alternatively, you can also try to extract features using the PyRadiomics command line interface.</p>

---
