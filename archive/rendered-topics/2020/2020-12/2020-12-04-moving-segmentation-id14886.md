# Moving segmentation

**Topic ID**: 14886
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/moving-segmentation/14886

---

## Post #1 by @tenzin_kunkyab (2020-12-04 21:50 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 4.11.0</p>
<p>Hi all,</p>
<p>I am wondering if there is a functionality in 3d slicer where I can move the segmentation in terms of its location? I am basically creating cube segmentation of different cartridges in a phantom. I basically need the segmentations to be the same size. Cloning the segmentation simply puts the segmentation in the exact same location as the parent. However, I want to move the cloned segmentation so that I can create exact segmentation for other location as well.</p>
<p>Thank you for your support.</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @muratmaga (2020-12-05 06:35 UTC)

<p>After the cloning, you will have a separate node, and you can put it under transform and use translation sliders to move wherever you want.</p>
<p>If your cartridges are of simple shapes (cube, sphere, cylinder etc) you can create models of exact dimension for each of them (SlicerIGT extension, CreateModels), place them wherever you want and then import them as segmentation.</p>

---

## Post #3 by @lassoan (2020-12-05 06:55 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="14886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>you can put it under transform and use translation sliders to move wherever you want.</p>
</blockquote>
</aside>
<p>You can do all this in the Data module, by right-clicking on the transforms column:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feba6c3e0da102f820d94c2011a2212209dbd36e.gif" alt="interactive_transform" data-base62-sha1="AlqGz5ztjSq3qCpgTcr9Glej4vQ" width="690" height="401" class="animated"></p>
<p>Transform is rotated by left-click-and-drag, and translated by Shift+left-click-and-drag.</p>
<p>“Harden transform” in the end if for permanently applying the transformation to the selected node, which is probably not needed for what the use case described above.</p>

---

## Post #4 by @tenzin_kunkyab (2020-12-05 18:50 UTC)

<p>Thank you so much!</p>
<p>this helps a lot!</p>
<p>best<br>
Tenzin</p>

---

## Post #5 by @manjula (2020-12-05 22:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Transform is rotated by left-click-and-drag, and translated by Shift+left-click-and-drag.</p>
</blockquote>
</aside>
<p>Apart from rotate, translate and scale is there a way to enable “interaction handles” or move it in slice view (other than using the transform module).  Idea is to restrict the translations/rotations to one axis to have more control and precision?</p>

---

## Post #6 by @lassoan (2020-12-05 23:03 UTC)

<p>This is still the stock VTK box widget, which is very limited. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is working on adding a markups ROI widget and the next one will be the transform widget, probably in about 6 months. Until then, modules can use plane widgets to specify position and orientation interactively (keep copying the plane transform into a transform node).</p>

---

## Post #7 by @tenzin_kunkyab (2020-12-06 02:56 UTC)

<p>Hi Andras,</p>
<p>My slicer doesn’t have the interaction in 3D view selection, do you think its the version of the slicer that I am working in?</p>
<p>best<br>
Tenzin</p>

---

## Post #8 by @lassoan (2020-12-06 03:19 UTC)

<p>Yes, you need to use latest stable or preview version of Slicer.</p>

---

## Post #9 by @lassoan (2020-12-08 01:20 UTC)

<p>A post was split to a new topic: <a href="/t/draw-a-fixed-sized-segment/14930">Draw a fixed sized segment</a></p>

---

## Post #10 by @mdezube (2022-01-01 20:59 UTC)

<p>Just wanted to add that this was incredibly helpful, thank you.</p>

---

## Post #11 by @Loi (2024-08-01 09:56 UTC)

<p>Dear Iassoan and other contributors to this discussion,<br>
Thank you for the very helpful posts!</p>
<p>Can I ask for a clarification?<br>
When I used the method above, I could manually transpose and fit segmentation masks to my data.<br>
However, when I save the segmentation as Nifti and load it on different software (e.g. ITK snap), the segmentation remains as previously.<br>
Also, there is an indication of differences in dimensions etc.<br>
Could you please describe the way to save our results?</p>
<p>I assumed that when I “harden” the transform it is applied on the images. Then I created labels from the initial segmentation file and saved. I did this because trying to save the corrected segmentation from the data list on Slicer, did not give me the option to save as nifti.</p>
<p>I suppose I am doing something very basic, wrong. Apologies :).</p>
<p>Looking forward to your response!<br>
Thank you!</p>

---

## Post #12 by @lassoan (2024-08-02 10:30 UTC)

<p>I don’t think ITK-snap can overlay segmentation if it has different geometry (origin, spacing, axis directions, or extents) than the main image.</p>
<p>You can either use more capable software (such as Slicer) that does not have such limitation; or you can resample the segmentation to match the geometry of the main image. Slicer can do this resampling, see instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">here</a>, but since resampling is a lossy operation, do it sparingly.</p>
<p>Nifti is an unnecessarily complicated yet limited file format. I would recommend to keep images and segmentations in nrrd format instead.</p>

---

## Post #13 by @Loi (2024-08-02 10:47 UTC)

<p>Thank you for your immediate and helpful reply!<br>
I use Slicer and would prefer the suggested file format, however my second step is to use ML feature extraction on images. The pipelines and software i used require NiFTi files and when i tried resampling the images were not accepted. I will try the steps again, any other suggestions would be much appreciated.<br>
It’s worth noting that segmentations were created on T1/T2/Flair/T1gd as usually. I essentially need to apply the labels on acquired perfusion maps (part of the brain volume, one 3D sequence). If I could appropriately coregister these in the common space I guessed segmentations would work. Unfortunately they don’t, despite image dimensions being the same to other sequences after registration.<br>
Thanks again for your help!</p>

---

## Post #14 by @lassoan (2024-08-02 13:26 UTC)

<p>In Segmentations module’s Export section, you need to select the image that you want to mask as “Reference image”.</p>
<p>Nifti is a really bad format for general-purpose medical image computing, but for neuroimaging its usage is justifiable, as many neuroimaging software support it.</p>

---

## Post #15 by @Logan_Moore (2024-10-31 00:00 UTC)

<p>This was very useful for a new measurement my lab wants to track. Is there a way to make this operative across 1000 individual models? Essentially, I need my 3D model, not a segmentation, to be within the planes in Slicer.</p>
<p>Would there be a simple way to make the planes automatically center to the bounding box of my rib or move the rib to what looks like the origin? If not that’s fine, this is much quicker than doing a crude transform to get it to align.</p>

---

## Post #16 by @muratmaga (2024-10-31 03:14 UTC)

<aside class="quote no-group" data-username="Logan_Moore" data-post="15" data-topic="14886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/logan_moore/48/69222_2.png" class="avatar"> Logan_Moore:</div>
<blockquote>
<p>Essentially, I need my 3D model, not a segmentation, to be within the planes in Slicer.</p>
</blockquote>
</aside>
<p>I am not sure about the ask. if you are asking whether you can put models under transform in the same way as segmentation, yeah sure you can do it. Most object can be put under transform.</p>

---
