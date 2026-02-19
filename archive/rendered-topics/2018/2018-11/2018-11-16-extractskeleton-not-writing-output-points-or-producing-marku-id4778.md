---
topic_id: 4778
title: "Extractskeleton Not Writing Output Points Or Producing Marku"
date: 2018-11-16
url: https://discourse.slicer.org/t/4778
---

# ExtractSkeleton not writing output points or producing markup fiducials (MacOS 10.12, Slicer 4.11-2018-11-14)

**Topic ID**: 4778
**Date**: 2018-11-16
**URL**: https://discourse.slicer.org/t/extractskeleton-not-writing-output-points-or-producing-markup-fiducials-macos-10-12-slicer-4-11-2018-11-14/4778

---

## Post #1 by @mschumaker (2018-11-16 18:53 UTC)

<p>I’m trying to use the ExtractSkeleton module to find the centreline of an artery. I’m posting to “Support” because I’m currently trying to do it from the GUI. On MacOS 10.12, and I just downloaded the pre-compiled newest nightly to test this.</p>
<p>Steps: I start with a Segmentation of an artery (about 15 pixels diameter, 100 pixels long). Using the Segmentations module, I export it to a label map. In ExtractSkeleton, I request a new Output Image, set skeleton type to 1D, Do not prune branches to True, number of points as default, an output points file name, and request a new markups fiducial node.<br>
Expected: An output image with voxels along the skeleton, a points file with 100 points, and a fiducial node with 100 points.<br>
Actual: An output image with voxels along the skeleton, but an empty points file and no points in the fiducial node.</p>
<p>So, the points file is being created, and the image of the skeleton is being created, but no points are written to the file or to the fiducial node.  Am I doing this correctly?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55e1b88fdf074ad4d60f31d4a94e75eeb97fb6eb.png" data-download-href="/uploads/short-url/cfKbLUsGHjlOWlwuAs9iHmc2OD1.png?dl=1" title="ExtractSkeleton-test" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55e1b88fdf074ad4d60f31d4a94e75eeb97fb6eb_2_690x397.png" alt="ExtractSkeleton-test" data-base62-sha1="cfKbLUsGHjlOWlwuAs9iHmc2OD1" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55e1b88fdf074ad4d60f31d4a94e75eeb97fb6eb_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55e1b88fdf074ad4d60f31d4a94e75eeb97fb6eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55e1b88fdf074ad4d60f31d4a94e75eeb97fb6eb.png 2x" data-dominant-color="9D9E9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ExtractSkeleton-test</span><span class="informations">981×565 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-11-19 16:21 UTC)

<p>ExtractSkeleton seems to work for me (tested quickly on linux and it generated a txt file of points).  Did you look in the log file?</p>

---

## Post #3 by @mschumaker (2018-11-19 16:47 UTC)

<p>Thanks for your reply. To be honest, I don’t know where the log file is stored, either for the compiled or pre-built application. Where can I find it?<br>
Thanks again.</p>

---

## Post #4 by @pieper (2018-11-19 17:00 UTC)

<p>Look under the Help menu for the Report a bug dialog and you can look at current and recent log files.</p>

---

## Post #5 by @mschumaker (2018-11-19 19:06 UTC)

<p>Thanks. According to the log file, it’s performing all of the tasks, but the .fcsv file in the same temp directory has nothing but a header.</p>
<p>ExtractSkeleton part of the log:</p>
<blockquote>
<p>[DEBUG][Qt] 19.11.2018 13:45:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “ExtractSkeleton”<br>
[DEBUG][Qt] 19.11.2018 13:45:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Found CommandLine Module, target is  /short/Slicer-SB-Nov6/Slicer-build/lib/Slicer-4.11/cli-modules/ExtractSkeleton<br>
[DEBUG][Qt] 19.11.2018 13:45:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ModuleType: CommandLineModule<br>
[ERROR][VTK] 19.11.2018 13:45:54 [vtkMRMLSubjectHierarchyNode (0x7fdc983504d0)] (/short/Slicer-Nov6/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.cxx:2153) - HasItemAttribute: Failed to find subject hierarchy item by ID 0<br>
[DEBUG][Qt] 19.11.2018 13:45:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Extract Skeleton command line:<br>
<br>
/short/Slicer-SB-Nov6/Slicer-build/lib/Slicer-4.11/cli-modules/ExtractSkeleton --type 1D --dontPrune --numPoints 100 --pointsFile /short/skeleton19.txt --fiducialsFile /var/folders/s9/4cbyyyf5723fkrpd4htrpd4w0000gn/T/Slicer/IGA_vtkMRMLMarkupsFiducialNodeB.fcsv /var/folders/s9/4cbyyyf5723fkrpd4htrpd4w0000gn/T/Slicer/IGA_vtkMRMLLabelMapVolumeNodeB.nrrd /var/folders/s9/4cbyyyf5723fkrpd4htrpd4w0000gn/T/Slicer/IGA_vtkMRMLLabelMapVolumeNodeC.nrrd<br>
[DEBUG][Qt] 19.11.2018 13:45:55 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Extract Skeleton standard output:<br>
<br>
Processed args.<br>
Read image.<br>
Initialized output image.<br>
Extracted skeleton.<br>
Wrote points file.<br>
Wrote output image.<br>
vtkDebugLeaks has found no leaks.<br>
[DEBUG][Qt] 19.11.2018 13:45:55 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Extract Skeleton completed without errors<br>
[INFO][VTK] 19.11.2018 13:45:55 [vtkMRMLVolumeArchetypeStorageNode (0x7fdc9d87b9b0)] (/short/Slicer-Nov6/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /var/folders/s9/4cbyyyf5723fkrpd4htrpd4w0000gn/T/Slicer/IGA_vtkMRMLLabelMapVolumeNodeC.nrrd. Dimensions: 256x256x132. Number of components: 1. Pixel type: unsigned char.</p>
</blockquote>
<p>.fcsv file:</p>
<blockquote>
<p>Markups fiducial file version = 4.11<br>
# CoordinateSystem = 1<br>
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID</p>
</blockquote>

---

## Post #6 by @pieper (2018-11-19 19:42 UTC)

<p>Seems to work okay for me - I draw a segmentation with sphere brush and extract the skeleton okay.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47871aea34011e954a1b4592cb078939e0595700.png" data-download-href="/uploads/short-url/acLmqQ6nERbfXzruCOnkyL62uYg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47871aea34011e954a1b4592cb078939e0595700_2_690x455.png" alt="image" data-base62-sha1="acLmqQ6nERbfXzruCOnkyL62uYg" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47871aea34011e954a1b4592cb078939e0595700_2_690x455.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47871aea34011e954a1b4592cb078939e0595700_2_1035x682.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47871aea34011e954a1b4592cb078939e0595700_2_1380x910.png 2x" data-dominant-color="BAB8B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1404×927 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @mschumaker (2018-11-19 21:15 UTC)

<p>I just tested ExtractSkeleton with a larger segmented volume, and I was able to get points and markup fiducials. The problem may be with the size and shape of my input label map. For the original, smaller diameter label map, I could only get an output label map if I set Do Not Prune to True. However, I had to set it to False for the larger input.<br>
They’re both roughly cylindrical, and 100 pixels long, but the original “smaller” input was 8 pixels diameter, and the larger input was 23 pixels diameter.</p>
<p>Thanks for your help!</p>

---
