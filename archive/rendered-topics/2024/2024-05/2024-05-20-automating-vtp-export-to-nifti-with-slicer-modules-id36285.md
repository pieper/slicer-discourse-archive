# Automating .vtp export to NIFTI with Slicer Modules

**Topic ID**: 36285
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/automating-vtp-export-to-nifti-with-slicer-modules/36285

---

## Post #1 by @jag (2024-05-20 21:06 UTC)

<p>Hi there, I am trying to convert a .vtp segmentation to a compressed NifTi file. I was able to do it with the Slicer GUI via the following steps:</p>
<ol>
<li>Add data → Choose files → select .vtp file</li>
<li>Right click on the imported model and convert it to a segmentation node</li>
<li>Switch into the Segmentations editor, load the active segmentation, select destination folder, file format as NifTi, select “use compression”, export.</li>
</ol>
<p>These steps work fine in the Slicer GUI, but I need to do this for a significant number of models, and was hoping to write a Python script to automate this process. I’m quite new to the Python-scripting side of Slicer, so am unsure of the Slicer modules I would need to import and use for the steps outlined above. The paths for the input and destination files are not an issue, but translating the Slicer GUI steps to the Slicer API is what I am confused about.</p>
<p>If it helps at all, ideally this program would be executed via <code>Slicer.exe --python-script path/to/script.py</code>.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2024-05-20 22:12 UTC)

<p><a class="mention" href="/u/jag">@jag</a> - there’s some good material on this topic on this forum but it can be hard to find with the default search function so I pasted your question into our experimental chatbot (we don’t expose it to everyone since it costs some money to use).  Have a look at the material below and let us know if it answers your question and if not ask some followups. The links may not be working right but the instructions seem reasonable and you may get further details from google or another chatbot. -Steve</p>
<p><a href="https://discourse.slicer.org/u/claude_3_opus_bot">claude_3_opus_bot</a>Forum Helper</p>
<p>Here are some potentially relevant topics from searching the Slicer discourse forum:</p>
<p><a href="https://discourse.slicer.org/t/converting-model-to-labelmap-for-deep-learning-segmentation/2823">Converting model to labelmap for deep learning segmentation</a> - Discusses converting a model (like VTP) to a segmentation labelmap volume using a Python script in Slicer. Shows example code for going from model node to segmentation node to labelmap volume node.</p>
<p><a href="https://discourse.slicer.org/t/conversion-between-surface-models-and-segmentations/14192">Conversion between surface models and segmentations</a> - Covers converting between model (like VTP surfaces) and segmentation representations using Python scripting. Gives code snippets for various conversion scenarios.</p>
<p><a href="https://discourse.slicer.org/t/segment-editor-manual-tutorial/7465">Segment editor manual/tutorial?</a> - The Segment Editor module is used when converting models to segmentations in the Slicer GUI. This topic links to tutorials and documentation on using the module that may help with understanding the steps to replicate in Python.</p>
<p><a href="https://discourse.slicer.org/t/how-can-i-save-segments-into-a-specific-folder/7045">How can I save segments into a specific folder</a> - Covers saving out segmentations to NRRD/NRRD files from the GUI and has some discussion on specifying output paths that is relevant for automation.</p>
<p>Based on those, here is a rough outline of the key steps in Python:</p>
<ol>
<li>Load the VTP file as a model node using <code>slicer.util.loadModel()</code></li>
<li>Create a new segmentation node</li>
<li>Import the model into the segmentation using <code>segmentationNode.AddSegmentFromClosedSurfaceRepresentation</code></li>
<li>Create a new labelmap volume node</li>
<li>Convert the segmentation to a labelmap and set the labelmap node as the output using <code>segmentationNode.GetBinaryLabelmapRepresentation</code></li>
<li>Set compression and other output options on the labelmap node</li>
<li>Save the labelmap node to a NIFTI file using <code>slicer.util.saveNode()</code></li>
</ol>
<p>The main Slicer Python APIs you’ll need are:</p>
<ul>
<li><code>slicer.util</code> for loading and saving nodes</li>
<li><code>slicer.vtkMRMLModelNode()</code> and <code>slicer.vtkMRMLSegmentationNode()</code> to create model and segmentation nodes</li>
<li>Methods on the <code>vtkMRMLSegmentationNode</code> to convert representations</li>
<li><code>vtkMRMLLabelMapVolumeNode</code> and its compression settings</li>
</ul>
<p>Let me know if you need any other information!</p>

---
