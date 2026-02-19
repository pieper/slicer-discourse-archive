---
topic_id: 14638
title: "Converting A Stl File To Nifti"
date: 2020-11-16
url: https://discourse.slicer.org/t/14638
---

# Converting a STL file to nifti

**Topic ID**: 14638
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/converting-a-stl-file-to-nifti/14638

---

## Post #1 by @ycaspi (2020-11-16 16:21 UTC)

<p>Hello Guys,</p>
<p>I am trying to convert an stl file to nifti using Dicer.</p>
<p>I found the following: Conversation: <a href="https://discourse.slicer.org/t/converting-stl-files-to-binary-label-maps-in-nii-format-using-python/13038/6" class="inline-onebox">Converting .stl files to binary label maps in .nii format using Python</a></p>
<p>I have tried to follow the instructions of Donnie Cameron.</p>
<p>However, when I give the command:</p>
<pre><code class="lang-auto">seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
</code></pre>
<p>I get the error message:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: SetReferenceImageGeometryParameterFromVolumeNode argument 1: method requires a VTK object
</code></pre>
<p>Similarly: If I follow Andras Lasso script and give the command:</p>
<pre><code class="lang-auto">outputLabelmapVolumeNode = 
slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
</code></pre>
<p>I also get the error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: ExportVisibleSegmentsToLabelmapNode argument 1: method requires a VTK object
</code></pre>
<p>Does anyone know what do I do wrong?</p>
<p>Best,<br>
Yaron</p>

---

## Post #2 by @lassoan (2020-11-17 00:23 UTC)

<p>See complete example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rasterize_a_model_and_save_it_to_a_series_of_image_files">script repository</a>.</p>

---

## Post #3 by @ycaspi (2020-11-17 10:26 UTC)

<p>Dear Andras,</p>
<p>Thanks for your reply. I have tried to follow the script for converting stl to TIFF images but still get error messages. In particular, the command</p>
<pre><code class="lang-auto">inputModel.GetBounds(bounds) 
</code></pre>
<p>returns the error message:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'bool' object has no attribute 'GetBounds'
</code></pre>
<p>Similarly, the command:<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)<br>
Returns the error message:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: ImportModelToSegmentationNode argument 1: method requires a VTK object
</code></pre>
<p>To me it looks as if the method to load the stl file is the problematic one (<code>inputModel = slicer.util.loadModel(inputModelFile)</code> ).<br>
Any idea how to solve it?</p>
<p>Thanks,<br>
Yaron</p>

---

## Post #4 by @cpinter (2020-11-17 10:58 UTC)

<p>The variable <code>inputModel</code> should contain a vtkMRMLModelNode and not a boolean</p>

---

## Post #5 by @ycaspi (2020-11-17 11:32 UTC)

<p>Dear Csaba,</p>
<p>The variable  <code>inputModel</code>  was set according to the script as:</p>
<pre><code class="lang-auto">inputModel = slicer.util.loadModel(inputModelFile)
</code></pre>
<p>Where <code>inputModelFile</code> was my path to my stl file.</p>
<p>And that created the boolean object.</p>
<p>Hence, I think that there is a problem in setting the stl as a vtk object in Slicer.<br>
Any idea of how to do it?</p>
<p>Yaron</p>

---

## Post #6 by @cpinter (2020-11-17 11:34 UTC)

<p>At this point this is regular Python programming.</p>
<p>If you see the documentation of the function you use you’ll see why you get a boolean:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; help(slicer.util.loadModel)
Help on function loadModel in module slicer.util:

loadModel(filename, returnNode=False)
    Load node from file.
    
    :param filename: full path of the file to load.
    :param returnNode: Deprecated.
    :return: loaded node (if multiple nodes are loaded then a list of nodes).
      If returnNode is True then a status flag and loaded node are returned.
</code></pre>

---

## Post #7 by @ycaspi (2020-11-17 16:14 UTC)

<p>Thanks.</p>
<p>Using the syntax:</p>
<pre><code class="lang-auto">[Status, inputModel] = slicer.util.loadModel(inputModelFile, returnNode=True)
</code></pre>
<p>indeed solved the problem.</p>
<p>Yaron</p>

---

## Post #8 by @lassoan (2020-11-17 16:19 UTC)

<p>The API is changed in Slicer-4.11. By default we don’t use Boolean flag to indicate error anymore, but raise an exception instead. This allows simpler syntax of <code>inputModel = slicer.util.loadModel(inputModelFile)</code>.</p>
<p>I would recommend to update to latest Slicer stable or preview release.</p>

---
