---
topic_id: 44922
title: "Recreating Segmentation From 3D Models"
date: 2025-10-30
url: https://discourse.slicer.org/t/44922
---

# Recreating segmentation from 3D models

**Topic ID**: 44922
**Date**: 2025-10-30
**URL**: https://discourse.slicer.org/t/recreating-segmentation-from-3d-models/44922

---

## Post #1 by @muratmaga (2025-10-30 19:42 UTC)

<p>Let’s say I have the original volume, and the segmentation object saved as a 3D model (like ply)  on the disk, but not the actual seg.nrrd file.</p>
<p>What is the suggested operation to reconstitute the segmentation map close to the original detail for further edits?</p>

---

## Post #2 by @mau_igna_06 (2025-11-01 01:19 UTC)

<p>According to this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day1_4_SegmentationBasics.pptx" rel="noopener nofollow ugc">document</a> (slide N° 5), you should be able to convert back and forward from labelmap representation to surface representation without any information loss</p>

---

## Post #3 by @muratmaga (2025-11-01 01:37 UTC)

<p>That’s what I thought, but wasn’t able to discover a way to do so. I tried creating a empty segment from the source volume I used to generate the model, and then use the import/export feature of the segmentations module to import the model into that blank segment use a labelmap.</p>
<p>Unfortunately, that’s not the same resolution at all, it ended up being fairly low res.</p>

---

## Post #4 by @mau_igna_06 (2025-11-01 01:42 UTC)

<p>According to this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files" rel="noopener nofollow ugc">example</a>, it may be compulsory to set the geometry information for the segmentation</p>

---

## Post #5 by @muratmaga (2025-11-01 01:44 UTC)

<p>That’s the part I am confused about. By creating a blank segmentation from the source volume, I assumed that the imported segmentation will inherit that geometry, but that’s not what I am seeing in experience.</p>
<p>Also for 3D models import/export feature of the Segmentations does not have a setting where you can put a reference volume to get the geometry from.</p>
<p>I must be overlooking something…</p>

---

## Post #6 by @pieper (2025-11-01 12:03 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> can you share a concrete example (a volume and model) and describe the steps you take?  At first I thought you were asking about registering the model to the volume, but I guess you are more concerned about the resolution of the rasterized model?</p>

---

## Post #7 by @muratmaga (2025-11-01 18:00 UTC)

<p>It boiled down from which stage the models were exported. If you kept the smoothing option on when you enabled the Show 3D button, and then export the model, you irrecoverably lost detail.</p>
<ol>
<li>Download the CTChest sample data, and segment bones (threshold 165-Max, closing filter 5, island tool to keep the largest island). Save the segmentation as seg.nrrd</li>
<li>Turn off smoothing in Show 3D button, then right-click on the segment in SH and export this segmentation as a model, export the model as ply.</li>
<li>Repeat the <span class="hashtag-raw">#2</span> but smoothing enabled (with default 0.5)</li>
<li>Reset the scene, reload the model the and the CT volume into the scene and try to create a high-resolution segmentation out these models.</li>
</ol>
<p>When import <span class="hashtag-raw">#3</span> it is lower resolution than the labelmap generated from <span class="hashtag-raw">#2</span>. In fact for me the import step <span class="hashtag-raw">#2</span> is 3-4 times longer than the one with smoothing enabled. You will see the difference in the labelmaps, not much for this low resolution sample data, but enough for us to make a difference for landmarking certain faint structures on dry bones such cranial sutures or small protuberances.</p>
<p>Unfortunately for this data, I think they were all exported with smoothing enabled, so I can’t find a way to generate higher detailed labelmaps version from them.</p>

---

## Post #8 by @chir.set (2025-11-01 20:20 UTC)

<p>The code below creates a new segmentation, updates its geometry sampling with the volume node and imports a model. There are more details with the test CT-chest volume, following the steps you described. The difference appears when the Show 3D button is deactivated/activated in the segment editor, whether the code is run or the model is imported in the Data module. The difference is even more important if the model has been saved without 3D smoothing.</p>
<p>I have no idea how far it may be helpful to you.</p>
<pre><code class="lang-auto">def createSegmentationWithGeometryAndImportModel():
  volume = getNode("CT-chest")
  segmentation = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
  segmentation.CreateDefaultDisplayNodes()
  segmentation.SetReferenceImageGeometryParameterFromVolumeNode(volume)

  segGeomLogic = slicer.vtkSlicerSegmentationGeometryLogic()
  segGeomLogic.SetInputSegmentationNode(segmentation)
  segGeomLogic.SetSourceGeometryNode(volume)
  segGeomLogic.CalculateOutputGeometry()
  segGeomLogic.ResampleLabelmapsInSegmentationNode()
  segGeomLogic.SetReferenceImageGeometryInSegmentationNode()
  
  model = getNode("SmoothedPLY") # NoSmoothedPLY afterwards.
  segLogic = slicer.modules.segmentations.logic()
  segLogic.ImportModelToSegmentationNode(model, segmentation)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69587e2cb1a29420ffbb75049ac3ace69b1d99b2.gif" alt="ImportModel" data-base62-sha1="f1VJebe2TFOjrFpQpi7LkM4ppCy" width="690" height="414" class="animated"></p>

---
