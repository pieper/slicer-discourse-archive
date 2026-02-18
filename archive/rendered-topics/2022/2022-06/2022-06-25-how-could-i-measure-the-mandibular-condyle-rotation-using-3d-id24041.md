# How could I measure the mandibular condyle rotation using 3D Slicer?

**Topic ID**: 24041
**Date**: 2022-06-25
**URL**: https://discourse.slicer.org/t/how-could-i-measure-the-mandibular-condyle-rotation-using-3d-slicer/24041

---

## Post #1 by @Moh_d_Al-Watary (2022-06-25 08:09 UTC)

<p>Hi dears in 3D SLICER community, wish you are doing well</p>
<p>I am running a project in which I am measuring:</p>
<ul>
<li>Mandibular condyle displacement using the following:
<ul>
<li>After doing registration and segmentation of condyles from different times CT scan (T0, T1, and T2)</li>
</ul>
</li>
</ul>
<p>Q. 1: When I saved registered T1 and T2 to continue working later, when I open them on the 3D Slicer they appear in a different direction (flipped left to right or upside down) so I have to start working again from zero, <strong>why this problem happened? How it be solved? How it be prevented?</strong></p>
<p>I used Pick’n paint, Model to Model distance, and Mesh statistics to export the values.</p>
<p>Sometimes in this step: The model-to-model distance is terminated with error!</p>
<ul>
<li>I want to measure the rotational changes of the condyle (Yaw, Pitch, and Roll) so how could I do this in the 4.11.2 3D Slicer version? How could I use the Q3DC module to achieve this?</li>
<li>Condyle remodeling (which is revealed by comparing T2 to both T1 and T0):
<ul>
<li>How also this step could be done?</li>
</ul>
</li>
</ul>
<p>Thank you so much for your highly appreciated help and support.</p>

---

## Post #2 by @pieper (2022-06-25 16:24 UTC)

<aside class="quote no-group" data-username="Moh_d_Al-Watary" data-post="1" data-topic="24041">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moh_d_al-watary/48/14124_2.png" class="avatar"> Moh_d_Al-Watary:</div>
<blockquote>
<p>appear in a different direction (flipped left to right or upside down)</p>
</blockquote>
</aside>
<p>Probably you have an issue with the coordinate system conventions.  You can read up on RAS and LPS in the forum: <a href="https://discourse.slicer.org/search?q=lps%20ras" class="inline-onebox">Search results for 'lps ras' - 3D Slicer Community</a></p>
<p>You can change options when loading if needed:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd4f47b3d321df30bd81e26aa468699d984b3fba.png" alt="image" data-base62-sha1="r0I67tzDNoVA30v311SptRDzPuO" width="310" height="114"></p>
<p>The SlicerCMF team might be able to comment on your other questions.</p>

---

## Post #3 by @lassoan (2022-06-25 16:46 UTC)

<aside class="quote no-group" data-username="Moh_d_Al-Watary" data-post="1" data-topic="24041">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moh_d_al-watary/48/14124_2.png" class="avatar"> Moh_d_Al-Watary:</div>
<blockquote>
<p>When I saved registered T1 and T2 to continue working later, when I open them on the 3D Slicer they appear in a different direction (flipped left to right or upside down) so I have to start working again from zero</p>
</blockquote>
</aside>
<p>When you apply a transform to an image or model, the original data is not modified you just change where it is located (and may be how it is warped) in the scene. If you want to permanently, irreversibly change the location then you need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform</a> and then save the modified node into a file.</p>
<p>In recent Slicer versions, you can export a transformed node into file by right-click on the node in Data module, choose <code>Export to file...</code> and check the <code>Apply transforms</code> option.</p>

---
