---
topic_id: 10144
title: "Calculating Shared Volume Between Two Models"
date: 2020-02-06
url: https://discourse.slicer.org/t/10144
---

# Calculating shared volume between two models

**Topic ID**: 10144
**Date**: 2020-02-06
**URL**: https://discourse.slicer.org/t/calculating-shared-volume-between-two-models/10144

---

## Post #1 by @aalarcon96 (2020-02-06 20:55 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.11</p>
<p>Hi,</p>
<p>I want to calculate the total volume of these two tumor models and the shared volume (AKA how much they overlap/purple area). They are .vtk files, not segmentations. Thanks in advance!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37ca0b3b26ede29274a7f742b511d54765a7b7ef.png" alt="image" data-base62-sha1="7Xx8xYUmRYKYoUWDsnUv2X9Hdkb" width="344" height="354"></p>

---

## Post #2 by @Juicy (2020-02-07 04:16 UTC)

<p>There may be a better way to do this but the first thing that springs to mind for me is that you could import the vtk models as segments using the segmentations module (Go down to Export/import models and labelmaps and select Import and Model). Import both models using this method.</p>
<p>Now go to segment editor. You will need to load a volume of some sort to use as a master volume. Then you can use the logical operators effect in segment editor set to ‘Intersect’ to leave only the volume where the models intersect. Once you have the segment which represents the intersection volume you can delete the other segment as it wont be needed.</p>
<p>Then go to the segment statistics module and use that to find the volume of the segment you have just created.</p>

---

## Post #3 by @lassoan (2020-02-07 13:59 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="2" data-topic="10144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>There may be a better way to do this but the first thing that springs to mind for me is that you could import the vtk models as segments using the segmentations module (Go down to Export/import models and labelmaps and select Import and Model). Import both models using this method.</p>
</blockquote>
</aside>
<p>Exactly. And after the model is imported, you can use Segment Comparison module (provided by SlicerRT extension) to compute percentage of shared volume, Dice coefficient, Hausdorff distance, etc.</p>

---

## Post #4 by @aalarcon96 (2020-02-07 16:49 UTC)

<p>Thank you for the help! I did what <a class="mention" href="/u/juicy">@Juicy</a> advised but it creates a weirdly shaped volume (pink) that is a different shape than the intersecting volume. Any suggestions on why?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3174c3a57333db998b4773d0a833bba001c09d.png" alt="image" data-base62-sha1="qz8LF0aLfz4JPZNcxLlEx3NCdrv" width="372" height="467"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ae524236dee66e9140899cf511322d324cecb05.png" alt="image" data-base62-sha1="1ynHRchDFirm8bHl7wraJ6KHuDj" width="362" height="456"></p>

---

## Post #5 by @Juicy (2020-02-07 19:59 UTC)

<p>I did try this on two vtk spheres and it worked fine. Is there any chance you could share just the two vtk models and I can see if I can recreate the problem?</p>
<p>Otherwise if it is the logical operators step which is causing you problems you could follow the advice above from <a class="mention" href="/u/lassoan">@lassoan</a> and use slicerRT which doesnt sound like you need to use logical operators.</p>

---

## Post #6 by @aalarcon96 (2020-02-10 15:45 UTC)

<p>I added the SlicerRT extension but it seems that some of the modules like Segment Comparison won’t load. <a class="mention" href="/u/juicy">@Juicy</a> how can I share with you the two vtk models? Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50ea8926c68274251299c32b5b7b170359814850.png" data-download-href="/uploads/short-url/bxOGFhpl7QHXla5jBYbY2j79Jq8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50ea8926c68274251299c32b5b7b170359814850_2_690x197.png" alt="image" data-base62-sha1="bxOGFhpl7QHXla5jBYbY2j79Jq8" width="690" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50ea8926c68274251299c32b5b7b170359814850_2_690x197.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50ea8926c68274251299c32b5b7b170359814850.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50ea8926c68274251299c32b5b7b170359814850.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">734×210 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Juicy (2020-02-10 19:24 UTC)

<p>I have sent you a private message with contact details if you wish to send the models through, thanks</p>

---

## Post #8 by @Juicy (2020-02-11 04:10 UTC)

<p>I managed to have a look at your models. Here is what worked for me:</p>
<ol>
<li>
<p>Import both the vtk models into a new instance of slicer</p>
</li>
<li>
<p>Go to the models module and change the colours of the models (in this case I made tumor 1 blue and tumor 2 green). I also made them translucent and turned on slice display visibility. (this isn’t necessary for volume calculation just good to visually check).</p>
</li>
<li>
<p>Go to the segmentations module and import both the models into a new segmentation node using the Export/import models and labelmaps.</p>
</li>
<li>
<p>Go to the segment editor and notice that all the effects are greyed out until you select a master volume. Instead of selecting a master volume click the small “Specify geometry button” (see pic below). In the drop down box select “Segmentation” (should be the lowest option). In my case my segmentation labelmap had voxel sizes of 0.08 x 0.08 x 0.08mm  which is good because you need small voxel sizes to accurately represent a small volume like this one. Then click “OK” and slicer will generate a dummy volume to use as a master volume which also has 0.08 x 0.08 x 0.08 voxel size.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f060331850d3d38e942330d719040137390402e1.jpeg" data-download-href="/uploads/short-url/yisHnb6jaJpcb4ULDjSlOt8nMsN.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f060331850d3d38e942330d719040137390402e1_2_690x451.jpeg" alt="1" data-base62-sha1="yisHnb6jaJpcb4ULDjSlOt8nMsN" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f060331850d3d38e942330d719040137390402e1_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f060331850d3d38e942330d719040137390402e1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f060331850d3d38e942330d719040137390402e1.jpeg 2x" data-dominant-color="A2AEAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">968×634 69.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>Then I selected tumor 1 from the list and clicked the “Logical Operators” as the effect. Change the operation to “Intersect” and select tumor 2 in the “Intersect with segment” box. Then click “Apply”. The tumor 1 segment will then be trimmed down to the area which intersects the other tumor 2.</p>
</li>
<li>
<p>I deleted tumor 2 as this is now longer needed for the calculation. I renamed the tumor 1 segment “Shared volume” and changed the colour to red. With the outlines of the models visible in the slice views you can now easily see that the “Shared Volume” is in the area where the models intersect.</p>
</li>
<li>
<p>Go to the Segment Statistics module and make the “Segmentation” node the input and press “Apply”</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a951c9b85ef0a7930f1eb546f168808586d90424.jpeg" data-download-href="/uploads/short-url/o9RVbN61pl1dUxM1WQpOMDWb0jy.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a951c9b85ef0a7930f1eb546f168808586d90424_2_690x383.jpeg" alt="2" data-base62-sha1="o9RVbN61pl1dUxM1WQpOMDWb0jy" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a951c9b85ef0a7930f1eb546f168808586d90424_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a951c9b85ef0a7930f1eb546f168808586d90424_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a951c9b85ef0a7930f1eb546f168808586d90424.jpeg 2x" data-dominant-color="A5A0A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1137×632 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This shows the shared volume is 3222.88 mm^3 or 3.22 cm^3.</p>
<p>I also converted the vtk files to STL and uploaded them in blender and used the boolean effect to generate a model of the shared volume. The result from blender was 3222.95 mm^2, so a very close agreement.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f1ae71886b3d366b6b1937f868e0b77ef9a17ad.jpeg" data-download-href="/uploads/short-url/bhNmfTiN6jSFwWSSsV09w5BPKXj.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f1ae71886b3d366b6b1937f868e0b77ef9a17ad_2_690x391.jpeg" alt="3" data-base62-sha1="bhNmfTiN6jSFwWSSsV09w5BPKXj" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f1ae71886b3d366b6b1937f868e0b77ef9a17ad_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f1ae71886b3d366b6b1937f868e0b77ef9a17ad.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f1ae71886b3d366b6b1937f868e0b77ef9a17ad.jpeg 2x" data-dominant-color="969CAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1003×569 74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Probably what when wrong for you was that you used a clinical scan as a reference volume (my fault as that is what I said to do) which typically have large voxel sizes around 0.5 x 0.5 x 0.5 for a fine slice CT scan (they will be even bigger for an MRI) this forces the segmentation to also have a large voxel size which will not be able to accurately represent a small volume like this one.</p>
<p>I also tried Segment Comparison which gave the volume of tumor 1 as 3.94 cm^2 and tumour 2 as 4.42 cm^2 but I couldn’t work out how to calculate the shared volume as I don’t understand what all the percentages mean in the Dice Coefficient area. <a class="mention" href="/u/lassoan">@lassoan</a>  could you advise on this? Also, why are there two volume outputs in the Segment Statistics module? Volume (1) seems to be in closer agreement with Blender in this case.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85ab0fdb1881b246600c0781e9f0f4a080227217.jpeg" data-download-href="/uploads/short-url/j4u07ZxngOEGRXu2fPIeDEhjh6D.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85ab0fdb1881b246600c0781e9f0f4a080227217_2_690x460.jpeg" alt="4" data-base62-sha1="j4u07ZxngOEGRXu2fPIeDEhjh6D" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85ab0fdb1881b246600c0781e9f0f4a080227217_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85ab0fdb1881b246600c0781e9f0f4a080227217.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85ab0fdb1881b246600c0781e9f0f4a080227217.jpeg 2x" data-dominant-color="89968E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">897×598 76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @Juicy (2020-02-11 06:24 UTC)

<p>Found some info on Segment Statistics in this post: <a href="https://discourse.slicer.org/t/segment-statistics/7303">https://discourse.slicer.org/t/segment-statistics/7303</a></p>
<p>My interpretation is one of the volumes is computed using a closed surface representation of the segment (similar to what you see when you press the 3d button in segment editor with surface smoothing ticked), and the other is computed by adding up the volume of all the individual voxels making up the segment.</p>
<p>I am guessing Volume (1) is the closed surface representation in this case? Volume (1) is slightly less in volume and agrees closely with the Blender computation which is based on surface models.</p>

---
