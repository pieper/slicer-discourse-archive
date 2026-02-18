# Question on Contour Editing

**Topic ID**: 38230
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/question-on-contour-editing/38230

---

## Post #1 by @alientex (2024-09-05 08:53 UTC)

<p>Hello,</p>
<p>Once a contour is available, I would like to manually adjust it by grabbing and moving the contour points. Additionally, a magnetic effect should be there to pull the constructed contour closer to the surface.</p>
<p>Is it possible to achieve this kind of functionality?</p>

---

## Post #2 by @cpinter (2024-09-05 09:10 UTC)

<p>There is no concept of “contour” in Slicer. Do you mean a closed curve markup?</p>
<p>Maybe some screenshots or video would be useful for better understanding.</p>

---

## Post #3 by @cpinter (2024-09-05 09:31 UTC)

<p>Thinking about this more you may be thinking about editing a segmentation in 2D in a way that it has an effect in 3D? Slicer is an application that works with 3D data, so tools focusing on 2D operations are not really present. You could look into the Fill between slices effect in Segment Editor. In any case, more information would be useful.</p>

---

## Post #4 by @alientex (2024-09-11 04:48 UTC)

<p>Sorry, I’m not familiar with that markup. However, here’s a video showcasing what I want to achieve in the slicer:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ac6dabdc721d3c1b254658be7dd7282dd3b828c.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/788a3b4afac65f2560bf660df9564c0b69663939.jpeg">
  </div><p></p>

---

## Post #5 by @alientex (2024-09-11 06:05 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="38230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Thinking about this more you may be thinking about editing a segmentation in 2D in a way that it has an effect in 3D?</p>
</blockquote>
</aside>
<p>Exactly that’s what I want.</p>

---

## Post #6 by @cpinter (2024-09-11 08:22 UTC)

<p>Unfortunately there is no tool for that in Slicer. I actually developed this in MITK around 2004 and it worked, but the project was in the end abandoned. This is not something very easy to add (Slicer principally works on labelmaps not surface meshes, and it would have its own complications), so this would be a medium sized project, and so far there has not been enough need.</p>
<p>I wonder if deformation vector fields could be used for this somehow.</p>
<p>In any case, please look at the Fill between slices effect, maybe you find it useful.</p>

---

## Post #7 by @muratmaga (2024-09-11 16:02 UTC)

<aside class="quote no-group" data-username="alientex" data-post="5" data-topic="38230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e79b87/48.png" class="avatar"> alientex:</div>
<blockquote>
<p>Exactly that’s what I want.</p>
</blockquote>
</aside>
<p>It might be possible to do this by use of Fiducial Registration Wizard, TPS transform and moving points. But it would be a lot of work. Ultimately this is not segmentation but sculpting, for which there are software better suited to the task than Slicer (I imagine blender for one)…</p>
<p>One place I can see it can be of interest to Slicer community is forensic or fossil reconstructions (so that you can plastically deform things to see what they look like). But again that would probably work better at the polygon data then labelmaps anyways…</p>

---

## Post #8 by @pieper (2024-09-11 16:07 UTC)

<p>What you show in the video is not that much different than just painting the segmentation and having the 3D model regenerated.  Depending on what you are trying to do, working directly on a mesh can have a lot of problems like triangles inverting or self intersecting.  It’s even worse when there’s more than one segment involved.  That’s why operating on the labelmap is preferred, especially when there’s a background reference volume involved.</p>

---

## Post #9 by @alientex (2024-09-26 12:33 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="38230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I actually developed this in MITK around 2004 and it worked, but the project was in the end abandoned</p>
</blockquote>
</aside>
<p>Is this project still available to you? If so, could you please share the repository link with me? I’d love to take a look.</p>
<p>Thank you!</p>

---

## Post #10 by @cpinter (2024-09-26 14:11 UTC)

<p>Unfortunately it was proprietary. Developed within GE Healthcare.</p>

---

## Post #11 by @alientex (2024-11-21 09:30 UTC)

<p>Hello again,</p>
<p>I came across a VTK class called vtkContourWidget that seems to be exactly what I want in Slicer. Is it possible to integrate this class and use it for 2D segmentation to achieve what was shown in the earlier video?</p>
<p>I would appreciate any help or ideas.</p>

---

## Post #12 by @coenwang01 (2024-12-29 08:57 UTC)

<aside class="quote no-group" data-username="alientex" data-post="11" data-topic="38230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e79b87/48.png" class="avatar"> alientex:</div>
<blockquote>
<p>vtkContourWidget</p>
</blockquote>
</aside>
<p>Any updates? We also want to achieve similar functionality in 3D Slicer.</p>

---

## Post #14 by @bernando (2025-05-02 03:27 UTC)

<p>Hi all,</p>
<p>I’m currently working on this feature as part of my master’s project. From what I understand so far, there seem to be two possible implementation approaches:</p>
<ol>
<li>Modifying the segmentation directly using labelmaps, similar to how other effects in Slicer operate.</li>
<li>Implementing it more like a sculpting tool, as muratmaga mentioned.</li>
</ol>
<p>The closest existing effects I’ve found are <strong>Fill Between Slices</strong> or <strong>Paint</strong>, as pointed out by <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/pieper">@pieper</a>. However, those effects directly modify the labelmap segmentation. In contrast, the behavior in the video you shared looks more like sculpting. When the contour is grabbed and moved, it appears that the model is regenerated, rather than the segmentation itself being updated — that is, it doesn’t relabel the voxels within the new contour area.</p>
<p>From this, I believe the feature would be better implemented as a sculpting tool rather than a traditional 2D segmentation effect, since the goal seems to be modifying the resulting mesh using the segmentation as a reference.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> — Since you’ve worked on this previously, would you be open to sharing some core ideas? I’m very interested in contributing to this feature and to Slicer in general as part of my thesis work.</p>

---

## Post #15 by @jamesobutler (2025-05-02 05:17 UTC)

<p><a class="mention" href="/u/bernando">@bernando</a> I think some existing effects that are closer to this idea of editing a surface model would be “SurfaceCut” of the SegmentEditorExtraEffects extension which is limited to convex surface modeling (no concavities). There is also a custom markup type called “GridSurface” of the “SlicerSurfaceMarkup” extension that can model concave and convex features in a 2D surface however not as a 3D surface type that could then be used to convert to a labelmap like the SurfaceCut segment editor effect.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects?tab=readme-ov-file#surface-cut">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects?tab=readme-ov-file#surface-cut" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/39645e15c43ffc6e5a225b9198607481/lassoan/SlicerSegmentEditorExtraEffects?tab=readme-ov-file#surface-cut" class="thumbnail">

  <h3><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects?tab=readme-ov-file#surface-cut" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional segmentation tools for 3D Slicer's...</a></h3>

    <p><span class="github-repo-description">Many additional segmentation tools for 3D Slicer's Segment Editor</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerHeart/SlicerSurfaceMarkup">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/77f7a4566e946e3cf8e1da5ddc09c5d4/SlicerHeart/SlicerSurfaceMarkup" class="thumbnail">

  <h3><a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerHeart/SlicerSurfaceMarkup: Extension to test the new grid surface markup with</a></h3>

    <p><span class="github-repo-description">Extension to test the new grid surface markup with</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @mikebind (2025-05-02 16:25 UTC)

<p>Another approach which might be helpful to users coming across this thread is the “Smudge” effect of the Paint tool.  This works in the labelmap space, but, with a spherical brush, allows pretty intuitive modifications of segment boundaries in 3D which seem generally similar to what one might hope to achieve by surface point modification on slice views.  You need to work in slice views, but it looks like that is what was being mostly proposed anyway.</p>

---

## Post #17 by @cpinter (2025-05-13 14:36 UTC)

<aside class="quote no-group" data-username="bernando" data-post="14" data-topic="38230">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c5a1d2/48.png" class="avatar"> bernando:</div>
<blockquote>
<p>Since you’ve worked on this previously, would you be open to sharing some core ideas? I’m very interested in contributing to this feature and to Slicer in general as part of my thesis work.</p>
</blockquote>
</aside>
<p>Sorry for the delay, vacations, illnesses…</p>
<p>Many people have asked about this feature in the past, and if you want to implement it, you could try, but I think the scope of this is beyond even a master’s degree, at least if you want to build it on the infrastructure currently exisitng in Slicer.</p>
<p>A summary of what the method I implemented back in the day looked like:</p>
<ul>
<li>Take the closed surface representation of a segment</li>
<li>Define a “range”, starting from a point and specifying a radius, and it marked the cells within that distance from the seed point</li>
<li>Define a displacement vector (see First and Last below)</li>
<li>Select a function. As I remember we had Gaussian, Sinusoid, and Triangle</li>
<li>Move the points in the range along the displacement vector according to the selected function</li>
<li>Regularization of the resulting mesh. This is very important, and this was quite difficult. The displacement caused some triangles to deform considerably: they got very large/small, elongated, or both. An algorithm was implemented for splitting/merging triangles until all triangles conformed with certain rules (minimum angle, area, etc.). Without this step, subsequent deformations caused a very irregular, ill-formed, uneven mesh. Moreover, the combination of the initial shape and the applied function could cause triangles to cross each other, which is not necessarily solvable by such regularization.</li>
</ul>
<p>Hopefully after 20 years I don’t break any NDAs by sharing this screenshot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d6c80b07fbe67c422f77b8cbb2f4477b169baf.jpeg" data-download-href="/uploads/short-url/leGPCS2MNEra9UZlZVCF2QgBtg3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d6c80b07fbe67c422f77b8cbb2f4477b169baf_2_690x481.jpeg" alt="image" data-base62-sha1="leGPCS2MNEra9UZlZVCF2QgBtg3" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d6c80b07fbe67c422f77b8cbb2f4477b169baf_2_690x481.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d6c80b07fbe67c422f77b8cbb2f4477b169baf_2_1035x721.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d6c80b07fbe67c422f77b8cbb2f4477b169baf.jpeg 2x" data-dominant-color="494E56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1224×854 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All this said, I don’t think this would make sense to implement in today’s Slicer. The main reason is that this method worked on surface meshes, and the main representation of segmentations in Slicer is binary labelmap, and if you’d want to do this exact workflow, you’d need to break out from that framework and work on model nodes, in a completely new module.</p>
<p>What I could imagine is a Segment Editor effect, which could work the way the video you linked shows, but directly on labelmaps. So from the usage point of view there would be a radius and a “point drag&amp;drop”. The main challenge is the algorithm. You’d need to somehow start from the surface of the segment defined by the start point and radius, and fill in (foreground or background) a shape defined by the function in a way that there are no holes or speckle.</p>
<p>If you like this idea I’d be happy to brainstorm more about it. However, I somehow think that whatever your use case may be, there are simpler ways to solve the need than implement this new tool. But if you definitely need this type of tool and you are (still) in the position to implement it, happy to provide guidance.</p>

---

## Post #18 by @nagy.attila (2025-05-13 20:38 UTC)

<p>Sorry, I just bumped into this thread right now:<br>
Isn’t maybe something the OP meant what we had at the very end of the Slicer 3 days, the tool with the control points? I think it was called ModelDraw <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I might not exactly get the idea based on the description, but if yes, well… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I know, I know… but I did like that tool, and the functionality!<br>
Here is  video on how it worked:</p><div class="youtube-onebox lazy-video-container" data-video-id="zQkK_opyYnI" data-video-title="Developer hangout 2015 02 17" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=zQkK_opyYnI" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/zQkK_opyYnI/maxresdefault.jpg" title="Developer hangout 2015 02 17" width="690" height="388">
  </a>
</div>

<p>Attila</p>

---

## Post #19 by @cpinter (2025-05-14 08:56 UTC)

<p>Yes, this seems to be exactly or almost exactly what was proposed.</p>
<p>A little brainstorming: as also mentioned above, this is very similar to the Fill between slices effect. If we want to reach the functionality of ModelDraw, maybe what could be done is:<br>
In the current slice view (mouse over), create a temporary closed curve tracing the edge of the labelmap slice, with a desired density of control points. When the user moves a control point, modify that slice in the labelmap, or if it was an interpolated slice, create one, thus a new slice will be added to fill between slices.<br>
This way the user will have this “ModelDraw-way” of modifying the slices, in addition to painting, as it was already possible in Fill between slices.</p>

---

## Post #20 by @nagy.attila (2025-05-14 19:49 UTC)

<p>Yes, that pretty much could replicate the functionality of the ModelDraw tool.<br>
One big shortcoming was that the number of control points could not be changed for a given label. I kinda know the reason, so this is not a criticism! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
On the other hand, the big advantage was that we could use curves to delineate the structures and then apply the labelmap (would be segment nowadays <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ).<br>
So yes, being able to use a closed curve tracing would be neat!</p>

---
