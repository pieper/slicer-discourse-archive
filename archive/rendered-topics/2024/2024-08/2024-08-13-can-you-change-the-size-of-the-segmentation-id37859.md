# Can you change the size of the segmentation?

**Topic ID**: 37859
**Date**: 2024-08-13
**URL**: https://discourse.slicer.org/t/can-you-change-the-size-of-the-segmentation/37859

---

## Post #1 by @Daniel_Murcia (2024-08-13 14:46 UTC)

<p>Hello community, a question, I made a segmentation of some structures in millimeters (mm) but I realized that my image had a scale in microns (um), I then made the change from millimeters to microns in the configurations so that I could get the measurements and other data in Microns, but when I made that adjustment the segmentations that I had made disappeared from my image, I suppose it was due to the change of measurements, what I want to know is if I can do something so that I can see my segmentations again in the image so as not to start over again since there are many segmentations that I perform.</p>
<p>Greetings and thanks in advance.</p>

---

## Post #2 by @muratmaga (2024-08-14 04:10 UTC)

<p>Bring back the units to defaults (mm), and follow the instructions in this thread.</p>
<aside class="quote quote-modified" data-post="1" data-topic="28140">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/adapt-voxel-spacing-of-segments-after-changing-voxel-dimension-of-master-volume/28140">Adapt voxel spacing of segments after changing voxel dimension of master volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Win10 
Slicer version: 5.2.1 r31317 / 77da381 
Hi, 
I am encountering the following problem: 

segments were obtained by using the segment editor
the voxel spacing of the master volume was: 1 x 1 x 1 mm³ (the default value)
now I would need to change the voxel spacing of the master volume and also the voxel spacing of the 
already obtained segments

Unfortunately I couldn´t find a smooth solution for this task; once the voxel dimensions of the master volume are changed, the cha…
  </blockquote>
</aside>

<p>You should of course correct the spacing in the master volume same way as well.</p>

---
