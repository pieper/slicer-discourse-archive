# Extra or missing triangle with vmtksurfaceendclipper script

**Topic ID**: 20530
**Date**: 2021-11-08
**URL**: https://discourse.slicer.org/t/extra-or-missing-triangle-with-vmtksurfaceendclipper-script/20530

---

## Post #1 by @Antoine_Mathieu (2021-11-08 15:09 UTC)

<p>Dear all,</p>
<p>I am using the vmtksurfaceendclipper script to clip the extremities of a segmentation and the output surface often contains either an extra or missing triangle part:</p>
<p><code>vmtksurfaceendclipper -ifile "C:/temp/debug-clip-3/input.vtk" -ofile "C:/temp/debug-clip-3/output.vtk"</code></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7da874def2ae6578f429348efaca85f3c8e2609.png" alt="vmtk1" data-base62-sha1="nWTVPDnBwfflmpHk2rNaohm93sZ" width="391" height="137"></p>
<p>I tried to process the script step by step and it seems that the extra/missing part is always connected to the (closest) point on the input surface provided via the <code>SetClosestPoint</code> method to the seamFilter. The issue is then visible on the vtkClipPolyData output:</p>
<blockquote>
<p><strong># vmtkSurfaceEndClipper.py line 311</strong></p>
<p>seamFilter = vtkvmtk.vtkvmtkTopologicalSeamFilter()<br>
seamFilter.SetInputData(clippedSurface)<br>
seamFilter.SetClosestPoint(seedPoint)<br>
seamFilter.SetSeamScalarsArrayName(“SeamScalars”)<br>
seamFilter.SetSeamFunction(plane)</p>
<p>clipper = vtk.vtkClipPolyData()<br>
clipper.SetInputConnection(seamFilter.GetOutputPort())<br>
clipper.GenerateClipScalarsOff()<br>
clipper.GenerateClippedOutputOn()</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74aaa95b4471cd75c79d76d39f9b3bc3a9d2eae9.png" data-download-href="/uploads/short-url/gE51GLrUZKsF5mxwmE4nqC43fpT.png?dl=1" title="vmtk2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74aaa95b4471cd75c79d76d39f9b3bc3a9d2eae9_2_517x204.png" alt="vmtk2" data-base62-sha1="gE51GLrUZKsF5mxwmE4nqC43fpT" width="517" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74aaa95b4471cd75c79d76d39f9b3bc3a9d2eae9_2_517x204.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74aaa95b4471cd75c79d76d39f9b3bc3a9d2eae9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74aaa95b4471cd75c79d76d39f9b3bc3a9d2eae9.png 2x" data-dominant-color="C2B660"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vmtk2</span><span class="informations">735×290 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any modification I could make to the seamFilter or the Clipper to fix this issue ? Or any post processing of the surface I could try ?<br>
I found this issue on VMTK Github (<a href="https://github.com/vmtk/vmtk/issues/169" class="inline-onebox" rel="noopener nofollow ugc">vmtksurfaceendclipper does not work consistently · Issue #169 · vmtk/vmtk · GitHub</a>) that seems related to this problem.</p>
<p>Thanks a lot for any suggestion,<br>
Antoine</p>

---

## Post #2 by @Antoine_Mathieu (2021-11-09 16:47 UTC)

<p>Dear all,</p>
<p>After more investigations I think I found the cause of the issue.</p>
<p>I tried to clip a cylinder (vtk.vtkCylinderSource()) providing an input point on the surface and a normal vector along the cylinder axis. These 2 inputs then define the cutting plane (displayed below as the red line) and provided as input to the seamFilter (vtkvmtkTopologicalSeamFilter).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd349fb15593608ef0bf53ccc9f7699eb1475b17.png" alt="vmtk3" data-base62-sha1="qZMZfqOnF0xTuEm7NJWYu2C4TnF" width="470" height="174"></p>
<p>I had a look at the scalar output of the seamFilter (vtkvmtkTopologicalSeamFilter) for each points around the desired cropping plane:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc50d5c3da0f37491da11297e6269b841b091b3.png" data-download-href="/uploads/short-url/vDRHBCMF47f9gSYMReozVaihain.png?dl=1" title="vmtk4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddc50d5c3da0f37491da11297e6269b841b091b3_2_504x375.png" alt="vmtk4" data-base62-sha1="vDRHBCMF47f9gSYMReozVaihain" width="504" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddc50d5c3da0f37491da11297e6269b841b091b3_2_504x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc50d5c3da0f37491da11297e6269b841b091b3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc50d5c3da0f37491da11297e6269b841b091b3.png 2x" data-dominant-color="D7D749"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vmtk4</span><span class="informations">748×556 90.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here I was surprised to find out that the SeamScalars value of closest point from my input was actually at 0.<br>
I believe this is the reason why the clipper filter (vtk.vtkClipPolyData) called right after considers this point as part of the area to clip since it uses the SeamScalars array to clip the surface:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b51e7d013d283de4ec8bab1af2b5a89af246506.png" alt="vmtk5" data-base62-sha1="d1QVKYwuIk32rmXo2uO89WGYd0i" width="503" height="174"></p>
<p>Looking into the seamFilter filter’s code (vtkvmtkTopologicalSeamFilter.cxx) I realized that this point will be defined as the closest point to the implicit plane and then be the starting point of the global analysis (first point in the seamQueue).</p>
<p>However it seems to me that the seamArray value is never filed for the specific point compared to all of its neighbors (no <code>seamArray-&gt;SetValue(…)</code> for this point) making the final value the same as the initialization 0. Maybe adding something like <code> seamArray-&gt;SetValue(point0Id,point0Value);</code> line 175 would help ?</p>
<p>To bypass the issue I manually set the seamValue of this specific point (after the seamFilter execution) to the distance between the point and the plane <code> plane.FunctionValue(pointPosition)</code> and then recall the clipper filter which here provide me the desired output:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13bd8366754bb77f687c80c1fda85ff6deddaca6.png" data-download-href="/uploads/short-url/2OD6l8v2lv5vqKJQMDzJLFk4Ovs.png?dl=1" title="vmtk6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13bd8366754bb77f687c80c1fda85ff6deddaca6_2_517x183.png" alt="vmtk6" data-base62-sha1="2OD6l8v2lv5vqKJQMDzJLFk4Ovs" width="517" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13bd8366754bb77f687c80c1fda85ff6deddaca6_2_517x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13bd8366754bb77f687c80c1fda85ff6deddaca6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13bd8366754bb77f687c80c1fda85ff6deddaca6.png 2x" data-dominant-color="D2D254"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vmtk6</span><span class="informations">749×265 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I hope this can be useful, tell me if you have any comments or suggestions.</p>
<p>Thank you,<br>
Antoine</p>

---

## Post #3 by @lassoan (2021-11-10 04:04 UTC)

<p>It would be awesome if you could submit a pull request with a proposed fix.</p>

---

## Post #4 by @Antoine_Mathieu (2021-11-10 16:52 UTC)

<p>No problem, I’ll be happy to contribute. I will prepare a pull request soon.</p>

---
