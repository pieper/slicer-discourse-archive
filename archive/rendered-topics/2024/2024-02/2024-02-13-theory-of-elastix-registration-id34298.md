---
topic_id: 34298
title: "Theory Of Elastix Registration"
date: 2024-02-13
url: https://discourse.slicer.org/t/34298
---

# Theory of elastix registration

**Topic ID**: 34298
**Date**: 2024-02-13
**URL**: https://discourse.slicer.org/t/theory-of-elastix-registration/34298

---

## Post #1 by @Alice_Durante (2024-02-13 15:54 UTC)

<p>Hi everyone<br>
I used the 3d slicer extension called “Registration- general registration-elastix”, and I managed to get a very good recording result, but I need some information for my thesis.</p>
<ol>
<li>Can you confirm me first of all whether this is a recording technique based on grey levels and not on geometry?</li>
<li>What kind of similarity measure does this extension use? Minimum squares differences, correlation coefficient etc…?</li>
<li>What kind of transformation model is used? Is it correct to say that B-Spline is used? If yes, can you tell me more about it?</li>
<li>On the information regarding the transformations there are some that mention the B-spline trasformation, what do those numbers mean?</li>
<li>I have also seen that it is possible to get a transformation visualization grid with different colors (red and green) depending on how much the voxel has been deformed, but personally I can not get the different colors, but only red, can you help me?<br>
Thank you</li>
</ol>

---

## Post #2 by @muratmaga (2024-02-13 16:45 UTC)

<p>There is a rich literature on image registration theory and application. You can start with an introductory guide to biomedical image registration to understand the keypoints. Elastix also has a their documentation that briefly explains the concepts. that looks like to a good place to start for all your inquiries</p>
<p><a href="https://elastix.lumc.nl/download/elastix-5.1.0-manual.pdf" class="onebox" target="_blank" rel="noopener">https://elastix.lumc.nl/download/elastix-5.1.0-manual.pdf</a></p>
<p>As for visualizing the transforms, please see the Slicer documentation. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualization-modes" class="inline-onebox">Transforms — 3D Slicer documentation</a></p>
<p>You have to be careful that these grids are specified in millimeters, so if you are working small voxel data (llike microns) 10mm spacing might be wider than your entire field of view.</p>

---

## Post #3 by @lassoan (2024-02-13 17:09 UTC)

<aside class="quote no-group" data-username="Alice_Durante" data-post="1" data-topic="34298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alice_durante/48/67737_2.png" class="avatar"> Alice_Durante:</div>
<blockquote>
<p>Can you confirm me first of all whether this is a recording technique based on grey levels and not on geometry?</p>
</blockquote>
</aside>
<p>Confirmed.</p>
<aside class="quote no-group" data-username="Alice_Durante" data-post="1" data-topic="34298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alice_durante/48/67737_2.png" class="avatar"> Alice_Durante:</div>
<blockquote>
<p>What kind of similarity measure does this extension use? Minimum squares differences, correlation coefficient etc…?</p>
<p>What kind of transformation model is used? Is it correct to say that B-Spline is used? If yes, can you tell me more about it?</p>
<p>On the information regarding the transformations there are some that mention the B-spline trasformation, what do those numbers mean?</p>
</blockquote>
</aside>
<p>A lot of metrics, transformations, optimizers, etc. are available in Elastix. The parameter set (e.g., “generic (all)”) specifies what is actually used. You can find definition of the parameter sets in the database folder that you can open by clicking the “Show database folder” button in “Advanced” section.</p>
<aside class="quote no-group" data-username="Alice_Durante" data-post="1" data-topic="34298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alice_durante/48/67737_2.png" class="avatar"> Alice_Durante:</div>
<blockquote>
<p>I have also seen that it is possible to get a transformation visualization grid with different colors (red and green) depending on how much the voxel has been deformed, but personally I can not get the different colors, but only red, can you help me?</p>
</blockquote>
</aside>
<p>Red usually means large displacement, including the bulk positioning transform that aligned the images to each other. If you are interested in coloring only by the deformable component then you can perform the registration in two steps: first do a rigid registration; and then use the output volume as moving volume in a second registration that includes warping. If you visualize the transform provided by the second registration, it will not be all red.</p>

---
