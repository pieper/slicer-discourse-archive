---
topic_id: 2254
title: "Zoom In Or Out Via Python Interactor Version 4 8 0 On Mac"
date: 2018-03-06
url: https://discourse.slicer.org/t/2254
---

# Zoom in or out via python interactor version 4.8.0 on MAC

**Topic ID**: 2254
**Date**: 2018-03-06
**URL**: https://discourse.slicer.org/t/zoom-in-or-out-via-python-interactor-version-4-8-0-on-mac/2254

---

## Post #1 by @Ahmed_Soufane (2018-03-06 23:28 UTC)

<p>Hi, I was wondering how can I control the zooming of the 3D view via python interactor on slicer ?<br>
like it can be seen on the attached pictures?<br>
thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2012700a7c1c835acd68c9864cd963946b61121c.png" data-download-href="/uploads/short-url/4zIMsjk1P6aViQxowrLVGiD063q.png?dl=1" title="35%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2012700a7c1c835acd68c9864cd963946b61121c_2_690x470.png" alt="35%20PM" data-base62-sha1="4zIMsjk1P6aViQxowrLVGiD063q" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2012700a7c1c835acd68c9864cd963946b61121c_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2012700a7c1c835acd68c9864cd963946b61121c_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2012700a7c1c835acd68c9864cd963946b61121c.png 2x" data-dominant-color="E3644A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">35%20PM</span><span class="informations">1076×734 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-03-07 01:05 UTC)

<p>You can use these to zoom in/out:</p>
<pre><code>camera = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLCameraNode').GetCamera()
camera.Dolly(1.2)
camera.Dolly(0.8)</code></pre>

---

## Post #3 by @Ahmed_Soufane (2018-03-07 01:44 UTC)

<p>I tried the provided code, but nothing has changed !!</p>

---

## Post #4 by @jcfr (2018-03-07 07:36 UTC)

<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="3" data-topic="2254" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>I tried the provided code, but nothing has changed !!</p>
</blockquote>
</aside>
<p>In that case, you may have multiple 3d views and/or cameras objects.</p>
<p>What is the output of:</p>
<pre><code class="lang-auto">getNodes("*Camera*")
</code></pre>

---

## Post #5 by @lassoan (2018-03-07 13:19 UTC)

<p>Yes, check the camera (you can also get the camera for a view as shown in examples in the script repository).</p>
<p>Also, the two <code>Dolly</code> commands in the example show how to zoom in and out. If you run them all at once then it zooms in and out, so you may not notice the difference. Make sure you execute the code snippet tline by line.</p>

---

## Post #7 by @Ahmed_Soufane (2018-03-07 20:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ad018ca1d578c7fac6512a532d2f5df2003813a.png" data-download-href="/uploads/short-url/m5xniNVcoj8qQxqoezBfzwqnr6O.png?dl=1" title="41%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ad018ca1d578c7fac6512a532d2f5df2003813a_2_690x88.png" alt="41%20PM" data-base62-sha1="m5xniNVcoj8qQxqoezBfzwqnr6O" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ad018ca1d578c7fac6512a532d2f5df2003813a_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ad018ca1d578c7fac6512a532d2f5df2003813a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ad018ca1d578c7fac6512a532d2f5df2003813a.png 2x" data-dominant-color="E6F1E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">41%20PM</span><span class="informations">858×110 14.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
this is what I got when I executed getNodes(“<em>Camera</em>”)</p>

---

## Post #8 by @jcfr (2018-03-07 21:09 UTC)

<p><a class="mention" href="/u/ahmed_soufane">@Ahmed_Soufane</a>:</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="2254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Make sure you execute the code snippet tline by line.</p>
</blockquote>
</aside>
<p>Did you try this ?</p>
<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="7" data-topic="2254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>this is what I got when I executed getNodes(“Camera”)</p>
</blockquote>
</aside>
<p>As a side note, you don’t have to generate a screemshot when sharing experiment done in the python interactor, you could copy the text and use the markdown syntax for code snippet. See <a href="https://meta.discourse.org/t/post-format-reference-documentation/19197" class="inline-onebox">Is there any reference documentation for post formatting? - support - Discourse Meta</a></p>
<p>Now, having only camera means that the code snippet posted by <a class="mention" href="/u/lassoan">@lassoan</a> is expected to work. I am running out of idea.</p>

---

## Post #9 by @Ahmed_Soufane (2018-03-07 21:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>camera.Dolly(0.8)</p>
</blockquote>
</aside>
<p>I executed this code snippet, line by line, but nothing has changed in the images. maybe because I am using an older version of 3D slicer 4.8.0 ? would you recommend updating to the newer version maybe this issue will be resolved ??</p>
<p>camera = slicer.mrmlScene.GetFirstNodeByClass(‘vtkMRMLCameraNode’).GetCamera()</p>
<blockquote>
<blockquote>
<blockquote>
<p>camera.Dolly(1.2)<br>
camera.Dolly(0.8)</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #10 by @jcfr (2018-03-07 21:44 UTC)

<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="9" data-topic="2254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>3D slicer 4.8.0</p>
</blockquote>
</aside>
<p>I tested with Slicer 4.8.1 and I confirmed it worked on Linux</p>
<p>Would be nice if you could try both 4.8.1 and the latest preview build.</p>

---

## Post #11 by @Ahmed_Soufane (2018-03-07 21:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>camera.Dolly(0.8)</p>
</blockquote>
</aside>
<p>what did you execute exactly in order to zoom in or out can you show me please, because I just downloaded slicer version 4.8.1, and still there is no response from slicer and nothing changed in any of the views …</p>

---

## Post #12 by @jcfr (2018-03-07 22:57 UTC)

<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="11" data-topic="2254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>what did you execute exactly</p>
</blockquote>
</aside>
<p>Here it is:</p>
<ol>
<li>Sample Data → MRHead</li>
<li>Enable volume Rendering</li>
<li>Open python interactor and copy/past the python code</li>
<li>Then press enter, and the dolly will update</li>
</ol>
<pre><code class="lang-auto"># Clear scene
slicer.mrmlScene.Clear(0)

# Download sample data
from SampleData import SampleDataLogic
mrhead = SampleDataLogic().downloadMRHead()

# Open VolumeRendering module
selectModule(slicer.modules.volumerendering)

# Get VolumeRendering widget
widget = slicer.modules.volumerendering.widgetRepresentation()

# Enable VolumeRendering for our dataset
widget.setMRMLVolumeNode(mrhead)

# Get rendering technique combobox and change to GPU technique to GPU
# XXX This is sub-optimal and brittle, we will improve the API to allow changing the technique more easily
slicer.util.findChild(widget, "RenderingMethodComboBox").currentIndex = 1

# Enable rendering
getNode("*GPU*Rendering*").SetVisibility(1)

# Get and update camera
camera = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLCameraNode').GetCamera()

# Update Dolly
camera.Dolly(0.8)


# ... 
camera.Dolly(1.2)
</code></pre>

---

## Post #13 by @Ahmed_Soufane (2018-03-07 23:14 UTC)

<p>what does updating dolly actually means ? Is is suppose to zoom in or out on the 3D view, because even though I have used the exact same code you sent. I got no response from slicer at all, it the 3D image did not zoom in or out ?</p>

---

## Post #14 by @jcfr (2018-03-08 00:15 UTC)

<blockquote>
<p>what does updating dolly actually means ?</p>
</blockquote>
<p>From the <a href="https://www.vtk.org/doc/nightly/html/classvtkCamera.html#ac1dcd796574d6b2abcade341587838c2">VTK documentation</a>:</p>
<pre><code class="lang-auto">Divide the camera's distance from the focal point by the given dolly value.

Use a value greater than one to dolly-in toward the focal point, and use a value less 
than one to dolly-out away from the focal point.
</code></pre>

---

## Post #15 by @pieper (2018-03-08 00:31 UTC)

<p>The code that Jc provided works for me.  Be sure to experiment by typing <code>camera.Dolly(X)</code> into the python console with different values of X and see what happens in the 3D view.</p>

---

## Post #16 by @talmazov (2019-07-02 20:37 UTC)

<p>Hey all,<br>
I am trying to accomplish the same thing with zooming but not with the 3D widget camera but in a slice rendering. I’ve tried SetDimension and SetFieldOfView but they distort the image.<br>
The Dolly function is a subset of the camera and not the slice.</p>
<p>I am essentially trying to recreate the right mouse click and drag that allows you to zoom-in on a set point.</p>
<p>Thanks!</p>

---

## Post #17 by @pieper (2019-07-02 20:52 UTC)

<p>You can use SetFieldOfView but compensate for the size of the render view like is done here (so you don’t distort the aspect ratio)</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/a02f79c7c788708a3dccfeb9ff4df76b6a5868be/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx#L370-L404" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a02f79c7c788708a3dccfeb9ff4df76b6a5868be/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx#L370-L404" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/a02f79c7c788708a3dccfeb9ff4df76b6a5868be/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx#L370-L404</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="370" style="counter-reset: li-counter 369 ;">
<li>if (vtkMRMLSliceLinkLogic::IsOrientationMatching(sliceNode, sNode))</li>
<li>  {</li>
<li>  // std::cout &lt;&lt; "Orientation match, flags = " &lt;&lt; sliceNode-&gt;GetInteractionFlags() &lt;&lt; std::endl;</li>
<li>  // std::cout &lt;&lt; "Broadcasting SliceToRAS, SliceOrigin, and FieldOfView to "</li>
<li>  //            &lt;&lt; sNode-&gt;GetName() &lt;&lt; std::endl;</li>
<li>  //</li>
<li>
</li>
<li>  // Copy the slice to RAS information</li>
<li>  if (sliceNode-&gt;GetInteractionFlags() &amp; sliceNode-&gt;GetInteractionFlagsModifier()</li>
<li>    &amp; vtkMRMLSliceNode::SliceToRASFlag)</li>
<li>    {</li>
<li>    sNode-&gt;GetSliceToRAS()-&gt;DeepCopy( sliceNode-&gt;GetSliceToRAS() );</li>
<li>    }</li>
<li>
</li>
<li>  // Copy the slice origin information</li>
<li>  if (sliceNode-&gt;GetInteractionFlags() &amp; sliceNode-&gt;GetInteractionFlagsModifier()</li>
<li>    &amp; vtkMRMLSliceNode::XYZOriginFlag)</li>
<li>    {</li>
<li>    // Need to copy the SliceOrigin.</li>
<li>    double *xyzOrigin = sliceNode-&gt;GetXYZOrigin();</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/a02f79c7c788708a3dccfeb9ff4df76b6a5868be/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx#L370-L404" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #18 by @talmazov (2019-07-02 21:54 UTC)

<p>Awesome, worked like a charm. I adapted it to constant value. Here is the snip code in case someone else runs into this issue.</p>
<pre><code># rescaling dimensions to zoom in using slice node's aspect ratio
x = 50
y = x * sliceNode.GetFieldOfView()[1] / sliceNode.GetFieldOfView()[0]
z = sliceNode.GetFieldOfView()[2]
sliceNode.SetFieldOfView(x,y,z)
sliceNode.Modified()</code></pre>

---
