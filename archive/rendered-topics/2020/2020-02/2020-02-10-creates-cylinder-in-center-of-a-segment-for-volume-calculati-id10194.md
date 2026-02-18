# Creates Cylinder in Center of a segment for volume calculation

**Topic ID**: 10194
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/creates-cylinder-in-center-of-a-segment-for-volume-calculation/10194

---

## Post #1 by @manjula (2020-02-10 20:09 UTC)

<p>Due to the processing difficulty i thought of a work around like in the video attached for my purpose. The script <a class="mention" href="/u/juicy">@Juicy</a> <a class="mention" href="/u/lassoan">@lassoan</a> help with do the trick by automating the process but i takes lot of time.</p>
<p>The way i think of working this out was,</p>
<ol>
<li>first segment the implant</li>
<li>Exported it to Blender as stl.</li>
<li>Get the center of object and made a cylinder with know dimensions.</li>
</ol>
<p>these cylinder were the size of what we were trying to grow which took lot of time.</p>
<ol start="4">
<li>
<p>reimported them to Slicer</p>
</li>
<li>
<p>Calculate the volume</p>
</li>
<li>
<p>to threshold the bone only, used thresholding only insde that segment.</p>
</li>
<li>
<p>This is superfast but I just want to know is this has any effect on calculations compare to growing the margins ?  Is this a correct method or completely wrong way of going about this ?</p>
</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="e1LACPTxRHI" data-video-title="Segment" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=e1LACPTxRHI" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/e1LACPTxRHI/maxresdefault.jpg" title="Segment" width="" height="">
  </a>
</div>

<ol start="2">
<li>
<p>The entire process depend on accurate alignment of the first cylinder and Bledner came in becuase i could not deduce how to get the center of segment with GetMesh().GetCenter()  and also i think it calculates the center of the bounding box which might not be what i want here.</p>
</li>
<li>
<p>When i did get the some kind of values for center and when i try to create the cylinder it was embarrassingly out of sync. <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20"></p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b488aa2bc90814d5916729c24eb78cad4231639.png" data-download-href="/uploads/short-url/hAC9cugsFbIWPqKGL3hpdTRBE6t.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b488aa2bc90814d5916729c24eb78cad4231639_2_690x391.png" alt="Screenshot" data-base62-sha1="hAC9cugsFbIWPqKGL3hpdTRBE6t" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b488aa2bc90814d5916729c24eb78cad4231639_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b488aa2bc90814d5916729c24eb78cad4231639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b488aa2bc90814d5916729c24eb78cad4231639.png 2x" data-dominant-color="999BCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">986×560 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>Provided the method is accurate, is it possible to get the center of my segment and then create a cylinder along the long axis  or is there a way of putting a fiducial to the center of the segment and then i can just draw a circle from that  ?</li>
</ol>

---

## Post #2 by @Juicy (2020-02-11 20:12 UTC)

<p>I cant really comment on the validity of growing the segment vs placing a cylinder around the segment as I dont know the project.</p>
<p>Looks like there are some great <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">new features</a> in Segment Statistics. You could find the centroid of the segment, place a cylinder model at the centroid and then align it with the principal axes of the segment (also found with segment statistics).</p>
<p>You could probably write a script which calls the logic of segment statistics to find centroid and principal axes and then places a vtk cylinder at the centroid and aligns it using a transform or perhaps you can specify angle on placement from the cration options for a vtk cylinder?</p>

---

## Post #3 by @manjula (2020-02-12 20:47 UTC)

<p>Dear <a class="mention" href="/u/juicy">@Juicy</a>,</p>
<p>Thanks you for the help. I was not aware of the new features in the segment statistics and it is extremely useful. Our problem for now was solved with the new update on the margin growing algorithm thanks to Prof <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> . Now the Margin growing is super fast !!! So we will not have to do work around on this now. But  I think the repetition script will be useful to many, some where along the way.</p>
<p>The Cylinder problem was also to work around our original problem but it is a common way that others have done analysis too.  So i would like to get to know how to do that properly even though it  is not needed for now.</p>
<p>From the script repository i get it,</p>
<p>implant = vtk.vtkCylinderSource()<br>
implant.SetHeight(3)<br>
implant.SetRadius(2)<br>
implant.SetCenter(3.0603, -0.409605, 14.2942)<br>
implant.SetResolution(100)</p>
<p>implantNode = slicer.modules.models.logic().AddModel(implant.GetOutputPort())<br>
implantNode.GetDisplayNode().SetColor(0,0,1)<br>
implantNode.GetDisplayNode().SetOpacity(1)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c50c7168bc7851b219e0e5c4d912925b0122b582.png" data-download-href="/uploads/short-url/s7aIGlbzYer6cklEbxNlylaF9DQ.png?dl=1" title="Screenshot from 2020-02-12 21-20-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c50c7168bc7851b219e0e5c4d912925b0122b582_2_690x335.png" alt="Screenshot from 2020-02-12 21-20-01" data-base62-sha1="s7aIGlbzYer6cklEbxNlylaF9DQ" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c50c7168bc7851b219e0e5c4d912925b0122b582_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c50c7168bc7851b219e0e5c4d912925b0122b582_2_1035x502.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c50c7168bc7851b219e0e5c4d912925b0122b582_2_1380x670.png 2x" data-dominant-color="999A9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-12 21-20-01</span><span class="informations">1872×909 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So as you said it is only a question of orienting/transforming the object axis but i could not see any things that sets the objects axis. So i guess it is under the transformation ?<br>
<a href="https://vtk.org/doc/nightly/html/classvtkGeneralTransform.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkGeneralTransform.html</a><br>
but i do not understand this step on how to set the transformation on the object from the script at all !!!<br>
If someone could help much appreciated.</p>

---

## Post #4 by @lassoan (2020-02-13 01:31 UTC)

<p>You can find examples of how to set transforms in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms">Transforms module documentation</a> and in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---
