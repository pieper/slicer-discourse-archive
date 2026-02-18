# Signed distance from mean shape and output csv/txt file for 400 subjects

**Topic ID**: 23490
**Date**: 2022-05-19
**URL**: https://discourse.slicer.org/t/signed-distance-from-mean-shape-and-output-csv-txt-file-for-400-subjects/23490

---

## Post #1 by @Khalid_Saifullah (2022-05-19 13:47 UTC)

<p>Hi all!</p>
<p>I am using SPHARM-PDM to generate shapes of subcortical structures. Using the output files “SubjectName_pp_surf_SPHARM_procalign.vtk”, I produced a mean vtk file with “Shape Variation Analyzer” module.</p>
<p>My next step is to find the signed shape difference for all of my subjects from the mean shape. Once I have the distance, I would like to get a csv/txt file that has the signed distance values for my 1002 vertices. With that csv/txt file, I will carry out my statistical analysis separately (I have this statistical analysis tool). Could you guide me to the right direction please?</p>

---

## Post #2 by @styner (2022-05-20 14:00 UTC)

<p>Hi Khalid<br>
This can be done in 2 ways:</p>
<p>“old” way: Use a helper module/tool called MeshMath (I am sure there are other options as well). It is distributed with SlicerSALT (in the bin folder), but you would need to call it via terminal access.</p>
<ol>
<li>compute difference as a vector field: MeshMath meanInput.vtk outputdiffvector.kwm.txt -subtract subjectInput.vtk<br>
2a. compute the signed magnitude of the difference vectors: MeshMath meanInput.vtk outputSignedMagnitude.kwm.txt -magdir outputdiffvector.kwm.txt<br>
2b. alternatively, also map the difference vector to the normal of the mean surface (removes component that runs along the surface, rather than orthogonal to it): MeshMath meanInput.vtk outputNormSignedMagnitude.kwm.txt -magNormDir outputdiffvector.kwm.txt</li>
</ol>
<p>New way: use Model to Model distance SlicerSalt module : source model =&gt; mean surface, target model =&gt; subject surface, distance =&gt; corresponding point to point, save target name in distance filed =&gt; check, vtk-output =&gt; the source model with the difference added as a scalar field.</p>
<ul>
<li>this will give you a signed magnitude (please double check), but will not provide an option to map the magnitude to the surface normal</li>
</ul>
<p>hope this helps<br>
Martin</p>

---

## Post #3 by @Khalid_Saifullah (2022-05-22 17:44 UTC)

<p>Thank you, Martin! It was very helpful.</p>
<p>I am using the “old method” as I can automate this by writing a command line script for my 400 subjects. I have a couple of follow-up questions.</p>
<p>i) It looks like MeshMath shows error with my SPHARM vtk files (e.g. “subjectID_pp_surf_SPHARM_procalign.vtk”) when I run the command “MeshMath input_mean.vtk subjectID_outputdiffvector.kwm.txt -subtract subjectID_pp_surf_SPHARM_procalign.vtk”.</p>
<p>The error message is:<br>
“Incomplete file record definition<br>
NDims required and not defined.<br>
MetaObject: Read: MET_Read Failed<br>
MetaMesh: M_Read: Error parsing file”</p>
<p>However, it works just fine if I first convert the files from vtk to meta using “VTK2Meta” tool that comes with spharm-pdm and then run the command with those meta files. Please let me know if this is okay.</p>
<p>ii) When I run what you suggested in 2b (as I am interested in the distance values along the surface normal), it generates two text files: “subjectID_outputNormSignedMagnitude.kwm_centered.txt” and “subjectID_outputNormSignedMagnitude.kwm.txt”. Could you let me know which is what and which one should I be using for my case, please?</p>
<p>Thanks in advance!<br>
Khalid</p>

---

## Post #4 by @styner (2022-05-22 19:14 UTC)

<p>Hi Khalid<br>
Re 1) forgot about that. You are correct, the files need to be in meta format (there is no loss of information by going from vtk to meta for the meshes)<br>
Re 2) centered subtracts the mean across the surface, so rather than the absolute value  (of the signed magnitude along the surface normal) this will return values relative to the mean. Generally the centered values are not needed (I cannot remember why we added that option), so you need the outputNormSignedMagnitude.kwm.txt files.<br>
Best<br>
Martin</p>

---

## Post #5 by @Khalid_Saifullah (2022-06-09 15:12 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a>,</p>
<p>Thank you Martin for taking the time in answering all the questions. I wanted to ask you two questions.</p>
<ol>
<li>For my subjects, if I am using gaussian filtering of 0.75 in 3 axes in the advanced post processed segmentation tab of SlicerSALT, and at the same time giving a Reg Temp and a Flip Temp as my input (i.e. running SPHARM-PDM on my template at the very beginning), do I need to apply the same gaussian filtering of 0.75 in 3 axes on the template while running SPHARM-PDM on the template and use that version as my Reg Temp and Flip Temp (instead of the version without gaussian filter)?</li>
<li>Does gaussian filtering of 0.75 in 3 axes sound reasonable enough not to cause any errors in my distance calculation and subsequent statistical analysis?</li>
</ol>
<p>Regards,<br>
Khalid</p>

---

## Post #6 by @styner (2022-06-10 13:56 UTC)

<p>If possible, do not use the gaussian smoothing, as it can remove parts. On the other hand, if you have medium sized holes in your data, then gaussian smoothing can fill these in. We usually process our shape data without the Gaussian smoothing, unless the segmentation have consistently holed or handles that need filling via an automated approach, such as the Gaussian smoothing.</p>

---

## Post #7 by @Khalid_Saifullah (2022-08-25 20:40 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a>,</p>
<p>Could you also tell me what this 0.75 or 1 gaussian smoothing value in 3 axes mean? Is it in mm or voxel size?</p>
<p>Regards,<br>
Khalid Saifullah</p>

---

## Post #8 by @styner (2022-08-25 21:43 UTC)

<p>it’s in millimeter (mm)</p>

---

## Post #9 by @Khalid_Saifullah (2022-09-10 19:35 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a>,</p>
<aside class="quote no-group" data-username="styner" data-post="8" data-topic="23490" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/styner/48/1024_2.png" class="avatar"> styner:</div>
<blockquote>
<p>it’s in millimeter (mm)</p>
</blockquote>
</aside>
<p>For a variance of of 2.25, the FWHM is 3.5mm [2.355*sqrt(2.25)]. Is my calculation correct?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2b45f964e18d9e1ee6bfe24e12c476db2e94e0d.png" data-download-href="/uploads/short-url/puTr9rjiuwoYhaJe81jr8Ohbnfn.png?dl=1" title="Screen Shot 2022-09-10 at 2.23.05 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2b45f964e18d9e1ee6bfe24e12c476db2e94e0d_2_690x45.png" alt="Screen Shot 2022-09-10 at 2.23.05 PM" data-base62-sha1="puTr9rjiuwoYhaJe81jr8Ohbnfn" width="690" height="45" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2b45f964e18d9e1ee6bfe24e12c476db2e94e0d_2_690x45.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2b45f964e18d9e1ee6bfe24e12c476db2e94e0d_2_1035x67.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2b45f964e18d9e1ee6bfe24e12c476db2e94e0d_2_1380x90.png 2x" data-dominant-color="EFF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-09-10 at 2.23.05 PM</span><span class="informations">1696×112 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Link: <a href="https://en.wikipedia.org/wiki/Full_width_at_half_maximum" class="inline-onebox" rel="noopener nofollow ugc">Full width at half maximum - Wikipedia</a></p>
<p>Regards,<br>
Khalid Saifullah</p>

---

## Post #10 by @styner (2022-09-12 19:31 UTC)

<p>I think so, but I don’t use FWHM</p>

---

## Post #11 by @Khalid_Saifullah (2022-09-12 23:45 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a>,</p>
<p>Thank you! I would also like to ask you about something else. Is there a way to find out the node to node distance (within one subject)? Basically, I would like to know about the distance from one node to another so that I can make a better choice about the variance of gaussian smoothing I am going to use to incorporate all my subjects in a generalized fashion.</p>
<p>I apologize going over the same issue again. Actually, I have got meaningful results for my subjects without using any smoothing but because I want to include most of my subjects, I need to use this smoothing.</p>
<p>Thank you for your support throughout the process! Much appreciated!</p>
<p>Regards,<br>
Khalid Saifullah</p>

---
