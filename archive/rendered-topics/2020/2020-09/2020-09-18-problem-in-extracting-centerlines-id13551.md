# Problem in extracting centerlines

**Topic ID**: 13551
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/problem-in-extracting-centerlines/13551

---

## Post #1 by @Deepa (2020-09-18 16:09 UTC)

<p>Hello All,</p>
<p>I am trying to extract centerlines of vessel segments present in an <a href="https://drive.google.com/file/d/1pSMQWkjCVzUwPHsjFEAcqzdJddv_87WP/view?usp=sharing" rel="noopener nofollow ugc">stl file </a>.  When I use this model in the extract centerline module all the endpoints are not detected after hitting Auto-detect.</p>
<p>I also tried the same on a smaller subset of the vessels present in the stl file shared above. The network extraction and centerline extraction didn’t find the properties of all the branches. Many endpoints are undetected in “Auto detect”.</p>
<p>Suggestions on how to get this working will be really helpful.</p>

---

## Post #2 by @Deepa (2020-09-22 15:21 UTC)

<p>This is a kind reminder.</p>

---

## Post #3 by @Deepa (2020-09-27 16:26 UTC)

<p>This is a kind reminder. I’d like to know if the centerline extraction will work on geometries like this</p>

---

## Post #4 by @lassoan (2020-09-28 05:25 UTC)

<p>These file contains a so badly corrupted mesh that it is really hard to make any sense of it. It is tricky because visually it looks OK. However, it has duplicate triangles all over the mesh (it looks like all the tubes are double-walled) and it self-intersects at hundreds of locations. If you got this from an attachment of a paper then I would suggest to contact the journal and/or the authors and ask for a corrected mesh. Or ask for the centerline that it was generated from.</p>
<p>I was able to make the mesh somewhat usable by using <a href="https://www.paraview.org/">ParaView</a>’s “Clean to grid” filter followed by “Extract surface”. However, it is still not perfect and VMTK can only process a single vessel tree at a time, so you need to tune mesh clearing further and to split the mesh to independent trees before attempting centerline analysis.</p>

---

## Post #5 by @Deepa (2020-09-28 06:28 UTC)

<p>Thanks a lot for looking into this.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Or ask for the centerline that it was generated from.</p>
</blockquote>
</aside>
<p>The centerline data of multiple trees are available in <a href="https://github.com/DeepaMahm/misc/blob/master/islet1.xml" rel="noopener nofollow ugc">xml file</a>.<br>
Each <code>&lt;vessel version="3" color="#6080FF" type="directed"&gt;</code> corresponds a single tree.<br>
I have parsed this data in Python. However, I am not sure how to compute the centerline lengths and diameter / generate stl file from this data. Any help will be greatly appreciated.</p>
<p>The 3D object file of a single tree is also available <a href="https://drive.google.com/file/d/1ixPXpNiJyR2A60q15ldc_GFDKVfF8oRv/view?usp=sharing" rel="noopener nofollow ugc">here</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I was able to make the mesh somewhat usable by using <a href="https://www.paraview.org/" rel="noopener nofollow ugc">ParaView</a>’s “Clean to grid” filter followed by “Extract surface”.</p>
</blockquote>
</aside>
<p>I will try if this works on the single tree object.</p>
<p>EDIT: I used “Clean to grid” filter followed by “Extract surface” and generated <a href="https://drive.google.com/file/d/1ILuFBIT5dNrxu0JQUcKDuK0uXiz8exYD/view?usp=sharing" rel="noopener nofollow ugc">this file</a><br>
The endpoints weren’t detected for this too</p>

---

## Post #6 by @lassoan (2020-09-28 13:52 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="5" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>The centerline data of multiple trees are available in <a href="https://github.com/DeepaMahm/misc/blob/master/islet1.xml">xml file </a>.<br>
Each <code>&lt;vessel version="3" color="#6080FF" type="directed"&gt;</code> corresponds a single tree.<br>
I have parsed this data in Python. However, I am not sure how to compute the centerline lengths and diameter / generate stl file from this data. Any help will be greatly appreciated.</p>
</blockquote>
</aside>
<p>Having a tree in XML makes things very simple. Centerline length computation is trivial (sum of Euclidean distances between points that make up a branch).</p>
<aside class="quote no-group quote-modified" data-username="Deepa" data-post="5" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I was able to make the mesh somewhat usable by using <a href="https://www.paraview.org/">ParaView</a>’s “Clean to grid” filter followed by “Extract surface”.</p>
</blockquote>
</aside>
<p>I will try if this works on the single tree object.</p>
<p>EDIT: I used “Clean to grid” filter followed by “Extract surface” and generated <a href="https://drive.google.com/file/d/1ILuFBIT5dNrxu0JQUcKDuK0uXiz8exYD/view?usp=sharing">this file</a><br>
The endpoints weren’t detected for this too</p>
</blockquote>
</aside>
<p>As I wrote above, you need to split the forest and process each tree separately. There is a problem also with self-intersections. Fortunately, you don’t need any of this, as you can already get the tree from the XML file.</p>
<hr>
<p>Since you already have a clear definition of the vessel tree in the XML file, you don’t need to use VMTK (which would provide end result very similar to the information in the XML file). I don’t think there is anything more I could help you with. You should be able to do the rest of the analysis by yourself, using various Python packages.</p>

---

## Post #7 by @Deepa (2020-09-28 13:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Having a tree in XML makes things very simple. Centerline length computation is trivial (sum of Euclidean distances between points that make up a branch).</p>
</blockquote>
</aside>
<p>Thank you, this helps a lot. May I know how the diameter can be computed?</p>

---

## Post #8 by @lassoan (2020-09-28 14:00 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="7" data-topic="13551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>May I know how the diameter can be computed?</p>
</blockquote>
</aside>
<p>As you can see in the XML file, vessel diameter is available for each point:</p>
<pre data-code-wrap="xml"><code class="lang-xml">...
&lt;point x="124.54" y="-421.36" z="-16.00" d="2.94"/&gt;
...
`</code></pre>

---

## Post #9 by @Deepa (2020-09-28 14:08 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> Yes, I mean to ask if it would be right to simply compute the average diameter, using the diameter of each point, for finding out the diameter of a branch.</p>
<p>I had tried this before and the values were different. So I am not sure what’s right approach</p>

---

## Post #10 by @lassoan (2020-09-28 15:02 UTC)

<p>This decision is up to you, whatever you find the most appropriate for your application.</p>

---

## Post #12 by @chir.set (2020-10-02 06:17 UTC)

<p>This case is going hopeless <img src="https://emoji.discourse-cdn.com/twitter/yawning_face.png?v=9" title=":yawning_face:" class="emoji" alt=":yawning_face:"></p>

---
