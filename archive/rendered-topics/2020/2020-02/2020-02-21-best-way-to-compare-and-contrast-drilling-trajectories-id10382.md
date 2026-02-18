# Best way to compare and contrast drilling trajectories

**Topic ID**: 10382
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/best-way-to-compare-and-contrast-drilling-trajectories/10382

---

## Post #1 by @mccarthyvetsurg (2020-02-21 14:30 UTC)

<p>Operating system: Windows 10<br>
Expected behavior:  unsure?<br>
Actual behavior:  unsure?</p>
<p>Does anyone know if 3D slicer can compare a preoperative drill trajectory to a post drill trajectory with STLs or if we can compare an intended drill trajectory to the actual?  What would be the best route to do this?   Thanks.</p>

---

## Post #2 by @lassoan (2020-02-21 14:36 UTC)

<p>Yes, these should be all doable quite easily. How do you represent drill trajectories? Entry point and target points? What would you like to compute (angle differences, point-to-line distances - such as in p47 Fig. 21 in <a href="http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Baum2019c.pdf">this thesis</a>)?</p>

---

## Post #3 by @mccarthyvetsurg (2020-02-21 15:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55fe97d6df6e7b790eaf0866b45cafbeb434d0fc.jpeg" data-download-href="/uploads/short-url/cgK2ZqjwsZu3zRXdVMGiNOsDsNC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55fe97d6df6e7b790eaf0866b45cafbeb434d0fc_2_690x388.jpeg" alt="image" data-base62-sha1="cgK2ZqjwsZu3zRXdVMGiNOsDsNC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55fe97d6df6e7b790eaf0866b45cafbeb434d0fc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55fe97d6df6e7b790eaf0866b45cafbeb434d0fc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55fe97d6df6e7b790eaf0866b45cafbeb434d0fc_2_1380x776.jpeg 2x" data-dominant-color="A1A3B2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 514 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So with my data set, I have CTs and two different drill paths,  I can define the target drill trajectory based on the STL that we created preoperatively that defines the safe corridor. Is there a way I can overlay that path with my path in the current view?  Thanks for your help!</p>
<p>I would like to compute angle differences, and the angles themselves, as well as yes point to line distance.</p>

---

## Post #4 by @lassoan (2020-02-21 15:18 UTC)

<p>You can load the STL file and overlay it is shown in the image if you enable display in Slice views.</p>
<p>To compute various errors, probably the simplest is to define the trajectories as “markups line” nodes and write a few lines of Python script that computes the errors based on the control point coordinates. If you prefer automatic computation of the hole’s axis then you can segment it using Segment Editor module and use Segment Statistics module to compute principal axis position and orientation. You need recent Slicer Preview Release for these.</p>

---

## Post #5 by @vet0282 (2020-02-21 17:36 UTC)

<p>Daniel,</p>
<p>My understanding is that you have two CT sets (preop for planning and postop), and you could segment sacrum in this dog. I assume difficulty you have is to overlap these two to compare planned drill trajectory/starting point with actual surgery. I previously did the same work as yours.</p>
<ol>
<li>
<p>Since positioning for CT is different between the two sets, you need registration. You can use one of many registration modules or extensions to do this. One easy way is to place a few fiducials on anatomical landmarks on the sacrum and use those for registration and add further shape matching.</p>
</li>
<li>
<p>Then you can compare the planned and actual trajectory.</p>
</li>
<li>
<p>You may use a line mark-up and measure an angle. Or you can place fiducials at the origin and end of each planned and actual drill hole. Then, you will have coordinates of fiducials and make 2 vectors. Then, you can calculate angle difference and displacement of the origin of the drilling.</p>
</li>
</ol>
<p>You may also want to measure angles from each plane or axis. Then, you can reformat (reslice) based on axes you assign on the sacrum.</p>
<p>Sun.</p>
<p>Sun Young Kim, DVM, MS, DACVS-Small Animal</p>
<p>Associate Professor of Small Animal Surgery<br>
Veterinary Clinical Sciences<br>
College of Veterinary Medicine<br>
625 Harrison Street<br>
West Lafayette, IN 47907<br>
U.S.A.</p>

---
