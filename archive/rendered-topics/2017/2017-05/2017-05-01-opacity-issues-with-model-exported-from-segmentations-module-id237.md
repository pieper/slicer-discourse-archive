---
topic_id: 237
title: "Opacity Issues With Model Exported From Segmentations Module"
date: 2017-05-01
url: https://discourse.slicer.org/t/237
---

# Opacity issues with model exported from segmentations module

**Topic ID**: 237
**Date**: 2017-05-01
**URL**: https://discourse.slicer.org/t/opacity-issues-with-model-exported-from-segmentations-module/237

---

## Post #1 by @mfolson (2017-05-01 23:44 UTC)

<p>Hi all,</p>
<p>I am attempting to create skull models from MR data in both the editor and<br>
segment editor modules. So far, I’ve had better luck using the segmentation<br>
tools to accomplish this. The problem I’m having now is that I would like to<br>
export the segmentation to a model node for quick viewing, however the<br>
exported models have odd transparency features. For example, the outside of<br>
the skull will be semi-transparent but the inside of the skull will appear<br>
solid even though it is made from a single segment. Thus when viewing the<br>
overall skull model, I see the inside curvature instead of the outside.</p>
<p>I have tried changing opacity settings before and after exporting to a model<br>
node, but the results have so far been the same. Am I missing a setting or<br>
is this just a drawback to exporting the segmentation? I’ve attached some<br>
sample images showing the correct model (using the create surface feature)<br>
and the problem model.</p>
<p>Thanks,<br>
Matt</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/f09069fdc761b2ac60671c20e270f93cb44099ce.JPG" data-download-href="/uploads/short-url/yk7ZUnlIq1DmvFTPiE61XGD6DRs.JPG?dl=1" title="Capture1.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f09069fdc761b2ac60671c20e270f93cb44099ce_2_641x500.JPG" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f09069fdc761b2ac60671c20e270f93cb44099ce_2_641x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09069fdc761b2ac60671c20e270f93cb44099ce.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09069fdc761b2ac60671c20e270f93cb44099ce.jpeg 2x" data-dominant-color="66959B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1.JPG</span><span class="informations">720×561 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/1d6d5fe40d852fbedb06932de97a6f8844dcc7fd.JPG" data-download-href="/uploads/short-url/4ckbcaJrQCTcjJSfd8Fbqa1WmQd.JPG?dl=1" title="Capture2.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1d6d5fe40d852fbedb06932de97a6f8844dcc7fd_2_637x500.JPG" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1d6d5fe40d852fbedb06932de97a6f8844dcc7fd_2_637x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d6d5fe40d852fbedb06932de97a6f8844dcc7fd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d6d5fe40d852fbedb06932de97a6f8844dcc7fd.jpeg 2x" data-dominant-color="67939B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2.JPG</span><span class="informations">728×571 37.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-05-01 23:50 UTC)

<p>Have you set the opacity to a value &lt;1.0?</p>
<p>This is a known limitation of VTK OpenGL rendering backend (due to displayed triangles are not ordered based on viewpoint).</p>
<p>In the short term you can use lower opacity values, which makes the artifacts less prominent. You can also save the model as an STL or PLY file and render in ParaView or other software.</p>
<p>We plan to switch to OpenGL2 rendering backend very soon (in a few weeks?). In this new rendering backend, rendering of transparent models works well (it uses depth peeling method).</p>

---

## Post #3 by @Fernando (2017-05-02 10:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> isn’t that a problem of flipped normals? I think I have already (very rarely) got meshes from a segmentation that looked <em>inside out</em>, so I had to flip the normals using the <code>Surface Toolbox</code>.</p>

---

## Post #4 by @lassoan (2017-05-02 16:04 UTC)

<p>I haven’t seen flipped normal in segmentations. Do you have a data set that has this issue?</p>
<p>The key question is if opacity was set to a value smaller than 1.0 - if yes, then most likely it’s related to rendering; if it’s exactly 1.0 then it is probably be caused by wrong ordering of triangles (and backface culling).</p>

---

## Post #5 by @mfolson (2017-05-02 18:11 UTC)

<p>Thank you both for the quick replies!</p>
<p>Andras, I have played with the opacity values &lt;1.0 and =1.0, but anything less than 1 renders in such a way that the outside and inside surfaces switch depending on orientation. This must be the issue with VTK OpenGL you mentioned.</p>
<p>Fernando, based on your suggestion I flipped the normals in the surface toolbox, but this yielded the same model. However, if I then unchecked the “flip normals” box and ran it again (so that no options were even used in the surface toolbox module), the correct model was created. Perhaps just running it through recomputes and fixes whatever odd ordering/opacity problems I’m seeing.</p>
<p>Anyways, this will work for me. Thanks for the help!</p>
<p>Best,<br>
Matt</p>

---
