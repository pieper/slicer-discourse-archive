# 3D Assessment of Mandibular asymmetry

**Topic ID**: 533
**Date**: 2017-06-19
**URL**: https://discourse.slicer.org/t/3d-assessment-of-mandibular-asymmetry/533

---

## Post #1 by @Pilar (2017-06-19 22:04 UTC)

<p>Hello 3DSlicer experts,<br>
I am a PhD Student, working on my PhD project.<br>
My goal is to measure the volume of the asymmetry using segmented mandibles (comparing one hemimandible with the other one).<br>
Following the tutorials I found on the website of DCBIA team, I have done the segmentation and the mirroring image with the software ITK-SNAP, the landmark approximation and the voxel based registration relative to the cranial base, the construction of the surface models and the quantification of the changes using a Color Map.<br>
But I was not able to find any tutorial about how to use SPHARM-PDM shape analysis for doing the statistics and I am having some challenges using color maps for quantification and also using a kind of reference to split the mandible in two halves.<br>
Can anybody help me to figure it out?</p>
<p>Looking forward to hearing from you.</p>

---

## Post #2 by @bpaniagua (2017-06-21 12:04 UTC)

<p>Hello Pilar,</p>
<p>Sorry for the delay in replying. We have put together a <a href="https://github.com/bpaniagua/SPHARM-PDM/blob/add-Tutorial2017/Modules/Scripted/ShapeAnalysisModule/Resources/Doc/SPHARM-PDM-Tutorial.pdf">new and updated SPHARM-PDM tutorial</a>. That should help you understanding how to run the updated SPHARM-PDM. SPHARM-PDM can be used as part of SlicerCMF, Slicer and it is currently a module of <a href="http://salt.slicer.org/">SlicerSALT</a>.</p>
<p>We are currently developing an updated ShapeStatistics module. It is currently possible to run our shape statistics methodology as matlab scripts and we are in the process of updating those scripts to Slicer modules.</p>
<p>Could you please describe what are your challenges for color map quantification?</p>
<p>What we have used in the past to split the mandibles are just based on landmarks, usually the mid-point between tmj condyles and the chin. This can be done using first Q3dc and then easy clip.</p>
<p>I hope that helps!<br>
Best regards,</p>
<p>Bea</p>

---

## Post #3 by @Pilar (2017-06-21 17:04 UTC)

<p>Hello Beatriz,<br>
Thank you for your kind and useful response.</p>
<p>So, if I understood it correctly, the first thing I must do is to locate the landmarks using Q3DC and then get the hemimandibles using the Easy Clip tool.<br>
I believe that I have to do this with the original CBCT and the mirror image models separately, in order to locate the mid-sagittal plane in each of them and then perform the color map. Is it that correct?</p>
<p>On the other hand, when I get both hemimandibles models and try to do the color map, I am not sure what I have to choose in Distance, in the Input/Output menu:<br>
-signed_closest_point<br>
-absolute_closets_point<br>
-corresponding_point_to_point</p>
<p>Thank you so much for your help.</p>
<p>Best</p>
<p>Pilar</p>

---

## Post #4 by @bpaniagua (2017-07-07 13:34 UTC)

<blockquote>
<p>On the other hand, when I get both hemimandibles models and try to do the color map, I am not sure what I have to choose in Distance, in the Input/Output menu:<br>
-signed_closest_point<br>
-absolute_closets_point<br>
-corresponding_point_to_point</p>
</blockquote>
<p>It depends of your input data. If you have the same number of points on the hemimandibles to compare, its corresponding_point_to_point. If not, its the closest point measurements, he signed closest point distance will give you directionality and magnitude of distance, the absolute measurement only magnitude.</p>
<p>Hope that helps!</p>

---

## Post #5 by @Pilar (2017-07-11 19:51 UTC)

<p>Got it. I will figure it out.</p>
<p>Thank you so much Beatriz</p>
<p>Best</p>
<p>Pilar</p>

---

## Post #6 by @Pilar (2017-07-18 22:03 UTC)

<p>Dear Dr Paniagua,</p>
<p>I have other questions about the following steps I have to do.<br>
As I told you in previous emails, I have done the segmentation and the mirroring image with the software ITK-SNAP, the landmark approximation and the voxel based registration relative to the cranial base, the construction of the surface models and the splits of the mandibles.<br>
To create the Colormap, I chose the mirroring image as Source model and the original CBCT as Target model. Is that step correct?<br>
I did that because in the DCBIA tutorials, when they are using the ModelToModelDistance tool, they chose the Model T2 as VTK File 1and Model T1 as VTK File 2, but in the 3DSlicer version I use, the names are Source and Target model instead of VTK File 1 and 2 as in the tutorials.</p>
<p>After doing that, I only could use the option absolute_closets_point because:</p>
<ul>
<li>The option signed_closets points creates a colormap with the same distances in every point (1), so the colormap has only one color, no matter the value I choose in every arrow, the range goes to 1 to 1</li>
<li>The option corresponding_point_to_point gives me error</li>
</ul>
<p>Once I get the Colormap and following the steps in the tutorial you told me, I am not sure the parameters I have to choose in the Shape Analysis Module to get the results I need (know if there are asymmetries between one hemimandibule and the other one). Could you guide me a little bit?</p>
<p>I suppose I have to do the following:</p>
<ul>
<li>Input file: the colormap I have created</li>
<li>Output file: I have to create 3 folders (number 1 for SegPostProcess, 2 forGenMeshPara and 3 for ParaToSPHARMMesh)<br>
and the next steps you explain.</li>
</ul>
<p>The problem is that I don’t understand the Advanced Parameters to SPHARM Mesh tab that are necessary in my project.</p>
<p>Looking forward to hearing from you, I really appreciate your help.</p>
<p>Best</p>
<p>Pilar</p>

---

## Post #7 by @bpaniagua (2017-08-10 13:00 UTC)

<p>Hi Pilar,</p>
<p>Sorry for the delay in replying.</p>
<blockquote>
<p>To create the Colormap, I chose the mirroring image as Source model and the original CBCT as Target model. Is that step correct?</p>
</blockquote>
<p>It really depends on what is the source model you want your vectors and distances to start from. This will determine the directionality in case you are doing signed distance computation, and in case you want to visualize vectors. Here are some examples that indicate how the selection of the source model will create distances and vectors oriented towards the target and how that will influence the sign of your distances.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3e283cee0292571e528fc6eefa96c4629339bef.jpeg" alt="image1" data-base62-sha1="nnN8hqpSI1Y4EkiYgqhgwv8mQxN" width="640" height="480"></p>
<p>So you basically choose what you want to show. I think when we did asymmetry studies we chose the original CBCT as source and the mirrored as target, but that should not matter as far as you are aware of how distances are computed when you are to report them.</p>
<blockquote>
<p>The option signed_closets points creates a colormap with the same distances in every point (1), so the colormap has only one color, no matter the value I choose in every arrow, the range goes to 1 to 1</p>
</blockquote>
<p>Do you see different magnitudes on the absolute_closest_point option? That is certainly weird. Would you be willing to send some snapshots or to share an example of your data to debug?</p>
<blockquote>
<p>The option corresponding_point_to_point gives me error</p>
</blockquote>
<p>Yes, unless you have the same number of points on both meshes you will not be able to use this option for the computation of measurements.</p>
<blockquote>
<p>Once I get the Colormap and following the steps in the tutorial you told me, I am not sure the parameters I have to choose in the Shape Analysis Module to get the results I need (know if there are asymmetries between one hemimandibule and the other one).</p>
</blockquote>
<p>Shape Analysis Module is only to represent a group of shapes with the same number of points (correspondence computation). If you wish to do so, there is a <a href="https://github.com/bpaniagua/SPHARM-PDM/blob/add-Tutorial2017/Modules/Scripted/ShapeAnalysisModule/Resources/Doc/SPHARM-PDM-Tutorial.pdf">new tutorial</a> that indicates how you can use your input meshes or input segmentations to calculate a correspondent version of your shapes for analysis using (for example) the option of corresponding_point_to_point in ModelToModel distance.</p>
<p>If you wish to visualize the closest_point (either signed or absolute) distances and vectors (these will always be the same for both of those options) you can use ShapePopulationViewer. Load your source model, that includes the distances/vectors computed with ModelToModel distance. You can also use our other quantification tools: MeshStatistics or Pick and Paint in case you are interested on specific areas of your mesh.</p>
<p>I hope that helps.<br>
Thank you,</p>
<p>Bea</p>

---

## Post #9 by @Pilar (2017-08-10 22:22 UTC)

<p>Hi Dr Beatriz,<br>
Thank you for your kind replying. Everything is really helpful.</p>
<pre><code>	Do you see different magnitudes on the absolute_closest_point option? That is certainly weird. Would you be willing to send some snapshots or to share an example of 		your data to debug?
</code></pre>
<p>I send you a snapshot of ShapePopulationViewer tool when I choose signed_closest_point and when I choose Absolute_closest_point, just in case I am doing something wrong.</p>
<p>SIGNED_CLOSEST_POINT</p>
<p>ABSOLUTE_CLOSEST_POINT</p>
<p>I am having problems trying to send you the .vtk files of my sample to let you debug them because they are too big, even though I tried to compress them. How can I do it?</p>
<p>Looking forward to hearing for you, I really appreciate your help.</p>
<p>Pilar</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca93cd0ce396aa1df9ef1ef21773867f146e54cf.png" data-download-href="/uploads/short-url/sU56TjQoqzOtVjwQbQ0IpnSL4Pt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca93cd0ce396aa1df9ef1ef21773867f146e54cf_2_690x439.png" alt="image" data-base62-sha1="sU56TjQoqzOtVjwQbQ0IpnSL4Pt" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca93cd0ce396aa1df9ef1ef21773867f146e54cf_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca93cd0ce396aa1df9ef1ef21773867f146e54cf_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca93cd0ce396aa1df9ef1ef21773867f146e54cf.png 2x" data-dominant-color="81768F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1253×798 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00801b0fe70d1c7a2c8f339547a8108e148a01a7.png" data-download-href="/uploads/short-url/4qsQj9LUOmusgmcBoaqshyLD27.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00801b0fe70d1c7a2c8f339547a8108e148a01a7_2_690x437.png" alt="image" data-base62-sha1="4qsQj9LUOmusgmcBoaqshyLD27" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00801b0fe70d1c7a2c8f339547a8108e148a01a7_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00801b0fe70d1c7a2c8f339547a8108e148a01a7_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00801b0fe70d1c7a2c8f339547a8108e148a01a7.png 2x" data-dominant-color="7B758E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1249×792 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @bpaniagua (2017-08-11 13:48 UTC)

<p>Hi Pilar</p>
<p>I see what the problem might be. The second snapshot looks reasonable. In the first snapshot you only are displaying the normal vectors, not the signed distances. Normal vectors are unit vectors that have a magnitude of 1. Can you please click in the attributes menu and see what are the data fields available?</p>
<p>Thank you!<br>
Bea</p>

---

## Post #11 by @Pilar (2017-08-11 14:46 UTC)

<p>Hi Beatriz,</p>
<p>I send you a snapshot choosing the signed distances in the attributes menu. Yes, I believe I have the positive and negative distances now.</p>
<p>I have another question, how can I save this file to use it to do the analysis afterwards?</p>
<p>Thank you so much for your help.</p>
<p>Pilar</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d800588818a6f8ab1cd95c66c17a65d23de52cf.png" data-download-href="/uploads/short-url/dl8GLzux5aShPUxLTXGiHS1Au9V.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d800588818a6f8ab1cd95c66c17a65d23de52cf_2_690x469.png" alt="image" data-base62-sha1="dl8GLzux5aShPUxLTXGiHS1Au9V" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d800588818a6f8ab1cd95c66c17a65d23de52cf_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d800588818a6f8ab1cd95c66c17a65d23de52cf_2_1035x703.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d800588818a6f8ab1cd95c66c17a65d23de52cf_2_1380x938.png 2x" data-dominant-color="66647F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1415×962 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @bpaniagua (2017-08-11 18:23 UTC)

<p>Hi PIlar,</p>
<p>The values that are used to generate the color maps are already part of the vtk file that you obtain from ModelToModel distance. What type of analysis did you have in mind?</p>
<p>Thank you,<br>
Bea</p>

---

## Post #13 by @Pilar (2017-08-11 19:38 UTC)

<p>Hi Dr Beatriz,</p>
<p>I was thinking in doing the SPHARM-PDM analysis (as you usually do) to calculate the differences between both hemimandibles and then compare all of the different skeletal classes (I, II, III) to establish if there is a bigger incidence of asymmetry depending on the skeletal class and the facial pattern of the patient.</p>
<p>I thought that I had to use the colormap file after doing the ShapePopulationViewer application but, if I understood you correctly, they are two different tasks, I mean, I can do the ShapePopulationViewer to obtain the figures and then apply the SPHARM-PDM analysis, following the tutorial you sent me, to get the values to do the statistic analysis. Using the Colormap.vtk file I got as the Input file, is it correct?</p>
<p>Thank you so much,</p>
<p>Pilar</p>

---

## Post #14 by @bpaniagua (2017-08-14 13:23 UTC)

<p>Hi Pilar,</p>
<p>The colormap you have calculated via closest point is already the input for some of the analysis that we provide through SlicerCMF. You could compare descriptive statistics of the colormaps accross those different skeletal classes.</p>
<p>SPHARM-PDM will help you compute a new representation for your hemimandibles in which all of them will have the same number of points. The input for that analysis is either the 3D models computed from the segmentations or the segmentations themselves. The output will be new 3D models that you will be able to use in a similar manner than your non-corresponding initial 3D models, you can run ModelToModelDistance, Pick and Paint and MeshStatistics, but you can also use ShapeAnalysisMANCOVA (a equality of means type of test that uses 3D model data with the same number of points instead of unidimensional variables).</p>
<p>I hope that helps,<br>
Bea</p>

---

## Post #15 by @Pilar (2017-08-14 19:35 UTC)

<p>Hi Dr Beatriz,</p>
<p>Thank you so much for your support. That really helped me a lot.</p>
<p>I will let you know if I have further questions.</p>
<p>Best regards,</p>
<p>Pilar</p>

---

## Post #16 by @Pilar (2017-09-20 18:59 UTC)

<p>Hi Dr Beatriz,</p>
<p>I still have some doubts getting the statistics.<br>
If I am interesting in doing just the descriptive statistics, I should use the colormap files with the Mesh Statistics tool.</p>
<ol>
<li>Don’t I need to use Pick and paint to create landmarks if I want to measure the entire model, do I?</li>
<li>I should choose the signed points to obtain the 3D distances (and then I have to compare the results between the different skeletal classes to know in which one the asymmetry is more prevalent or bigger). Am I right?</li>
<li>What’s the point in choosing PointToPointAlongZ, Y and X? Is it to identify the area where the asymmetry is more important?</li>
</ol>
<p>Thank you so much in advance for your support.</p>
<p>Pilar</p>

---

## Post #17 by @bpaniagua (2017-09-20 19:37 UTC)

<p>Hi Pilar</p>
<blockquote>
<p>Don’t I need to use Pick and paint to create landmarks if I want to measure the entire model, do I?</p>
</blockquote>
<p>No you dont need to use pick and paint if you want compute your stats over the entire model, that is only necessary if you want your descriptive statistics computed for a region of interest.</p>
<blockquote>
<p>I should choose the signed points to obtain the 3D distances (and then I have to compare the results between the different skeletal classes to know in which one the asymmetry is more prevalent or bigger). Am I right?</p>
</blockquote>
<p>Yes, that is one way to do it. Just confirming, do all your hemimandibles have the same number of points? Your descriptive statistics will be computed over a certain number of points (number of 3D distances for hemimandible) and if you want to compare descriptive statistics from model to model (avg from model 1 to avg from model 2) they should have the same number of points otherwise I imagine statistics would become hairy. I am not an statistician, probably best checking this with an expert.</p>
<blockquote>
<p>What’s the point in choosing PointToPointAlongZ, Y and X? Is it to identify the area where the asymmetry is more important?</p>
</blockquote>
<p>Those metrics are computed from your 3D vectors, they are the projections of your vector into the X, Y and Z axis. If your data is aligned in medical coordinates a high value of X will be an asymmetry in the Left-Right axis, of Y in the Posterior-Anterior axis and Z in the Superior-Inferior axis. It might depend on the scanner, at least this is what our scanners alignment. The might be useful to detect direction specific differences in your problem.</p>
<p>I hope that helps!<br>
Best,</p>
<p>Bea</p>

---

## Post #18 by @Pilar (2017-09-21 10:42 UTC)

<p>Hi Dr Beatriz,</p>
<p>I am not sure if all of my hemimandibles have the same number of points?<br>
How can I know it? Do I have to use SPHARM-PDM to compute a new representation of my hemimandibes with the same numbers of points as you explained to me in previous emails?</p>
<p>Thank you!!</p>
<p>Pilar</p>

---

## Post #19 by @bpaniagua (2017-09-25 13:58 UTC)

<p>Hi Pilar,</p>
<p>Do you run SPHARM as part of your processing pipeline? I cant recall right now.<br>
Thank you!</p>
<p>Bea</p>

---

## Post #20 by @Pilar (2017-09-25 14:53 UTC)

<p>Hello Dr Beatriz,</p>
<p>After doing the segmentation and the mirroring image, I superimposed both files using voxel based registration. After that, I created the 3D models and using Q3DC, Angle Planes and Easy clip, I got the hemimandible models.<br>
The colormap I have calculated via closest point is already the input file I got with the Model To Model Distance tool.</p>
<p>I was thinking in using SPHARM as part of my processing pipeline following the protocol used in the bibliography I found, but just if it is necessary to get the descriptive statistics.</p>
<p>Thank you</p>
<p>Pilar</p>

---

## Post #21 by @bpaniagua (2017-09-25 16:12 UTC)

<p>Hi Pilar,</p>
<p>I see, well then I would double check with somebody that can confirm that comparing summary statistics computed from populations with different number of values is correct.</p>
<p>Best,<br>
Bea</p>

---

## Post #22 by @Pilar (2017-09-25 16:31 UTC)

<p>Great!!</p>
<p>Thank you so much Dr Beatriz.<br>
Looking forward to hearing from you.</p>
<p>Pilar</p>

---

## Post #23 by @Pilar (2017-10-23 16:07 UTC)

<p>Hi Dr Beatriz,<br>
could you figure it out how to do the statistics?</p>
<p>Looking forward to hearing from you.</p>
<p>Best</p>
<p>Pilar</p>

---

## Post #24 by @bpaniagua (2017-10-23 17:28 UTC)

<p>Hi Pilar,</p>
<p>I am sorry you are still struggling with this.<br>
My suggestion was along the lines “if i were you, I would figure out…” so there is probably a misunderstanding… I did not say I would figure it out, but suggested you talk to a statistician about it.</p>
<p>Do you need some ideas for names?</p>
<p>Thank you,<br>
Bea</p>

---

## Post #25 by @Pilar (2017-10-23 17:40 UTC)

<p>Hi Dr Beatriz,</p>
<p>Sorry for the misunderstanding.<br>
Yes, could you please tell some statistics who can help me? Thank you so<br>
much</p>
<p>Pilar</p>
<p>El El lun, oct. 23, 2017 a las 7:38 p. m., Beatriz Paniagua &lt;<br>
<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; escribió:</p>

---

## Post #26 by @danila (2020-06-02 14:16 UTC)

<p>Hi Dr Beatriz,<br>
I have a similar problem, and I don’t know how to solve it. Could you help me?</p>
<p>My goal is to measure the linear and volumetric change of a jaw before and after an orthognathic surgery (therefore comparing the pre and post CBCT).</p>
<p>Following the tutorial I found on the DCBIA team website, I made the segmentation of the anterior skull base at t0 and t1 with the ITK-SNAP software.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aad3db73a45cd7102c0a680cc2a28f92a356af2.png" data-download-href="/uploads/short-url/8n4Rm4L7IFrSOsU1Qh4u5X6BfHQ.png?dl=1" title="immagine 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_690x431.png" alt="immagine 1" data-base62-sha1="8n4Rm4L7IFrSOsU1Qh4u5X6BfHQ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_1380x862.png 2x" data-dominant-color="2D382D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 1</span><span class="informations">2880×1800 577 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I do the landmarks approximation about the two scans with Slicer and subsequently the recording performed on voxel relating to the skull base (using: basaline scan - T1; basaline segmentation - segmentation of anterior skull base at T1; follow-up scan - T2landmarks; follow-up segmentation - segmentation of skull base at T2landmarks).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f.jpeg" data-download-href="/uploads/short-url/wWvSfhqMX0e4WAmcHe59ouhgZGL.jpeg?dl=1" title="immagine 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_690x431.jpeg" alt="immagine 2" data-base62-sha1="wWvSfhqMX0e4WAmcHe59ouhgZGL" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_1035x646.jpeg 1.5x" data-dominant-color="9A9AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 2</span><span class="informations">2880×1800 733 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After the registration I have segmented the first mandible on the t1 scan and the second mandible on the t2 scan obtained from the voxel recording. Then I transformed the segmentations of the two mandible into 3D surface models. I uploaded the two models on Slicer and I apply the module “model to model distance”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e208f1dc2dd32060dd82b6f403f47ca380431cc.png" data-download-href="/uploads/short-url/dqGDER1gMdaTyHRcCtOyoKy9l9O.png?dl=1" title="immagine 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_690x431.png" alt="immagine 4" data-base62-sha1="dqGDER1gMdaTyHRcCtOyoKy9l9O" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_1380x862.png 2x" data-dominant-color="B6BAD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 4</span><span class="informations">2880×1800 784 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I use the module “Shape Analysis Viewer” to obtain a color map.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de.png" data-download-href="/uploads/short-url/1l9LFRA5Msnincwqen12E3gjC9g.png?dl=1" title="immagine 5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_690x382.png" alt="immagine 5" data-base62-sha1="1l9LFRA5Msnincwqen12E3gjC9g" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_1380x764.png 2x" data-dominant-color="6B6286"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 5</span><span class="informations">2880×1598 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I would like to take a statistic analysis about this, but I don’t know how I can do. Can you help me?</p>
<p>The flow that I have use is correct?</p>
<p>Thanks again for the support.</p>

---

## Post #27 by @lili-yu22 (2022-02-27 23:58 UTC)

<p>if l split the mandible unevenly， after spharm pdm，how can l know the difference is because the uneven split or the growth，thank you</p>

---

## Post #28 by @lili-yu22 (2023-12-12 07:39 UTC)

<p>can anyone help me to solve this question</p>

---
