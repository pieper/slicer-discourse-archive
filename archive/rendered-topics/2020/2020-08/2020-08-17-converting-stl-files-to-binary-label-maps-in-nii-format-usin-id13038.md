# Converting .stl files to binary label maps in .nii format using Python

**Topic ID**: 13038
**Date**: 2020-08-17
**URL**: https://discourse.slicer.org/t/converting-stl-files-to-binary-label-maps-in-nii-format-using-python/13038

---

## Post #1 by @DC-3T (2020-08-17 08:29 UTC)

<p>Dear all,</p>
<p>I hope you’re doing well. I’ve spent the last week or two struggling to convert a large number of .stl files (~1,000) drawn in 3D Slicer 4.10.2 into .nii binary label maps using Python. The .stl data were derived from segmentations drawn on Dixon MRI .nii data that I’m using as the reference volumes for the conversions. I spent some time working with the example code from the Wiki (<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="nofollow noopener">Documentation</a>), but with little success. Looking through the forum here I found some good tips (e.g. <a href="https://discourse.slicer.org/t/load-a-stl-file-and-save-it-to-a-binary-label-map-through/11315">Load a .stl file and save it to a binary label map</a>), and I came up with the following script:</p>
<pre><code class="lang-auto">stl_list = sys.argv[2:]  # Get list of .stl files
dixon_path = os.path.join(sys.argv[1], 'mDIXONvol.nii.gz')
dixonVolumeNode = slicer.util.loadVolume(dixon_path, returnNode=True)[1]

for stl_file_name in stl_list:
	t = time()

	# Extract abbreviated ROI name from .stl filename	
	stl_name = os.path.splitext(stl_file_name.split("_")[-1])[0]
	
	segmentation = slicer.util.loadSegmentation(stl_file_name, returnNode=True)[1]
	ids = vtk.vtkStringArray()
	segmentation.GetDisplayNode().GetVisibleSegmentIDs(ids)	

	outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
	slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentation, ids, outputLabelmapVolumeNode, dixonVolumeNode)
	slicer.util.saveNode(outputLabelmapVolumeNode, os.path.join(cwd, stl_name + ".nii.gz"))
	print("Converted " + stl_name + ".stl to " + stl_name + ".nii in " + str(round(time() - t, 3)) + "s")
exit()
</code></pre>
<p>Unfortunately, this leads to blank .nii files (all zeros), which becomes apparent when I load the .nii labelmaps in the 3D Slicer GUI. I can’t figure out why this is happening. I do, however, get the following warning during processing:</p>
<pre><code class="lang-auto">CalculateOutputGeometry: No image geometry specified, default geometry is calculated (0.333381665360425;0;0;30.7908134460449;0;0.333381665360425;0;-72.2878036499023;0;0;0.333381665360425;-9.96676349639893;0;0;0;1;0;160;0;179;0;543;)
</code></pre>
<p>I’m not sure why this warning is appearing, given that I’m using the original reference volumes for the conversion. Could there be a coordinate system issue here? I’d really appreciate any insights you might be able to share here.</p>
<p>With gratitude,<br>
Donnie</p>

---

## Post #2 by @lassoan (2020-08-17 12:54 UTC)

<p>The scripts are probably intended for latest Slicer Preview Release. Let us know if you have trouble making them work with that Slicer version.</p>

---

## Post #3 by @DC-3T (2020-08-18 16:11 UTC)

<p>Thanks very much for the tip. Using Slicer 4.11 I’m still getting empty .nii volumes with the script above, but I’ll have another go at the code from the script repository and I’ll report back.</p>

---

## Post #4 by @DC-3T (2020-08-18 16:25 UTC)

<p>Just to give some helpful context, using the ‘Model to LabelMap’ tool in the GUI produces the desired results, so the underlying data appear to be OK.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8196103add5d7cc525a91ba4d7fc24248c3a3581.jpeg" data-download-href="/uploads/short-url/iun6o4jwHhjHE4xxk6PCvledxCN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8196103add5d7cc525a91ba4d7fc24248c3a3581_2_690x242.jpeg" alt="image" data-base62-sha1="iun6o4jwHhjHE4xxk6PCvledxCN" width="690" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8196103add5d7cc525a91ba4d7fc24248c3a3581_2_690x242.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8196103add5d7cc525a91ba4d7fc24248c3a3581_2_1035x363.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8196103add5d7cc525a91ba4d7fc24248c3a3581.jpeg 2x" data-dominant-color="5E5964"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1305×458 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-08-19 02:01 UTC)

<p>This works well for me:</p>
<pre><code class="lang-auto">stl_file_name = ...
output_file_name = ...
reference_volume_path = ...

referenceVolumeNode = slicer.util.loadVolume(reference_volume_path)
segmentationNode = slicer.util.loadSegmentation(stl_file_name)
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, outputLabelmapVolumeNode, referenceVolumeNode)
slicer.util.saveNode(outputLabelmapVolumeNode, output_file_name)
</code></pre>
<p>Try this and if it works for you, too, then start modifying it line-by-line to see where it goes wrong.</p>

---

## Post #6 by @DC-3T (2020-08-19 10:17 UTC)

<p>Thanks very much for the code. I gave it a try, and I’m still getting the following message: “CalculateOutputGeometry: No image geometry specified, default geometry is calculated”. The output volume is still just an array of zeros as well. I’m not sure why this happens, and I’ve confirmed that the reference volumes and models are all loaded correctly…</p>
<p>I was, however, able to get the example code from the script repository to work in Slicer 4.11, after some modifications. Here is my working code:</p>
<pre><code class="lang-auto">referenceVolumeNode = slicer.util.loadVolume(ref_volume)
inputModel = slicer.util.loadModel(stl_file)

# Convert model to labelmap
seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
seg.CreateBinaryLabelmapRepresentation()
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)

# Set image directions to correct flip L-R issue
imageDirections = [[-1,0,0], [0,1,0], [0,0,1]] 
outputLabelmapVolumeNode.SetIJKToRASDirections(imageDirections)
	
slicer.util.saveNode(outputLabelmapVolumeNode, "seg.nii.gz"))
</code></pre>
<p>Aside from the unexpected left-right flip, which I’ve corrected here, the code works like a charm. Thanks very much for your help!</p>

---

## Post #7 by @lassoan (2020-08-19 12:56 UTC)

<p>Thanks for sharing the script that worked for you. Probably the very latest Slicer Preview Release (that you download today or later) would work with the shorter script I provided (<a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> pushed a fix for properly handling STL files in either RAS or LPS coordinate system).</p>

---

## Post #8 by @DC-3T (2020-09-02 15:40 UTC)

<p>Sorry for the slow reply. I downloaded the latest Slicer Preview Release (2020-09-01) to test the shorter script you provided and the code now works! The “CalculateOutputGeometry: No image geometry specified, default geometry is calculated” message still appears, but the resulting label maps are perfect, and do not exhibit the left-right flip I mentioned above. Thanks again for your help with this issue.</p>

---

## Post #9 by @rohand24 (2021-07-15 17:42 UTC)

<p>Hi,</p>
<p>Thank you for this thread. I am able to convert my Model ‘.stl’ files to Segmentations ‘.seg.nrrd’ files.<br>
I am not facing the direction related issue. But I wanted to know how to set the Segmentation labelmap geometry using python code, rather than using Segment Editor in GUI.</p>
<p>My Code -</p>
<p>referenceVolumeNode = slicer.mrmlScene.GetFirstNodeByClass(‘vtkMRMLScalarVolumeNode’) <span class="hashtag-raw">#Gets</span> the already loaded DICOM Volume<br>
inputModel = slicer.util.loadModel(model_filepath) # .stl filepath</p>
<p>seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)<br>
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)<br>
seg.CreateBinaryLabelmapRepresentation()<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, labelmapVolumeNode, referenceVolumeNode)</p>
<p>slicer.util.saveNode(referenceVolumeNode, output_volume_filepath))<br>
slicer.util.saveNode(seg, output_segmentation_filepath)</p>
<p>My segmentation geometry is currently:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bd1f1bee5bf5f5bc0333e141439caa602eca5fb.png" alt="image" data-base62-sha1="d6hfIdRYt9eoRGZid2lZ5wX7VEL" width="490" height="373"></p>
<p>I need to set my segmentation geometry to this, using python script code.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d555a028357f93abb5493eb0b71d88b7c365d44.png" alt="image" data-base62-sha1="6t2lLKvkKexIY5qNJHJPazJUdmc" width="490" height="373"></p>
<p>Kindly help.</p>
<p>Thank you.</p>

---

## Post #10 by @lassoan (2021-07-15 18:28 UTC)

<p>See a complete example for specifying segmentation geometry in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">script repository</a>.</p>

---

## Post #11 by @lassoan (2023-02-18 04:54 UTC)

<p>A post was merged into an existing topic: <a href="/t/stl-file-stores-the-annotation-results-of-ct-data-and-i-want-to-convert-it-to-nii-format-for-deep-learning/27898/2">stl file stores the annotation results of CT data, and I want to convert it to nii format for deep learning.</a></p>

---

## Post #12 by @xiaoli (2024-07-15 06:10 UTC)

<p>Hello sir, I don’t know if you have time, but I would like to ask you a question.<br>
After converting STL data to Nii.gz data, my own STL file was complete, but I found that many neural tubes were broken after conversion. I don’t know how to reduce this kind of breakage. Do you have a good solution</p>

---

## Post #13 by @sajad_amiri (2024-08-25 20:29 UTC)

<p>Hello friends,<br>
I have a folder containing STL masks of lesions from my dataset, and I want to extract Radiomics features. Should I first convert the STLs to binary masks? If it’s not necessary to convert them for feature extraction, please let me know how to extract features directly from STL files and a reference image. I would greatly appreciate a Python code for batch processing rather than single-image mode. Thank you!</p>

---
