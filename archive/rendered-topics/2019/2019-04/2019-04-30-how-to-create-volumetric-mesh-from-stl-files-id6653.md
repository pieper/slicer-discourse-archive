---
topic_id: 6653
title: "How To Create Volumetric Mesh From Stl Files"
date: 2019-04-30
url: https://discourse.slicer.org/t/6653
---

# How to create volumetric mesh from stl files

**Topic ID**: 6653
**Date**: 2019-04-30
**URL**: https://discourse.slicer.org/t/how-to-create-volumetric-mesh-from-stl-files/6653

---

## Post #1 by @Tarun_Choudhary (2019-04-30 13:53 UTC)

<p>Hi Andras,<br>
Many thanks for your reply. I tried importing stls in 3D slicer as per the instructions you mentioned but I am getting this error message when i click apply button.</p>
<p>Mesh generation using Cleaver is started in working directory: /tmp/Slicer-tarun/SegmentMesher/20190430_130934_055</p>
<p>Error: ‘NoneType’ object has no attribute ‘GetColorNode’</p>
<p>reference link : <a href="https://discourse.vtk.org/t/vtk-polydata-to-imagedata/863/2" rel="nofollow noopener">https://discourse.vtk.org/t/vtk-polydata-to-imagedata/863/2</a></p>

---

## Post #2 by @lassoan (2019-04-30 14:30 UTC)

<p>Could you please copy the contents of the application log? (menu: Help / Report a bug)</p>
<p>Please also try if mesh generation succeeds if you follow steps described in the tutorial: <a href="https://github.com/lassoan/SlicerSegmentMesher/blob/master/README.md#tutorial" rel="nofollow noopener">https://github.com/lassoan/SlicerSegmentMesher/blob/master/README.md#tutorial</a></p>

---

## Post #4 by @Tarun_Choudhary (2019-04-30 14:43 UTC)

<p>The log file is too long so posted only last few lines.</p>

---

## Post #5 by @lassoan (2019-04-30 14:53 UTC)

<p>Could you please upload the log to dropbox/onedrive/google drive and post the link?<br>
Please also try meshing on a simpler data set as described in the tutorial I referenced above.</p>

---

## Post #6 by @Tarun_Choudhary (2019-04-30 15:07 UTC)

<p>The uploaded log file is here:<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1f9A5du8xvI1BRl5eZseeREqDKUXsBpwW/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1f9A5du8xvI1BRl5eZseeREqDKUXsBpwW/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1f9A5du8xvI1BRl5eZseeREqDKUXsBpwW/view?usp=sharing" target="_blank" rel="nofollow noopener">Slicer_27931_20190430_140821.log</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @Tarun_Choudhary (2019-04-30 15:12 UTC)

<p>Hi Andras,</p>
<p>The sample data in the example on the link talks about the scanned image data; I am not using any of the scanned image. My case is different, I have three stl files each having the cad geometry of a component. All three STLs make an assembly. And i want to make a voxel mesh of the assembly with each component having a unique material property.</p>
<p>Kind Regards,<br>
Tarun</p>

---

## Post #8 by @lassoan (2019-04-30 15:18 UTC)

<p>Do you need rectilinear grid? Once you have imported the meshes into a segmentation node, go to Data module, right-click on the segmentation node and click “Export visible segments to binary labelmap”. You can then save the exported labelmap as a 3D volume (in nrrd, mha, … format).</p>

---

## Post #9 by @Tarun_Choudhary (2019-04-30 15:31 UTC)

<p>Hi Andras,</p>
<p>I want to create Unstructured Grid from stls. Let me try this method which you described above.</p>

---

## Post #10 by @Tarun_Choudhary (2019-04-30 15:47 UTC)

<p><a href="https://drive.google.com/file/d/1HN-gBb3zPduAcE1zrKrax7k8QKx5nw9j/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1HN-gBb3zPduAcE1zrKrax7k8QKx5nw9j/view?usp=sharing</a><br>
<a href="https://drive.google.com/file/d/1_SasNmV1LBFIEgy3xxQiMiaVLrlZBofg/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1_SasNmV1LBFIEgy3xxQiMiaVLrlZBofg/view?usp=sharing</a><br>
<a href="https://drive.google.com/file/d/1zIgdYqjZxXqjnbFJEkejfSUzpVTnyK3R/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1zIgdYqjZxXqjnbFJEkejfSUzpVTnyK3R/view?usp=sharing</a><br>
<a href="https://drive.google.com/file/d/19LyzDfYdjOPqGB3cZci1A2jFUvlAKPmB/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/19LyzDfYdjOPqGB3cZci1A2jFUvlAKPmB/view?usp=sharing</a><br>
<a href="https://drive.google.com/file/d/1DLRLOHYuTcAGB5fiKbS-eUlRRwjhJeDM/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1DLRLOHYuTcAGB5fiKbS-eUlRRwjhJeDM/view?usp=sharing</a></p>

---

## Post #11 by @Tarun_Choudhary (2019-04-30 15:49 UTC)

<p>I have shared sample CAD files in form of .vtp (converted from stl). And I want to create voxel mesh of all three in one assembly with three different group of material.</p>

---

## Post #12 by @lassoan (2022-04-06 05:24 UTC)

<p>A post was split to a new topic: <a href="/t/segmentation-from-point-cloud/22843">Segmentation from point cloud</a></p>

---
