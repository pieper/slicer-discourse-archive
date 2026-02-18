# How to use VMTK split the vessel tree's branch?

**Topic ID**: 15667
**Date**: 2021-01-26
**URL**: https://discourse.slicer.org/t/how-to-use-vmtk-split-the-vessel-trees-branch/15667

---

## Post #1 by @RayCui (2021-01-26 03:18 UTC)

<p>My purpose is to get the branched segmentation file(such as .nii.gz, .mhd) and the centerline file from the whole binary vessel tree.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/lantiga">@lantiga</a></p>
<ol>
<li>
<p>How can I convert the centerline (vtkPolyData) obtained by vtkvmtkPolyDataCenterlines() into numpy array or .nii.gz file similar to the original mask?</p>
</li>
<li>
<p>The vtkvmtkPolyDataCenterlines is very slowly in my lung vessel tree data. Does anyone have idea to accerelate the speed? Besides, I found that the centerline obtained by vtkvmtkPolyDataNetworkExtractionis faster than vtkvmtkPolyDataCenterlines, but its output  seem to can not be used for input of vtkvmtkCenterlineBranchExtractor?</p>
</li>
<li>
<p>According to the obtained centerline, How can I split the branch of original mask by assign different labels to each branch? I checked the class list of VMTK, and find vtkvmtkUnstructuredGridCenterlineGroupsClipper or vtkvmtkPolyDataCenterlineGroupsClipper maybe satisfy my needs, but both methods encountered problems:</p>
</li>
</ol>
<ul>
<li>The mask is readed as structuredGrid uses vmtkImageReader() , and input to vtkvmtkUnstructuredGridCenterlineGroupsClipper will report an error.</li>
<li>vtkvmtkPolyDataCenterlineGroupsClipper will output the splitted surface, How can I convert it into a volume and output a .nii.gz file?</li>
</ul>
<p>Look forward to your reply<br>
Thanks.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4617930580b79f14b5b41ef2f3705fba54b9f019.png" alt="image" data-base62-sha1="a03VHo3Py1aY1E76RLfqTRbFttn" width="376" height="400"></p>

---

## Post #2 by @RayCui (2021-01-26 11:32 UTC)

<p>What’s the difference of <em>vtkvmtkPolyDataNetworkExtraction()</em> and <em>vtkvmtkPolyDataCenterlines()</em> ?<br>
I find that:</p>
<ol>
<li>
<p>speed. The <em>vtkvmtkPolyDataNetworkExtraction()</em> is faster than  <em>vtkvmtkPolyDataCenterlines()</em> , and sametime, the number of points in centerline network is less than in centerline polydata. Does <em>vtkvmtkPolyDataNetworkExtraction()</em>  only contain the endpoints of each line？How can I resample the centerline network(vtkPolyData) to get the centerline volume that’s size is consistent with the original mask?</p>
</li>
<li>
<p>accuracy. <em>vtkvmtkPolyDataNetworkExtraction()</em>  seems to be less accurate than <em>vtkvmtkPolyDataCenterlines()</em>  in blood vessels. But the <em>vtkvmtkPolyDataCenterlines()</em>  can easily get the flying centerlines(out of vessel) on small blood veesels. So, I prefer the <em>vtkvmtkPolyDataNetworkExtraction()</em>.</p>
</li>
</ol>
<p>flying centerlines example from <a href="https://discourse.slicer.org/t/how-to-obtain-the-complete-center-lines-using-vmtk/14068">How to obtain the complete center lines using VMTK?</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38f3dca10a5f5264ce7b7359d85d99e44f1e795.jpeg" data-download-href="/uploads/short-url/wt5hitwiQqA3HFwTyc54irOSKCp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e38f3dca10a5f5264ce7b7359d85d99e44f1e795_2_311x500.jpeg" alt="image" data-base62-sha1="wt5hitwiQqA3HFwTyc54irOSKCp" width="311" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e38f3dca10a5f5264ce7b7359d85d99e44f1e795_2_311x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38f3dca10a5f5264ce7b7359d85d99e44f1e795.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38f3dca10a5f5264ce7b7359d85d99e44f1e795.jpeg 2x" data-dominant-color="909EC0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">438×704 70.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0227b2a98245e232e353dd0ea8c605952db3658.jpeg" data-download-href="/uploads/short-url/ygkt2odCYYrzmD5BIr6ysPL8P9e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0227b2a98245e232e353dd0ea8c605952db3658_2_328x500.jpeg" alt="image" data-base62-sha1="ygkt2odCYYrzmD5BIr6ysPL8P9e" width="328" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0227b2a98245e232e353dd0ea8c605952db3658_2_328x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0227b2a98245e232e353dd0ea8c605952db3658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0227b2a98245e232e353dd0ea8c605952db3658.jpeg 2x" data-dominant-color="9299C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">479×728 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2021-01-29 06:16 UTC)

<p>You can find all the details in <a href="http://lantiga.github.io/media/AntigaPhDThesis.pdf">Luca Antiga’s PhD Thesis</a>. In short:</p>
<ul>
<li>network extraction just provides geometrical medial line network; it is fast and simple and can create map of any topology (for example, it may contain loops)</li>
<li>centerline extraction provides a tree of centerlines that makes anatomical sense (not just geometrical)</li>
</ul>
<p>I’ve noticed that automatically centerline endpoints computed by network extraction are not applicable directly as input to centerline extraction. You probably could solve this by moving endpoints automatically to the closest point on the Voronoi surface (or maybe slightly further along). If you fix it then it would be nice if you could send a pull request to help others.</p>

---
