# Get 3d model segmentations for 2d tracked images

**Topic ID**: 33916
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/get-3d-model-segmentations-for-2d-tracked-images/33916

---

## Post #1 by @pfrwilson (2024-01-22 18:47 UTC)

<p>I am using slicer to display tracked 2d ultrasound images of the prostate. My data consists of sequence browser nodes controlling the 2D image data and tracking transformation.</p>
<p>By creating a 3d volume reconstruction, segmenting it, converting to binary labelmap and using the model maker module, I have a 3d model node of the prostate. I also have several needle models indicating the location of several biopsies. The needle models observe transforms to get them into the correct position in 3d.</p>
<p>Now i’d like to export the 2d ultrasound images along with the intersection between the prostate and the needle as masks. Basically at every timestep in the sequence browser i’d like to be able to export the 3 2d images: the ultrasound image pixels, the prostate intersection for that slice as binary mask, and the needle intersection for that slice as binary mask.</p>
<p>So far, I have tried using the “convert model to segmentation node” feature, then used the following idea:</p>
<pre data-code-wrap="python"><code class="lang-python">referenceVolume = getNode("Tracked2dUltrasoundData")
segmentationNode = getNode("ProstateSegmentation")
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)
</code></pre>
<p>to try to create a label map node with the same geometry as the 2d image containing the mask intersections. However, there is no luck - following these lines of code the labelmapVolumeNode will be observing the same transform as the 2d image but it will be empty, i.e. no intersection.</p>
<p>Any advice on how to proceed from here?</p>
<p>Thanks,</p>
<p>Paul</p>

---

## Post #2 by @lassoan (2024-01-23 23:21 UTC)

<p>The code snippet looks OK. Could you please provide an example scene that we can try it on? (upload to somewhere and post the link here, make sure no patient information is included)</p>

---

## Post #3 by @pfrwilson (2024-02-02 18:48 UTC)

<p>Hi Andras,</p>
<p>I have uploaded a slicer scene here:</p>
<p><a href="https://drive.google.com/drive/folders/1rx7WYvwej2zvAaG6-QWcAH3clJMdg1Xv?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1rx7WYvwej2zvAaG6-QWcAH3clJMdg1Xv?usp=sharing</a><br>
However, i’m not sure if it will load properly because it depends on an external module. In any case, you should be able to load the prostate model (<code>ProstateModel</code>), the segmentation I generated from the model (<code>ProstateModel-segmentation</code>), and the cineloop <code>BMode_8</code> with observes a chain of transforms and can be played back using the <code>SequenceBrowser_8</code>.</p>
<p>The following lines:</p>
<pre data-code-wrap="python"><code class="lang-python"># (1) 
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "NewLabelMap")
segmentationNode = getNode("ProstateModel-segmentation")
referenceVolumeNode = getNode("BMode_8")
 slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)
</code></pre>
<p>Did not work - the NewLabelMap array has a sum of 0 indicating that no pixels were filled despite having a clear overlap with the segmentation. However, when I don’t observe the tracking transform, the function works as expected, e.g:</p>
<pre data-code-wrap="python"><code class="lang-python"># (2)
referenceNode.SetAndObserveTransformNodeID(None)
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)
</code></pre>
<p>In this case the label map is filled in, although with the refrence volume being in a nonsense coordinate system. This leads me to believe that the issue is in the transform being observed by the reference volume. Note that after running code example (1), <code>labelmapVolumeNode</code> is now observing the transform that the reference volume was observing.</p>
<p>Let me know if you have any insight as to what the problem is here.</p>
<p>Paul</p>

---
