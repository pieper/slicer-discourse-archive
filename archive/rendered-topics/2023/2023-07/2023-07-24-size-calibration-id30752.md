# Size calibration?

**Topic ID**: 30752
**Date**: 2023-07-24
**URL**: https://discourse.slicer.org/t/size-calibration/30752

---

## Post #1 by @telomere (2023-07-24 08:34 UTC)

<p>Hi.<br>
I made some models in blender and imported in 3d slicer.</p>
<p>But the size of the models was a bit smaller than that in blender.</p>
<p>I made a cylinder model in blender with the height of 8mm but it was about 6mm in slicer.</p>
<p>Actually it was denominated as 8m in blender(using Metric unit system) but when I export it as a STL and print it with 3d printer, it became 8mm exactly. But I don’t know why it is not correct in 3d slicer.</p>
<p>Any way to calibrate with slicer?</p>
<p>PS. please answer my previous question if anyone knows.</p><aside class="quote quote-modified" data-post="1" data-topic="30740">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/what-should-i-do-to-activate-the-list/30740">What should I do to activate the list?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 


I want to move one model to the location of the other model using model registration in SlicerIGT module. 
But there’s no list in ‘Input fixed(dense) model’ and ‘input moving(sparse) model’. 
What should I do to make the models selectable? 
It says ‘This model may require to contain a dense/sparse set of points’, but I don’t get what this mean. 


More basic question… 
In segment editor module, I want to import other models so turning into segmentations modules, I tried to import models i…
  </blockquote>
</aside>

<p>Thanks…</p>

---

## Post #2 by @lassoan (2023-07-25 12:01 UTC)

<p>The cylinder is 8mm in Slicer, too, as Slicer uses the length unit (specified in application settings) as unit for STL file import, which is millimeter by default.</p>
<p>Have your loaded the STL file as Model or Segmentation? How did your measure the cylinder size? Can you attach a screenshot?</p>

---

## Post #3 by @telomere (2023-07-25 13:17 UTC)

<p>Thanks for the answer.<br>
It has been solved after I checked scene unit in blender(green marked at screenshot below).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb01784caab12fada3c35027d8db500d762bb0c4.png" alt="slicercommu1" data-base62-sha1="zOuZEmyE0R2LSvz23EvCcTCxB2Y" width="241" height="314"></p>
<p>I measured the cylinder size just by the ruler.<br>
To measure more precisely I wanted to see the dimension of boundary of the model but it was not possible. Do you know how to know the dimension(xmm x ymm x zmm) of the boundary?(boundary means the white box at the below screenshot).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9daf6e9832ec9c0a2d2ce9dbaa11b453c6e9620.png" alt="slicercommu2" data-base62-sha1="v5eJTY2UKjdroi8kTkbNNTcVDI4" width="199" height="208"></p>

---

## Post #4 by @lassoan (2023-07-31 17:23 UTC)

<p>You can type <code>getNode('YourModelNodeName').GetBounds()</code> into the Python console to get the bounds of the model (in scene length unit, which is millimeter by default).</p>

---
