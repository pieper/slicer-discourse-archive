---
topic_id: 36313
title: "Is There A Way To Significantly Reduce The Time For Calculat"
date: 2024-05-22
url: https://discourse.slicer.org/t/36313
---

# Is there a way to significantly reduce the time for calculating centerlines?

**Topic ID**: 36313
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-significantly-reduce-the-time-for-calculating-centerlines/36313

---

## Post #1 by @tomo-akiyama (2024-05-22 06:00 UTC)

<p>Hello, everyone,</p>
<p>I’m interested in smoothing the centerlines of the cerebral arteries.</p>
<p>I segmented the MRA images and extracted the voxels of arteries. Using VTK’s marching cubes, I created a mesh and further performed Taubin smoothing and remeshing with pymeshlab.</p>
<p>After that, I attempted to extract centerlines using vmtkcenterlines. The sources are 2 points on the internal carotid artery and 1 point on the basilar artery, while the targets are peripheral points (approximately 150 points). I’m using Apple silicon, M3pro, with an Intel version of conda in a virtual environment (Python 3.10.13). The centerlines extraction takes about 12 hours at the fastest, which is too long. Is there a good way to shorten this?</p>
<p>I tried keeping the sources as the 3 points and selecting 3 random points as targets for the same centerlines extraction, but it still took over 10 hours. I also tried using a supercomputer, but it did not lead to a reduction in time.</p>
<p>The code I used is as follows:</p>
<p>def vmtk_extract_centerline(file_name, sources, targets):<br>
# vmtk_extract_centerline(mesh, sources, targets, seedselector=“pointlist”):<br>
#==============================================================================<br>
# args: mesh: 3D mesh (vtkPolydata)<br>
#       sources: 3D coordinates of source points (numpy.ndarray)<br>
#       targets: 3D coordinates of target points (numpy.ndarray)<br>
#       seedselector: Options include “pickpoint”, “openprofiles”, “carotidprofiles”, “profileidlist”, “idlist” and “pointlist”.<br>
# returns: centerlines (vtkPolyData)<br>
#==============================================================================<br>
source_points = sources.flatten().tolist()<br>
target_points = targets.flatten().tolist()</p>
<pre><code># Read the input surface mesh from a file
file_extension = os.path.splitext(file_name)[1].lower()
if file_extension == ".vtp":
    reader = vtk.vtkXMLPolyDataReader()
elif file_extension == ".ply":
    reader = vtk.vtkPLYReader()
else:
    raise ValueError(f"Unsupported file extension: {file_extension}")

reader.SetFileName(file_name)
reader.Update()
mesh = reader.GetOutput()

# Extract centerline
centerline_extractor = vmtkscripts.vmtkCenterlines()
centerline_extractor.Surface = mesh

# Define source and target points
# http://www.vmtk.org/vmtkscripts/vmtkcenterlines.html
centerline_extractor.SeedSelectorName = "pointlist"
centerline_extractor.SourcePoints = source_points 
centerline_extractor.TargetPoints = target_points
centerline_extractor.Execute()

centerlines = centerline_extractor.Centerlines
return centerlines
</code></pre>
<p>Any advice would be greatly appreciated.<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be23578038917851c2329af4d02c43183e94ab45.jpeg" data-download-href="/uploads/short-url/r82rcUBBoZBXc6cGPurtfuAEuKF.jpeg?dl=1" title="スクリーンショット 2024-05-22 14.52.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be23578038917851c2329af4d02c43183e94ab45_2_667x500.jpeg" alt="スクリーンショット 2024-05-22 14.52.48" data-base62-sha1="r82rcUBBoZBXc6cGPurtfuAEuKF" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be23578038917851c2329af4d02c43183e94ab45_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be23578038917851c2329af4d02c43183e94ab45_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be23578038917851c2329af4d02c43183e94ab45_2_1334x1000.jpeg 2x" data-dominant-color="EEF5ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-05-22 14.52.48</span><span class="informations">1920×1438 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2024-05-22 08:35 UTC)

<p>If you use the ‘Extract centerline’ module in Slicer, it has a ‘Preprocess input surface’ option than may significantly reduce processing time. It will still be long since you have so many end points, and it is not clear whether it’s a single surface or if it has distinct islands.</p>

---

## Post #3 by @lassoan (2024-05-23 12:41 UTC)

<p>Probably the mesh has serveral magnitudes more points than necessary. Try the Extract Centerline module in 3D Slicer as <a class="mention" href="/u/chir.set">@chir.set</a> suggested to make sure you properly preprocess your mesh.</p>
<p>Network extraction should take just a couple of seconds. Since brain vasculature does not have a tree topology (it has circles), this may be your only option to get a full centerline graph anyway.</p>
<p>You can still use centerline curve extraction for a few selected branches, if you need more realistic shape at branching points or you want to search for shortest path between two points in the vasculature.</p>

---

## Post #4 by @tomo-akiyama (2024-05-28 02:22 UTC)

<p>@ <a href="/u/chir.set">chir.set</a></p>
<p>Thank you for your response.</p>
<p>As I always processed in Python on VS Code, I am not familiar with 3D Slicer, and it took me some time to get used to it, which caused my delayed response.</p>
<p>As you pointed out, the Extract Centerline in 3D Slicer significantly reduced the processing time (what took over 10 hours on Python was done in less than a minute). The difficulty lies in understanding the extent of decimation and subdivision in the 3D Slicer preprocess. However, even when I used a very detailed mesh preprocessed with a different script for centerline extraction in 3D Slicer, the processing time was still very short.</p>
<p>I wonder why the processing time is so much longer when using the same VMTK library in Python, but so much shorter in 3D Slicer?</p>
<p>Anyway, thank you very much.</p>

---

## Post #5 by @tomo-akiyama (2024-05-28 02:25 UTC)

<p>@ <a href="/u/lassoan">lassoan</a></p>
<p>Thank you for your response.</p>
<p>As you and <a class="mention" href="/u/chir.set">@Chir.set</a> mentioned, using 3D Slicer allowed me to perform centerline extraction extremely quickly. I wonder why the processing time is so much longer when using the same VMTK library in Python, but so much shorter in 3D Slicer?</p>
<p>Anyway, it was really helpful. Thank you very much.</p>

---

## Post #6 by @tomo-akiyama (2024-05-28 03:38 UTC)

<p>There is one more thing I would like to ask.</p>
<p>I found that auto-detecting endpoints in 3D Slicer is very useful.</p>
<p>However, in the image, the artifact areas (the red circles in Figure 1) are not vessels, yet the centerline extraction still extracts centerlines through them, despite not specifying them as endpoints.</p>
<p>Is there a way to prevent this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e991d9d860565d329681601be2dd9f17280f6f81.jpeg" data-download-href="/uploads/short-url/xkfJyLvyVUQ9OKuIN1tqsQ4LaJH.jpeg?dl=1" title="Fig 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e991d9d860565d329681601be2dd9f17280f6f81_2_690x403.jpeg" alt="Fig 1" data-base62-sha1="xkfJyLvyVUQ9OKuIN1tqsQ4LaJH" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e991d9d860565d329681601be2dd9f17280f6f81_2_690x403.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e991d9d860565d329681601be2dd9f17280f6f81_2_1035x604.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e991d9d860565d329681601be2dd9f17280f6f81_2_1380x806.jpeg 2x" data-dominant-color="B7B6BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig 1</span><span class="informations">1920×1123 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used auto-detect for the endpoints, and unchecked the inlet area as shown in Figure 2 (though I’m not sure if this is correct).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94951ded54b5e4d4eec518ab213b170a9a39eded.jpeg" data-download-href="/uploads/short-url/lcq97w4ZeLHsHBNm3sFiVyXyCQt.jpeg?dl=1" title="Fig 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94951ded54b5e4d4eec518ab213b170a9a39eded_2_690x420.jpeg" alt="Fig 2" data-base62-sha1="lcq97w4ZeLHsHBNm3sFiVyXyCQt" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94951ded54b5e4d4eec518ab213b170a9a39eded_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94951ded54b5e4d4eec518ab213b170a9a39eded_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94951ded54b5e4d4eec518ab213b170a9a39eded_2_1380x840.jpeg 2x" data-dominant-color="BABAC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig 2</span><span class="informations">1920×1171 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2024-05-28 04:21 UTC)

<p>I implemented smart preprocessing in the 3D Slicer module, which makes the centerline extraction practically usable on meshes created by 3D image segmentation. I made the source code publicly available on github with a permissive license (anybody can freely use it for any purpose without restrictions), so you are free to take it and use it anywhere. However, if you want to implement a VTK-based application that is readily usable in clinical workflows then your best option is probably to develop it within 3D Slicer (by adding a custom Python scripted module that guides the user through your entire workflow with a simplified user interface).</p>

---

## Post #8 by @chir.set (2024-05-28 06:54 UTC)

<aside class="quote no-group" data-username="tomo-akiyama" data-post="6" data-topic="36313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomo-akiyama/48/69831_2.png" class="avatar"> tomo-akiyama:</div>
<blockquote>
<p>Is there a way to prevent this?</p>
</blockquote>
</aside>
<p>This is the ‘Network’ centerline, which as I understood, is based on geometry and is always extractible and fast. Have you tried the ‘Tree’ centerline. This one accounts for blood flow, is heavily dependent on the quality of the mesh and may not give expected results.</p>

---

## Post #9 by @tomo-akiyama (2024-05-28 07:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="36313" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I implemented smart preprocessing in the 3D Slicer module, which makes the centerline extraction practically usable on meshes created by 3D image segmentation. I made the source code publicly available on github with a permissive license (anybody can freely use it for any purpose without restrictions), so you are free to take it and use it anywhere. However, if you want to implement a VTK-based application that is readily usable in clinical workflows then your best option is probably to develop it within 3D Slicer (by adding a custom Python scripted module that guides the user through your entire workflow with a simplified user interface).</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/chir.set">@chir.set</a><br>
<a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks.<br>
I will make sure to read the GitHub page carefully.</p>
<p>As you mentioned, selecting Tree resulted in the extraction of the centerline as I imagined, taking the branching into account. However, what could be the difference between the blood vessels where the centerline is successfully extracted and those where it is not, as shown in the figure?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ed8062f799d4cad7238c63a9c534ba45c865ada.jpeg" data-download-href="/uploads/short-url/bfu4u1DAQscqpeZs4vR70IKHKvo.jpeg?dl=1" title="スクリーンショット 2024-05-28 16.32.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed8062f799d4cad7238c63a9c534ba45c865ada_2_501x500.jpeg" alt="スクリーンショット 2024-05-28 16.32.45" data-base62-sha1="bfu4u1DAQscqpeZs4vR70IKHKvo" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed8062f799d4cad7238c63a9c534ba45c865ada_2_501x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed8062f799d4cad7238c63a9c534ba45c865ada_2_751x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed8062f799d4cad7238c63a9c534ba45c865ada_2_1002x1000.jpeg 2x" data-dominant-color="9C97D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-05-28 16.32.45</span><span class="informations">1884×1878 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I thought the issue might be that the blood vessels are too thin, so I moved the endpoints and the regions in the figure to relatively thicker parts of the blood vessels, but the result did not change.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91e7f11084451458cf13276eb9b1ed3eb42df4f8.jpeg" data-download-href="/uploads/short-url/kOKahOQlzw1fOVTsUaDJdp7lDgk.jpeg?dl=1" title="スクリーンショット 2024-05-28 16.36.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91e7f11084451458cf13276eb9b1ed3eb42df4f8_2_472x500.jpeg" alt="スクリーンショット 2024-05-28 16.36.17" data-base62-sha1="kOKahOQlzw1fOVTsUaDJdp7lDgk" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91e7f11084451458cf13276eb9b1ed3eb42df4f8_2_472x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91e7f11084451458cf13276eb9b1ed3eb42df4f8_2_708x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91e7f11084451458cf13276eb9b1ed3eb42df4f8_2_944x1000.jpeg 2x" data-dominant-color="9F9AD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-05-28 16.36.17</span><span class="informations">1800×1906 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2024-05-31 21:13 UTC)

<p>When centerline extraction cannot find a path then indeed you need to move the desired endpoints closer to thicker branches. If path is still not found then you need to move the endpoints even further so that there is a sufficiently thick path connecting them. You can also trying increasing the number of points from 5000 to 10000 or more. If you select an output model for the Voronoi surface then you can see the surface where the path is searched along.</p>

---

## Post #11 by @tomo-akiyama (2024-06-02 23:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you for your advice.<br>
I will try various approaches based on your suggestions.</p>

---
