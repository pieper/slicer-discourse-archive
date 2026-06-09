---
topic_id: 47237
title: "Issues 3D view .vtk model"
date: 2026-06-04
url: https://discourse.slicer.org/t/47237
last_bumped: 2026-06-08T17:19:25.847Z
---

# Issues 3D view .vtk model

**Topic ID**: 47237
**Date**: 2026-06-04
**URL**: https://discourse.slicer.org/t/issues-3d-view-vtk-model/47237

---

## Post #1 by @Stephan_Collins (2026-06-04 13:32 UTC)

<p>Dear greatest community of all,</p>
<p>I am having issues displaying models whilst segments are looking just fine in 3D view. I am running slicer on linux on a calculation server, never had this kind of troubles before…<br>
affects both slicer 10 and 11.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7002f82b9d5caa608e633b790e3613df9c10c2f8.jpeg" data-download-href="/uploads/short-url/fYTPZHT064MFQHllNXL0l45JEb6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/7002f82b9d5caa608e633b790e3613df9c10c2f8_2_690x386.jpeg" alt="image" data-base62-sha1="fYTPZHT064MFQHllNXL0l45JEb6" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/7002f82b9d5caa608e633b790e3613df9c10c2f8_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/7002f82b9d5caa608e633b790e3613df9c10c2f8_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/7002f82b9d5caa608e633b790e3613df9c10c2f8_2_1380x772.jpeg 2x" data-dominant-color="BEBFC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×1072 326 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-06-04 15:14 UTC)

<p>You need to explain your issue a little better. It is not clear from the screenshot.</p>

---

## Post #3 by @Stephan_Collins (2026-06-05 10:07 UTC)

<p>My apologies Murat,</p>
<p>when visualising a model, the light projected on the model seem to be coming only from one direction.<br>
If I am looking from a certain angle, model appears:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88da1d8f469676e08aac7505927a481c5da89fa8.jpeg" data-download-href="/uploads/short-url/jwEfgrU72C4BWIQdjJGNj8tJ4ko.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88da1d8f469676e08aac7505927a481c5da89fa8_2_690x254.jpeg" alt="image" data-base62-sha1="jwEfgrU72C4BWIQdjJGNj8tJ4ko" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88da1d8f469676e08aac7505927a481c5da89fa8_2_690x254.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88da1d8f469676e08aac7505927a481c5da89fa8_2_1035x381.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88da1d8f469676e08aac7505927a481c5da89fa8.jpeg 2x" data-dominant-color="909DB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×402 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
but as I am changing angle, the model start loosing illumniation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a432f9d98db27392001667f2bca82fd9993af54.jpeg" data-download-href="/uploads/short-url/61RZWwJomwvvCGN6CNGTBZi2fRi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a432f9d98db27392001667f2bca82fd9993af54_2_690x229.jpeg" alt="image" data-base62-sha1="61RZWwJomwvvCGN6CNGTBZi2fRi" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a432f9d98db27392001667f2bca82fd9993af54_2_690x229.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a432f9d98db27392001667f2bca82fd9993af54_2_1035x343.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a432f9d98db27392001667f2bca82fd9993af54.jpeg 2x" data-dominant-color="7B809E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1058×352 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And eventually becomes completely black upon a full 90° rotation: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b583d582e08ae1a302724ea72d3e0fde15e6d5c.jpeg" data-download-href="/uploads/short-url/hB9MrFZAjOjpMRICJi2GSErYtzu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b583d582e08ae1a302724ea72d3e0fde15e6d5c_2_690x229.jpeg" alt="image" data-base62-sha1="hB9MrFZAjOjpMRICJi2GSErYtzu" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b583d582e08ae1a302724ea72d3e0fde15e6d5c_2_690x229.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b583d582e08ae1a302724ea72d3e0fde15e6d5c_2_1035x343.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b583d582e08ae1a302724ea72d3e0fde15e6d5c.jpeg 2x" data-dominant-color="6F7097"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1159×385 69.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This issue is happenning on both slicer10 and 11. To clarify, we are  operating on a Linux-based system. I connect to our calculation server cluster interactively using NoMachine for remote access.</p>
<p>This issue is only on .vtk models, whereas .obj and segmentations are looking fine.</p>

---

## Post #4 by @Stephan_Collins (2026-06-05 10:40 UTC)

<p>More information. I just uploaded some old .vtk files produced via slicermorph or slicermorph+distance to distance models and they loaded fine. So neither slicer 10 or 11 or my environment settings are to blame I think.</p>
<p>However, tt seems that it is only the most recent .vtk files I created via slicermorph that have been affected. I think those would have been created on the latest build (version 11).<br>
I’m now trying creating a .vtk model on slicermorph slicer 10 to see if that works.</p>

---

## Post #5 by @Stephan_Collins (2026-06-05 10:50 UTC)

<p>Dear all again, and sorry for multiple posts and troubleshooting in small steps but I found that slicermorph on slicer 10 is working as expected:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27306f442cfc842740e0a593d8d07a72c71236c5.jpeg" data-download-href="/uploads/short-url/5AGoj7Oyucod9YMuk8rpyiZUmUd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27306f442cfc842740e0a593d8d07a72c71236c5_2_690x228.jpeg" alt="image" data-base62-sha1="5AGoj7Oyucod9YMuk8rpyiZUmUd" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27306f442cfc842740e0a593d8d07a72c71236c5_2_690x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27306f442cfc842740e0a593d8d07a72c71236c5_2_1035x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27306f442cfc842740e0a593d8d07a72c71236c5.jpeg 2x" data-dominant-color="8C84B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×371 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here, the model works well. I saved it, reopenned it and again, it displays fine.</p>
<p>So I think it must have something to do with slicer11/slicermorph.</p>

---

## Post #6 by @mikebind (2026-06-05 16:20 UTC)

<p>I have run into this before, but unfortunately I don’t remember the details of what the problem was or what made it go away.  I haven’t ever used SlicerMorph, though, so that can’t have been the source of the problem when I ran into it.  Try turning off “Shadows visibilty” in the 3D view settings.  I think the most likely source of the problem is that there is something wrong with the surface normals on these models in particular.  Is it possible that the surface normals for these models are unset, or all in the same direction?  I think that would lead to the type of behavior you are seeing (i.e. uniform illumination from a single direction across the entire model, which disappears completely at 90 degrees to the normal vector).  You could try Surface Toolbox to recalculate the surface normals and see if that fixes the issue.</p>

---

## Post #7 by @muratmaga (2026-06-05 16:57 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="3" data-topic="47237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>This issue is only on .vtk models, whereas .obj and segmentations are looking fine.</p>
</blockquote>
</aside>
<p>As <a class="mention" href="/u/mikebind">@mikebind</a> said this is probably related to surface normals. Are vtk files generated the same way as the obj? Why do you have two different formats?</p>

---

## Post #8 by @Stephan_Collins (2026-06-06 08:33 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="6" data-topic="47237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Shadows visibilty</p>
</blockquote>
</aside>
<p>Hello, and thank you for your answers.</p>
<p>Shadows visibility was set to off. I tried to set it to “on,” and that crashed Slicer 11 on my server. I restarted it, and it was back to the default “off.”</p>
<p>I started looking into the Surface Toolbox, and using the “Splitting” function in Compute Surface Normals worked. I also tried: 1) auto_orient normals, which had no effect; and 2) flip normals, which had the expected effect: the model lighting effect turned on, until I rotated the model by 90°, and then it went black again.</p>
<p>So, splitting works. I set the feature angle for splitting at 90, and I have a good result (not sure what I’d need to change it to but 90° seemed to give the best result). This model is the result of a model-to-model distance computation, and I can tell the end result is correct, so it is purely a display problem that is only apparent in Slicer 11, not Slicer 10.</p>
<p>An important note also: I only used SlicerMorph GPA to create these models, so I don’t know yet if it is specific to SlicerMorph or to Slicer 11 in general on my setup. What is clear is that if I run a GPA in Slicer 11 and load/create a model via the interactive 3D tab, I get those “black” models: the original model and the warped model, even though my original model, if loaded separately, appears normal.</p>
<p>So, things go awry when I use SlicerMorph on Slicer 11 only. Slicer 10 is okay.</p>
<p>Why I use .vtk and .obj is possibly only because I use different modules to export models and they are set by default to either .obj and .vtk. I should probably have enforced using only .obj only ?</p>

---

## Post #9 by @muratmaga (2026-06-06 17:33 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="1" data-topic="47237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>slicer on linux on a calculation server,</p>
</blockquote>
</aside>
<p>How are you accessing this server and how is Slicer displayed? The most important thing are you running this locally on the server or remote connecting to it via some application? When you are running slicer on a remote machine there are many layers of complexities and libraries in between and it is very hard to chase it. Slicer 5.10 and 5.11 uses different vtk builds so that might be reason.</p>
<aside class="quote no-group" data-username="Stephan_Collins" data-post="4" data-topic="47237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>.vtk files produced via slicermorph</p>
</blockquote>
</aside>
<p>What module do you use in SlicerMorph to generate these? Most SlicerMorph modules (e.g., GPA or ALPACA) doesn’t build 3D models, it simply modifies their existing geometry by deformations.  That should not change or matter for anything. Though if the deformation is extreme, surface normals may flip (but that often a sign that there is something wrong with the deformation, like landmark orders messed up etc)…</p>

---

## Post #10 by @Stephan_Collins (2026-06-08 07:04 UTC)

<p>Thanks for the suggestions.</p>
<p>The machine I am using is a shared calculation/computing server at CCUB/UBE. I access it through NoMachine, so Slicer is running on the remote server in a fully interactive desktop session. I am not running Slicer locally on my workstation. I understand that this adds extra complexity because the display goes through the remote desktop stack, graphics drivers/OpenGL, Qt/VTK, etc., and that the different VTK builds between Slicer 5.10 and 5.11 could be relevant.</p>
<p>Regarding the <code>.vtk</code> files: they are produced/processed through SlicerMorph, specifically in the GPA workflow. What seems strange is that a model created in slicer10 GPA, displays correctly in Slicer 5.11 if I simply open it as a model. The issue appears only when I select that model as the template in GPA to display the transformation. At that point, it shows the display problem I have been facing from the very start (as soon as I “apply” after selecting the model template and landmarls</p>
<p>So it does not look like the <code>.vtk</code> file is generally incompatible with Slicer 5.11, because it can be opened and visualized normally. The problem seems to be triggered specifically by the GPA template selection/display step, or by how GPA handles the mesh after it is chosen as a template. and again, it could be due to different vtk handlers in slicer11 as again, no problem whatso ever in 10.<br>
Hope this makes sense</p>

---

## Post #11 by @muratmaga (2026-06-08 17:19 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="10" data-topic="47237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>So it does not look like the <code>.vtk</code> file is generally incompatible with Slicer 5.11</p>
</blockquote>
</aside>
<p>VTK should be compatible, since it is the format used by the VTK library slicer uses. I think you need to do a simpler test. Create a VTK an OBJ file from a simple segmentation of a sample data using 5.10 and 5.11 and if you can replicate the problem.</p>

---
