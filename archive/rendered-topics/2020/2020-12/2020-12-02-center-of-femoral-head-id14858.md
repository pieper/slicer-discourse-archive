# Center of femoral head

**Topic ID**: 14858
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/center-of-femoral-head/14858

---

## Post #1 by @felix2609 (2020-12-02 23:49 UTC)

<p>Hello everyone,</p>
<p>is there any possibility to mark the center of the femoral head? In planning softwares you can draw a circle around the contour of the femoral head, but i see no possibility to draw a circle and mark its center.</p>
<p>Thank you for your help!</p>

---

## Post #2 by @muratmaga (2020-12-03 00:02 UTC)

<p>I am not sure how you define the contour of the femoral head, but if you are planning in 3D view, you can easily trace it via the closed curve markups tool and calculate its centroid.</p>

---

## Post #3 by @lassoan (2020-12-03 05:56 UTC)

<p>We provide general tools in Slicer and you can easily handcraft your specialized tools using Python scripting. For example, you can specify a sphere using markups fiducials, either directly determining the optimal sphere from multiple points and/or manually positioning a sphere by adjusting a few control points.</p>
<p>You can get a best-fit sphere if you place a couple of markups fiducial points on the femur head surface (either in slice views or in 3D) then copy-paste this code snippet into the Python console:<br>
<s><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Specify_a_sphere_by_multiple_of_markups_points">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Specify_a_sphere_by_multiple_of_markups_points</a></s> <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d50bcdfbc1ad236d586b9705d8373ccf5fc12f11.jpeg" data-download-href="/uploads/short-url/uoGZx8VI7L6StSFqwxajdPOh5sZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d50bcdfbc1ad236d586b9705d8373ccf5fc12f11_2_533x500.jpeg" alt="image" data-base62-sha1="uoGZx8VI7L6StSFqwxajdPOh5sZ" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d50bcdfbc1ad236d586b9705d8373ccf5fc12f11_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d50bcdfbc1ad236d586b9705d8373ccf5fc12f11_2_799x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d50bcdfbc1ad236d586b9705d8373ccf5fc12f11_2_1066x1000.jpeg 2x" data-dominant-color="7D7976"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1306×1223 368 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you prefer interactive adjustment then you can place one fiducial in the sphere’s center, one at the sphere’s boundary and copy-paste this code snippet in the Python console: <s><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_define.2Fedit_a_circular_region_of_interest_in_a_slice_viewer.3F">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_define.2Fedit_a_circular_region_of_interest_in_a_slice_viewer.3F</a></s> <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer</a></p>
<p>You can make out a Slicer module from these code snippets (and anything else you need to do in your workflow) - see tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">here</a>.</p>

---

## Post #4 by @felix2609 (2020-12-05 15:27 UTC)

<p>thank you for your help! do you know how to calculate the center of a 2d circle segmentation and get a center point?</p>

---

## Post #5 by @felix2609 (2020-12-05 15:29 UTC)

<p>thank you very much! works good but i can´t remove the circle once it´s set. How can i remove it?</p>

---

## Post #6 by @lassoan (2020-12-05 15:44 UTC)

<aside class="quote no-group" data-username="felix2609" data-post="4" data-topic="14858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/94ad74/48.png" class="avatar"> felix2609:</div>
<blockquote>
<p>do you know how to calculate the center of a 2d circle segmentation and get a center point?</p>
</blockquote>
</aside>
<p>You can use Segment Statistics module to get bounding box center and size. You can use the GUI or this script: <s><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment</a></s><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment</a></p>
<p>What kind of data do you work with? What would you like to achieve?</p>
<aside class="quote no-group" data-username="felix2609" data-post="5" data-topic="14858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/94ad74/48.png" class="avatar"> felix2609:</div>
<blockquote>
<p>can´t remove the circle once it´s set</p>
</blockquote>
</aside>
<p>You can remove the node or hide it or not even create a model node for displaying the sphere.</p>

---

## Post #7 by @eliagre (2023-02-21 16:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can get a best-fit sphere if you place a couple of markups fiducial points on the femur head surface (either in slice views or in 3D) then copy-paste this code snippet into the Python console: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Specify_a_sphere_by_multiple_of_markups_points" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Specify_a_sphere_by_multiple_of_markups_points </a></p>
</blockquote>
</aside>
<p>Hello, I’m trying to apply your code to define my best-fit sphere. When I enter the code, I get the following error message:<br>
“Traceback (most recent call last):<br>
File “”, line 37, in <br>
NameError: name ‘markups’ is not defined”</p>
<p>I’m not familiar with python, so I don’t know how to fix this. Could you help me out, please?<br>
The code I applied was found on this webpage, under " Specify a sphere by multiple control points": <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>Operating system: win11<br>
Slicer 5.2.1</p>

---

## Post #8 by @muratmaga (2023-02-21 17:26 UTC)

<p>There is a typo in the script. Replace the markups with pointListNode and it should work.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you fix?</p>

---

## Post #9 by @eliagre (2023-02-21 17:31 UTC)

<p>It worked perfectly now, thank you!</p>

---

## Post #10 by @lassoan (2023-02-21 18:13 UTC)

<p>Thanks, fixed <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">here</a>.</p>

---

## Post #11 by @jcfr (2023-02-22 06:05 UTC)

<p>For reference, the corresponding documentation fix has also been backported to the <code>5.2</code> maintenance branch.</p>

---
