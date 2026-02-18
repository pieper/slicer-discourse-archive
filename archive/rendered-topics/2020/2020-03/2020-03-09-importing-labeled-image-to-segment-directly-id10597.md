# Importing labeled image to segment directly

**Topic ID**: 10597
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/importing-labeled-image-to-segment-directly/10597

---

## Post #1 by @muntahi398 (2020-03-09 13:04 UTC)

<p>Dear slicer experts,<br>
Recently I was working with some 3D image volume analysis in another software. Then I am trying to further analyze and visualize the volume in 3d slicer.<br>
work step</p>
<ul>
<li>Import volume of segemented and labeled image(integer values)</li>
<li>Import all labels as individaul segments in 3d slicer segement editor</li>
<li>Draw interconnectivity (obtained from Fiji Morphlibj-&gt;Region adjacency) overlayed on this volume.</li>
</ul>
<p>I could not find a direct way other than inidividally creating segment and thresholding. Is there any shorter way around?<br>
Split island to segment does not seem to be a good option as segments are touching and have different shapes.</p>
<p>Another fact is that in segment editor each segment editor voxel seems to be quite bigger than original volume voxel. In a very low resolution volume, segement shape gets worse because  of coarse edge. Is there any way to control segment editor voxel size?</p>
<p>I have uploaded a sample labeled volume here <a href="https://drive.google.com/file/d/1koy0e7d4f6BmtjDcMpYa5NfueOrHNYKs/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1koy0e7d4f6BmtjDcMpYa5NfueOrHNYKs/view?usp=sharing</a><a href="https://drive.google.com/file/d/1koy0e7d4f6BmtjDcMpYa5NfueOrHNYKs/view?usp=sharing" rel="nofollow noopener">labeled volume</a></p>
<p>Regards</p>

---

## Post #2 by @lassoan (2020-03-09 13:29 UTC)

<p>You can load your image by simply drag-and-dropping to the application window then right-click on it in Data module to convert it to segmentation (tested in a recent Slicer-4.11 release).</p>
<p>In the future, do not use tiff or other 2D consumer image file formats for saving 3D data, as there is no standard way of storing basic image geometry information in them (image spacing, origin, axis directions). If you save your 3D volume in nrrd file format then you will not lose image spacing information and in recent Slicer-4.11 releases you can load the image directly as segmentation (without the need to first load as labelmap and then convert to segmentation).</p>

---

## Post #3 by @muntahi398 (2020-03-09 18:23 UTC)

<p>Hi  Andras,<br>
thank you very  much and “Data module --&gt; convert it to segmentation” worked nicely.</p>
<p>The data set I got was old and was already in Tiff format, but I will use current datasets with nrrd format.</p>
<p>Could you suggest a way to draw tubes from a list of fiducial points? as shown in <a href="https://www.slicer.org/wiki/Modules:Fiducials-Documentation-3.6#:~:text=Usage,wish%20to%20place%20your%20fiducials." rel="nofollow noopener">fiducia</a></p>
<p>And if this  option is already available can you suggest, how to measure the Geodesic distance between 2 points in a 3d segment and  draw Geodesic path with fiducial point?  I found this script of yours for <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_distance_of_points_from_surface" rel="nofollow noopener">surface</a>.</p>

---
