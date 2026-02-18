# LR rotation transform reduces axial resolution

**Topic ID**: 40508
**Date**: 2024-12-04
**URL**: https://discourse.slicer.org/t/lr-rotation-transform-reduces-axial-resolution/40508

---

## Post #1 by @Shirly_Someck (2024-12-04 14:48 UTC)

<p>Hi,</p>
<p>I performed an LR rotation transform using an angle and this matrix:<br>
self.transform = np.array([<br>
[1, 0, 0, 0],<br>
[0, cos_angle, sin_angle, 0],<br>
[0, -sin_angle, cos_angle, 0],<br>
[0, 0, 0, 1]<br>
])<br>
From what I understand, it should only effect the sagittal plane, but it changes the spacing of the axial plane - from ~0.2 to ~2mm slices!<br>
Why does it do that?</p>
<p>Thanks for any help in advance</p>

---

## Post #2 by @Shirly_Someck (2024-12-11 13:46 UTC)

<p>anyone? I could really use the help.<br>
When I do it manually there is no problem…</p>

---

## Post #3 by @cpinter (2024-12-11 15:20 UTC)

<p>If you did this in Slicer we’d appreciate if you told us</p>
<ul>
<li>What Slicer version you use</li>
<li>What modules you used, what steps did you take exactly</li>
<li>What did you expect, what happened instead, how did you found out</li>
<li>Preferably include screenshots</li>
</ul>

---

## Post #4 by @Shirly_Someck (2024-12-11 16:04 UTC)

<p>Thank you for answering!</p>
<p>Yes it is a part of an extension I’m working on in pycharm (2024.1.4)<br>
I am using Slicer 5.6.2, using a linear transform.<br>
I wanted to simply align the scan to a marked line by rotating around the LR axis. Manually, on a single sagittal slice, I marked the angle between the chosen line and the horizontal line using markups module, and put that angle in the LR rotation in the transforms module. Programmatically, the user marks two control points creating a line, and I calculate the projection of the line on the XY plane (I checked that the angle is identical to the manual process). Then I calculate the transform as I wrote in the first post (again, I checked it is the same as the manual transform is shown), and then I apply the transform using this line of code:<br>
targetNode.SetAndObserveTransformNodeID(transformNode.GetID())<br>
where targetNode is the scan volume, and the transformNode is:<br>
self.transform = np.array([<br>
[1, 0, 0, 0],<br>
[0, cos_angle, sin_angle, 0],<br>
[0, -sin_angle, cos_angle, 0],<br>
[0, 0, 0, 1]<br>
])<br>
transformNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLinearTransformNode”,<br>
“AlignTransform”)<br>
slicer.util.updateTransformMatrixFromArray(transformNode, self.transform)</p>
<p>The transform is done as I expected (only the sagittal changes), but for some reason, the axial slices which were 0.2 mm thin, become 2 mm thin. I found out when I was trying to move on with marking a target point in the axial plane and I scrolled a bit to find I already passed it because each slice was ten-fold larger…<br>
What screenshots could help the debugging?</p>

---

## Post #5 by @cpinter (2024-12-12 09:48 UTC)

<aside class="quote no-group" data-username="Shirly_Someck" data-post="4" data-topic="40508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shirly_someck/48/77978_2.png" class="avatar"> Shirly_Someck:</div>
<blockquote>
<p>simply align the scan</p>
</blockquote>
</aside>
<p>Are you talking about a CT that you loaded from DICOM?</p>
<blockquote>
<p>What screenshots could help the debugging?</p>
</blockquote>
<p>I think what could help is one actual matrix that you calculate (Transforms module), and the slice views before and after applying the transform.</p>
<p>Thanks!</p>

---

## Post #6 by @Shirly_Someck (2024-12-30 15:01 UTC)

<blockquote>
<p>Are you talking about a CT that you loaded from DICOM?</p>
</blockquote>
<p>MRI from nii</p>
<p>The transform matrix:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b539bfa53a286df64eb8c7e4b56c1aeaad23e834.png" data-download-href="/uploads/short-url/pRc9aRIbA87i2WTlVwMFZMKftiY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b539bfa53a286df64eb8c7e4b56c1aeaad23e834.png" alt="image" data-base62-sha1="pRc9aRIbA87i2WTlVwMFZMKftiY" width="589" height="150"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">589×150 8.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>slice view before:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73d05a7aaba6e2f2de8c17aac6a20ecf7ce57387.jpeg" data-download-href="/uploads/short-url/gwxiRDsHeM5lMA7SZ3KdBctkuYn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73d05a7aaba6e2f2de8c17aac6a20ecf7ce57387_2_517x294.jpeg" alt="image" data-base62-sha1="gwxiRDsHeM5lMA7SZ3KdBctkuYn" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73d05a7aaba6e2f2de8c17aac6a20ecf7ce57387_2_517x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73d05a7aaba6e2f2de8c17aac6a20ecf7ce57387_2_775x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73d05a7aaba6e2f2de8c17aac6a20ecf7ce57387_2_1034x588.jpeg 2x" data-dominant-color="241F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×737 85.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>slice view after:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eef0f9627b32ebf8b3318bf04a2e563f573d70e.jpeg" data-download-href="/uploads/short-url/8YJMTXBeZaryvMsmScZNmMErAfQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eef0f9627b32ebf8b3318bf04a2e563f573d70e_2_516x303.jpeg" alt="image" data-base62-sha1="8YJMTXBeZaryvMsmScZNmMErAfQ" width="516" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eef0f9627b32ebf8b3318bf04a2e563f573d70e_2_516x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eef0f9627b32ebf8b3318bf04a2e563f573d70e_2_774x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eef0f9627b32ebf8b3318bf04a2e563f573d70e_2_1032x606.jpeg 2x" data-dominant-color="221D1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1283×752 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>also, it seems to only happen some of the time… and I couldn’t figure out what I’m doing different in each case…</p>
<p>Here is the transform that doesn’t recreate the problem (keeps the same axial resolution):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cd10fa967306635e61c6df953f7180130f8296a.png" data-download-href="/uploads/short-url/mngoBGgS3m1hALbJULFtdZviNpo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cd10fa967306635e61c6df953f7180130f8296a.png" alt="image" data-base62-sha1="mngoBGgS3m1hALbJULFtdZviNpo" width="578" height="147"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">578×147 9.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2025-01-01 16:21 UTC)

<p>What makes you think that the slice spacing is changed?</p>
<p>Are you trying to compute the ACPC transform? You can do the using the <a href="https://github.com/Slicer/SlicerNeuro/blob/main/Docs/ACPCTransform/acpctransform.md">ACPC transform module</a> in SlicerNeuro extension.</p>

---

## Post #8 by @Shirly_Someck (2025-01-01 16:55 UTC)

<p>I think the slice spacing is changed because when I scroll through the slices I see that they are ~2 mm apart in the I-S axis, whereas when I do this manually the spacing remains 0.2 mm</p>
<p>I am computing the AC-PC transform, but in the meantime I chose to do it with my own code since I need things that are not accessible through the the ACPC transform module (such as setting the MCP as origin)</p>

---

## Post #9 by @lassoan (2025-01-01 17:29 UTC)

<p>The step size of the slice offset is computed as the diameter of the ellipsoid inscribed in a voxel in the direction of the slice normal. If you have an image with anisotropic spacing then changing the orientation of the volume will result in a different step size. This should not matter much, as you are browsing reformatted slices anyway. If you want to step through exact slices then use “rotate slice to volume plane”.</p>
<p>Is using a the MCP as origin a common need? If yes, and this is the only reason you don’t use the ACPC module then we could add one more point input to the ACPC module (it would take maybe half an hour to implement).</p>

---

## Post #10 by @Shirly_Someck (2025-01-06 17:32 UTC)

<p>ok, thanks, I think I got it. I can also manually set the slice spacing, but how exactly does that work? I couldn’t find the documentation of that option</p>
<p>In my understanding, MCP is commonly used in surgery planning as the origin.<br>
First of all, thanks for the offer for MCP implementation!<br>
However, it is not the only reason I don’t use it… for example from UI point of view, I want the button of creating the markup (line or control point list) to be in the GUI (not on the toolbar); I want the point size to be much smaller for accurate pinpoint; I want to see the coordinates of each point on the GUI so I can move a point in very fine steps; etc…</p>

---
