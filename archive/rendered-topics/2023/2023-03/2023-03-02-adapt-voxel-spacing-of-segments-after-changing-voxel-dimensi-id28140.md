# Adapt voxel spacing of segments after changing voxel dimension of master volume

**Topic ID**: 28140
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/adapt-voxel-spacing-of-segments-after-changing-voxel-dimension-of-master-volume/28140

---

## Post #1 by @MrMarkus (2023-03-02 09:21 UTC)

<p>Operating system: Win10<br>
Slicer version: 5.2.1 r31317 / 77da381</p>
<p>Hi,</p>
<p>I am encountering the following problem:</p>
<ul>
<li>segments were obtained by using the segment editor</li>
<li>the voxel spacing of the master volume was: 1 x 1 x 1 mm³ (the default value)</li>
<li>now I would need to change the voxel spacing of the master volume and also the voxel spacing of the<br>
already obtained segments</li>
</ul>
<p>Unfortunately I couldn´t find a smooth solution for this task; once the voxel dimensions of the master volume are changed, the change of the “link”: source geometry - segmentation (in segment editor) causes the dimension of the segmentation to increase.</p>
<p>Intuitively I expected that a change of the master volume from 1 x 1 x 1 → 0.25 x 0.25 x 0.25 mm³ and subsequent changing the segmentation from 1 x 1 x 1 → 0.25 x 0.25 x 0.25 mm³ would cause no change in dimension of the segmentation; instead the voxel number of the segmentation is increased by 4 (1 → 0.25) in each dimension.</p>
<p>What is the right way to change / adapt the voxel spacing of the segments and the corresponding master volume?</p>
<p>Thanks.</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2023-03-02 16:30 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="28140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>What is the right way to change / adapt the voxel spacing of the segments and the corresponding master volume?</p>
</blockquote>
</aside>
<p>The right way is to set/check the spacing of the master volume prior to segmentation avoid exactly this situation. Data spacing should be correctly set for everything downstream to work correctly.</p>
<p>You can fix it manually by:</p>
<ol>
<li>Right click on your existing segmentation and export it as a labelmap,</li>
<li>Use the Volumes module to edit it in the way you did with master volume,</li>
<li>right click the labelmap after changing the image header properties and export it again segmentation.</li>
</ol>

---
