# How can I export to a segmentation to OBJ file using Python?

**Topic ID**: 4576
**Date**: 2018-10-29
**URL**: https://discourse.slicer.org/t/how-can-i-export-to-a-segmentation-to-obj-file-using-python/4576

---

## Post #1 by @mikebind (2018-10-29 19:31 UTC)

<p>I have several segmentations and would like to export each to an OBJ file.  The segmentations were created by segmenting each frame of a Sequence of image volumes.  The segmentations are not currently organized into a Sequence, but easily could be.  However, I haven’t done so because manually exporting to OBJ (using Segmentations/Export to files…) just exports the single segmentation currently associated with the proxy node (which is sensible, but not what I want). The segmentations are generated in a custom extension I’ve written where I do one careful manual segmentation and then automatically modify and propagate it to segment all other image volumes in the Sequence. There are 10 to 20 volumes in each Sequence I’m interested in processing, so it would save a lot of time if I could just add a button to my extension that would cycle through the generated segmentations and export each to OBJ rather than having to manually export each one.   I have successfully understood how to work with the python-based nodes to use segment editor effects, but the “Export to files” code seems to be entirely C++ based, and I don’t see how to interact with it from my extension.  I’d appreciate any help anyone can offer. Also, I’m not clear on whether a post like this should be tagged Development (because it involves questions about coding) or Support (because it’s a question about usage).  Advice on that would also be welcome. Thanks!</p>

---

## Post #2 by @cpinter (2018-10-30 13:31 UTC)

<p>Thanks for the nice explanation of your question!<br>
The part of that C++ code that actually does the exporting is this one function call:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationFileExportWidget.cxx#L195-L202" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationFileExportWidget.cxx#L195-L202" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationFileExportWidget.cxx#L195-L202</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="195" style="counter-reset: li-counter 194 ;">
<li>vtkSlicerSegmentationsModuleLogic::ExportSegmentsClosedSurfaceRepresentationToFiles(</li>
<li>  d-&gt;DestinationFolderButton-&gt;directory().toLatin1().constData(),</li>
<li>  d-&gt;SegmentationNode.GetPointer(),</li>
<li>  segmentIds.GetPointer(),</li>
<li>  d-&gt;FileFormatComboBox-&gt;currentText().toLatin1().constData(),</li>
<li>  d-&gt;CoordinateSystemComboBox-&gt;currentText() == "LPS",</li>
<li>  d-&gt;SizeScaleSpinBox-&gt;value(),</li>
<li>  d-&gt;MergeIntoSingleFileCheckBox-&gt;isChecked());</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Type this in the python console and you’ll get info about how to use it:</p>
<pre><code>help(slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles)
</code></pre>
<p>(I think it’s fine to put this post to the development category, as it’s about extension programming)</p>

---

## Post #3 by @mikebind (2018-10-31 15:09 UTC)

<p>Thanks, this is exactly what I needed.</p>

---
