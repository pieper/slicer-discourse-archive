# How does Slicer finds the optimal viewing window (min/max values) when importing nifti file?

**Topic ID**: 2763
**Date**: 2018-05-06
**URL**: https://discourse.slicer.org/t/how-does-slicer-finds-the-optimal-viewing-window-min-max-values-when-importing-nifti-file/2763

---

## Post #1 by @NaglisR (2018-05-06 13:41 UTC)

<p>Hi,</p>
<p>I want to find out how does Slicer determines the optimal viewing window (min/max values) when importing nifti file. I know that when importing dicoms the windowing info is in the metadata, however as far as I know nifti and nrrd files does not contain this info in the metadata. How is Slicer able to display the correct viewing window (for the brain tissue) after importing a nifti file?</p>

---

## Post #2 by @pieper (2018-05-06 15:45 UTC)

<p>It’s done in the code linked below - basically it is heuristic that looks at the histogram and expects a big hump of dark background, and then a hump of brighter foreground (a reasonable approximation of most CT and MR images).  Then it ignores the background and picks a range around the foreground.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/cdcfeb14564316be607c2c062ca4e418753d1c40/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L708-L862" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/cdcfeb14564316be607c2c062ca4e418753d1c40/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L708-L862" target="_blank">Slicer/Slicer/blob/cdcfeb14564316be607c2c062ca4e418753d1c40/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L708-L862</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="708" style="counter-reset: li-counter 707 ;">
<li>//---------------------------------------------------------------------------</li>
<li>void vtkMRMLScalarVolumeDisplayNode::CalculateAutoLevels()</li>
<li>{</li>
<li>if (!this-&gt;GetAutoWindowLevel() &amp;&amp; !this-&gt;GetAutoThreshold())</li>
<li>  {</li>
<li>  vtkDebugMacro("CalculateScalarAutoLevels: " &lt;&lt; (this-&gt;GetID() == NULL ? "nullid" : this-&gt;GetID())</li>
<li>                &lt;&lt; ": Auto window level not turned on, returning.");</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>vtkImageData *imageDataScalar = this-&gt;GetScalarImageData();</li>
<li>if (!imageDataScalar)</li>
<li>  {</li>
<li>  vtkDebugMacro("CalculateScalarAutoLevels: input image data is null");</li>
<li>  return;</li>
<li>  }</li>
<li>// Make sure the point data is up to date.</li>
<li>// Remember, the display node pipeline is not connected to a consumer (volume</li>
<li>// display nodes are cloned by the slice logic) therefore no-one has run the</li>
<li>// filters.</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/cdcfeb14564316be607c2c062ca4e418753d1c40/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L708-L862" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
