---
topic_id: 14792
title: "Automate Tasks In Python"
date: 2020-11-27
url: https://discourse.slicer.org/t/14792
---

# Automate tasks in Python

**Topic ID**: 14792
**Date**: 2020-11-27
**URL**: https://discourse.slicer.org/t/automate-tasks-in-python/14792

---

## Post #1 by @kuonlp (2020-11-27 16:37 UTC)

<p>Is it actually possible to automate all the tasks that can be done through the GUI in Python? I have spent quite some hours trying to do very simple things but I was unsuccessful.</p>
<p>More specifically, I want to use the module “Model to Label Map”. So far, I could:</p>
<pre><code>import slicer
volume = slicer.util.loadVolume(path1)
model = slicer.util.loadModel(path2)
slicer.util.selectModule(slicer.modules.modeltolabelmap)
</code></pre>
<p>The next step is to change the settings or parameters of this particular module; then click on “Apply”, and once it’s done, saving the output somewhere. Any idea how I can do these steps?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2020-11-27 16:41 UTC)

<p>Yes, everything that you do on the GUI can be done using Python scripting, too.</p>
<p>Instead of “Model to Label Map” we generally recommend to use Segmentations module to do all conversions between segmentations, models, and labelmap volumes. You can import a model into a segmentation (that can be edited using Segment Editor effects and can be exported to labelmap) using a single command, as shown here: <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L34">https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L34</a></p>
<p>You can find lots of additional examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations</a></p>

---

## Post #3 by @kuonlp (2020-11-28 13:08 UTC)

<p>Hello Andras, thank you very much for your quick answer. Some comments/follow-up questions:</p>
<ol>
<li>
<p>What is exactly a “segmentation node”? Is it a voxelized version of the “model node” (the mesh), because getting this is my ultimate goal.</p>
</li>
<li>
<p>I don’t find very clear how to use the function to convert a “model node” to a “segmentation node”. It appears to be one line but it requires the “polydata” that it’s more unclear how to generate. In that example, it is iterating over certain pre-defined positions (line 24), creating some “SphereSource” objects and appending them to the initially-empty polydata. How would I find these “pre-defined positions”. I’m not sure what this is, and whether I have do the same in my case. Isn’t it another way to get a “segmentation node”? Is there another way around to use the Model To LabelMap functionality?</p>
</li>
<li>
<p>I couldn’t find any function to do the “Model To LabelMap” with the parameters/settings that I find in the GUI. More specifically, the GUI shows the settings “label value”.</p>
</li>
<li>
<p>Related to 3), I wanted to ask about another parameter that does not appear in “settings” in the latest version of Slicer. This parameter is “sampling space”, which appears in version 4.3 and I found it crucial in my data. Without this parameter I get empty volumes whereas with this parameter (and an appropriate tuning) I get favorable results.</p>
</li>
</ol>
<p>Thank you very much again for your answers.</p>

---

## Post #4 by @lassoan (2020-11-28 18:43 UTC)

<aside class="quote no-group" data-username="kuonlp" data-post="3" data-topic="14792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/fbc32d/48.png" class="avatar"> kuonlp:</div>
<blockquote>
<p>What is exactly a “segmentation node”?</p>
</blockquote>
</aside>
<p>See detailed explanation here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="kuonlp" data-post="3" data-topic="14792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/fbc32d/48.png" class="avatar"> kuonlp:</div>
<blockquote>
<p>I don’t find very clear how to use the function to convert a “model node” to a “segmentation node”. It appears to be one line but it requires the “polydata” that it’s more unclear how to generate</p>
</blockquote>
</aside>
<p>Have a look at examples in the script repository, for example this: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rasterize_a_model_and_save_it_to_a_series_of_image_files" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="kuonlp" data-post="3" data-topic="14792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/fbc32d/48.png" class="avatar"> kuonlp:</div>
<blockquote>
<p>I couldn’t find any function to do the “Model To LabelMap” with the parameters/settings that I find in the GUI. More specifically, the GUI shows the settings “label value”.</p>
</blockquote>
</aside>
<p>See the example above how to specify output image geometry (origin, spacing, axis directions). Other settings can be controlled by adjusting conversion parameters, see fore example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Re-convert_using_a_modified_conversion_parameter" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #5 by @kuonlp (2020-11-30 09:55 UTC)

<p>Hi again Andras, I really appreciate your help.</p>
<p>I’m getting closer to the desired solution. The snippet below seems to load the image and the model converted into a labelmap.</p>
<pre><code># Load the Nifti file, the image
referenceVolumeNode = slicer.util.loadVolume(niftiImage_path)
# Load the mesh
inputModel = slicer.util.loadModel(mesh_path)

seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
</code></pre>
<p>However, in Slice view, the loaded segmentation and the image are not aligned. This is crucial to later save the segmentation. This surprises me because I would expect that the function SetReferenceImageGeometryParameterFromVolumeNode would put the “seg” in the same orientation and coordinates as the referenceVolumeNode (the image). As you can see below, the bottom-right corner of the image is closer to the top-left corner of the segmentaiton.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb1d2e83a3025bbcdafae7709dfddcf35d967b36.png" alt="pic1" data-base62-sha1="qHhO7KVQeU4nVh7OcaCKulDZ0we" width="532" height="388"></p>
<p>Is there a way to align these two automatically? I could see that I can “move” the image by changing the “image origin”, but this is done visually and I can’t just do this. If there is no other way, how can I change this “image origin” from python?</p>
<p>Thanks.</p>

---

## Post #6 by @lassoan (2020-11-30 20:42 UTC)

<p>This is probably an RAS/LPS coordinate system mismatch. See more information and options to resolve it here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default</a></p>

---

## Post #7 by @kuonlp (2020-12-01 09:53 UTC)

<p>That was indeed the problem.</p>
<p>Once again, thank you very much Andras <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---
