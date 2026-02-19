---
topic_id: 23077
title: "Scene Loading Line And Node Error"
date: 2022-04-21
url: https://discourse.slicer.org/t/23077
---

# Scene Loading Line and Node Error

**Topic ID**: 23077
**Date**: 2022-04-21
**URL**: https://discourse.slicer.org/t/scene-loading-line-and-node-error/23077

---

## Post #1 by @rlorenzoni (2022-04-21 19:18 UTC)

<p>Hello,</p>
<p>I have run into the following issue rarely before.  Because of this, I save important (read: time-consuming) segmentations two different ways once I finish.  I saved the Scene and associated files (png, nrrd, etc.) to both a USB and a shared network drive, but I am getting an error message (screenshot below) regardless of which location I open from and trying three different workstations and different versions of Slicer.  The version I used to create the Segmentation is 4.13.0-2021-12-03, but the latest and older versions also return an error.  The png and seg/nrrd files are not corrupted when I open them elsewhere, only the .mrml file seems to be affected.</p>
<p>I looked through the top 50 Support topics with a keyword search and couldn’t find an answer.  I am hoping there is something I can do to restore/access the file.  Please help!  Thanks.</p>
<p>Error Detail:<br>
"- Error: Loading S:/CARD_SHARE/3D Printing/3D Visualization/3D (2022-3-30) - MV - Dextro VA Discord PA iIVC Shunt - CHLA/2022-04-19-Scene.mrml - ERROR: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLStorableNode.cxx, line 322</p>
<p>vtkMRMLScalarVolumeNode (000001201CE5EA70): vtkMRMLStorableNode::UpdateScene failed: Failed to read node 2501: 3D_BTFE_WH (vtkMRMLScalarVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode1.</p>
<ul>
<li>Error: Loading S:/CARD_SHARE/3D Printing/3D Visualization/3D (2022-3-30) - MV - Dextro VA Discord PA iIVC Shunt - CHLA/2022-04-19-Scene.mrml - ERROR: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLStorableNode.cxx, line 322</li>
</ul>
<p>vtkMRMLSegmentationNode (000001201E5E4410): vtkMRMLStorableNode::UpdateScene failed: Failed to read node HeteroTAPVR (vtkMRMLSegmentationNode1) using storage node vtkMRMLSegmentationStorageNode1."</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a02f47fbb8c789bba71bcdde6e513dcd5b13e55.png" alt="image" data-base62-sha1="1qz6za2G3XGsx97Fh4lMkf7Unpr" width="428" height="298"></p>

---

## Post #2 by @lassoan (2022-04-23 05:16 UTC)

<p>A few months ago we added detailed reporting of any potential scene loading and saving errors. This is the main reason you are seeing these errors. From the error messages it is hard to tell if this indicates loading failure of any valid data; or it is just due to presence of storage node that is not used anymore, but for some reason it did not get deleted from the scene.</p>
<p>You can get rid of unused nodes by just loading the files into a clean scene (instead of loading the .mrml or .mrb file).</p>

---

## Post #3 by @rlorenzoni (2022-04-27 16:38 UTC)

<p>Thank you.  Opening a new Slicer window and adding all the non-.mrml files to that scene worked.  I appreciate your help to restore my work…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/911baa606aeb13624b2e159b355e4c6c1f6ea621.jpeg" data-download-href="/uploads/short-url/kHGvooQh3EAFOBgytSUwiYvGihr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/911baa606aeb13624b2e159b355e4c6c1f6ea621_2_311x500.jpeg" alt="image" data-base62-sha1="kHGvooQh3EAFOBgytSUwiYvGihr" width="311" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/911baa606aeb13624b2e159b355e4c6c1f6ea621_2_311x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/911baa606aeb13624b2e159b355e4c6c1f6ea621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/911baa606aeb13624b2e159b355e4c6c1f6ea621.jpeg 2x" data-dominant-color="917790"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">448×720 80.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
