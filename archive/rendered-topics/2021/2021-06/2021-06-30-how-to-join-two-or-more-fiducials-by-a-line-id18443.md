# How to join two or more fiducials by a line?

**Topic ID**: 18443
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/how-to-join-two-or-more-fiducials-by-a-line/18443

---

## Post #1 by @Rahulsabharwal (2021-06-30 20:26 UTC)

<p>How can we pass a line through two mark up fiducials ?<br>
Or even three of them.  Like making an axis to join them.</p>

---

## Post #2 by @smrolfe (2021-06-30 21:31 UTC)

<p>If you have two points in a markups fiducial node ‘F’, you can create a new markups line node using the snippet:</p>
<pre><code class="lang-auto">F=getNode('F')
L=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
firstPoint = F.GetNthControlPointPositionVector(0)
L.AddControlPoint(firstPoint)
secondPoint = F.GetNthControlPointPositionVector(1)
L.AddControlPoint(secondPoint)
</code></pre>
<p>A line will only work with two points, if you have more than that you would need to use a markups curve node.</p>

---

## Post #3 by @esomjai (2023-05-04 11:09 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="18443">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<pre><code class="lang-auto">F=getNode('F')
L=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
firstPoint = F.GetNthControlPointPositionVector(0)
L.AddControlPoint(firstPoint)
secondPoint = F.GetNthControlPointPositionVector(1)
L.AddControlPoint(secondPoint)
</code></pre>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a>,</p>
<p>I was wondering how to modify the code snippet if my landmarks (control points) are in different markups fiducial nodes. How can I just specify the names of my control points that would be the endpoints of my linear distances?</p>

---

## Post #4 by @smrolfe (2023-05-04 18:26 UTC)

<p>Do you know the index of the control point in each node? If so, you can use the same method but select the second control point from a different node.</p>
<p>If you need to do this by control point name, you can loop through the points in each node, use <code>c1.GetNthControlPointLabel()</code> to get the point name, and match to the name you are looking for.</p>

---

## Post #6 by @esomjai (2023-05-05 11:06 UTC)

<p>Thank you for the quick reply <a class="mention" href="/u/smrolfe">@smrolfe</a> !<br>
I am quite unfamiliar with python scripting - can you point me to a guide on how to apply the c1.GetNthControlPointLabel() function?<br>
I tried replacing the initial code with your suggestion like this:<br>
<code>L=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode') firstPoint = c1.GetNthControlPointLabel('praR') L.AddControlPoint(firstPoint) secondPoint = c1.GetNthControlPointLabel('paR') L.AddControlPoint(secondPoint)</code></p>
<p>However, I keep getting the error message:  NameError: name ‘c1’ is not defined</p>
<p>My goal with this would be that the linear measurements are defined by their name and not the position and each time I can run the script after I placed the landmarks by hand e.g I have my endpoints as node names (e.g. prn-porion, se-sellion) and would like to compute the lines using the node names (e.g. prn-se).<br>
I would also like to name the newly generated line in the script (e.g. ear width R).</p>

---

## Post #7 by @smrolfe (2023-05-05 17:01 UTC)

<p>If you are collecting landmark points, I strongly recommend that you use the same order every time, i.e. “prn-porion” has the same landmark number for each subject. If some subjects are missing points, these can be included with the position set to missing. Please see our tutorials on the <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Markups_1#the-control-points-menu" rel="noopener nofollow ugc">control point position status</a> and <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Markups_3" rel="noopener nofollow ugc">landmark template creation</a> for more information.</p>
<p>For two point lists, named “F” and “G”, the following snippet will create a line measurement between landmark 0 in each list and name the line “myMeasurement”. To run, replace “F” and “G” with your point list names and “0” with the point number of the landmark in each list.</p>
<pre><code class="lang-auto">F=getNode('F')
G=getNode('G')
L=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
firstPoint = F.GetNthControlPointPositionVector(0)
L.AddControlPoint(firstPoint)
secondPoint = G.GetNthControlPointPositionVector(0)
L.AddControlPoint(secondPoint)
L.SetName("myMeasurement")
</code></pre>

---

## Post #8 by @smrolfe (2023-05-05 17:09 UTC)

<aside class="quote no-group" data-username="esomjai" data-post="6" data-topic="18443">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/e274bd/48.png" class="avatar"> esomjai:</div>
<blockquote>
<p>However, I keep getting the error message: NameError: name ‘c1’ is not defined</p>
</blockquote>
</aside>
<p>For the example above, replace <code>c1</code> with <code>F</code>. The function <code>GetNthControlPointLabel()</code> takes an integer point number and returns a string with the point name. So to check the name at point 0, you can use:</p>
<pre><code class="lang-auto">labelName = F.GetNthControlPointLabel(0)
</code></pre>

---

## Post #9 by @lassoan (2023-05-06 18:03 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="7" data-topic="18443">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>If you are collecting landmark points, I strongly recommend that you use the same order every time, i.e. “prn-porion” has the same landmark number for each subject</p>
</blockquote>
</aside>
<p>You can also find a control point by label. I’ve just tried and bing chat provides a perfect answer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9aae2ff4f37f82d4edcaed71a7a12f237f552de.jpeg" data-download-href="/uploads/short-url/quusdt5VO6tx9iSdFErpRKRp1hQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9aae2ff4f37f82d4edcaed71a7a12f237f552de_2_690x469.jpeg" alt="image" data-base62-sha1="quusdt5VO6tx9iSdFErpRKRp1hQ" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9aae2ff4f37f82d4edcaed71a7a12f237f552de_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9aae2ff4f37f82d4edcaed71a7a12f237f552de_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9aae2ff4f37f82d4edcaed71a7a12f237f552de_2_1380x938.jpeg 2x" data-dominant-color="E9E5EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1869×1273 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ll add a <code>GetControlPointIndexByLabel()</code> method to markups node to be able to find a control point by a simple call.</p>

---

## Post #10 by @esomjai (2023-05-08 22:00 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
I realise it is a quite simple question, thank you for taking the time to answer it. My Bing search was less successful (although having asked the same question) - would you mind providing me with the full code you got?</p>

---

## Post #11 by @lassoan (2023-09-10 12:40 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-set-colors-of-markups/31636">How to set colors of markups?</a></p>

---
