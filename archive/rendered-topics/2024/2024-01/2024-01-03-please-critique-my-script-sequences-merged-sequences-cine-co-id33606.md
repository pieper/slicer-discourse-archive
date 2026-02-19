---
topic_id: 33606
title: "Please Critique My Script Sequences Merged Sequences Cine Co"
date: 2024-01-03
url: https://discourse.slicer.org/t/33606
---

# Please critique my script : sequences, merged sequences, CINE, color, opacity, .mrb

**Topic ID**: 33606
**Date**: 2024-01-03
**URL**: https://discourse.slicer.org/t/please-critique-my-script-sequences-merged-sequences-cine-color-opacity-mrb/33606

---

## Post #1 by @Deep_Learning (2024-01-03 16:42 UTC)

<p>Below is a script that I am using to save CINE CTA volumes and segmentations as an mrb. Def works!!! Provides custom color and opacity. Plays as CINE.</p>
<p>Looking for any performance improvements. Memory improvements.</p>
<p>My subject hierarchy looks good. Below with 1 timepoint.<br>
I am concerned that I have two segmentation sequences and two volume sequences in All nodes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71ba6986123f8ff198f17c8098b19e787f8908d.png" data-download-href="/uploads/short-url/nQiYHtc5GF7lR2YzweSUOIutm57.png?dl=1" title="Screenshot from 2024-01-03 10-52-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a71ba6986123f8ff198f17c8098b19e787f8908d_2_690x175.png" alt="Screenshot from 2024-01-03 10-52-14" data-base62-sha1="nQiYHtc5GF7lR2YzweSUOIutm57" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a71ba6986123f8ff198f17c8098b19e787f8908d_2_690x175.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71ba6986123f8ff198f17c8098b19e787f8908d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71ba6986123f8ff198f17c8098b19e787f8908d.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-01-03 10-52-14</span><span class="informations">727×185 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b513c7b715d46023d19d02d2a4181ead8f6b0103.png" alt="Screenshot from 2024-01-03 10-53-14" data-base62-sha1="pPSNEEWTHauqF4giSKZVjQGB0nV" width="619" height="291"></p>
<pre><code class="lang-auto">import slicer  # Import slicer module

# Default Medical Record Number (MRN)
mrn='123456'

def saveMRB(mrn=mrn):
   """
   Save the scene to a file named after the MRN in an anonymized directory.
   """
   anonymized_save_directory = "/path/to/save/directory/"  # Anonymized directory path
   sceneSaveFilename = f"{anonymized_save_directory}{mrn}.mrb"
   slicer.util.saveScene(sceneSaveFilename)

# Anonymized directory paths for image and segmentation data


anonymized_img_directory = "/path/to/image/directory/"
anonymized_seg_directory = "/path/to/segmentation/directory/"



# Process each MRN
try:
   print("Processing MRN: ", mrn)

   dir_img = anonymized_img_directory
   dir_seg = anonymized_seg_directory
   seg_prefix = "_v10 "

   # Variables for segmentation color and opacity settings
   vars_name = [var1,…]  # 18
   vars_color = {var1: [1, 1, 1], … }
   op1 = 0.4
   vars_opacity = {var1: 1, }

   # Create sequence nodes for volume and segmentation
   volumeSequenceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "Volume sequence")
   segmentationSequenceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "Segmentation sequence")
   mergedSequenceBrowserNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceBrowserNode", "Merged")

   for count in range(10):  # Adjust the range as needed
       print("Timepoint: ", count)
        # = getNode(f"{mrn}_{str(count).zfill(3)}_0000")
       volumeNode =slicer.util.loadVolume(f"{dir_img}{mrn}/{mrn}_{str(count*5).zfill(3)}_0000.nii.gz")
       volumeSequenceNode.SetDataNodeAtValue(volumeNode, str(count))

       segmentationNode = slicer.util.loadSegmentation(f"{dir_seg}{mrn}{seg_prefix}/{mrn}_{str(count*5).zfill(3)}.nii.gz")
       displayNode = segmentationNode.GetDisplayNode()
       displayNode.SetOpacity3D(1.0)
       segmentation = segmentationNode.GetSegmentation()

       for count_seg in range(18):
           sourceSegmentName = "Segment_" + str(count_seg + 1)
           sourceSegmentId = segmentation.GetSegmentIdBySegmentName(sourceSegmentName)
           if sourceSegmentId:
               segment = segmentation.GetSegment(sourceSegmentId)
               segment.SetName(vars_name[count_seg])
               segment.SetColor(vars_color[vars_name[count_seg]][0], vars_color[vars_name[count_seg]][1], vars_color[vars_name[count_seg]][2])
               segmentation.SetConversionParameter("Smoothing factor", "0.15")

       segmentationNode.CreateClosedSurfaceRepresentation()
       segmentationSequenceNode.SetDataNodeAtValue(segmentationNode, str(count))
       slicer.mrmlScene.RemoveNode(segmentationNode.GetDisplayNode())
       slicer.mrmlScene.RemoveNode(segmentationNode)

   mergedSequenceBrowserNode.AddSynchronizedSequenceNode(segmentationSequenceNode)
   mergedSequenceBrowserNode.SetSaveChanges(segmentationSequenceNode, True)
   mergedSequenceBrowserNode.AddSynchronizedSequenceNode(volumeSequenceNode)
   mergedSequenceBrowserNode.SetSaveChanges(volumeSequenceNode, True)
   slicer.modules.sequences.toolBar().setActiveBrowserNode(mergedSequenceBrowserNode)
   mergedProxyNode = mergedSequenceBrowserNode.GetProxyNode(segmentationSequenceNode)
   slicer.util.setSliceViewerLayers(foreground=mergedProxyNode)
   mergedProxyNode = mergedSequenceBrowserNode.GetProxyNode(volumeSequenceNode)
   slicer.util.setSliceViewerLayers(background=mergedProxyNode)

   v = slicer.util.getNode('View1')
   v.SetBoxVisible(False)
   v.SetAxisLabelsVisible(False)

   layoutManager = slicer.app.layoutManager()
   threeDWidget = layoutManager.threeDWidget(0)
   threeDView = threeDWidget.threeDView()
   threeDView.resetFocalPoint()

   sequenceProxyNode = mergedSequenceBrowserNode.GetProxyNode(segmentationSequenceNode)
   segmentationSequenceDisplayNode = sequenceProxyNode.GetDisplayNode()

   for count_seg in range(18):
       sourceSegmentName = "Segment_" + str(count_seg + 1)
       segmentationSequenceDisplayNode.SetSegmentOpacity3D(sourceSegmentName, vars_opacity[vars_name[count_seg]])

   saveMRB(mrn)

except Exception as e:
   print("Error processing MRN", mrn, ":", e)
   slicer.mrmlScene.Clear(0)



</code></pre>

---

## Post #2 by @mikebind (2024-01-03 17:50 UTC)

<p>Regarding the apparent duplication of the sequences, check the mrml node type on each of those (there’s a “Show MRML ID’s” checkbox below the list).  I suspect one of the duplicates is the actual sequence node, and the other is the proxy node, and they just have the same name.</p>

---
