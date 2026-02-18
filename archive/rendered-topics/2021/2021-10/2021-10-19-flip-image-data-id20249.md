# Flip image data

**Topic ID**: 20249
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/flip-image-data/20249

---

## Post #1 by @keri (2021-10-19 19:28 UTC)

<p>Hi,</p>
<p>I is it possible to flip <code>vtkImageData</code> and wrap the result in <code>vtkMRMLScalarVolumeNode</code>?</p>
<p>For example I can see that VTK has <a href="https://vtk.org/doc/nightly/html/classvtkImageFlip.html" rel="noopener nofollow ugc">vtkImageFlip</a> but for me it doesnt work:</p>
<pre><code class="lang-auto">  vtkNew&lt;vtkImageData&gt; imageData;
  imageData-&gt;SetDimensions(samples.size(), uXL.size(), uIL.size());
  imageData-&gt;AllocateScalars(VTK_FLOAT, 1);
  imageData-&gt;GetPointData()-&gt;SetScalars(TRACE);

  vtkNew&lt;vtkImageFlip&gt; imageFlip;
  imageFlip-&gt;SetInputData(imageData);
  imageFlip-&gt;SetFilteredAxis(1);
  imageFlip-&gt;Update();

  vtkNew&lt;vtkMRMLScalarVolumeNode&gt; volumeNode;
  volumeNode-&gt;SetName(nodeName.c_str());
  volumeNode-&gt;SetAndObserveImageData(imageData);
</code></pre>
<p>I think I do something wrong…</p>
<p>By the way simple rotation transform doesn’t solve my issue</p>

---

## Post #2 by @keri (2021-10-19 19:40 UTC)

<p>I’m sorry<br>
I just found a solution on internet.<br>
I should have been using:</p>
<pre><code class="lang-cpp">...
volumeNode-&gt;SetAndObserveImageData(imageFlip-&gt;GetOutput()); // `imageFlip-&gt;GetOutput()` returns `vtkImageData`
</code></pre>

---
