# Groups tutorial - sample data / guidance?

**Topic ID**: 6375
**Date**: 2019-04-03
**URL**: https://discourse.slicer.org/t/groups-tutorial-sample-data-guidance/6375

---

## Post #1 by @celstark (2019-04-03 01:03 UTC)

<p>I’m looking to take FreeSurfer segmentations of the hippocampus and identify any pre/post intervention changes in shape.  I’ve gone through the very <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf" rel="nofollow noopener">nice tutorial on getting SPHARM run on all my segmentations</a> and I’ve gotten the SPHARM Shaple Analysis Module to run through cleanly.</p>
<p>But, I’m having trouble moving past this for group-level analysis.  I’ve found the <a href="https://github.com/jcfr/slicer-salt/blob/master/docs/GROUPS-Tutorial-July16_2018.pdf" rel="nofollow noopener">GROUPS tutorial PDF</a> (I should note that the main <a href="http://salt.slicer.com" rel="nofollow noopener">salt.slicer.com</a> page has an <a href="https://github.com/slicersalt/slicersalt.github.io/blob/master/doc/GROUPS-Tutorial-July16_2018.pdf" rel="nofollow noopener">incorrect link</a>) and it’s helping, but I’m not there yet.  In particular, I’ve gone through and put down several fiducials on all my hippocampi, but I’m a bit lost on where my “Common unit sphere” is supposed to have come from.  I believe the “Input Models” is the “Step3_ParaToSPHARMMesh” folder that’s created and my “Input Fiducial Files” is, of course, where I have those .fscv files I made with the Markups tool.  But, I’ve clearly missed a step or more between the Shape Analysis Module and running a group analysis as even that first step of rigid alignment is hanging me up.</p>
<p>This might all be a good bit easier to work through if I could find the tutorial data that the PDF refers to (Summer2018/GroupsTutorial).  Is that available somewhere?  That and/or any other guidance on moving forward would be greatly appreciated.</p>
<p>Thanks,</p>
<p>Craig</p>

---

## Post #2 by @bpaniagua (2019-04-08 19:16 UTC)

<p>Hi Craig,</p>
<p>I have corrected the tutorial links in the <a href="http://salt.slicer.org" rel="nofollow noopener">salt.slicer.org</a> page. Thank you for pointing that out.</p>
<p>GROUPS right now is just a way to adjust and optimize the SPHARM-PDM parameterizations to account for population information. The regular SPHARM-PDM computation only takes into account the geometry of each single case and that at times is insufficient.</p>
<p>If you refer to the option to do group statistical comparison and hypothesis testing based on shape, that module will be integrated into SALT as soon as Slicer finalizes the transition between Python 2 and Python 3.</p>
<p>We will make an announcement when it is ready, hopefully very soon.<br>
Thank you!</p>
<p>Bea</p>

---

## Post #3 by @celstark (2019-04-09 15:39 UTC)

<p>Thanks  - I’ll be on the lookout!</p>
<p>Craig</p>

---

## Post #4 by @JON (2019-10-01 13:19 UTC)

<p>Hi,</p>
<p>Wanted to check if there is any update on the above?<br>
Furthermore, it seems to me that the <em>Study-specific Shape Analysis</em> is not available yet, right?</p>
<p>My aim is to compare the shapes of two groups statistically (to see where the shape differs between te groups)?</p>
<p>Looking forward to hearing from you,<br>
Jasper</p>

---

## Post #5 by @thomshaw92 (2019-10-25 10:46 UTC)

<p>Hi <a class="mention" href="/u/bpaniagua">@bpaniagua</a>!<br>
I was also interested in the GROUPS analysis, as it seems like a lot of the other group based analyses no longer work/are out of date from the other forums.<br>
Has this been updated yet?<br>
Thank you!<br>
Tom</p>

---

## Post #6 by @styner (2019-10-25 13:36 UTC)

<p>Hi Tom and Jasper</p>
<p>GROUPS is not a group difference analysis tool, but rather a group-wise correspondence optimization. Basically, it improves upon the SPHARM correspondence to generate a better one and thus any subsequent analysis would be more sensitive (see also [1,2] for the methods on GROUPS).</p>
<p>For the statistical analysis, SlicerSALT has a group comparison/analysis module called “Covariance Significance Testing” (internally named MFSDA). There is also a module called “Population Analysis” (internally called Shape Variation Analyzer), which allows you to do PCA analysis and inspection of PCA shape spaces.</p>
<p>Martin</p>
<ol>
<li>Lyu I, Perdomo J, Yapuncich GS, Paniagua B, Boyer DM, Styner M. Group-wise Shape Correspondence of Variable and Complex Objects. Proc SPIE Int Soc Opt Eng. 2018 Mar;10574. PMCID: PMC6205236</li>
<li>Lyu I, Kim SH, Seong J-K, Yoo SW, Evans A, Shi Y, Sanchez M, Niethammer M, Styner M. Robust estimation of group-wise cortical correspondence with an application to macaque and human neuroimaging studies. Frontiers in Neuroscience. 2015;9:210. PMCID: PMC4462677)</li>
</ol>

---

## Post #7 by @thomshaw92 (2019-10-25 14:58 UTC)

<p>Dear Martin <a class="mention" href="/u/styner">@styner</a>,<br>
Thank you for the speedy reply, that makes much more sense now, thank you!<br>
I’ve had a pretty thorough search of the Slicer Docs and a quick google search but I can’t find any documentation on MFSDA/ covariance significance testing or how to use it. Is there one of those wonderful google slides presentations for this module?<br>
Thanks for your help!<br>
Cheers<br>
Tom</p>

---

## Post #8 by @bpaniagua (2019-10-25 15:22 UTC)

<p>Hi <a class="mention" href="/u/thomshaw92">@thomshaw92</a></p>
<p>The MSFDA tutorial is currently being developed (hopefully soon) but what you need to run the  Covariance Significance Testing is a file with all your covariates per shape and a shape where you want to map the p-values, alongside, of course with your correspondent geometries from SPHARM (or other shape modeling method)</p>
<p>You have<a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a">an example here</a>, where you can see the file formats and what you need to run the module.</p>
<p>Let us know how it goes!<br>
Bea</p>
<p>ps. The only functionality of what we call GROUPS in SALT is the ability of solving SPHARM-correspondence ambiguities <a href="https://docs.google.com/presentation/d/1_Od20WHcl6IKxN-n1yIYMmDC9sUmkZXFj2YXCAkHQKA/present?slide=id.p6">by providing expert landmarks</a>, so it is a correspondence optimization method as Martin said, not a statistical shape analysis method.   It is though very useful when you have shapes where correspondence is known by the user but not trivial by just looking at the geometry (symmetries, etc) HTH!!</p>

---

## Post #9 by @thomshaw92 (2019-10-26 02:27 UTC)

<p>Thanks for the info!<br>
I had a go at it, and got some nice results now, though I think I should run my data through GROUPS first to solve some of these correspondence ambiguities.</p>
<p>A couple of things:</p>
<ol>
<li>How can I create a spherical template for the groups I wish to compare?</li>
<li>I’m assuming my “shape for p-values” should also be an average shape that represents both of my samples?</li>
<li>Do the input shapes need to be in the same physical space (i.e., do I need to register them beforehand)</li>
<li>Is there a FWE correction applied?</li>
<li>What do the beta values and para values mean in the ‘Attribute’ section of the ShapePopulationViewer once I have my result? Do I look at these or the p-vals or both (new to shape analysis here).</li>
</ol>
<p>There’s also a small bug in the Covariate Significance Testing module of Slicer Salt (run on windows, latest versions etc.) When I load one CSV into the module, then load another one, it concatenates both of the CSVs. I have to restart SlicerSALT whenever I want to run it with different groups.</p>
<p>Thanks for your replies, now that it is all working I am seeing the light! Thanks for the great tool <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Cheers,<br>
Tom</p>

---

## Post #10 by @bpaniagua (2019-10-28 13:39 UTC)

<blockquote>
<ol>
<li>How can I create a spherical template for the groups I wish to compare?</li>
</ol>
</blockquote>
<p>The spherical template is the vtk of the spherical parameterization (*pp_para.vtk) from an specific case that you want to replicate in the rest of the population</p>
<blockquote>
<ol start="2">
<li>I’m assuming my “shape for p-values” should also be an average shape that represents both of my samples?</li>
</ol>
</blockquote>
<p>That’s correct.</p>
<blockquote>
<ol start="3">
<li>Do the input shapes need to be in the same physical space (i.e., do I need to register them beforehand)</li>
</ol>
</blockquote>
<p>Yes. If you use the procalign option in SPHARM, the module will output the procrustes aligned correspondent meshes.</p>
<blockquote>
<ol start="4">
<li>Is there a FWE correction applied?</li>
</ol>
</blockquote>
<p>I believe so, yes.</p>
<blockquote>
<ol start="5">
<li>What do the beta values and para values mean in the ‘Attribute’ section of the ShapePopulationViewer once I have my result? Do I look at these or the p-vals or both (new to shape analysis here).</li>
</ol>
</blockquote>
<p>The beta values will be the magnitude of the difference, the p-values will be the significance of the difference. I would visualize mainly the p-values to see when the shape differences are significant, and confirm with beta maps when necessary.</p>
<p>I hope that helps!<br>
Bea</p>

---

## Post #11 by @JON (2019-10-30 05:20 UTC)

<p>Hi <a class="mention" href="/u/bpaniagua">@bpaniagua</a>,</p>
<p>Thank you so much for your answers above (and Martin as well!; and sorry for the delay in my answers - I was out of office).<br>
I followed your suggestions and all seems to be working now, thanks!</p>
<p>I have another question:</p>
<aside class="quote no-group" data-username="bpaniagua" data-post="10" data-topic="6375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>The spherical template is the vtk of the spherical parameterization (*pp_para.vtk) from an specific case that you want to replicate in the rest of the population</p>
</blockquote>
</aside>
<p>I might be misunderstanding, but if I want to do a group analysis (e.g. see where on the mean shape group 1 differs from group 2) isn’t it useful to use the spherical parameterisation of a “mean” subject instead of 1 specific case?</p>
<p>Looking forward again to hearing from you.</p>
<p>Best,<br>
Jasper</p>

---

## Post #12 by @styner (2019-10-30 13:16 UTC)

<p>Hi Jasper,<br>
You are partially correct. I.e. our information needs to be corrected.</p>
<p>It’s less about 1 specific case or the mean, as all surfaces after SPHARM reconstruction have the same spherical template (i.e. the same spherical sampling). Thus the mean and the individual subject have the same spherical template. This is not to be confused with the parametrization of the original surface (as opposed to the SPHARM reconstruction), which is different for each surface.</p>
<p>To recap:</p>
<ol>
<li>
<p>the “*pp_surf.vtk” and “*pp_para.vtk” are the original surface and its spherical mapping. These are different across surfaces and do not use these for statistics modules.</p>
</li>
<li>
<p>the “*pp_surf_SPHARM.vtk” and “*pp_surf_para.vtk” are the SPHARM reconstruction and the spherical mapping of that reconstruction. The “*pp_surf_para.vtk” are all the same for all surfaces/subjects. SALT generates this para.vtk for all surfaces, and you can safely delete all but one of these (keep one for the Covariate Significance Testing module).</p>
</li>
</ol>
<p>Martin</p>

---

## Post #13 by @JON (2019-10-31 02:42 UTC)

<p>Hi Martin <a class="mention" href="/u/styner">@styner</a>,</p>
<p>Ah I see, thanks a lot for the clarification.<br>
I will use one of the *pp_surf_para.vtk’s</p>
<p>Best,<br>
Jasper</p>

---

## Post #14 by @Shane_TANG (2019-10-31 21:27 UTC)

<p>Hi Tom <a class="mention" href="/u/thomshaw92">@thomshaw92</a>:<br>
Thanks for asking this question cuz I feel like a lot of people are still confused by this Covariate Significance Testing module. Could you please detail what file format did you use for each entry?</p>
<ol>
<li>
<p>Select csv file<br>
I assume this should be a csv file containing TWO columns. The 1st column is the path-to-vtk files, and the 2nd column is the group index (like 0,1).</p>
</li>
<li>
<p>Select spherical template<br>
I used mean model generated by Population Analysis module but anyway it’s a .vtk file.</p>
</li>
<li>
<p>Select shape for p-values<br>
I am totally confused here and I have no idea what should be put here. So I just used the same file as entry 2, the mean model.</p>
</li>
</ol>
<p>And finally I only got a output.csv file with nothing else. From that <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="noopener nofollow ugc">one example</a> provided by Beatriz <a class="mention" href="/u/bpaniagua">@bpaniagua</a> (Thanks Bea!)  the output should contain 4 files.</p>
<p>I don’t know how to make this correct. Could you please give some suggestions? Thanks a lot!</p>
<p>My user interface looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3430ecfe768ce380b3a71b93edbb874294eec2f6.png" data-download-href="/uploads/short-url/7rHEo2FD9zpayY8JwdPKpeLVhBk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3430ecfe768ce380b3a71b93edbb874294eec2f6_2_480x500.png" alt="image" data-base62-sha1="7rHEo2FD9zpayY8JwdPKpeLVhBk" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3430ecfe768ce380b3a71b93edbb874294eec2f6_2_480x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3430ecfe768ce380b3a71b93edbb874294eec2f6_2_720x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3430ecfe768ce380b3a71b93edbb874294eec2f6_2_960x1000.png 2x" data-dominant-color="D4DBE6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1544×1606 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Shane</p>

---

## Post #15 by @thomshaw92 (2019-11-01 02:20 UTC)

<aside class="quote no-group" data-username="bpaniagua" data-post="10" data-topic="6375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>Yes. If you use the procalign option in SPHARM, the module will output the procrustes aligned correspondent meshes.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/bpaniagua">@bpaniagua</a>, what is the procalign option in SPHARM? I can’t see it.  Is this the “Use Reg Template” option? If so, is my reg template (Mesh file) going to be a sphere or just a randomly chosen exemplar from my sample?</p>
<p>I was thinking of first registering my samples together (volumetrically using ANTS) and then creating an “average” mesh as my “Reg Template (mesh file)”, is that sensible?<br>
Thanks again for your help!</p>

---

## Post #16 by @thomshaw92 (2019-11-01 02:31 UTC)

<p>Hey <a class="mention" href="/u/shane_tang">@Shane_TANG</a></p>
<aside class="quote no-group" data-username="Shane_TANG" data-post="14" data-topic="6375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shane_tang/48/5039_2.png" class="avatar"> Shane_TANG:</div>
<blockquote>
<ol>
<li>Select csv file<br>
I assume this should be a csv file containing TWO columns. The 1st column is the path-to-vtk files, and the 2nd column is the group index (like 0,1).</li>
</ol>
</blockquote>
</aside>
<p>Yep that’s what I had</p>
<aside class="quote no-group" data-username="Shane_TANG" data-post="14" data-topic="6375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shane_tang/48/5039_2.png" class="avatar"> Shane_TANG:</div>
<blockquote>
<ol start="2">
<li>Select spherical template<br>
I used mean model generated by Population Analysis module but anyway it’s a .vtk file.</li>
</ol>
</blockquote>
</aside>
<p>See Martin’s response above. I didn’t use the population analysis module because it does a different thing.</p>
<aside class="quote no-group" data-username="Shane_TANG" data-post="14" data-topic="6375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shane_tang/48/5039_2.png" class="avatar"> Shane_TANG:</div>
<blockquote>
<ol start="3">
<li>Select shape for p-values<br>
I am totally confused here and I have no idea what should be put here. So I just used the same file as entry 2, the mean model.</li>
</ol>
</blockquote>
</aside>
<p>For this one you need an examplar image (one produced by SPHARM) that isn’t a sphere (it’s the shape that you are comparing between groups).</p>
<p>I had a bit of trouble making it all work, double check manually that the files in your CSV exist, I can see you have over 350 shapes that you are comparing and mine would always crash if one didn’t exist.</p>
<p>I’m by no means the expert here though. Hope that helps!</p>

---

## Post #17 by @Shane_TANG (2019-11-10 21:34 UTC)

<p>Dear Martin, <a class="mention" href="/u/styner">@styner</a> <a class="mention" href="/u/bpaniagua">@bpaniagua</a><br>
Thanks for providing the answers.</p>
<p>When you guys say shapes, what kind of shape should we put into the <em><strong>Covariate Significance Testing</strong></em> module? SlicerSALT 2.2.1 was used in my project.<br>
I have 2 patient groups and want to compare the shape deformity in hippocampus between these 2 groups.</p>
<ol>
<li>I have pre-processed all the data using FLIRT (a linear registration tool in FSL) with DOF of 6 (only translation and rotation) so I <strong>did NOT</strong> use procalign during SPHARM-PDM.</li>
<li>Then, I fed all the *<strong>_pp_surf_SPHARM.vtk</strong> files (see the pic below) into the <em><strong>Covariate Significance Testing</strong></em> module.</li>
<li>I used the mean shape of all <strong>healthy subjects</strong> as <strong>both the template and the shape for writing p-val</strong>. (see pic below)</li>
</ol>
<details>
<summary>
Pics for Point 2 and 3</summary>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d496e59ce00c494dcc81b6af61a1bf34049be362.jpeg" data-download-href="/uploads/short-url/ukEwaFOude9CVLnEWuaPQLGZFia.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d496e59ce00c494dcc81b6af61a1bf34049be362_2_690x150.jpeg" alt="image" data-base62-sha1="ukEwaFOude9CVLnEWuaPQLGZFia" width="690" height="150" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d496e59ce00c494dcc81b6af61a1bf34049be362_2_690x150.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d496e59ce00c494dcc81b6af61a1bf34049be362_2_1035x225.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d496e59ce00c494dcc81b6af61a1bf34049be362_2_1380x300.jpeg 2x" data-dominant-color="2F2B3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×416 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5db584765d8fb7d90ff1d6a74a2f093820c39486.png" data-download-href="/uploads/short-url/dmZiQMF4A6VFP402upxGhsDcylo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5db584765d8fb7d90ff1d6a74a2f093820c39486_2_350x215.png" alt="image" data-base62-sha1="dmZiQMF4A6VFP402upxGhsDcylo" width="350" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5db584765d8fb7d90ff1d6a74a2f093820c39486_2_350x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5db584765d8fb7d90ff1d6a74a2f093820c39486_2_525x322.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5db584765d8fb7d90ff1d6a74a2f093820c39486_2_700x430.png 2x" data-dominant-color="DCE0E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×578 34.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</details>
<p>But then I got, in “pvalues.json” file, <strong>“Gpvals”: [[1.0]], “clu_pvals”: [[1.0]], “Lpvals_fdr”: [[0.997606067488982],</strong> with a series of pvalues for each point (I feel they are FDR corrected) all greater than 0.997 which means there is no difference of any point between these two groups. But before when using StatNonParaTestPDM, we could detect the differences.</p>
<p>Could you please give me suggestions on where I went wrong?</p>
<p>Notes: I saw from the <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="noopener nofollow ugc">one example</a> provided by Bea that input vtk files are all ellipsoids. I don’t know where these ellipsoids come from. And, I attached my input csv file here for your reference to see if I have wrongly constructed the csv file. (<a href="https://drive.google.com/file/d/1aPQne0i0pTJXhnc61t_R7tfzPb-a2NQ9/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">pos_neg.csv - Google Drive</a>)</p>
<p>Many thanks!</p>
<p>Shane</p>

---

## Post #18 by @styner (2019-11-11 19:16 UTC)

<p>Hi Shane<br>
Re 1. Using an external rigid registration of the surfaces instead of rigid-Procrustes is fine (though I think in this particular case Procrustes should outperform flirt in alignment accuracy).<br>
Re 2 &amp; 3. It is not clear what you used for the spherical template. You mentioned you used the mean shape of the all healthy subjects. To use the actual mean surface as the shape for visualizing the p-vals is fine (this is what we are commonly doing too). But, if you used that same surface as a spherical template, then this would not work. Rather you need the spherical surface (literally the unit sphere, just sampled the same way as your surfaces). As mentioned in one of my earlier messages, you need to use the sphere (pp_surf_para) surface of any of the surfaces. These sphere surfaces are exactly the same for all subjects (and thus is the same also for the mean).</p>
<p>Martin</p>

---

## Post #19 by @Shane_TANG (2019-11-11 19:43 UTC)

<p>Dear Martin,</p>
<p>Thanks for your answer! Yes, I am also using the <em><strong>Mean</strong></em> as the spherical template. That’s because the input files of mine are not ellipsoids so I used this mean hippocampus shape as the spherical template (in this <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="noopener nofollow ugc">one example</a>, the input files are ellipsoids and please see the <strong>figure 1</strong> below). But my input files are just the  *<strong>_pp_surf_SPHARM.vtk</strong> files which are hippocampus shapes not ellipsoids (please see <strong>figure 2</strong> below). Do I need to do some thing to make my input files into the ellipsoids?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35d67dd6d39685b6faaa51f8db4840c144bf5f87.jpeg" data-download-href="/uploads/short-url/7GgQP0HPh0wqdkIpDGu3tVYpnvh.jpeg?dl=1" title="Figure 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35d67dd6d39685b6faaa51f8db4840c144bf5f87_2_100x170.jpeg" alt="Figure 1" data-base62-sha1="7GgQP0HPh0wqdkIpDGu3tVYpnvh" width="100" height="170" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35d67dd6d39685b6faaa51f8db4840c144bf5f87_2_100x170.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35d67dd6d39685b6faaa51f8db4840c144bf5f87_2_150x255.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35d67dd6d39685b6faaa51f8db4840c144bf5f87_2_200x340.jpeg 2x" data-dominant-color="4B701F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure 1</span><span class="informations">504×650 48.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Besides, I’ve tried not using FLIRT but using procalign (first applied SPHARM-PDM on the template <strong>.nii.gz</strong> file and used the <strong>template_pp_surf_SPHARM.vtk</strong> as the Reg Template in SlicerSALT). But then I found the surfaces were not like in the same direction. A is pointed to the left while B is in the same direction as the template. Do I need to make them like the figure above where FLIRT was used?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d299010476d8c236902c0f14f37bd9b713023022.png" alt="image" data-base62-sha1="u324QYuQ1umNJoTwU6FwdK33iWS" width="134" height="183"></p>
<p>Many thanks!</p>
<p>Shane</p>

---

## Post #20 by @bpaniagua (2019-11-12 14:15 UTC)

<p>HI Shane,</p>
<p>Your shapes might be flipped after procalign because there is a flip in the parameterization.<br>
You should look at how the *spharm.vtk meshes with the phi color map look like. SPHARM-PDM has a way to flip them in a consistent way, see more info starting on slide 44 of our most recent spharm tutorial <a href="https://docs.google.com/presentation/d/1ZZ6UpONwTl_GKk66Kde9Brq0PIDujw2pKavm1RD1SBo/present?slide=id.p44">here</a>.</p>
<p>HTH<br>
Bea</p>

---

## Post #21 by @Shane_TANG (2019-11-15 01:17 UTC)

<p>Dear Bea and Martin, <a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/styner">@styner</a></p>
<p>Thanks for your answer! Following on Bea’s suggestion, I have quality controlled all the files and made sure that they are all aligned using phi color map. So, input the files, select one *_pp_surf_para.vtk as the spherical template, select mean model of all healthy subjects as the shape for visualizing the p-values. But I still got p-values in the range of 0.889 to 0.999, nothing significant.</p>
<p>I noticed some abnormalities in the <strong>pvalues.json</strong> file. I have 2 groups, same as the <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="nofollow noopener">example</a>, but I am afraid that the <em><strong>Covariate Significance Testing</strong></em> module assumes I only have 1 group instead of 2. To be more specific, in the <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="nofollow noopener">example</a>, the <strong>pvalues.json</strong> looks like this<br>
“Gpvals”: [[0.279, 0.256]],<br>
“clu_pvals”: [[0.026, 0.022]],<br>
“Lpvals_fdr”: [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [0.805, 0.8053], … ]</p>
<p>Like, they are paired which, I think, mean there are 2 groups. Whreas in my <strong>pvalues.json</strong> file,</p>
<p>“Gpvals”: [[0.412]],<br>
“clu_pvals”: [[1.0]],<br>
“Lpvals_fdr”: [[0.996], [0.999], [0.889], [0.899],…]</p>
<p>Is it that I’ve constructed the csv file in a wrong way? My csv file looks like this (2 columns):<br>
VTKfiles  class<br>
path-to-vtk       0<br>
path-to-vtk       0<br>
path-to-vtk       0<br>
path-to-vtk       1<br>
path-to-vtk       1<br>
path-to-vtk       1</p>
<p>Many thanks!</p>
<p>Shane</p>

---

## Post #22 by @bpaniagua (2019-11-18 14:28 UTC)

<p>Hi Shane,</p>
<p>Have you tried to include the full paths to your vtk files in the csv you are constructing?<br>
Are you able to run the examples data without trouble and see the two areas of significant p-values in the ellipsoid example?</p>
<p>Thanks,</p>
<p>Bea</p>

---

## Post #23 by @Shane_TANG (2019-11-18 23:42 UTC)

<p>Hi Bea, <a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/styner">@styner</a></p>
<p>Yes, the path used was the full path.</p>
<p>Yes, I am able to run the <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="noopener nofollow ugc">example </a>and have seen the two significant different areas (see pic below):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8616ef303af913cd7e56c5446ad4a2aae68e74.jpeg" data-download-href="/uploads/short-url/flcnfjYkhl1N1yUqLDkQtJ8Lc2w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8616ef303af913cd7e56c5446ad4a2aae68e74_2_112x187.jpeg" alt="image" data-base62-sha1="flcnfjYkhl1N1yUqLDkQtJ8Lc2w" width="112" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8616ef303af913cd7e56c5446ad4a2aae68e74_2_112x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8616ef303af913cd7e56c5446ad4a2aae68e74_2_168x280.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8616ef303af913cd7e56c5446ad4a2aae68e74_2_224x374.jpeg 2x" data-dominant-color="812329"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">554×942 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I found the pvalus.json file for this <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" rel="noopener nofollow ugc">example</a> after running on my computer looks like:<br>
“Gpvals”: [[0.0]],<br>
“clu_pvals”: [[0.0]],<br>
“Lpvals_fdr”: [[0.999], [0.999], [0.999], [0.0], [3.1578e-10], … ]<br>
In <em><strong>ShapePopulationViewer</strong></em>, I can see the attributes have <strong>distance</strong>,<br>
<strong>pvalue_0</strong>, <strong>betavalues_0_0</strong>, <strong>betavalues_0_1</strong>, <strong>betavalues_1_0</strong>, <strong>betavalues_1_1</strong>, <strong>betavalues_2_0</strong>, <strong>betavalues_2_1</strong></p>
<p>However, for my data, I just got<br>
<strong>pvalue_class</strong>, <strong>betavalues_0_class</strong>, <strong>betavalues_0_1</strong>, <strong>betavalues_1_class</strong>, <strong>betavalues_1_1</strong>, <strong>betavalues_2_class</strong>, <strong>betavalues_2_1</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/078fc8daa31f43dd885250a7e53a0bd54005a203.jpeg" data-download-href="/uploads/short-url/14ToL5RddWxA8k8C8PPTwfbiEvx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/078fc8daa31f43dd885250a7e53a0bd54005a203_2_259x200.jpeg" alt="image" data-base62-sha1="14ToL5RddWxA8k8C8PPTwfbiEvx" width="259" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/078fc8daa31f43dd885250a7e53a0bd54005a203_2_259x200.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/078fc8daa31f43dd885250a7e53a0bd54005a203_2_388x300.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/078fc8daa31f43dd885250a7e53a0bd54005a203_2_518x400.jpeg 2x" data-dominant-color="372B43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1252×966 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It seems that <strong>“class”</strong> substitutes <strong>“0”</strong> in my case. But the p-values in my case are still 0.95 to 0.99, nothing significant. I am so confused by this …<img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>
<p>Many thanks!</p>
<p>Best regards,</p>
<p>Yutao</p>

---

## Post #24 by @JON (2019-11-19 08:12 UTC)

<p>Hi all, and especially <a class="mention" href="/u/bpaniagua">@bpaniagua</a>,</p>
<p>I’m still struggling a bit with the shape analysis. It seems that I have the same problem as <a class="mention" href="/u/shane_tang">@Shane_TANG</a>. So I’m eagerly following this thread.</p>
<p>Furthermore, I’ve noticed the following two things:</p>
<ol>
<li>
<p>When I inspect the output dir of Step 3, I noticed that the *SPHARM_procalign.vtk’s are half the size of the *SPARHM.vtk’s. What is the reason for this? Seems a bit strange that the SPHARM’s that are procrustes aligned, contain less information. But I might be missing something here.</p>
</li>
<li>
<p>When I load the bump**.vtk of the example data for shape statistics I noticed that the attributes contain “distance”. However, when I load a *SPHARM.vtk in SlicerSalt from my own dataset, it does not contain the attribute “distance”. What might be happening here?</p>
</li>
</ol>
<p>Looking forward again to your reply!</p>
<p>Many thanks <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>Best,<br>
Jasper</p>

---

## Post #25 by @Shane_TANG (2019-11-19 20:58 UTC)

<p>Hi Jasper, <a class="mention" href="/u/jon">@JON</a></p>
<p>For 2, I actually cannot run that example on my Mac. My results above was run on a Windows 10 PC. You might want to try on windows system as I feel Slicer behaves differently on MacOS and Windows.</p>
<p>But I am still confused where I went wrong. It also seemed the module didn’t recognize that I have 2 groups…<img src="https://emoji.discourse-cdn.com/twitter/crying_cat_face.png?v=9" title=":crying_cat_face:" class="emoji" alt=":crying_cat_face:"></p>
<p>Many thanks!</p>
<p>Shane</p>

---

## Post #26 by @JON (2019-12-12 11:26 UTC)

<p>Hi all, <a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/thomshaw92">@thomshaw92</a> <a class="mention" href="/u/styner">@styner</a></p>
<p>I have another question regarding the output of the covariance significance testing module.<br>
I have a CSV file with 4 columns:</p>
<p>File (column 1), Group (column 2), Age (column 3), Gender (column 4)<br>
path/to/volume.vtk 1 49 1<br>
path/to/volume.vtk 0 51 1<br>
path/to/volume.vtk 1 37 1<br>
…</p>
<p>And the outputs contain three p-value attributes: pvalue_1, pvalue_2, pvalue_Group Age Gender</p>
<p>What do these three attributes mean? Is pvalue_1 the attribute for the p-values of the variable “Group” and pvalue_2 the attribute for the p-values of the variable “Age”, and pvalue_Group Age Gender the attribute for the pvalues of the interaction between group<em>age</em>gender? Or is it just for the third variable (i.e. gender)?</p>
<p>Looking forward to hearing from you.<br>
Many thanks in advance!</p>
<p>Best,<br>
Jasper</p>

---

## Post #27 by @Jared_Vicory (2019-12-12 21:01 UTC)

<p>Hi <a class="mention" href="/u/jon">@JON</a>,</p>
<p>Sorry about that, you’ve run into a bug in how the module uses the covariate names to name the data arrays. I’ve submitted a fix for this problem that should start showing up in the SlicerSALT nightly builds in the next few days (you can check out the <a href="https://github.com/Kitware/SlicerSALT/pull/208" rel="nofollow noopener">pull request</a> to monitor progress).</p>
<p>What’s happening currently is that all of the labels are getting incorrectly applied to the first covariate. So in your case, ‘pvalue_Group Age Gender’ should be the pvalue for Group, pvalue_1 is for Age, and pvalue_2 is for Gender.</p>
<p>Jared</p>

---

## Post #28 by @JON (2019-12-13 12:00 UTC)

<p>Hi <a class="mention" href="/u/jared_vicory">@Jared_Vicory</a>,</p>
<p>Thanks for your quick response. I will monitor the progress and get the latest build whenever it’s ready.</p>
<p>Best,<br>
Jasper</p>

---
