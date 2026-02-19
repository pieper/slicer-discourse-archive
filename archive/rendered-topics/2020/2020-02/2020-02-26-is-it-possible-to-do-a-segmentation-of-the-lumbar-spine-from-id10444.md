---
topic_id: 10444
title: "Is It Possible To Do A Segmentation Of The Lumbar Spine From"
date: 2020-02-26
url: https://discourse.slicer.org/t/10444
---

# Is it possible to do a segmentation of the lumbar spine from CT-data and use the 3D model (.igs) for further finite element analysis in ABAQUS or FEBio?

**Topic ID**: 10444
**Date**: 2020-02-26
**URL**: https://discourse.slicer.org/t/is-it-possible-to-do-a-segmentation-of-the-lumbar-spine-from-ct-data-and-use-the-3d-model-igs-for-further-finite-element-analysis-in-abaqus-or-febio/10444

---

## Post #1 by @Jeff_S (2020-02-26 15:25 UTC)

<p>I have never worked with 3D Slicer before and I am quiet new in this field. But I would like create a 3D model out of CT-DICOM-data. It is important that the HU values of the cortical and trabecular bone will be safed in the output (as .igs) for further Finite element analysis in ABAQUS or FEBio.<br>
Furthermore I would like to know if it is possible in 3D Slicer to do material assignment and volumetric meshing.<br>
I would appreciate any support.<br>
Thank you in advance</p>

---

## Post #2 by @lassoan (2020-02-26 18:11 UTC)

<p>You can segment spine CT in Slicer and use Segment Mesher module (provided by SegmentMesher extension) to create a FE mesh. Segment Mesher uses Cleaver2 for mesh generation, which is developed by the same group as FEBio, so it should be compatible with it.</p>

---

## Post #3 by @Jeff_S (2020-02-26 20:33 UTC)

<aside class="quote no-group" data-username="Jeff_S" data-post="1" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>never worked with 3D Slicer before and I am quiet new in this field. But I would like create a 3D model out of CT-DICOM-data. It is important that the HU values of the cortical and trabecular bone will be</p>
</blockquote>
</aside>
<p>Thanks a lot for your fast reply Mr. Lasso, I really appreciate it. So did I understood it correctly that with the extension I can create tetrahedral (volumetric) meshes? Ho about the assignment of material properties?<br>
I also read that I need another software like Autodesk Meshmixer to smoothen the 3D object prior FE analysis, is that correct?</p>

---

## Post #4 by @lassoan (2020-02-26 20:48 UTC)

<aside class="quote no-group" data-username="Jeff_S" data-post="3" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>did I understood it correctly that with the extension I can create tetrahedral (volumetric) meshes?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="Jeff_S" data-post="3" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>Ho about the assignment of material properties?</p>
</blockquote>
</aside>
<p>The segment index is saved as cell scalar in the mesh. In your mesh preprocessor, you should be able to select part of the mesh based on this cell scalar and define material properties.</p>
<aside class="quote no-group" data-username="Jeff_S" data-post="3" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>I also read that I need another software like Autodesk Meshmixer to smoothen the 3D object prior FE analysis, is that correct?</p>
</blockquote>
</aside>
<p>Cleaver (the mesher that Segment Mesher module uses by default) creates smooth meshes. You can adjust meshing parameters to control resolution and smoothness. You should not need any other postprocessing. Meshmixer wouldn’t work anyway, as it can only deal with surface meshes.</p>

---

## Post #5 by @Jeff_S (2020-05-20 10:51 UTC)

<p>Dear Mr. Lasso,<br>
finally I have created a model of an lumbar vertebra out of DICOM data. I premeshed it as you suggested via Segment Mesher Modul and eported the the model as .stl and .obj file. The problem I am facing now is that I cannot load a volume mesh into FeBio (only .stl files). Do you know how or what I should do?<br>
Thanks a lot for your advices in advance</p>

---

## Post #6 by @lassoan (2020-05-20 15:31 UTC)

<p>FeBio Studio can import CTK unstructured grid saved in legacy VTK file format in ASCII mode. You can generate such file in Slicer by choosing “Unstructured grid (.vtk)” as File Format and uncheck “Compress” option (click “Show options” checkbox if you don’t see the options). Unfortunately, FeBio Studio is still in beta and has many issues. If you find that it has trouble opening your file then report it (see feedback email address <a href="https://febio.org/febio-studio/">here</a>).</p>

---

## Post #7 by @Jeff_S (2020-05-21 09:32 UTC)

<p>Thanks a lot for your help!<br>
I tried to safe the file as .vtk but still cannot load it into FEBio. I can only load the .stl file as binary format. Hence I wrote FEBio, if there is any other possibilitie. I will keep you updated.<br>
Do you know if ABAQUS is better in this case?</p>

---

## Post #8 by @lassoan (2020-05-21 17:03 UTC)

<p>I’ve just talked to the developer of FEBio Studio about this and he fixed unstructured grid import from ASCII VTK files today. I don’t know when he will update the FEBio download page, so ask him on the FEBio forum or at the contact email address.</p>

---

## Post #9 by @Jeff_S (2020-05-23 09:52 UTC)

<p>Thank you so much for your efforts!<br>
I tried to safe another 3D model in .vtk but it is showing me this error: "Cannot write data file: C:/Users/Admin/Documents/Jeffs-Data/Test/5. Trial_ Threshold_300-1800 L5/23052020_L5/LabelMapVolume.vtk.<br>
Do you want to continue saving?<br>
Do you know what is the problem?</p>

---

## Post #10 by @muratmaga (2020-05-23 13:06 UTC)

<p>Likely a permission issue. Try to save to a folder where you have right permission.</p>

---

## Post #11 by @lassoan (2020-05-23 18:31 UTC)

<p>Also make sure you don’t have any special characters in any of the folder or file names.</p>
<p>You might find some more details in the application log.</p>

---

## Post #12 by @lassoan (2020-06-08 17:00 UTC)

<p>3 posts were split to a new topic: <a href="/t/difference-of-spacing-was-detected-during-dicom-loading/11930">Difference of spacing was detected during DICOM loading</a></p>

---

## Post #14 by @Jeff_S (2020-06-08 16:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05d2083017afc0a065f7e20b201eaed498e6f7d7.png" data-download-href="/uploads/short-url/Punu7bD0a5mG4lTvtzsotw43v9.png?dl=1" title="vertebral model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05d2083017afc0a065f7e20b201eaed498e6f7d7_2_549x499.png" alt="vertebral model" data-base62-sha1="Punu7bD0a5mG4lTvtzsotw43v9" width="549" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05d2083017afc0a065f7e20b201eaed498e6f7d7_2_549x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05d2083017afc0a065f7e20b201eaed498e6f7d7_2_823x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05d2083017afc0a065f7e20b201eaed498e6f7d7.png 2x" data-dominant-color="544B54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vertebral model</span><span class="informations">984×895 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I would like to create a volumetric model of this vertebra. I tried to mesh it with the segment mesher module in order to export it as .vtk file and the result looks like that:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e00b70476fc5c92c554b004d37232cfd95d7dac.png" data-download-href="/uploads/short-url/6yXuI3yl35NZRLxvQ2kq7oXr6VK.png?dl=1" title="meshed model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e00b70476fc5c92c554b004d37232cfd95d7dac_2_565x500.png" alt="meshed model" data-base62-sha1="6yXuI3yl35NZRLxvQ2kq7oXr6VK" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e00b70476fc5c92c554b004d37232cfd95d7dac_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e00b70476fc5c92c554b004d37232cfd95d7dac_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e00b70476fc5c92c554b004d37232cfd95d7dac.png 2x" data-dominant-color="575762"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">meshed model</span><span class="informations">1004×888 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What am I doing wrong?</p>

---

## Post #15 by @lassoan (2020-06-08 17:04 UTC)

<p>How to biomechanical analysis of the vertebra:</p>
<ul>
<li>solidify the bone using “Wrap solidify” effect (provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>)</li>
<li>generate a volumetric mesh using SegmentMesher extension</li>
<li>save generated volumetric mesh with “Compress” option disabled into .vtk file</li>
<li>load .vtk file into FeBIO Studio</li>
</ul>

---

## Post #16 by @Jeff_S (2020-06-09 12:05 UTC)

<p>Dear Mr. Lasso thank you for your reply!<br>
Unfortunately today the extension database did not work, so I could not try the SurfaceWrapSolidify extension yet<br>
But I am also not sure if this solidifying module can lead to the model I need, cause I think for a precise FE analysis I need to model the cancellous bone as well and with this module it seems, that the cancellous bone will be extracted? Please correct me if I am wrong</p>

---

## Post #17 by @lassoan (2020-06-09 13:05 UTC)

<blockquote>
<p>Unfortunately today the extension database did not work</p>
</blockquote>
<p>Every day the Slicer Preview Release shows up around 1am EST but extension builds are completed around 10am EST, so depending on your timezone, you may not see extensions for a while. You can retry installing extensions now or install yesterday’s release (<a href="https://download.slicer.org/?offset=-1" class="inline-onebox">Download 3D Slicer | 3D Slicer</a>).</p>
<aside class="quote no-group" data-username="Jeff_S" data-post="16" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>But I am also not sure if this solidifying module can lead to the model I need, cause I think for a precise FE analysis I need to model the cancellous bone as well and with this module it seems, that the cancellous bone will be extracted?</p>
</blockquote>
</aside>
<p>The holes you see in the mesh are not there because you have such big holes in the bone. It is a segmentation error, because the average intensity of the bone decreases due to partial volume effect and it becomes so similar to soft tissue’s intensity that they become classified as soft tissue = outside segmentation.</p>
<p>Therefore, you need to fill in these “holes” in the segment and to reproduce material properties, you set different material properties within this mesh. You can take samples of the CT volume at every mesh point to decide where in the mesh you set material properties corresponding to cortical/cancellous bone.</p>

---

## Post #18 by @Jeff_S (2020-06-12 09:51 UTC)

<p>Thanks a lot for your reply!<br>
I tried the Wrap Solidify Module, but this is the best I could get out of it. There are still holes and even peaks on the surface. What am I doing wrong with the setup?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a57a1866e6ed0de1263209d7687806e21ea15c16.jpeg" data-download-href="/uploads/short-url/nBSmYK9x8hvRdbPy8jvlvDvSc18.jpeg?dl=1" title="wrap solidify.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a57a1866e6ed0de1263209d7687806e21ea15c16_2_690x268.jpeg" alt="wrap solidify.PNG" data-base62-sha1="nBSmYK9x8hvRdbPy8jvlvDvSc18" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a57a1866e6ed0de1263209d7687806e21ea15c16_2_690x268.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a57a1866e6ed0de1263209d7687806e21ea15c16_2_1035x402.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a57a1866e6ed0de1263209d7687806e21ea15c16_2_1380x536.jpeg 2x" data-dominant-color="9F9F97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">wrap solidify.PNG</span><span class="informations">1650×642 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Therefore, you need to fill in these “holes” in the segment and to reproduce material properties, you set different material properties within this mesh. You can take samples of the CT volume at every mesh point to decide where in the mesh you set material properties corresponding to cortical/cancellous bone.</p>
</blockquote>
</aside>
<p>How do I set material properties in 3DSlicer? I though it will be done for example in FEBio?</p>

---

## Post #19 by @lassoan (2020-06-12 16:26 UTC)

<p>The main issue is that you have chosen to enable “Create shell” and chose thickness that is comparable to your voxel size.</p>
<p>If the goal is finite-element analysis then a shell is not a good model, so do not enable “Create shell” option.</p>
<aside class="quote no-group" data-username="Jeff_S" data-post="18" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>How do I set material properties in 3DSlicer?</p>
</blockquote>
</aside>
<p>You will get material IDs (corresponding to segment indices) when Segment mesher module creates a volumetric mesh using Cleaver2. You can also add CT density values to the volumetric mesh using Probe volume with model module.</p>
<p>Your FEM software can use these additional scalar values in your mesh to set material properties. I don’t know which FEM package can read VTK unstructured grids and which can use material IDs or density values stored in cell scalars, but you can ask their developers and report back to us what you learned.</p>

---

## Post #20 by @Jeff_S (2020-06-16 16:39 UTC)

<p>Thank you very much for your help. I finally created a volumetric model of the vertebra with the following adjustmens:</p>
<ol>
<li>Wrap solidify module → Carve holes: 1mm</li>
<li>Smoothing → Closing(fill holes): 1mm</li>
<li>Gaussian Filter: 1mm<br>
The result looks like that:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55879ddbd5c4c1246bdc7fff87d73305d0f9c656.png" data-download-href="/uploads/short-url/ccD8OXHzr2CMScPAHK7mvueauSW.png?dl=1" title="model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55879ddbd5c4c1246bdc7fff87d73305d0f9c656_2_674x500.png" alt="model" data-base62-sha1="ccD8OXHzr2CMScPAHK7mvueauSW" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55879ddbd5c4c1246bdc7fff87d73305d0f9c656_2_674x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55879ddbd5c4c1246bdc7fff87d73305d0f9c656.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55879ddbd5c4c1246bdc7fff87d73305d0f9c656.png 2x" data-dominant-color="786C6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model</span><span class="informations">951×705 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>but the problem now is, if I want to mesh it, I get a very edged and reduced model. I tried different paramaters and this seems the best (but still not good enough): scale= 3; multiplier=1; grading=5<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456d1275ee148c7f8c5aa1c16f691ba03944bf5d.png" data-download-href="/uploads/short-url/9UaD92hhhlHazG6DXB4kpa3APTL.png?dl=1" title="model2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/456d1275ee148c7f8c5aa1c16f691ba03944bf5d_2_659x500.png" alt="model2" data-base62-sha1="9UaD92hhhlHazG6DXB4kpa3APTL" width="659" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/456d1275ee148c7f8c5aa1c16f691ba03944bf5d_2_659x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456d1275ee148c7f8c5aa1c16f691ba03944bf5d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/456d1275ee148c7f8c5aa1c16f691ba03944bf5d.png 2x" data-dominant-color="71686B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model2</span><span class="informations">952×722 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Any idea, what I am doing wrong or what I should improve?</p>

---

## Post #21 by @lassoan (2020-06-16 17:13 UTC)

<p>This looks really nice. Your volumetric mesh resolution looks very good, too, but of course you may want to adjust the mesh depending on what you want to model (heat transfer, mechanical stresses, etc.) and where.</p>
<p>Note that computational mesh does not have to be as high resolution as the visualization mesh. It would result in unnecessarily complex mesh, leading to very long computation times and robustness issues. Computational mesh surface does not have to be smooth either, except in special cases (such as when you are specifically interested in modeling surface contacts). Once the computation is complete, you can transfer displacements or other computed values over the visualization mesh.</p>
<p>What kind of modeling do you plan to do?</p>

---

## Post #22 by @Jeff_S (2020-06-17 09:42 UTC)

<p>Thank you very much, without your help, I would not get so far!</p>
<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What kind of modeling do you plan to do?</p>
</blockquote>
</aside>
<p>I would like to model the lumbar spine (later also a osteoporotic one, if possible) with all necessary components such as intervertebral discs etc. and include pedicle screws and rods to calculate the stress distribution.</p>

---

## Post #23 by @lassoan (2020-06-21 17:10 UTC)

<p>For these probably the current resolution is good. If you insert a rod then the mesh resolution will be automatically increased around the hole. I think you can also specify spatially varying mesh resolution with an image (it is called “field” in Cleaver). We don’t expose this option in Segment Mesher user interface, but you can specify additional command-line parameters.</p>

---

## Post #24 by @Farhan (2020-09-18 19:42 UTC)

<p>is FeBIO a open source software for student?</p>

---

## Post #25 by @lassoan (2020-09-18 21:03 UTC)

<p>Yes, it is open-source and free, even for commercial purposes.</p>

---

## Post #26 by @Farhan (2020-09-19 12:02 UTC)

<p>It worked for meshing method cleaver but not with TetGen in FeBIO Studio.<br>
Saying:<br>
Failed reading file:<br>
C:/Users/CG-DTE/Documents/NewFolder/Model.vtk<br>
ERROR: Only float data type is supported for POINT section.<br>
How to sovle this problem. What I am doing wrong.</p>

---

## Post #27 by @lassoan (2020-09-19 19:33 UTC)

<p>I would recommend to post this as an issue on the FeBIO Studio project page: <a href="https://github.com/febiosoftware/FEBioStudio/issues">https://github.com/febiosoftware/FEBioStudio/issues</a></p>

---

## Post #28 by @lassoan (2020-10-10 14:58 UTC)

<p>4 posts were split to a new topic: <a href="/t/exporting-segmentation-to-abaqus/13974">Exporting segmentation to Abaqus</a></p>

---

## Post #29 by @Jeff_S (2020-10-10 15:07 UTC)

<p>Thank you very much!<br>
Unfortunately it does not work and I get this error:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘pip_install’ is not defined</p>

---

## Post #30 by @lassoan (2020-10-10 15:14 UTC)

<p>You need to use latest Slicer Stable Release.</p>

---

## Post #31 by @Giovanni_Cunha (2021-03-08 15:18 UTC)

<p>Hi everyone</p>
<ol>
<li>
<p>I have created a volumetric mesh from a mandible segmentation (photos). However It was necessary to change the parameters to visualize all parts of the mandible (compare the 2 photos) I have changed the values but acctually I dont know which one represents. ( the new parameters scale 0.8, multiplier 1, grading 5.  Could someone explain? To perform analyses of strees distribution what are the best parameters?</p>
</li>
<li>
<p>Regarding the mesh created: As the SCALE parameter increased the surface of the volumetric mesh has changed (more triangles). I would like to know if it could interfere when the file is exported? Manly if it can interfere in the FEA analysis</p>
</li>
<li>
<p>How can I change the geometric shape from triangles to tetahedral shape?</p>
</li>
<li>
<p>I have read the answer above but I was not able to understant: How can I set material properties in 3D slicer. Could someone send some prints or at least a short tutorial?</p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b803d7d96678aa05397d1f4e9ec4014bd1558d35.png" alt="volumetric_mesh" data-base62-sha1="qfS5ublgx0tB2NS1BQB9yn4tUwt" width="621" height="380"></p>

---

## Post #32 by @lassoan (2021-03-08 15:37 UTC)

<aside class="quote no-group" data-username="Giovanni_Cunha" data-post="31" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<p>I have created a volumetric mesh from a mandible segmentation (photos). However It was necessary to change the parameters to visualize all parts of the mandible (compare the 2 photos) I have changed the values but acctually I dont know which one represents. ( the new parameters scale 0.8, multiplier 1, grading 5. Could someone explain?</p>
</blockquote>
</aside>
<p>See explanation of all parameters <a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters">here</a>.</p>
<aside class="quote no-group" data-username="Giovanni_Cunha" data-post="31" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<p>To perform analyses of strees distribution what are the best parameters?</p>
</blockquote>
</aside>
<p>Each analysis is different, you need to determine the parameters that work for you.</p>
<aside class="quote no-group" data-username="Giovanni_Cunha" data-post="31" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<p>Regarding the mesh created: As the SCALE parameter increased the surface of the volumetric mesh has changed (more triangles). I would like to know if it could interfere when the file is exported? Manly if it can interfere in the FEA analysis</p>
</blockquote>
</aside>
<p>It does not interfere with the export. What you see is what is exported. It does not interfere with FEA analysis either - the solver will work whatever mesh you provide. Of course the results will change if you use very large elements and the computation time will be very long if you have many small elements. However, since there is almost no displacement, you can probably vary the meshing parameters in a wide range and you will still get convergence and very similar results.</p>
<aside class="quote no-group" data-username="Giovanni_Cunha" data-post="31" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<p>How can I change the geometric shape from triangles to tetahedral shape?</p>
</blockquote>
</aside>
<p>Volumetric mesh elements generated by Cleaver are already tetrahedral.</p>
<aside class="quote no-group" data-username="Giovanni_Cunha" data-post="31" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<ol>
<li>I have read the answer above but I was not able to understant: How can I set material properties in 3D slicer. Could someone send some prints or at least a short tutorial?</li>
</ol>
</blockquote>
</aside>
<p>You set material properties in the pre-processor of your solver, not in Slicer. What you can do in Slicer is to create separate segments for each material (e.g., cortical bone and cancellous bone are in two separate segments), or assign CT density to each mesh point (using Probe volume with model module) and then use that information in your preprocessor. You can ask details about this on the <a href="https://febio.org/support/">FEBio forum</a> (or forum of any other solver you use).</p>

---

## Post #34 by @Giovanni_Cunha (2021-03-08 16:35 UTC)

<p>Thank you Mr Iasson</p>
<p><strong>See explanation of all parameters [here]</strong>(<a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a>).</p>
<p>I am sorry, unfortunatelly the name of the parameters are different from Slicer, for example the <strong>advanced options</strong> (where the parameters are) has a different name<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024a4581f673692925df044a6704495b5719287f.jpeg" data-download-href="/uploads/short-url/kg5152uf8BaOHe4P1gO9WePqnZ.jpeg?dl=1" title="advanced option" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024a4581f673692925df044a6704495b5719287f_2_690x323.jpeg" alt="advanced option" data-base62-sha1="kg5152uf8BaOHe4P1gO9WePqnZ" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024a4581f673692925df044a6704495b5719287f_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024a4581f673692925df044a6704495b5719287f_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024a4581f673692925df044a6704495b5719287f_2_1380x646.jpeg 2x" data-dominant-color="89898B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">advanced option</span><span class="informations">1907×895 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">Advanced:
  -b [ --background_mesh ] arg       input background mesh
  -I [ --indicator_functions ]       the input files are indicator functions (boundary is defined as isosurface
                                     where image value = 0)
  -z [ --sizing_field ] arg          sizing field path (use precomputed sizing field for adaptive mode)
  -w [ --write_background_mesh ]     write background mesh
  --simple                           use simple interface approximation
  -j [ --fix_tet_windup ]            ensure positive Jacobians with proper vertex wind-up
                                     (prevents inside-out tetrahedra in the output mesh)
                                     This flag is specified by SlicerSegmentMesher module, no need to specify it as additional option.
  -e [ --strip_exterior ]            strip exterior tetrahedra (remove temporary elements that are added to make the volume cubic)
                                     This flag is specified by SlicerSegmentMesher module, no need to specify it as additional option.
</code></pre>
<p>I can presume that Slicer uses the Cleaver, but I was not able to identify the name of the parameters in the code above. Could you help me?</p>

---

## Post #35 by @Giovanni_Cunha (2021-03-08 16:43 UTC)

<blockquote>
<p>or assign CT density to each mesh point (using Probe volume with model module) and then use that information in your preprocessor.</p>
</blockquote>
<p>Where can I find this tool? I was looking for in the Models module but I did not find (photo)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26b2e287ec904f76201861542e7fe5e2c9eca84b.jpeg" data-download-href="/uploads/short-url/5wloZ39AgHBhfBkpeTA59J9bbnR.jpeg?dl=1" title="Models module" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26b2e287ec904f76201861542e7fe5e2c9eca84b_2_690x321.jpeg" alt="Models module" data-base62-sha1="5wloZ39AgHBhfBkpeTA59J9bbnR" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26b2e287ec904f76201861542e7fe5e2c9eca84b_2_690x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26b2e287ec904f76201861542e7fe5e2c9eca84b_2_1035x481.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26b2e287ec904f76201861542e7fe5e2c9eca84b_2_1380x642.jpeg 2x" data-dominant-color="87888A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Models module</span><span class="informations">1913×891 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #36 by @lassoan (2021-03-08 16:45 UTC)

<aside class="quote no-group" data-username="Giovanni_Cunha" data-post="34" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<p>I am sorry, unfortunatelly the name of the parameters are different from Slicer, for example the <strong>advanced options</strong> (where the parameters are) has a different name</p>
</blockquote>
</aside>
<p>Adaptive mesh sizing is essentially controlled by 3 parameters, so you should be able to find which one is which.</p>
<p>Please use latest Slicer Stable Release. It exposes some more parameters, and the GUI contains a bit more explanations.</p>
<aside class="quote no-group quote-modified" data-username="Giovanni_Cunha" data-post="35" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovanni_cunha/48/6942_2.png" class="avatar"> Giovanni_Cunha:</div>
<blockquote>
<blockquote>
<p>or assign CT density to each mesh point (using Probe volume with model module) and then use that information in your preprocessor.</p>
</blockquote>
<p>Where can I find this tool? I was looking for in the Models module but I did not find (photo)</p>
</blockquote>
</aside>
<p>You can click the search icon in the module toolbar (or hit Ctrl-F) to open the module finder and type <code>probe</code>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b652f16cf1fde7ce7a056a193a8896b21450045.png" data-download-href="/uploads/short-url/jT99xVCTUBk3B6mTCnUjpZw2DLT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b652f16cf1fde7ce7a056a193a8896b21450045_2_646x500.png" alt="image" data-base62-sha1="jT99xVCTUBk3B6mTCnUjpZw2DLT" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b652f16cf1fde7ce7a056a193a8896b21450045_2_646x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b652f16cf1fde7ce7a056a193a8896b21450045_2_969x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b652f16cf1fde7ce7a056a193a8896b21450045.png 2x" data-dominant-color="EEF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1179×912 50.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #37 by @Giovanni_Cunha (2021-03-08 16:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="36" data-topic="10444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Adaptive mesh sizing is essentially controlled by 3 parameters, so you should be able to find which one is which.</p>
</blockquote>
</aside>
<p>OK! thanks. Just to confirm. About The –<strong>scale</strong>  –<strong>multiplier</strong> and  –<strong>grading</strong></p>
<p>Scale: If the value increase the mesh improves? If the value decrease the mesh become more coarser?</p>
<p>Multiplier: What is its function? This tool is used to multiplier the value of the Scale?</p>
<p>Grading: What is its function? If the value increases the mesh become more detailed?</p>

---

## Post #38 by @lassoan (2021-03-08 17:18 UTC)

<p>Multiplier (sampling rate) allows you to skip voxels. Equivalent to downsampling the input volume.</p>
<p>Scaling controls overall output mesh element size.</p>
<p>Grading controls how much the output mesh element size are allowed to change throughout the mesh.</p>

---

## Post #39 by @lassoan (2021-03-08 17:28 UTC)

<p>You may find the March 15 session of the <a href="https://github.com/FunkyMUG/FunkyMUG#current-schedule">FunkyMUG user group</a> useful for learning about how to create biomechanical models for FEA.</p>

---
