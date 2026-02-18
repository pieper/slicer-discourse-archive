# Human airway model

**Topic ID**: 34195
**Date**: 2024-02-07
**URL**: https://discourse.slicer.org/t/human-airway-model/34195

---

## Post #1 by @D_Dand (2024-02-07 21:55 UTC)

<p>Hello everyone,</p>
<p>I am a new member of our community and have a question that I would like to discuss with you.<br>
Does anyone try to build the entire human airway (upper and lower airway) from bronchi to nasal/oral cavity and export as one STL file? I tried using <strong>lung CT segmented extension</strong>. The lower airway looks very good, but the upper airway. I have a problem with my upper airway that there is leaking area in CT images that made up an issue (please find in picture below). Anyone has done this type of things, please give me suggestion how can I build up the entire human airway?</p>
<p>I am more than happy to listen to you all!<br>
Thank you very much in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970b3713cec52fd918e4457f2f8db98acc054405.jpeg" data-download-href="/uploads/short-url/lyc7PNf5V5jciyppywTiOJm8DyJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970b3713cec52fd918e4457f2f8db98acc054405_2_690x390.jpeg" alt="image" data-base62-sha1="lyc7PNf5V5jciyppywTiOJm8DyJ" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970b3713cec52fd918e4457f2f8db98acc054405_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970b3713cec52fd918e4457f2f8db98acc054405_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970b3713cec52fd918e4457f2f8db98acc054405.jpeg 2x" data-dominant-color="B2B3B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1045×591 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2024-02-07 23:51 UTC)

<p>For the upper airway, I would recommend that you familiarize yourself with the tools in the Segment Editor module. You should be able to get to what you want with a simple sequence of steps.  For example, Threshold to find all air (something like &lt;-250 HU should work), then Islands → Keep selected island and click in trachea.  If the upper airway remains connected to the external air (which is likely), break the connections using the Scissors tool or via Paint or Erase, then keep selected island again.</p>

---

## Post #3 by @D_Dand (2024-02-12 22:57 UTC)

<p>Thank you very much! I am curious if you ever try to export file from Slicer and then import to and CAD software. So far, I see Slicer is just able to convert file into meshing file (STL etc.) but CAD. I would like to edit the file a little bit in Solidworks.</p>

---

## Post #4 by @mikebind (2024-02-13 00:26 UTC)

<p>I don’t use any CAD software, and I believe it is quite challenging to go from arbitrary meshes back to mathematical primitives used in CAD.  If you search this forum for “CAD”, there are many hits and you may be able to find more information there.</p>

---

## Post #5 by @D_Dand (2024-02-13 16:41 UTC)

<p>Hi Mike,</p>
<p>So have you ever edited the 3d model generated from Slicer 3D? how can you do that? For instance, I want to remove certain areas, but the scissors will remove the entire part vertically, so if I remove something on top of other things, it will remove both top and bottom things.</p>

---

## Post #6 by @mikebind (2024-02-14 23:09 UTC)

<p>Yes, I frequently edit segmentations using a variety of Segment Editor tools.  Then if I need a surface model I export it from the edited segment.<br>
Specifically with the scissors tool, you have a lot of flexibility in how it works:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c5906c5643e65b0c779a5aa61cff11f26c0934.png" alt="image" data-base62-sha1="7nZD4DxCDrrAO5ieyqor8yBjkos" width="569" height="318"></p>
<p>For example, you could limit the range around the edited slice by selecting the “Symmetric” option and entering the range in which you want edits to occur.   If that doesn’t offer fine enough control, you can use the “Erase” tool to work down to the level of single voxels (or circular or spherical regions of customized size).  Familiarizing yourself with all the segment editor tools will generally help you find the most efficient ways to get to your final desired segmentation.</p>

---

## Post #7 by @D_Dand (2024-05-23 18:17 UTC)

<p>Hi Mike,</p>
<p>I am back. After trying, I still find hard to segment the upper airways. Have you ever done upper airway? Could you please share your workflow?</p>
<p>Thank you very much!</p>

---

## Post #8 by @mikebind (2024-05-23 18:37 UTC)

<p>Yes, I’ve mostly done upper airway segmentations.  As for any segmentation task, the best way to approach it depends on exactly what you want to get out of the final segmentation.  However, my usual approach would be as I outlined above:</p>
<ul>
<li>Threshold to create a segment of all the air in the scan (say &lt; -250 HU)</li>
<li>Use Islands tool to keep selected island, clicking somewhere in the upper airway airspace (this will typically eliminate enclosed air spaces in the skull from the segmentation, but not the external air, which is usually connected via at least the nostrils and often the mouth as well)</li>
<li>If the space near the nostrils and mouth opening are not important regions to include in the segmentation, then I use the Erase tool with a spherical brush of large size to erase the region including the mouth opening and nostril openings.  Then, I use keep selected island again to keep only the island with the airway.  If the external air remains at this step, then it must have residual connection somewhere; locate that area and erase it.</li>
<li>If the space near the nostrils and mouth opening are important to include in the segmentation, then you need to be more careful in the erasing step.  I might pick a coronal plane at the mouth opening and erase there, using a non-spherical (planar) brush, and similarly for an axial plane at the nasal opening.</li>
<li>If that’s not good enough, then you would just need to be carefully drawing the boundaries there anyway, so you might as well be painting that area from scratch. If you were to take that approach, you could paint in the boundary region you want as a separate segment, and then subtract it from the air segment (using Logical operators), keep the island you want, and add back in the boundary region (again using Logical operators).</li>
</ul>
<p>You can also edit regions using the Scissors tool, as mentioned above.  I mostly use Scissors looking at the 3D view, and angle the view so that I can lasso the region I want to remove without stuff I don’t want to remove in front or behind it.</p>

---

## Post #9 by @D_Dand (2024-05-23 18:53 UTC)

<p>Hi Mike,<br>
Thank you very much. I am working on it. Ultimately, I would like to reconstruct a 3D model of human airway (upper and lower one) and simulate in CFD model for airflow simulation. For lower airway, I do not have much trouble but upper one.</p>
<p>Following your suggestion:<br>
Step 1: I used Segment editor module, I select threshold, range: -1024 to -250. Then click apply, but there is nothing happen. Did I do something wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf7d2fc452e336a63de8800f41bf89e2a0705fa2.png" data-download-href="/uploads/short-url/tBx2Wg2aPF75X1FHX8xWSzBdXMe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf7d2fc452e336a63de8800f41bf89e2a0705fa2_2_690x322.png" alt="image" data-base62-sha1="tBx2Wg2aPF75X1FHX8xWSzBdXMe" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf7d2fc452e336a63de8800f41bf89e2a0705fa2_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf7d2fc452e336a63de8800f41bf89e2a0705fa2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf7d2fc452e336a63de8800f41bf89e2a0705fa2.png 2x" data-dominant-color="ADACAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×467 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e5b656aa8cf14fdc74b626e9f2783b8220e3840.png" data-download-href="/uploads/short-url/4ky8Ea6z2MOFwn9OVpusN5uB7UY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e5b656aa8cf14fdc74b626e9f2783b8220e3840_2_690x318.png" alt="image" data-base62-sha1="4ky8Ea6z2MOFwn9OVpusN5uB7UY" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e5b656aa8cf14fdc74b626e9f2783b8220e3840_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e5b656aa8cf14fdc74b626e9f2783b8220e3840.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e5b656aa8cf14fdc74b626e9f2783b8220e3840.png 2x" data-dominant-color="A8A7A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×462 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @mikebind (2024-05-23 19:26 UTC)

<p>That should work…  When you click Apply, the areas which are flashing green should become the segment.  Perhaps you have something odd in your masking settings?  Scroll down below the apply button and make sure it looks something like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33a3814e0bdae71a7e76d86f90e83a70babc8a10.png" alt="image" data-base62-sha1="7mOERnzAim3s49k7QK0dPr0RJWo" width="479" height="203"></p>
<p>If you had an editable intensity range which didn’t overlap the threshold range or if the editable area was “Inside all segments”, for example, then the newly created segment would be empty (because there would be no overlap between the threshold region and the editable mask).</p>

---

## Post #11 by @D_Dand (2024-05-23 19:35 UTC)

<p>Hi Mike,</p>
<p>I think it is just a glitch. Now it works fine. One more thing, I see scissors can trim unnecessary parts. How about when we want to add more part, for instance: attached pics.As you see there is a black space in lower airway, it should be selected. Now, I used level tracer, and thought it would help. But then, it is just for one slice but cannot convert it into 3D.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe4a214139cd62059ea312a86f7a56dd20d6329.png" data-download-href="/uploads/short-url/kwW7AMypy2GZ9LObIjzNRrgAUNH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe4a214139cd62059ea312a86f7a56dd20d6329_2_690x318.png" alt="image" data-base62-sha1="kwW7AMypy2GZ9LObIjzNRrgAUNH" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe4a214139cd62059ea312a86f7a56dd20d6329_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe4a214139cd62059ea312a86f7a56dd20d6329.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe4a214139cd62059ea312a86f7a56dd20d6329.png 2x" data-dominant-color="959492"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×461 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e605b2fa3b36ea87b8b0a4605d32ce514c811a4b.png" data-download-href="/uploads/short-url/wOS1LGA6LqJBpz9HFfMHvk61iJ5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e605b2fa3b36ea87b8b0a4605d32ce514c811a4b_2_690x317.png" alt="image" data-base62-sha1="wOS1LGA6LqJBpz9HFfMHvk61iJ5" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e605b2fa3b36ea87b8b0a4605d32ce514c811a4b_2_690x317.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e605b2fa3b36ea87b8b0a4605d32ce514c811a4b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e605b2fa3b36ea87b8b0a4605d32ce514c811a4b.png 2x" data-dominant-color="959492"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×460 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be0ef9e598d16705ca78766491e6a68d5400f47.jpeg" data-download-href="/uploads/short-url/aPfJtqDz77yLfC4aSf6b34JbG9V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be0ef9e598d16705ca78766491e6a68d5400f47_2_690x370.jpeg" alt="image" data-base62-sha1="aPfJtqDz77yLfC4aSf6b34JbG9V" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be0ef9e598d16705ca78766491e6a68d5400f47_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be0ef9e598d16705ca78766491e6a68d5400f47_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be0ef9e598d16705ca78766491e6a68d5400f47.jpeg 2x" data-dominant-color="45454B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1109×596 90.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @mikebind (2024-05-23 19:51 UTC)

<p>There are again lots of possible ways.  Easiest in this case might be to paint with a spherical brush and intensity masking settings.  To extend the existing segment, I would select it, choose the Paint tool, select Sphere brush, and adjust the diameter until it is slightly larger than the diameter of the airway region you are trying to fill in.  Then, in the “Masking” settings, I would check the “Editable intensity range” checkbox and make -1024 to -250 editable. (This will prevent the  non-air tissue from being included even if you paint over it). Then I would center the slice views on the region you want to fill in, and paint it in on whatever view the best aligns with the center of the tube.  If your paintbrush is too big and includes some adjacent lung or external air, you can remove that with scissors or with keep selected island as before. If your paintbrush is too small and misses some of the desired airway, either increase the size of the paintbrush or do another pass filling in the missed areas with a smaller brush size</p>

---

## Post #13 by @D_Dand (2024-05-28 13:58 UTC)

<p>Hi Mike,</p>
<p>Thank you for your advice. I got this. Your method works very well with upper airway. But I tried it with lower airway, and always leaks somewhere (I guess from Bronchiole). Do you have any comments on this?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73eac6ed6de5fbc53058b81b804758385b55091f.png" alt="image" data-base62-sha1="gxrUPxt34DLlFmb0zxDPmLeQkXB" width="317" height="420"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbaa799ea936bf92436395ea36ce6e75e8bc1501.jpeg" data-download-href="/uploads/short-url/vlfO2RBsBRgMqbzR3qum7N9g893.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbaa799ea936bf92436395ea36ce6e75e8bc1501_2_414x500.jpeg" alt="image" data-base62-sha1="vlfO2RBsBRgMqbzR3qum7N9g893" width="414" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbaa799ea936bf92436395ea36ce6e75e8bc1501_2_414x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbaa799ea936bf92436395ea36ce6e75e8bc1501_2_621x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbaa799ea936bf92436395ea36ce6e75e8bc1501_2_828x1000.jpeg 2x" data-dominant-color="969ACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">877×1057 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @mikebind (2024-05-28 16:47 UTC)

<p>What do you want it to look like?  For me, the easiest approach from your final picture would usually be to carefully use the scissors tool in the 3D view and just cut away until all that remained was what I wanted.  Depending on how much of the bronchial structure you want, that may be very challenging or fairly easy to accomplish.</p>

---

## Post #15 by @2023pth0110 (2024-11-26 17:54 UTC)

<p><a class="mention" href="/u/d_dand">@D_Dand</a> Hi, I am also working on the project “Drug Transport in Respiratory System” for which I need 3D model from oral cavity to bronchiis , Lower portion below the trachea I have made using Lung segmentation tool but the upper portion I am not able to make it.Please help me or If possible kindly share the stl file you made or else please guide how to obtain the geometry</p>

---
