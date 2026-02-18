# Segment skin surface

**Topic ID**: 697
**Date**: 2017-07-16
**URL**: https://discourse.slicer.org/t/segment-skin-surface/697

---

## Post #1 by @togen (2017-07-16 12:09 UTC)

<p>Dear community,<br>
since I just recently got to know the software 3D Slicer, I might need your help. I turned dicom ct scans into stl format and have a specific problem I couldn’t deal with so far: Is there a possibility to “remove all volume” out of the stl scans? I only need the surface/skin of the scan. The result I am looking for should basically be the most outward layer of the scan, like the cover of the whole scanned object. I already read a lot of instructions and watched tutorials but I haven’t found a solution yet <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=5" title=":confused:" class="emoji" alt=":confused:"><br>
Is there anyone who can help me with that? Thank you very much in advance for any kind of help!</p>
<p>Kind regards,<br>
Tony</p>

---

## Post #2 by @lassoan (2017-07-16 15:47 UTC)

<p>These kind of operations are all available, but it is not clear what you would like to achieve.</p>
<aside class="quote no-group" data-username="togen" data-post="1" data-topic="697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ac91a4/48.png" class="avatar"> togen:</div>
<blockquote>
<p>Is there a possibility to “remove all volume” out of the stl scans?</p>
</blockquote>
</aside>
<p>Do you mean masking the volume: blank out all areas of the volume that are outside all segments?</p>
<aside class="quote no-group" data-username="togen" data-post="1" data-topic="697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ac91a4/48.png" class="avatar"> togen:</div>
<blockquote>
<p>I only need the surface/skin of the scan.</p>
</blockquote>
</aside>
<p>Do you need a surface or a volume?</p>

---

## Post #3 by @togen (2017-07-16 16:03 UTC)

<p>Thanks for your fast reply!</p>
<p>I just need the surface of a skull, the most outward layer of the scan, no volume at all. The final result should look like the image of a 3D-photography.<br>
Thank you very much for your help!</p>

---

## Post #4 by @lassoan (2017-07-16 16:18 UTC)

<p>To segment skin surface:</p>
<ul>
<li>Open Segment Editor module</li>
<li>Extract skin surface using Threshold effect (choose appropriate threshold value and click Apply)</li>
<li>Remove speckles and other disconnected regions using Islands effect, “Keep largest island” option</li>
<li>Click “Create surface” to visualize the surface in 3D</li>
<li>If there are larger parts of the segment that are not needed, remove them using Scissors effect, either in 2D or 3D</li>
<li>Smooth the surface by Smoothing effect, Median option</li>
</ul>
<p>If airways in the head are not filled then you can fill them by using island effect and brush tool or use the following sequence instead of simple thresholding:</p>
<ul>
<li>Install SegmentEditorExtraEffects extension, restart Slicer</li>
<li>Open Segment editor module</li>
<li>Choose Flood filling effect, set neighborhood size to 5.0</li>
<li>Click outside the body =&gt; it should segment all areas outside the body without leaking into the airways</li>
<li>Invert the segment using Logical operators effect, Invert operation</li>
</ul>

---

## Post #5 by @togen (2017-07-17 19:32 UTC)

<p>Thank you for your detailed reply!<br>
I followed the steps but the result isn’t as good as I hoped…</p>
<p>I think the main problem is, that it’s impossible to extract the skin by using the treshold effect since the airways, dura and also vessels got the same density in tissue that underwent formalin fixation.<br>
I tried to remove the regions I am not interested in by using the eraser and the islands effect over and over, but this method takes a lot of time for removing every single voxel in critical areas f.ex. the area between the lips and the tongue.<br>
So I am still wondering wether there’s an option for receiving a stl file only containing the most outward voxels of my skull without manually processing. Since I want to measure the distances of the skulls surface in 2 different ct scans that I turned into stl files (before and after an operation of the skull), I am looking for an option that excludes me as a potential error by not removing exactly the same voxels in the before and after operation scans. I hope you understand what I mean :S</p>
<p>Thank you for any kind of help in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/722edb274fe47907b275cf1aeca0f8bf92926ca9.jpg" data-download-href="/uploads/short-url/gi6ORdjlBoYaGGBpkdm61Q1L49j.jpg?dl=1" title="Bildschirmfoto 2017-07-17 um 21.23.08.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/722edb274fe47907b275cf1aeca0f8bf92926ca9_2_517x500.jpg" width="517" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/722edb274fe47907b275cf1aeca0f8bf92926ca9_2_517x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/722edb274fe47907b275cf1aeca0f8bf92926ca9_2_775x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/722edb274fe47907b275cf1aeca0f8bf92926ca9_2_1034x1000.jpg 2x" data-dominant-color="433DB4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2017-07-17 um 21.23.08.jpg</span><span class="informations">1218×1177 359 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2017-07-18 04:22 UTC)

<aside class="quote no-group" data-username="togen" data-post="5" data-topic="697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ac91a4/48.png" class="avatar"> togen:</div>
<blockquote>
<p>impossible to extract the skin by using the treshold effect since the airways, dura and also vessels got the same density in tissue that underwent formalin fixation</p>
</blockquote>
</aside>
<p>As long as there is a layer of material that has different density than air, Flood filling effect clicked on outside air should work. It will not leak into airways as long as neighborhood size is large enough.</p>
<p>Also, it is always an option to use ‘Grow from seeds’ or ‘Watershed’ effect. Create a segment and paint a couple of strokes inside the head, in multiple slices. Create another segment and paint outside in the air, in multiple slices. Then switch to ‘Grow from seeds’ or ‘Watershed’ effect and click initialize. Add more strokes where the segmentation results shown are not correct.</p>
<p>There are many segmentation tools. You have to spend some time with all of them to see what they can do (with slightly varying input parameters) and see which work the best for you.</p>
<p>If you can find similar data sets among sample data sets (in Slicer sample data or in TCIA database) or share anonymized data then I can try a couple of methods and let you know which of them seem the most promising.</p>

---

## Post #7 by @togen (2017-07-22 09:50 UTC)

<p>I followed all your advices but haven’t received a convincing result yet.<br>
Since you offered to help me in case I get stuck again, herewith I would like to ask for support.</p>
<p>As I already said, I want to turn a dicom CT scan of a skull (fixation with formalin) into a stl file containing only the most outward, single layer of voxels of my skull, so the final result should look like an ultra-thin, hollow head with no structes, like airways or brain inside.</p>
<p>I tried the flood filling effect but my notebook didn’t manage to deal with settings like neighborhoodsize 7.0 or bigger which were needed to prevent leaking of airways.<br>
So I tried again to manually erase the parts inside the skull after using treshold effect, but then, even though I had a quite good result, I couldn’t turn the edited scan into a stl file since it wasn’t possible to create a label map of or rather using the model maker effect (I hope it was the right way for getting my file ready to be saved as stl?).<br>
In case you could show me, how to receive such a stl file, I would be extremly glad and thankful.</p>
<p>Thank you very much for any kind of help in advance.</p>

---

## Post #8 by @lassoan (2017-07-22 12:22 UTC)

<aside class="quote no-group" data-username="togen" data-post="7" data-topic="697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ac91a4/48.png" class="avatar"> togen:</div>
<blockquote>
<p>my notebook didn’t manage to deal with settings like neighborhoodsize 7.0 or bigger</p>
</blockquote>
</aside>
<p>Use the Crop volume module to decrease the file size so that tour notebook can handle it. Decrease the size of region of interest and/or increase spacing. With a spacing factor of 2x, memory need is decreased by 8x.</p>

---

## Post #9 by @Chuan (2023-10-09 17:34 UTC)

<p>Hi Tony,</p>
<p>Recently, I had a similar task with yours (6 years ago). I wonder which method did you finally select to extract the body skin?</p>
<p>Best,<br>
Chuan</p>

---

## Post #10 by @lassoan (2023-10-10 10:56 UTC)

<p>See a segmentation recipe for a fully automatable skin surface extraction method: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>

---

## Post #11 by @Chuan (2023-10-11 12:41 UTC)

<p>Hi Lassoan,</p>
<p>Thanks for your sharing, but there is one problem: what I get is not an outer surface but a volume filled inside.<br>
Do you know how to get the only outer surface?</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #12 by @lassoan (2023-10-11 12:49 UTC)

<aside class="quote no-group" data-username="Chuan" data-post="11" data-topic="697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>but there is one problem: what I get is not an outer surface but a volume filled inside.</p>
</blockquote>
</aside>
<p>The filling is just visualization, to make it easier to see what is inside and outside of each segment. You can turn off the filling in “Display” options in Segmentations module.</p>
<aside class="quote no-group" data-username="Chuan" data-post="11" data-topic="697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>Do you know how to get the only outer surface?</p>
</blockquote>
</aside>
<p>If you mean how to write the segmentation to a surface mesh file, you can follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file">these instructions</a>.</p>

---

## Post #13 by @Chuan (2023-10-12 08:09 UTC)

<p>Hi Lassoan,</p>
<p>Thank you very much for your help. Even though the wrap solidity is not perfectly ideal (it will not only automatically fill the body inside, but also fill the gap between legs and arms/ fingers, as shown below),  now I know how to extract the outer surface!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f700736030f43228435252513416c4ceea6e894.jpeg" data-download-href="/uploads/short-url/6LEsxBdKl3rjDSaxONgUrCM2yl6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f700736030f43228435252513416c4ceea6e894_2_396x500.jpeg" alt="image" data-base62-sha1="6LEsxBdKl3rjDSaxONgUrCM2yl6" width="396" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f700736030f43228435252513416c4ceea6e894_2_396x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f700736030f43228435252513416c4ceea6e894_2_594x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f700736030f43228435252513416c4ceea6e894.jpeg 2x" data-dominant-color="998AAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">649×818 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,<br>
Chuan</p>

---

## Post #14 by @lassoan (2023-10-12 11:09 UTC)

<p>You can remove tendinitis thin membranes by additional processing. For example, use Margin effect to shrink until the membrane disappears and then dilate the same amount to get back to the original size.</p>

---
