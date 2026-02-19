---
topic_id: 13822
title: "Slicerigt Fiducial To Model Registration Details"
date: 2020-10-02
url: https://discourse.slicer.org/t/13822
---

# SlicerIGT Fiducial to Model registration details

**Topic ID**: 13822
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/slicerigt-fiducial-to-model-registration-details/13822

---

## Post #1 by @Prashant_Pandey (2020-10-02 17:24 UTC)

<p>Hi, I’m trying to figure out the ICP registration details used in SlicerIGT’s Fiducial to Model registration module.</p>
<p>I’m looking here: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialsToModelRegistration/FiducialsToModelRegistration.py" rel="noopener nofollow ugc">https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialsToModelRegistration/FiducialsToModelRegistration.py</a> and <a href="https://github.com/Kitware/VTK/blob/master/Common/DataModel/vtkIterativeClosestPointTransform.cxx" rel="noopener nofollow ugc">https://github.com/Kitware/VTK/blob/master/Common/DataModel/vtkIterativeClosestPointTransform.cxx</a></p>
<p>Am I understanding correctly that only 200 points are used by default even if the surface model and markups node has many more points? How is the sampling achieved, is it uniform or based on distance?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-10-03 00:04 UTC)

<p>The beauty of VTK is that if you have any detailed question then you can go and read it in the code (and even modify as needed). VTK’s ICP implementation picks every N-th point for registration, see here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/5b6b705835795ca14782514303c45ab7dd89dd1e/Common/DataModel/vtkIterativeClosestPointTransform.cxx#L293-L298" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/5b6b705835795ca14782514303c45ab7dd89dd1e/Common/DataModel/vtkIterativeClosestPointTransform.cxx#L293-L298" target="_blank" rel="noopener">Kitware/VTK/blob/5b6b705835795ca14782514303c45ab7dd89dd1e/Common/DataModel/vtkIterativeClosestPointTransform.cxx#L293-L298</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="293" style="counter-reset: li-counter 292 ;">
<li>int step = 1;</li>
<li>if (this-&gt;Source-&gt;GetNumberOfPoints() &gt; this-&gt;MaximumNumberOfLandmarks)</li>
<li>{</li>
<li>  step = this-&gt;Source-&gt;GetNumberOfPoints() / this-&gt;MaximumNumberOfLandmarks;</li>
<li>  vtkDebugMacro(&lt;&lt; "Landmarks step is now : " &lt;&lt; step);</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Prashant_Pandey (2020-10-04 13:19 UTC)

<p>Yes, I saw that part but unfortunately I got a little lost in the code (I’m not used to C++). Does it select every n-th point uniformly, or is it the N closest points per iteration?</p>
<p>The reason I am asking about this is that we are trying to replicate the SlicerIGT Fiducial-Model registration functionality in MATLAB. Although there is a built-in MATLAB ICP function, the optimization details are a little different  and we are trying to match them exactly to what’s happening in Slicer and VTK. Currently, our post-registration mean distance error calculations are off by about 0.25mm</p>

---

## Post #4 by @lassoan (2020-10-04 14:18 UTC)

<p>It uses every n-th point, so it is not a random or spatially uniform sampling, but it depends on the order of points in the point list (so, it is rather poor sampling and in unlucky cases, you can end up with spatially very non-uniform distribution).</p>
<aside class="quote no-group" data-username="Prashant_Pandey" data-post="3" data-topic="13822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>The reason I am asking about this is that we are trying to replicate the SlicerIGT Fiducial-Model registration functionality in MATLAB. Although there is a built-in MATLAB ICP function, the optimization details are a little different and we are trying to match them exactly to what’s happening in Slicer and VTK.</p>
</blockquote>
</aside>
<p>The was always one of the major issues with Matlab: even though it had some high-quality algorithm libraries, their results were very often not reproducible (we could never reproduce exact same results as in Matlab in independent implementations). Since so many more packages are available for Python, many of them are very high quality, they are all open-source, reproducible, collaboratively developed, and widely accessible with non-restrictive licensing, nowadays it is really hard to find justification to use Matlab. Matlab still provides some unique tools for some niche applications, but it is not the best computing environment for engineers and scientists as it used to be 10-20 years ago.</p>
<p>In short, it may be hard to find people to help you with porting algorithms to Matlab from C++ or Python.</p>

---

## Post #5 by @Georgia_Grzybowski (2020-10-04 14:32 UTC)

<p>Hi,<br>
I am also working on this with Prash and thanks for your help so far. I looked through the code and am having trouble actually understanding the details of what it is doing. I see in lines 293 -298 that it is getting a step so it can step through the function and retrieve 200 points from the sample given at every step. Is this just done to the target points? Then it seems that only those points are transformed forward to make the error calculations? Is this process repeated every loop iteration or does it just need to be done once so only the nth points are run through the icp loop?</p>

---

## Post #6 by @lassoan (2020-10-04 14:46 UTC)

<aside class="quote no-group" data-username="Georgia_Grzybowski" data-post="5" data-topic="13822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/georgia_grzybowski/48/4222_2.png" class="avatar"> Georgia_Grzybowski:</div>
<blockquote>
<p>Is this just done to the target points?</p>
</blockquote>
</aside>
<p>Only source points are sampled.</p>
<aside class="quote no-group" data-username="Georgia_Grzybowski" data-post="5" data-topic="13822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/georgia_grzybowski/48/4222_2.png" class="avatar"> Georgia_Grzybowski:</div>
<blockquote>
<p>Then it seems that only those points are transformed forward to make the error calculations?</p>
</blockquote>
</aside>
<p>Only sampled points are used for error computation.</p>
<aside class="quote no-group" data-username="Georgia_Grzybowski" data-post="5" data-topic="13822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/georgia_grzybowski/48/4222_2.png" class="avatar"> Georgia_Grzybowski:</div>
<blockquote>
<p>Is this process repeated every loop iteration or does it just need to be done once so only the nth points are run through the icp loop?</p>
</blockquote>
</aside>
<p>The same sampled source points are used in all iterations.</p>

---

## Post #7 by @Georgia_Grzybowski (2020-10-05 14:42 UTC)

<p>Thanks for the answers. Just to confirm, 200 points aren’t resampled every iteration of the icp? It looks like the 200 points are resampled every iteration as the step code starting on line 293 is within the icp loop starting on line 264? On 3d slicer in this Fiducial to Model registration the absolute mean distance error is given after the registration in the user interface not the RMS error. But it looks from the code that RMS is actually what is calculated and optimized by default? Can you clarify this? And final question, the loop will stop when the mean distance is &lt;= max mean distance which is set to 0.01 by default? But when I have run the slicer module the mean distance errors I get are larger than 0.01 (maybe about 0.3mm to 1mm) so I am not sure how this is ever satisfied? Thank you!</p>

---
