# Multiply two images using "Multiply Scalar Volumes" or "Mask Scalar Volume" and save the resulting image (using Python)

**Topic ID**: 10947
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/multiply-two-images-using-multiply-scalar-volumes-or-mask-scalar-volume-and-save-the-resulting-image-using-python/10947

---

## Post #1 by @Vishal_P (2020-03-31 20:49 UTC)

<p>I am a beginner trying to automate some tasks in 3D Slicer using Python.</p>
<p>I have a mask image and another input volume image both in nifti format.<br>
how can I use python to automate the multiplication between two images and save the output to a folder?</p>
<p>so far I was able to load the two images.</p>
<pre><code class="lang-python">slicer.mrmlScene.Clear(False)
[success, volume] = slicer.util.loadVolume(filename = 'stripped_AX_FLAIR_stretched.nii',returnNode=True) 
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)
[success, labelmapVolumeNode] = slicer.util.loadLabelVolume(filename = 'Edema_AX_FLAIR_label.nii', returnNode=True)
</code></pre>

---

## Post #2 by @lassoan (2020-04-01 02:28 UTC)

<p>You can use <code>arrayFromVolume</code> function as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Combine_multiple_volumes_into_one">example in the script repository</a>.</p>

---

## Post #3 by @Vishal_P (2020-04-01 21:01 UTC)

<p>Thanks for the reply Lasso, Certainly this is the way to proceed. but while executing the script. i get an error that the segment volume dimension is not aligned.</p>
<p>“”"<br>
ValueError: shapes (26,512,512) and (13,179,150) not aligned: 512 (dim 2) != 179 (dim 1)</p>
<p>“”"<br>
what can i do to overcome this error?</p>

---

## Post #4 by @lassoan (2020-04-01 21:32 UTC)

<p>It seems that the two volumes have different sizes. How did you create them?</p>

---

## Post #5 by @Vishal_P (2020-04-01 21:52 UTC)

<p>initially, I had a master_volume file and a label_file (which contains multiple labels).</p>
<p>to extract segment_volumes of each individual label from the label_file, I separated each label from label_file using the segment editor module and converted them back to individual label files and saved them to my folder directory.<br>
(this process has been executed completely in Python)</p>
<p>Currently, I am trying to automate the task of masking the individual labels (extracted from label_file) on to the master_volume to extract the segment_volumes using python and save them as a nifti file.</p>
<p>for example<br>
the first image is the individual label separated from label_file.<br>
the second image is the result when masked with master_volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d836eeeb815ccc4ceecf028fd60a60d0175995.png" data-download-href="/uploads/short-url/sNBcY2DnkcCuSd4yjaSBtsC8HHv.png?dl=1" title="Screen Shot 2020-03-23 at 4.07.37 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d836eeeb815ccc4ceecf028fd60a60d0175995.png" alt="Screen Shot 2020-03-23 at 4.07.37 PM" data-base62-sha1="sNBcY2DnkcCuSd4yjaSBtsC8HHv" width="552" height="500" data-dominant-color="0A0E0A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-03-23 at 4.07.37 PM</span><span class="informations">1200×1086 993 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-04-01 22:46 UTC)

<aside class="quote no-group" data-username="Vishal_P" data-post="5" data-topic="10947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vishal_p/48/6438_2.png" class="avatar"> Vishal_P:</div>
<blockquote>
<p>to extract segment_volumes of each individual label from the label_file, I separated each label from label_file using the segment editor module and converted them back to individual label files and saved them to my folder directory.</p>
</blockquote>
</aside>
<p>This should not be necessary. Instead, <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node">export the segmentation to labelmap volume</a> (you can specify the volume node that you want to combine it with as reference volume) and then this exported labelmap volume will have the correct geometry. Using numpy, you can very easily extract a single label value, combine it with another array, etc.</p>

---

## Post #7 by @Vishal_P (2020-04-02 01:21 UTC)

<p>i am using slicer 4.10.2<br>
in MacOS Catalina</p>
<pre><code class="lang-auto">seg_node = slicer.vtkMRMLSegmentationNode()
        slicer.mrmlScene.AddNode(seg_node)
        seg = seg_node.GetSegmentation()
        seg.CopySegmentFromSegmentation(segmentation,segmentation.GetNthSegmentID(i))
        lab_node = slicer.vtkMRMLLabelMapVolumeNode()
        slicer.mrmlScene.AddNode(lab_node)
        slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg_node,lab_node,volume)
</code></pre>
<p>the code works fine till i reach the last line, when i execute ExportVisibleSegmentsTo LabelMapNode, my jupyter notebook kernel dies and 3d slicer crashes giving me a prompt to reopen 3d slicer.</p>

---

## Post #8 by @Vishal_P (2020-04-02 03:12 UTC)

<p>Got the desired result using “ExportSegmentsToLabelmapNode” and by declaring “reference volume” dimensions are preserved.<br>
As the dimensions are equal now, I was able to perform the multiplication operation.</p>
<p>Thanks for your guidance…! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>arr_vt = vtk.vtkStringArray()<br>
arr_vt.InsertNextValue(segmentation.GetNthSegmentID(0))<br>
result = arr_vt.GetValue(0)<br>
print(result)</p>
</blockquote>
<blockquote>
<p>slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg_node,arr_vt,lab_node,volume)</p>
</blockquote>
<blockquote>
<p>vol_1=slicer.util.getNode(‘str*’)<br>
vol_2=slicer.util.getNode(‘LabelMapVolume’)<br>
a = slicer.util.arrayFromVolume(vol_1)<br>
b = slicer.util.arrayFromVolume(vol_2)<br>
c = a * b</p>
</blockquote>
<blockquote>
<p>volumeNode_result = slicer.modules.volumes.logic().CloneVolume(volume, “multiply”)<br>
slicer.util.updateVolumeFromArray(volumeNode_result, c)<br>
setSliceViewerLayers(background=volumeNode_result)</p>
</blockquote>

---

## Post #9 by @Ramadhan_Gunia (2022-07-26 20:14 UTC)

<p>Hello, kindly assist me with the whole code you used to solve the problem “[Multiply two images using “Multiply Scalar Volumes” or “Mask Scalar Volume” and save the resulting image (using Python)”</p>

---
