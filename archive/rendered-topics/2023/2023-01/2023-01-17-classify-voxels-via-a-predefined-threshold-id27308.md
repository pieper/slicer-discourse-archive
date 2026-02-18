# Classify voxels via a predefined threshold

**Topic ID**: 27308
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/classify-voxels-via-a-predefined-threshold/27308

---

## Post #1 by @AmandineG (2023-01-17 16:54 UTC)

<p>Hi,</p>
<p>I am a user of 3Dslicer Mac version 5.2.1, with MarkUpsToModel, Sandbox and SegmentEditorExtraEffects extensions.<br>
I used the threshold tool on a paralumbar muscle after obtaining its volume and extraction but it did not succeed.</p>
<p>My goal is to obtain a muscle volume or a muscle area in binary color: black for the pure muscle and white for the fat in the muscle, via a predefined cutoff, like this exemple:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c67f7f94c35148ef80c4c814b6cb8419ffced30.png" alt="Capture d’écran 2022-12-14 à 10.37.03" data-base62-sha1="hKxXp4Fk5mHTYEgaAh8QMC8goDu" width="504" height="177"></p>
<p>This is what I get when using threshold, and it doesn’t work:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2b48f3d48be2bb0712044fe9dc15f66851ccc9f.png" data-download-href="/uploads/short-url/rMrtwNkOGVw1LoZJuGMp66U8ckn.png?dl=1" title="Capture d’écran 2023-01-16 à 17.35.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b48f3d48be2bb0712044fe9dc15f66851ccc9f_2_517x323.png" alt="Capture d’écran 2023-01-16 à 17.35.10" data-base62-sha1="rMrtwNkOGVw1LoZJuGMp66U8ckn" width="517" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b48f3d48be2bb0712044fe9dc15f66851ccc9f_2_517x323.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b48f3d48be2bb0712044fe9dc15f66851ccc9f_2_775x484.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b48f3d48be2bb0712044fe9dc15f66851ccc9f_2_1034x646.png 2x" data-dominant-color="ACABA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-01-16 à 17.35.10</span><span class="informations">1440×900 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>No post seems to explain this subject precisely: on 3Dslicer, is it possible to carry out a binary classification of pixels or voxels via a predefined threshold in a gray scale?</p>
<p>Thanks</p>

---

## Post #2 by @Sunderlandkyl (2023-01-17 20:18 UTC)

<p>What have you tried so far? From your picture it seems that you are using the threshold visualization options in the Volume module.</p>
<p>Have you tried using the Segment Editor module? The Threshold editor effect may provide what you need. You can find documentation on the module here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a></p>

---

## Post #4 by @AmandineG (2023-01-18 15:23 UTC)

<p>Thank you for your help.<br>
Indeed, I tried different threshold tools (SegmentEditor → Local threshold // Volume → threshold // Filtering → threshold scalar volume), but not this one.</p>
<p>Once the threshold is done and saved, how to get a percentage of black voxel and white voxel in a table? Currently, I get this table in Quantification → SegmentStatistics but it doesn’t separate the 2 colors I want to get.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef31e472b713a062f2379e0231cc63ab0071933.png" data-download-href="/uploads/short-url/rfdB4gu7R3HC5sfTAPTVqsiyL7R.png?dl=1" title="Capture d’écran 2023-01-18 à 16.19.35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef31e472b713a062f2379e0231cc63ab0071933_2_516x225.png" alt="Capture d’écran 2023-01-18 à 16.19.35" data-base62-sha1="rfdB4gu7R3HC5sfTAPTVqsiyL7R" width="516" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef31e472b713a062f2379e0231cc63ab0071933_2_516x225.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef31e472b713a062f2379e0231cc63ab0071933_2_774x337.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef31e472b713a062f2379e0231cc63ab0071933_2_1032x450.png 2x" data-dominant-color="DFDFE0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-01-18 à 16.19.35</span><span class="informations">1283×558 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #5 by @muratmaga (2023-01-18 18:05 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="4" data-topic="27308">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>Once the threshold is done and saved, how to get a percentage of black voxel and white voxel in a table? Currently, I get this table in Quantification → SegmentStatistics but it doesn’t separate the 2 colors I want to get.</p>
</blockquote>
</aside>
<p>After you threshold, there is no black voxel or white voxel. Only the voxels that assigned to that segment, the count  of which are given in the table under the Number of Voxels field.</p>
<p>If you use a different threshold and then create a new segment, you can simply divide these two numbers.</p>
<p>What are you trying to calculate?</p>

---

## Post #6 by @AmandineG (2023-01-19 08:38 UTC)

<p>Thank you for your answer.</p>
<p>I’m trying to classify the pixels/voxels in a total muscle on MRI in a binary way according to an intensity threshold/cutoff, for example:</p>
<ul>
<li>Black = pure muscle, and</li>
<li>White = muscle fat (like the first image in my first post).</li>
</ul>
<p>I would like to do this work on a volume and on a surface.<br>
The final goal would be to get the percentage of black and white pixels/voxels in the volume and the surface.</p>

---

## Post #7 by @muratmaga (2023-01-19 16:21 UTC)

<p>Within a fixed region, If you set one threshold to define muscle + fat and set it as a segment, then create a second segment and threshold specific to the muscle only, you can do what I said above, which is</p>
<p><code>(number of voxels in segment1 - number of voxels in segment2) / number of voxels in segment1 *100</code></p>
<p>which will give you the percentage of fat voxels in the defined area.</p>
<p>But you have to keep the area exactly the same in both segments.</p>

---

## Post #8 by @AmandineG (2023-02-01 10:31 UTC)

<p>Thank you so much for your reply!</p>
<p>I tried to apply your method but there is an error:<br>
If I explode it in voxels, my volume of interest is 621650 voxels.<br>
With the same thresholding at 75 :</p>
<ul>
<li>If I choose to take the fat (white) in my volume of interest, it makes 188201 voxels.</li>
<li>If I choose to take the pure muscle (black) in my volume of interest, it makes 431195 voxels.</li>
<li>If I sum the two, I should in theory find the voxels of my total volume, that is 621650 voxels. Now, 188201+431195=619396.<br>
 → Do you know where the lost voxels are?</li>
</ul>
<p>Moreover, in the table created with the Segment statistics tool, they describe volume (1) (columns B C D), volume (2) (columns E F G), volume (3) (columns N O) cf image. What do the (1) (2) (3) correspond to?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2ad15fc4a9f2e22321c9e6930d7cddbe3632ebc.png" data-download-href="/uploads/short-url/rMbsLPHIHhyNzxUBZnLKdUrycDW.png?dl=1" title="Capture d’écran 2023-01-31 à 14.57.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ad15fc4a9f2e22321c9e6930d7cddbe3632ebc_2_517x303.png" alt="Capture d’écran 2023-01-31 à 14.57.45" data-base62-sha1="rMbsLPHIHhyNzxUBZnLKdUrycDW" width="517" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ad15fc4a9f2e22321c9e6930d7cddbe3632ebc_2_517x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ad15fc4a9f2e22321c9e6930d7cddbe3632ebc_2_775x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2ad15fc4a9f2e22321c9e6930d7cddbe3632ebc_2_1034x606.png 2x" data-dominant-color="8D8D90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-01-31 à 14.57.45</span><span class="informations">1437×844 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6bd8149a3fe44c98f88aec7ad1b876b915b730c.png" data-download-href="/uploads/short-url/uDGbRtl4g7LJIjC6pc6PJMos3eY.png?dl=1" title="Capture d’écran 2023-01-31 à 14.58.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6bd8149a3fe44c98f88aec7ad1b876b915b730c_2_517x300.png" alt="Capture d’écran 2023-01-31 à 14.58.09" data-base62-sha1="uDGbRtl4g7LJIjC6pc6PJMos3eY" width="517" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6bd8149a3fe44c98f88aec7ad1b876b915b730c_2_517x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6bd8149a3fe44c98f88aec7ad1b876b915b730c_2_775x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6bd8149a3fe44c98f88aec7ad1b876b915b730c_2_1034x600.png 2x" data-dominant-color="8C8C8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-01-31 à 14.58.09</span><span class="informations">1439×838 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #10 by @muratmaga (2023-02-01 18:30 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="8" data-topic="27308">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>I tried to apply your method but there is an error:<br>
If I explode it in voxels, my volume of interest is 621650 voxels.<br>
With the same thresholding at 75 :</p>
</blockquote>
</aside>
<p>Actually I found my mistake do it this way and you will get correct values</p>
<ol>
<li>Download MRhead sample data</li>
<li>create three empty segments</li>
<li>In the first segment using the paint brush in 3D mode create a spherical region (I used 10%) in the center of the brain</li>
<li>Copy this region to segment_2 and Segment_3 using Logical Operators</li>
<li>Hide segment_1</li>
<li>Switch to Segment_2, go to threshold tool and enter these threshold values 0 - 34.99 and then set the Masking fields to: Editable area to Inside Segment_2 and then modify other segments: Overwrite Visible (your segment_3 should be visible, that important). Then hit apply.</li>
<li>Turn the visibility on for segment_1, go to segment editor and calculate values.</li>
</ol>
<p>You will see that sum of voxel counts of segment_2 and segment_3 are now identical to the segment_1. This procedure split the original region into two none overlapping segmentations. You can adopt this procedure to your own dataset.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4f0af6d8d5697d5cacb8b7568fd5e4d266e4c16.jpeg" data-download-href="/uploads/short-url/s6dfv2ADjSxcuCaaKVuwh4hSAXs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4f0af6d8d5697d5cacb8b7568fd5e4d266e4c16_2_518x500.jpeg" alt="image" data-base62-sha1="s6dfv2ADjSxcuCaaKVuwh4hSAXs" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4f0af6d8d5697d5cacb8b7568fd5e4d266e4c16_2_518x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4f0af6d8d5697d5cacb8b7568fd5e4d266e4c16_2_777x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4f0af6d8d5697d5cacb8b7568fd5e4d266e4c16_2_1036x1000.jpeg 2x" data-dominant-color="9D9C9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1426×1375 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @AmandineG (2023-02-07 14:48 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="27308">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Logical Operators</p>
</blockquote>
</aside>
<p>Thank you for your reply!</p>
<p>I’m trying with MRhead sample data but it’s not very clear for me : what is “Logical Operators”?</p>
<p>Moreover, in your table, they describe volume (1) (columns B C D), volume (2) (columns E F G), volume (3) (columns N O). What do the (1) (2) (3) correspond to?</p>
<p>Thanks</p>

---

## Post #12 by @muratmaga (2023-02-07 15:53 UTC)

<p><a class="mention" href="/u/amandineg">@AmandineG</a> you can find answers to your questions here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#logical-operators" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#logical-operators</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>

---

## Post #13 by @AmandineG (2023-02-09 16:58 UTC)

<p>Thank you so much for your help and these links!</p>
<p>I was able to apply your threshold method on MRhead and then on my MRI. This technique is really easier, thank you.</p>
<p>Concerning the volumes and the “Segment Statistics” table, I understood that (1) (2) and (3) represent different volumes, but according to you, which volume represents better the reality (i.e. the real volume) between Labelmap statistics, scalar volume statistics or closed surface statistics?<br>
A topic has already been opened concerning this question but there is no answer ( <a href="https://discourse.slicer.org/t/differences-between-closed-surface-volume-labelmap-volume-and-scalar-volume/23556" class="inline-onebox">Differences between closed surface volume, labelmap volume and scalar volume</a> ).</p>
<p>Thanks</p>

---
