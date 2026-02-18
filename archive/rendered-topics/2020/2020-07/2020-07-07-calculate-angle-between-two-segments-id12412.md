# Calculate angle between two segments

**Topic ID**: 12412
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/calculate-angle-between-two-segments/12412

---

## Post #1 by @AurelienCD (2020-07-07 09:39 UTC)

<p>Dear 3dslicer community.</p>
<p>I try to write script which would calculate the angle between two segments.</p>
<p>Here is the image I have<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4771e2a6984c4137261da3f001da5c9a079ebdc.jpeg" alt="image" data-base62-sha1="s20Nag8GQotF4ViIDzPk4IJv4XG" width="481" height="332"></p>
<p>I obtained the segments using simple threshold</p>
<p>Then I would need to draw (automatically by python script as it is a part of an extension) lines through the segments and calculate the angle between the two lines.</p>
<p>As part of the extension I already have the center coordinates of the segments.</p>
<p>do you have any ideas ?</p>
<p>if it is needed, the whole script which give me the image is here:<br>
<a href="https://github.com/AurelienCD/Radiotherapy_Quality_Control/blob/master/Twist_MLC_Alignment_TOMOTHERAPY_QC.py" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/AurelienCD/Radiotherapy_Quality_Control/blob/master/Twist_MLC_Alignment_TOMOTHERAPY_QC.py</a></p>
<p>Many thanks,</p>
<p>AurelienCD</p>

---

## Post #2 by @Mik (2020-07-07 12:05 UTC)

<p>Greetings,</p>
<p>Get two points (e.g. along axis of symmetry) from each segment. Two points gives you a vector for each segment. Calculate cross or dot product of that vectors, that gives you either sine or cosine value of the angle.</p>
<p>The problem is how to calculate two points along axis of symmetry, or something like that? If the task is not on the plane, then you need three points.</p>

---

## Post #3 by @vertebra (2020-07-07 14:24 UTC)

<p><a class="mention" href="/u/aureliencd">@AurelienCD</a></p>
<p>Hello! I would use the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_markup_lines" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_markup_lines</a></p>

---

## Post #4 by @James_Hoctor (2020-07-07 15:42 UTC)

<p><a class="mention" href="/u/aureliencd">@AurelienCD</a></p>
<p>I would consider using Principal Component Analysis, specifically the <a href="https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html" rel="nofollow noopener">sklearn implementation</a>.</p>
<ol>
<li>Form an n-by-2 matrix of points in image space, either taking the positions of all points in one segment, or all points on the boundary of a segment (experiment to find which works better for you). Call this matrix <code>X</code>.</li>
<li>Use <code>sklearn.decomposition.PCA().fit(X).components_</code> to get the first principal component. This should be a 2-vector that points along the length of the segment.</li>
<li>Measure the angles between these orientation vectors.</li>
</ol>

---

## Post #5 by @lassoan (2020-07-07 16:27 UTC)

<p>Segment Statistics module solves this very nicely: it can compute oriented bounding box and principal axes directions for each segment, directly from the segmentation.</p>
<aside class="quote quote-modified" data-post="1" data-topic="10203">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">New Segment Statistics: Oriented Bounding Box, Diameter and More</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    New statistics have been added to the Segment Statistics module: 

Centroid
Oriented bounding box
Feret diameter
Perimeter
Roundness
Flatness
Elongation
Principal axes/moments

These statistics are not enabled by default. To enable them, click on the “Options” button beside the “Labelmap Statistics” checkbox, and select the statistics that you would like calculated from the popup window. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474.png" data-download-href="/uploads/short-url/2zZH7fLta4P90vWGbpxlusk3hqY.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
You can read the documentation for the Segment Statistics module <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmentstatistics.html" rel="noopener nofollow ugc">here</a>. 
Oriented bounding box: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72285939b0de724fdb92c1f2509b07eb474397a.jpeg" data-download-href="/uploads/short-url/wYIg0J7wFKzWP3CWq8W1fDzMzsm.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[…</a>
  </blockquote>
</aside>


---

## Post #6 by @AurelienCD (2020-07-08 06:44 UTC)

<p>Thank you James for your correction of my code on github it help a lot. I am a beginner and comments are still necessary <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @AurelienCD (2020-07-08 06:50 UTC)

<p>Thank you Andras, I will use that new module.</p>
<p>thank you everyone for your help.</p>
<p>all the best,</p>
<p>Aurélien</p>

---
