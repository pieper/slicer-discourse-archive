# Create a short video to visualise a transform

**Topic ID**: 39794
**Date**: 2024-10-22
**URL**: https://discourse.slicer.org/t/create-a-short-video-to-visualise-a-transform/39794

---

## Post #1 by @Matteboo (2024-10-22 12:32 UTC)

<p>Hello,<br>
I have a transform that I apply to an organ segmentation. It would be nice to have a short animation of the segmentation moving from its original position/orientation/shape to the final one to visualize the transform.</p>
<p>This would be very helpfull to communicate with healthcare professional and for outside communication in general.</p>
<p>Is there any module/script that could help me to do that ?</p>

---

## Post #2 by @pieper (2024-10-22 12:37 UTC)

<p>Yes, this would be nice.  Not all transforms are easy to interpolate, but for something like a grid transform it’s doable.  This could be added to the Animator module with some scripting.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator" target="_blank" rel="noopener">SlicerMorph/Docs/Animator at master · SlicerMorph/SlicerMorph</a></h3>


  <p><span class="label1">Extension to import microCT data and conduct 3D morphometrics in Slicer - SlicerMorph/SlicerMorph</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Matteboo (2024-10-22 12:46 UTC)

<p>Unfortunately, I have a B-spline transform.<br>
Fortunately, I don’t have a computation time limit.<br>
My first idea is to compute the destination position for each voxel and make them move linearly between the starting and ending position, taking a screenshot of the created segmentation at everystep and putting everything together as a video.<br>
This would work with any transform.</p>

---

## Post #4 by @pieper (2024-10-22 13:03 UTC)

<p>Did you try just interpolating the coefficients of the b-spline control points?</p>

---

## Post #5 by @Matteboo (2024-10-22 13:31 UTC)

<p>I didn’t<br>
I haven’t started coding this (and I don’t think I will soon)<br>
I don’t know how to interpolate the coefficient of the b-spline control point (and I haven’t looked into it).<br>
Also, I think it’s easier to code soething that works with every transform even if it’s more computationnally costly.</p>

---

## Post #6 by @pieper (2024-10-22 17:16 UTC)

<p>Actually, you should be able to do something quick with <code>SetDisplaycementScale</code> so very little coding required (at least for the bspine case).</p>
<p>I just did this with a bspline registration result</p>
<pre><code class="lang-auto">&gt;&gt;&gt; 
&gt;&gt;&gt; bs = getNode("BS*")
&gt;&gt;&gt; t = bs.GetTransformFromParent()
&gt;&gt;&gt; t.GetDisplacementScale()
1.0
&gt;&gt;&gt; t.SetDisplacementScale(.5)
&gt;&gt;&gt; t.SetDisplacementScale(.25)
&gt;&gt;&gt; t.SetDisplacementScale(.75)
</code></pre>

---
