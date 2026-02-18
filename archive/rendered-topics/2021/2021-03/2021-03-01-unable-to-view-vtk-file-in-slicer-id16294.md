# Unable to view vtk file in slicer

**Topic ID**: 16294
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/unable-to-view-vtk-file-in-slicer/16294

---

## Post #1 by @akshay_pillai (2021-03-01 19:06 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am able to view this vtk file using paraview under points gaussian but not when I upload this to slicer. Is there a reason I am unable to see the vtk data in slicer? And how do I make it visible?</p>

---

## Post #2 by @jcfr (2021-03-01 20:37 UTC)

<p>Do you have an example of file causing problem ? Is there any relevant information in the log (in application menu bar: <code>View-&gt;Error log</code>) ?</p>

---

## Post #3 by @akshay_pillai (2021-03-01 20:47 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Sorry, yes I do see an error. “.vtk does not contain coordinate system information. Assuming LPS.” I cant upload the file though. Have you seen this error. Anyhting I can do ?</p>

---

## Post #4 by @lassoan (2021-03-01 21:02 UTC)

<p>Lack of coordinate system information is just a warning, you can ignore it because the assumption of LPS is probably correct.</p>
<p>If you need to use points Gaussian to see the data set in Paraview then probably you do not have any cells. To display point cloud, you need to at least specify vertex cells, or run the point cloud through a glyph filter or surface reconstructor.</p>
<p>For example, if you want to apply a glyph filter on a point cloud loaded as a model node in Slicer then copy-paste this snippet into Slicer’s Python console:</p>
<pre><code class="lang-python">modelNode = getNode('MyModel')  # replace this with the actual name of your model node
glyph=vtk.vtkGlyph3D()
glyph.SetInputData(modelNode.GetPolyData())
glyph.Update()
modelNode.SetAndObservePolyData(glyph.GetOutput())
</code></pre>
<p>How do you plan to use this data in Slicer?</p>

---

## Post #5 by @akshay_pillai (2021-03-01 21:17 UTC)

<p>I just wanted to view the points as a 3d model in slicer. Thanks for that, I tried the glyph filter method but I get this: AttributeError: ‘MRMLCorePython.vtkMRMLModelNode’ object has no attribute ‘GetPointData’</p>

---

## Post #6 by @akshay_pillai (2021-03-01 21:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> Here is a vtk file that I have issues with. I just want to upload to slicer and view as 3d.</p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1YtIR6HN8F0lBicQ0xzlhnb04oYvJPAQc/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1YtIR6HN8F0lBicQ0xzlhnb04oYvJPAQc/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1YtIR6HN8F0lBicQ0xzlhnb04oYvJPAQc/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">x.vtk</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2021-03-01 21:36 UTC)

<aside class="quote no-group" data-username="akshay_pillai" data-post="5" data-topic="16294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>Thanks for that, I tried the glyph filter method but I get this: AttributeError: ‘MRMLCorePython.vtkMRMLModelNode’ object has no attribute ‘GetPointData’</p>
</blockquote>
</aside>
<p>I’ve updated thr code snippet, it should work now.</p>

---

## Post #8 by @akshay_pillai (2021-03-02 15:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hey, thank you, that worked, but it still doesn’t display. What line can I use to display it or view it in the Data module?</p>

---

## Post #9 by @lassoan (2021-03-02 22:35 UTC)

<p>The remaining issue was that the 3D view had to be centered.</p>

---
