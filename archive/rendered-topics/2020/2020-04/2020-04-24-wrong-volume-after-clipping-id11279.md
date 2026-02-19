---
topic_id: 11279
title: "Wrong Volume After Clipping"
date: 2020-04-24
url: https://discourse.slicer.org/t/11279
---

# Wrong Volume after Clipping

**Topic ID**: 11279
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/wrong-volume-after-clipping/11279

---

## Post #1 by @siaeleni (2020-04-24 02:52 UTC)

<p>Hi all,<br>
I am trying to clip a model and I expect to have a smaller volume after clipping.<br>
I use vtkClipPolyData and vtkImplicitBoolean for clipping (my own way).<br>
Green is the initial input and the blue is the cropped and I expect the volume to be smaller.<br>
As you can see in the image I created the segmentation for both and it seems that I compare the right things. But if you check the Volumes are not correct.</p>
<p>Could you help or give any workaround?<br>
Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b93a2a6dc7621e4ad808e4bf48952bb3d46e1f3.jpeg" data-download-href="/uploads/short-url/6duPZiizMBmneHQRAa413WYuyUb.jpeg?dl=1" title="pic3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b93a2a6dc7621e4ad808e4bf48952bb3d46e1f3_2_690x362.jpeg" alt="pic3" data-base62-sha1="6duPZiizMBmneHQRAa413WYuyUb" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b93a2a6dc7621e4ad808e4bf48952bb3d46e1f3_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b93a2a6dc7621e4ad808e4bf48952bb3d46e1f3_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b93a2a6dc7621e4ad808e4bf48952bb3d46e1f3_2_1380x724.jpeg 2x" data-dominant-color="848599"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic3</span><span class="informations">1910×1003 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/234c69695ee89aa8fbaf16678dd8f8c82270a60f.jpeg" data-download-href="/uploads/short-url/52gqdGxwgR9y5ugulyV7ckHUj7x.jpeg?dl=1" title="pic4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c69695ee89aa8fbaf16678dd8f8c82270a60f_2_690x310.jpeg" alt="pic4" data-base62-sha1="52gqdGxwgR9y5ugulyV7ckHUj7x" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c69695ee89aa8fbaf16678dd8f8c82270a60f_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c69695ee89aa8fbaf16678dd8f8c82270a60f_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/234c69695ee89aa8fbaf16678dd8f8c82270a60f.jpeg 2x" data-dominant-color="EDF1F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic4</span><span class="informations">1094×493 71.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-04-24 03:04 UTC)

<p>Model volume can only be interpreted for closed surfaces. Are your models all closed surfaces?</p>
<p>Are the volumes correct if you import the models into a segmentation and compute the volume of the segment (using Segment Statistics module)?</p>

---

## Post #3 by @siaeleni (2020-04-24 03:33 UTC)

<p>Thanks for your answer.</p>
<p>I used Segment Statistics Module and here are the results<br>
Seems that there is an issue with the “Cutter”. I tried to close it with the following way but I am not sure if that is the right way:</p>
<blockquote>
<p>segmentationNode.CreateClosedSurfaceRepresentation()</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d097179121f97e01f2b0685be61a70fd76162ff.png" data-download-href="/uploads/short-url/1Rkreg68jpT8CNgNsbecaYGc0vZ.png?dl=1" title="pic5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d097179121f97e01f2b0685be61a70fd76162ff.png" alt="pic5" data-base62-sha1="1Rkreg68jpT8CNgNsbecaYGc0vZ" width="689" height="125" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic5</span><span class="informations">1346×245 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-04-24 04:08 UTC)

<p>I don’t know what results do you expect. Did Segment Statistics provide correct results?</p>
<p>It would help if you could upload the scene somewhere and post the link here so that I can have a look.</p>

---

## Post #5 by @siaeleni (2020-04-24 04:13 UTC)

<p>I think I need the ones from Segment Statistics Column C and not Column F.<br>
How can I close the segmentation for the cutter model? I try</p>
<blockquote>
<p>segmentationNode.CreateClosedSurfaceRepresentation()</p>
</blockquote>
<p>but it is not updating anything. But if I will try to close the surface from the “Segmentation” module works.<br>
Do I miss something in the code?</p>

---

## Post #6 by @lassoan (2020-04-24 04:21 UTC)

<p>Segments in a segmentations node are always “closed”, regardless of what representations are used. Calling <code>CreateClosedSurfaceRepresentation()</code> just ensures that closed surface representation is present. Segment statistics computes volume from both labelmap and closed surface representations (you can find more details in the tooltip when you hover the mouse over the table).</p>
<p>If you want to recreate closed surface representation from labelmap representation then make labelmap the master representation and delete and create closed surface representation.</p>

---

## Post #7 by @siaeleni (2020-04-24 04:33 UTC)

<p>Sure, I have uploaded these two files and I expect the cutter to have less Volume.<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="15" height="15">
      <a href="https://www.dropbox.com/sh/nyjcb2uall589du/AACuxDpoNByKpZPl_UZLxuPFa?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/nyjcb2uall589du/AACuxDpoNByKpZPl_UZLxuPFa?dl=0" target="_blank" rel="nofollow noopener">Data</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Hope that helps,<br>
Thanks</p>

---

## Post #8 by @lassoan (2020-04-24 05:02 UTC)

<p>I don’t know how did you close the surface but Segmentation module’s closed surface to labelmap importer closed it correctly, so I would recommend to use that.</p>

---

## Post #9 by @siaeleni (2020-04-24 13:59 UTC)

<p>I use the following code</p>
<pre><code>&gt; def export():
&gt;   segmentationNode = slicer.util.getNode("Cutter-segmentation")
&gt;   segmentationNode.CreateClosedSurfaceRepresentation()
&gt;   segmentation=segmentationNode.GetSegmentation()
&gt;   for segmentIndex in range(segmentation.GetNumberOfSegments()):
&gt;     segmentID = segmentation.GetNthSegmentID(segmentIndex)
&gt;     polydata = vtk.vtkPolyData()
&gt;     segmentationNode.GetClosedSurfaceRepresentation(segmentID, polydata)
&gt;     writer = vtk.vtkSTLWriter()
&gt;     writer.SetInputData(polydata)
&gt;     writer.SetFileName("D:/Cutter1.stl")
&gt;     writer.Update()
</code></pre>
<p>Do I miss something?<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/sh/1xdr5y39x87pq6v/AABuchDT9MURWnO_EesygLiGa?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/1xdr5y39x87pq6v/AABuchDT9MURWnO_EesygLiGa?dl=0" target="_blank" rel="nofollow noopener">Data</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
