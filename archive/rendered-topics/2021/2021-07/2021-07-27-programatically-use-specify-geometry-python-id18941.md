---
topic_id: 18941
title: "Programatically Use Specify Geometry Python"
date: 2021-07-27
url: https://discourse.slicer.org/t/18941
---

# Programatically use "Specify Geometry" (Python)

**Topic ID**: 18941
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/programatically-use-specify-geometry-python/18941

---

## Post #1 by @Alex_Vergara (2021-07-27 10:06 UTC)

<p>Hello</p>
<p>I want to control programatically this option “Specify Geometry”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/434d93e8bd11758b4afb46f337a8f9aea13ea480.png" data-download-href="/uploads/short-url/9BocphBkSB4SVBXU3CEHHSsbaTu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/434d93e8bd11758b4afb46f337a8f9aea13ea480_2_690x368.png" alt="image" data-base62-sha1="9BocphBkSB4SVBXU3CEHHSsbaTu" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/434d93e8bd11758b4afb46f337a8f9aea13ea480_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/434d93e8bd11758b4afb46f337a8f9aea13ea480.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/434d93e8bd11758b4afb46f337a8f9aea13ea480.png 2x" data-dominant-color="3C3F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">770×411 54.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Basically reassign a new source volume to the segmentation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbb55177f454b7b9e7c9dd87d6ca9bd3e54044d0.png" alt="image" data-base62-sha1="t45oJSnaRK9qBy2yRJqBbaKAhQQ" width="614" height="301"></p>
<p>I have tried to use</p>
<pre data-code-wrap="python"><code class="lang-python">            newsegmNode = shNode.GetItemDataNode(newsegmID)
            newsegmNode.SetReferenceImageGeometryParameterFromVolumeNode(
                DERSNode.data)
            newsegmNode.CreateDefaultDisplayNodes()
            newsegmNode.CreateBinaryLabelmapRepresentation()
</code></pre>
<p>But it just changes the Master Volume, not the source volume. I want the segmentation to be revoxelized in the new source volume.</p>
<p>Is there a way to achieve this?</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2021-07-27 18:58 UTC)

<p>If you already have a binary labelmap then setting a reference image geometry will have no effect.</p>
<p>One option is to create closed surface representation, delete the binary labelmap representation, then create binary labelmap representation (it will be generated from the closed surface representation, using the reference image geometry).</p>
<p>Another option is to resample the labelmap representation as it is done <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationGeometryWidget.cxx#L495-L517">here</a>. I’ll add this code as a method to the <code>vtkSlicerSegmentationGeometryLogic</code> class to make it more easily accessible from Python.</p>

---

## Post #3 by @Alex_Vergara (2021-07-28 08:27 UTC)

<p>OK, I have tried the first approach</p>
<pre><code class="lang-python">newsegmNode.CreateClosedSurfaceRepresentation()
newsegmNode.GetSegmentation().SetMasterRepresentationName(closedSurfaceReprName)
newsegmNode.SetReferenceImageGeometryParameterFromVolumeNode(DERSNode.data)
newsegmNode.CreateBinaryLabelmapRepresentation()
newsegmNode.GetSegmentation().SetMasterRepresentationName(binaryLabelmapReprName)
</code></pre>
<p>But it doesn’t worked, it still has the old voxelization, is there something wrong here in this code snippet?</p>

---

## Post #4 by @lassoan (2021-07-28 12:36 UTC)

<p>You missed the step of deleting the labelmap representation.</p>

---

## Post #5 by @Alex_Vergara (2021-07-29 08:33 UTC)

<p>I though that setting the master representation would delete any other representation. OK I have tried this</p>
<pre><code class="lang-python">newsegmNode.CreateClosedSurfaceRepresentation()
newsegmNode.GetSegmentation().SetMasterRepresentationName(closedSurfaceReprName)
newsegmNode.RemoveBinaryLabelmapRepresentation()
newsegmNode.SetReferenceImageGeometryParameterFromVolumeNode(DERSNode.data)
newsegmNode.CreateBinaryLabelmapRepresentation()
newsegmNode.GetSegmentation().SetMasterRepresentationName(binaryLabelmapReprName)
</code></pre>
<p>But still no success, I mean the master representation has changed, but<br>
doing with the code I get these volumes</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Segment</th>
<th>Number of voxels [voxels]</th>
<th>Volume [cm3]</th>
</tr>
</thead>
<tbody>
<tr>
<td>1-Anterior</td>
<td>758</td>
<td>65.3669</td>
</tr>
<tr>
<td>2-Lateral</td>
<td>80</td>
<td>6.89889</td>
</tr>
<tr>
<td>3-Posterior</td>
<td>220</td>
<td>18.9719</td>
</tr>
<tr>
<td>4-Inferior</td>
<td>137</td>
<td>11.8143</td>
</tr>
</tbody>
</table>
</div><p>Now doing it manually I get (the correct values)</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Segment</th>
<th>Number of voxels [voxels]</th>
<th>Volume [cm3]</th>
</tr>
</thead>
<tbody>
<tr>
<td>1-Anterior</td>
<td>788</td>
<td>67.954</td>
</tr>
<tr>
<td>2-Lateral</td>
<td>113</td>
<td>9.74468</td>
</tr>
<tr>
<td>3-Posterior</td>
<td>254</td>
<td>21.904</td>
</tr>
<tr>
<td>4-Inferior</td>
<td>165</td>
<td>14.229</td>
</tr>
</tbody>
</table>
</div>

---

## Post #6 by @lassoan (2021-08-03 16:31 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="5" data-topic="18941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Now doing it manually I get (the correct values)</p>
</blockquote>
</aside>
<p>What steps do you do manually and how?</p>

---

## Post #7 by @Alex_Vergara (2021-08-04 13:16 UTC)

<p>click on specify geometry<br>
select a diferent node<br>
click OK</p>
<p>Usually the new node has been modified by registration so I need the segmentation to account for the grid deformation</p>

---

## Post #8 by @Alex_Vergara (2021-08-12 12:36 UTC)

<p>OK, I will describe more the steps</p>
<p>take two (n&gt;1 actually but lets take 2 for simplicity) same patient CT, obtained at different  days, segment a structure in one of them.<br>
Purpose: obtain the volume evolution in time of the structure.</p>
<ul>
<li>
<p>Option 1:<br>
Segment the same structure in the second CT.<br>
Advantage: Each segmentation has the geometry of the respective time CT<br>
Disadvantage: Not scalable for many time points and many structures</p>
</li>
<li>
<p>Option 2:<br>
Segment in the first CT; Elastic transform the second; measure<br>
Advantage: Easily scalable<br>
Disadvantage: The volume does not change in time because the original segmentation is not recalculated for the geometry of the rest of the time points</p>
</li>
<li>
<p>Option 3:<br>
Segment in the first CT; get the elastic transformation without modifying the second; get the inverse of that transformation and apply to the respective segmentation; measure<br>
Advantage: Easily scalable<br>
Disadvantage: The volume does not change in time because the original segmentation is not recalculated for the geometry of the rest of the time points</p>
</li>
</ul>
<p>I tried to do options 2 and 3 without success, because the lines above doesn’t produce the same result as the option 1 (I can live with some % difference due to difference in segmentation, but not more than 20% as showed).<br>
Doing the master geometry change manually does the trick in both 2 and 3 as showed. So I need to reproduce this programatically.</p>

---

## Post #9 by @lassoan (2021-08-12 18:09 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="8" data-topic="18941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Disadvantage: The volume does not change in time because the original segmentation is not recalculated for the geometry of the rest of the time points</p>
</blockquote>
</aside>
<p>Do you mean that you use Segment Statistics to compute the volume, but the transform is only taken into account if you harden it?</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="8" data-topic="18941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Doing the master geometry change manually does the trick in both 2 and 3 as showed. So I need to reproduce this programatically.</p>
</blockquote>
</aside>
<p>In recent Slicer Preview Releases, you can use <a href="https://github.com/Slicer/Slicer/blob/1a692bf36e9c99c47661fbf5fdba0fd3c3e72f95/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationGeometryLogic.h#L63">vtkSlicerSegmentationGeometryLogic::ResampleLabelmapsInSegmentationNode</a> method to resample the labelmap. However, in recent Slicer Preview Releases, Segment Statistics module already hardens any transforms on a copy of the segmentation node, so the volume computation should be correct.</p>

---

## Post #10 by @Edgaras_Misiulis (2022-09-12 07:47 UTC)

<p>Hello,</p>
<p>how to access the<br>
vtkSlicerSegmentationGeometryLogic<br>
and ResampleLabelmapsInSegmentationNode from python?</p>
<p>Thank you</p>

---

## Post #11 by @Edgaras_Misiulis (2022-09-12 08:49 UTC)

<p>found a good example about it here:</p>
<aside class="quote quote-modified" data-post="5" data-topic="19025">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pj_yu/48/11851_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/change-segmentation-oversampling-factor/19025/5">Change segmentation oversampling factor</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your help again! 
The source code of vtkSlicerSegmentationGeometryLogic::ResampleLabelmapsInSegmentationNode is really helpful, and I finally completed this function correctly based on the source code. The issues aren’t technical issues, and since it works right now, there’s no needs to worry about upgrading. 
For those who are interested, here is my code. 
segmentIDs = vtk.vtkStringArray()
segmentationNode.GetSegmentation().GetSegmentIDs(segmentIDs)

#Create desired geometry…
  </blockquote>
</aside>


---

## Post #12 by @AnabelVazquez (2024-06-24 10:39 UTC)

<p>Hi,</p>
<p>I have a dataset of 65 patients, each with a CT volume and its segmentation node (containing two labels: pancreas and lesion).</p>
<p>I’m preprocessing this dataset using Python.</p>
<p>I have cropped and resized the original CT images to the bounding box of the pancreas + lesion area. This cropping and resizing was performed using the Radiomics library with a BSpline interpolator.</p>
<p>Next, I’m trying to generate a segmentation scene with this new volume and its segmentation node. I call Slicer with a subprocess, load the segmentation node and the cropped volume in Slicer, and then associate the segmentation node with the cropped volume. This is to resize the segmentations to match the spacing of the cropped volume. I specify the geometry using the SetReferenceImageGeometryParameterFromVolumeNode(volume) command, which works well for most cases. However, for 2 cases, I encounter issues:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83743ed001d1591a95c312cae2ddcd84027758a0.png" data-download-href="/uploads/short-url/iKTBozBnPVwxGrCOzKhCBxqBknC.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83743ed001d1591a95c312cae2ddcd84027758a0.png" alt="imagen" data-base62-sha1="iKTBozBnPVwxGrCOzKhCBxqBknC" width="465" height="500" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">588×632 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
[Here I show an example of 3 cases preproceessed with python, reading the volume and segmentation node with sitk: 1 works correctly and the next 2 cases have a half spacing of the reference volume after appliying this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99bb5b460f0db3e0cabb773e542ce6deaa775c2b.png" data-download-href="/uploads/short-url/lVYsFSYXFlht3xiZv5J22ctFhi3.png?dl=1" title="Captura de pantalla 2024-06-24 123855" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99bb5b460f0db3e0cabb773e542ce6deaa775c2b.png" alt="Captura de pantalla 2024-06-24 123855" data-base62-sha1="lVYsFSYXFlht3xiZv5J22ctFhi3" width="690" height="266" data-dominant-color="292B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-06-24 123855</span><span class="informations">767×296 32.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
]</p>
<p>When I open the Slicer scene and perform this process manually, I get the correct results.</p>
<p>Why might this be happening? Is there another command I need to include?</p>
<p>Thanks for your help.</p>

---
