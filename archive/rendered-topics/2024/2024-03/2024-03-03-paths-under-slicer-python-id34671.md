# Paths under Slicer python

**Topic ID**: 34671
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/paths-under-slicer-python/34671

---

## Post #1 by @muratmaga (2024-03-03 03:23 UTC)

<p>Why does the first segmentation load fail, even though the file is clearly found? Do files always have to be referred with their full path?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; os.getcwd()
'/Users/amaga'
&gt;&gt;&gt; os.path.isfile("MD/"+segmentation)
True
&gt;&gt;&gt; slicer.util.loadSegmentation("MD/"+segmentation)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 903, in loadSegmentation
    return loadNodeFromFile(filename, "SegmentationFile", properties, returnNode)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 734, in loadNodeFromFile
    raise RuntimeError(errorMessage)
RuntimeError: Failed to load node from file: MD/IMPC_sample_data.seg.nrrd
Error: Loading MD/IMPC_sample_data.seg.nrrd -  load failed.

[VTK] vtkMRMLSegmentationStorageNode::ReadDataInternal: Segmentation file '/Users/amaga/Documents/MD/IMPC_sample_data.seg.nrrd' is not found while trying to read node (vtkMRMLSegmentationStorageNode5).
[VTK] vtkMRMLStorageNode::ReadData: Failed to read node IMPC_sample_data_11 (vtkMRMLSegmentationNode5) from filename='MD/IMPC_sample_data.seg.nrrd'
[VTK] LoadSegmentationFromFile: Error reading MD/IMPC_sample_data.seg.nrrd
&gt;&gt;&gt; slicer.util.loadSegmentation("/Users/amaga/MD/IMPC_sample_data.seg.nrrd")
&lt;MRMLCorePython.vtkMRMLSegmentationNode(0x7fcd19ef9f80) at 0x170fcebe0&gt;
</code></pre>

---

## Post #2 by @muratmaga (2024-03-03 16:56 UTC)

<p>I will rephrase my question, now I see why the first load is failing. Because the path is incorrect.</p>
<p>So, why is the command <code>loadSegmentation("MD/"+segmentation)</code> expanding the path to</p>
<pre><code class="lang-auto">/Users/amaga/Documents/MD/IMPC_sample_data.seg.nrrd'
</code></pre>
<p>As shown in the first line, working directory is <code>/Users/amaga</code>. Where is the Documents coming from?</p>

---

## Post #3 by @pieper (2024-03-03 17:14 UTC)

<p>Probably that’s where your scene is saved.  There’s logic to try to find relative paths with respect to the scene file if they can’t be found. (This code is 16-17 years old, so maybe it’s time to revisit that logic - it’s used in all scene loading so we’d need to be careful.  Maybe changing the slicer.util behavior to create absolute paths would be cleaner).</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/c7fe8657c6a4bc0666685349b3222ff3c1b4fa02/Libs/MRML/Core/vtkMRMLStorageNode.cxx#L648">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/c7fe8657c6a4bc0666685349b3222ff3c1b4fa02/Libs/MRML/Core/vtkMRMLStorageNode.cxx#L648" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/c7fe8657c6a4bc0666685349b3222ff3c1b4fa02/Libs/MRML/Core/vtkMRMLStorageNode.cxx#L648" target="_blank" rel="noopener">Slicer/Slicer/blob/c7fe8657c6a4bc0666685349b3222ff3c1b4fa02/Libs/MRML/Core/vtkMRMLStorageNode.cxx#L648</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="638" style="counter-reset: li-counter 637 ;">
          <li>  {</li>
          <li>    return "Cancelled";</li>
          <li>  }</li>
          <li>  if (state == this-&gt;SkippedNoData)</li>
          <li>  {</li>
          <li>    return "SkippedNoData";</li>
          <li>  }</li>
          <li>  return "(undefined)";</li>
          <li>}</li>
          <li></li>
          <li class="selected">//----------------------------------------------------------------------------</li>
          <li>std::string vtkMRMLStorageNode::GetFullNameFromFileName()</li>
          <li>{</li>
          <li>  return this-&gt;GetFullNameFromNthFileName(-1);</li>
          <li>}</li>
          <li></li>
          <li>//----------------------------------------------------------------------------</li>
          <li>std::string vtkMRMLStorageNode::GetFullNameFromNthFileName(int n)</li>
          <li>{</li>
          <li>  std::string fullName = std::string("");</li>
          <li>  const char *fileName;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @muratmaga (2024-03-03 17:22 UTC)

<p>This example was with a blank Slicer session, no scene was saved. But for my Slicer. yes default scene location is in indeed <code>/Users/amaga/Documents</code> as shown in the Application Preferences.</p>
<p>So these loadSegmentation loadVolume functions always prefix the scene path, if a relative path provided? I am trying to understand how to work with relative paths with respect to a cloned repo.</p>

---

## Post #5 by @pieper (2024-03-03 17:30 UTC)

<p>I think the best bet in your code would be to construct the absolute path before calling <code>loadSegmentation</code>.</p>

---

## Post #6 by @muratmaga (2024-03-03 23:56 UTC)

<p>It is not so much about how to make it work then why this is happening. It is a valid file path, and error is unexpected (and I don’t think this is documented anywhere). I am writing a tutorial so it is important to explain why this is happening, which otherwise looks like weird behavior.</p>
<p>Is it because the working directory inside the Slicer mrml is different than working directory in the python, or the cwd function inside the python console has no bearing on the path of the scene?</p>

---

## Post #7 by @muratmaga (2024-03-04 06:12 UTC)

<p>To further the confusion, loadVolume is perfectly happy with relative path,</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.loadVolume("MD/"+segmentation)
&lt;MRMLCorePython.vtkMRMLScalarVolumeNode(0x7fe6a3408d80) at 0x1754e6d60&gt;
</code></pre>
<p>while loadSegmentation fails:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.loadSegmentation("MD/"+segmentation)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 903, in loadSegmentation
    return loadNodeFromFile(filename, "SegmentationFile", properties, returnNode)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 734, in loadNodeFromFile
    raise RuntimeError(errorMessage)
RuntimeError: Failed to load node from file: MD/IMPC_sample_data.seg.nrrd
Error: Loading MD/IMPC_sample_data.seg.nrrd -  load failed.

[VTK] vtkMRMLSegmentationStorageNode::ReadDataInternal: Segmentation file '/Users/amaga/Documents/MD/IMPC_sample_data.seg.nrrd' is not found while trying to read node (vtkMRMLSegmentationStorageNode1).
[VTK] vtkMRMLStorageNode::ReadData: Failed to read node IMPC_sample_data_3 (vtkMRMLSegmentationNode1) from filename='MD/IMPC_sample_data.seg.nrrd'
[VTK] LoadSegmentationFromFile: Error reading MD/IMPC_sample_data.seg.nrrd
</code></pre>

---

## Post #8 by @pieper (2024-03-05 22:10 UTC)

<p>It’s kind of deep in the logic of the scene loading so someone would need to spend some time tracking it down.  I still think generating absolute paths is best practice anyway.  I can’t think of any time when I have used relative paths or relied on the working directory to get the right data.  Maybe the easy thing is to add a warning if a non-absolute path is passed.  The docs say ‘full path’ but that is ambiguous and maybe it should say ‘absolute’.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadNodeFromFile">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadNodeFromFile</a></p>

---
