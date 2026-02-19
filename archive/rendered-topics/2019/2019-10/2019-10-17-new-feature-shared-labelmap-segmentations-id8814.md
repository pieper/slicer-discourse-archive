---
topic_id: 8814
title: "New Feature Shared Labelmap Segmentations"
date: 2019-10-17
url: https://discourse.slicer.org/t/8814
---

# New feature: Shared labelmap segmentations

**Topic ID**: 8814
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/new-feature-shared-labelmap-segmentations/8814

---

## Post #1 by @Sunderlandkyl (2019-10-17 13:51 UTC)

<p>Segmentations can now store multiple segments in shared 3D volumes, which allows significant decrease in memory usage and improvement in speed.</p>
<p>Previously, segmentations could only contain several tens of segments before the application started to slow down. Segmentations was almost unusable for cases such as atlases, which could contain hundreds of segments. By sharing binary labelmaps between segments, performance remains fast when editing and visualizing, even when the number of segments is high.</p>
<p>For users:</p>
<ul>
<li>Improved speed and memory usage: tested on SPL brain atlas (304 segments)
<ul>
<li>import time: 10.95 sec -&gt; 4.55 sec</li>
<li>loading time: 5.69 sec -&gt; &lt;0.3 sec</li>
<li>saving time: 18.09 sec -&gt; 5.86 sec; peak memory usage: 5958 MB -&gt; 1344 MB</li>
<li>slice browsing: 7.7 fps -&gt; 37.1 fps</li>
<li>painting in an effect (overwrite mode): 3.73 sec -&gt; &lt;0.1 sec</li>
</ul>
</li>
<li>Segmentation is saved as a simple 3D nrrd file if there are no overlapping segments.</li>
<li>3D nrrd labelmap (such as the ones from ITK-Snap) can be loaded into Slicer direclty as segmentation (choose “Segmentation” in “Description” column in “Add data” dialog).</li>
<li>By default, segments are stored on a single layer unless the user paints a region that should overlap another segment on the same layer.</li>
<li>The current layer number for each segment can be displayed in the segmentation table by right-clicking on the table and enabling “Show layer column”.</li>
<li>The number of layers can be collapsed in the Segmentations module under the “Binary labelmap layers” section.</li>
</ul>
<p>For developers:</p>
<ul>
<li>Saved .seg.nrrd files contain two new attributes to represent shared segments: SegmentX_Layer (List dimension in the NRRD file that contains the segment), and SegmentX_LabelValue (Voxel value used to represent the segment).</li>
<li>A summary of the API changes can be found in the migration guide:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Segmentations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Segmentations</a>
</li>
</ul>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748</p>

---

## Post #2 by @Fernando (2019-10-23 16:34 UTC)

<p>This is great. I have been looking forward to it for a while: <a href="https://discourse.slicer.org/t/segmentations-can-get-big/545" class="inline-onebox">Segmentations can get big!</a></p>
<p>Thanks!</p>

---
