---
topic_id: 885
title: "Group Analysis With Spharm Pdm"
date: 2017-08-16
url: https://discourse.slicer.org/t/885
---

# Group analysis with SPHARM-PDM

**Topic ID**: 885
**Date**: 2017-08-16
**URL**: https://discourse.slicer.org/t/group-analysis-with-spharm-pdm/885

---

## Post #1 by @laurapascal (2017-08-16 20:59 UTC)

<p>Interesting questions form Panos about group analysis with SPHARM-PDM tool:</p>
<hr>
<p><em>I am trying to compare regional differences in hippocampal structure between three groups (2 diseased groups, and one healthy control group), and I’m having some trouble with the pipeline.</em></p>
<p><em>I have volumetric binary files of the hippocampus for each subject (within each group). I used the Shape Analysis Module in SlicerSALT to process each one of those files, and the result was three subdirectories: Step1_SegPostProcess, Step2_GenParaMesh, and Step3_ParaToSPHARMMesh in my subject directory.</em></p>
<p><em>What would be the next step in order to statistically compare the regional differences between the three groups? Does SPHARM-PDM do the statistical analysis, or is there another software I should download? Also, do I need to create average volumes before I do any sort of statistical analysis or is the software itself going to take care of that?</em></p>
<hr>
<p>For now, in order to statistically compare the regional differences between two models, you can apply the module <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="nofollow noopener">ModelToModelDistance</a> (available as a module of 3DSilcer): it will compute a distance map between two models with the option <em>corresponding_point_to_point</em> (which will compute the distance euclidean for each corresponding point of your two models). You can then visualize the distance map in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ShapePopulationViewer" rel="nofollow noopener">ShapePopulationViewer</a> (available in SlicerSALT and 3DSlicer) by displaying the attribute <em>PointToPointVector</em>.</p>
<p>If you want to compare the average group models to each other, you should create an average model of each of your group by using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ShapeVariationAnalyzer" rel="nofollow noopener">ShapeVariationAnalyzer</a> (available as a module in 3DSlicer) before to apply ModelToModelDistance. The real purpose of this module is not really to compute mean of a population of models but it contains this option. First step is to create a CSV file by using the first tab of the module “Creation of CSV file” and then create your average models by using the tab “Compute of mean group”.</p>

---

## Post #2 by @pfotiad (2017-09-06 21:46 UTC)

<p>Hi Laura,<br>
Thank you for your response! I used the ShapeVariationAnalyzer module in SlicerSalt, and after exporting a csv file with the paths for each vtk file (of each subject in each group) and their corresponding group, I tried to compute the mean of each group.</p>
<p>Specifically:</p>
<ol>
<li>Under “Computation of mean groups” and “Selection of groups,” I selected the CSV file from the first step,</li>
<li>Pressed “Compute mean group,”</li>
<li>Selected the path for the exported csv file, and pressed “Export”</li>
</ol>
<p>However, the CSV file (with the mean shapes) that is created is basically an empty file, and I get an error in the terminal saying:<br>
— Compute the mean of all the group —<br>
Traceback (most recent call last):<br>
File “./ShapeVariationAnalyzer-master/ShapeVariationAnalyzer/ShapeVariationAnalyzer.py”, line 850, in onComputeMeanGroup<br>
self.logic.computeMean(group, listvtk)<br>
File “./ShapeVariationAnalyzer-master/ShapeVariationAnalyzer/ShapeVariationAnalyzer.py”, line 1866, in computeMean<br>
computeMean = slicer.modules.computemean<br>
AttributeError: ‘module’ object has no attribute ‘computemean’</p>
<p>Do you happen to know what might be causing this issue? Should I download another module (i.e. MeshMath) to compute the mean group?<br>
Thank you in advance once again for your time and help!</p>

---

## Post #3 by @bpaniagua (2017-09-07 13:36 UTC)

<p>Hi Panos,</p>
<p>Are you using ShapeVariationAnalyzer in the packaged version of SlicerSALT?<br>
The packages available <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5898b7ef8d777f07219fcb14">here</a>.</p>
<p>Thanks,<br>
Bea</p>

---

## Post #4 by @pfotiad (2017-09-07 15:06 UTC)

<p>Hi Bea,</p>
<p>Thank you for sending me the packaged version! I was actually not using the packaged version of SlicerSALT, just an older version where I had downloaded the ShapeVariationAnalyzer as an additional module.</p>
<p>However, I’m still running on an issue. When I add the paths of the three groups and try to export the csv, the software crashes. I even tried manually creating the csv file (using the older version of SlicerSALT) and loading it to the packaged software for preview, but it still crashed.</p>
<p>The error that comes up in the terminal is:<br>
“Cannot mix incompatible Qt library (version 0x40805) with this library (version 0x40807).”</p>
<p>I’ve seen this issue occur to others but I couldn’t find a solution online. (I’m using Centos 7.)<br>
Do you know if there is a workaround to fix that issue?</p>
<p>Thanks again for your time and help,<br>
Panos</p>

---

## Post #5 by @bpaniagua (2017-09-07 15:26 UTC)

<p>Yes, this is what I thought. I believe we need to contact the developers of the extension to see what is happening.</p>
<p><a class="mention" href="/u/juanprietob">@juanprietob</a>, Panos seems to be having problems using ShapeVariationAnalyzer in SlicerSALT.<br>
SlicerSALT uses the Slicer tag acf259a ([1] from three months ago) as basis. Do we need to update our Slicer tag to make it work with this extension?</p>
<p>Thank you!<br>
Bea</p>
<p>[1] (HEAD) BUG: Removed memory leaks using GetNodesByClass from Python (3 months ago) </p>

---

## Post #6 by @bpaniagua (2017-09-07 15:26 UTC)

<p>Also, <a class="mention" href="/u/pfotiad">@pfotiad</a>, have you tried to use ShapeVariationAnalyzer with the most recent Slicer nightly version?</p>
<p>Thank you!<br>
Bea</p>

---

## Post #7 by @pfotiad (2017-09-07 16:03 UTC)

<p>Hi Bea,</p>
<p>I just downloaded it to try it out! It unfortunately gives me the same incompatibility error as before, with the only difference being that now it says:<br>
"Cannot mix incompatible Qt library (version 0x40805) with this library (version 0x40806)“<br>
instead of<br>
"Cannot mix incompatible Qt library (version 0x40805) with this library (version 0x40807)”</p>
<p>Best,<br>
Panos</p>

---

## Post #8 by @stevenagl12 (2017-10-23 19:54 UTC)

<p>Can you do Procrustes analysis on objects with SPHARM? Or do you know if there is a different module that can do Procrustes analysis? Finally, can you also build statistical shape models with SPHARM?</p>

---

## Post #9 by @bpaniagua (2017-10-23 20:32 UTC)

<p>Hi Steven,</p>
<p>You can do procrustes analysis using SPHARM. You just have to use the regTemplate option in SPHARM-PDM. There is more information on how to do that in <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf">our detailed tutorial.</a></p>
<p>Thanks!<br>
Bea</p>

---

## Post #10 by @Suji_L_Lee (2019-07-23 11:19 UTC)

<p>Hi bea,</p>
<p>You mean this option below picture?<br>
“Registration Template Options”</p>
<p>Thank you in advance!<br>
Suji<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10d34fd77ad5d402f988fba432387f112b05ef4e.png" data-download-href="/uploads/short-url/2oQn8n5doX3IkdLQgHtB9jYBvMW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d34fd77ad5d402f988fba432387f112b05ef4e_2_663x500.png" alt="image" data-base62-sha1="2oQn8n5doX3IkdLQgHtB9jYBvMW" width="663" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d34fd77ad5d402f988fba432387f112b05ef4e_2_663x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d34fd77ad5d402f988fba432387f112b05ef4e_2_994x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d34fd77ad5d402f988fba432387f112b05ef4e_2_1326x1000.png 2x" data-dominant-color="DCE4E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1595×1202 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @bpaniagua (2019-09-16 15:20 UTC)

<p>Yes, that is the option that i meant.<br>
Sorry for the delay in replying.,</p>

---

## Post #12 by @Suji_L_Lee (2022-08-08 08:47 UTC)

<p>Hi <a class="mention" href="/u/bpaniagua">@bpaniagua</a> ,</p>
<p>Thank you for your response.</p>
<p>But do you have other way to compute mean group template in 3D Slicer?</p>
<p>Cause I cannot access the ShapeVariationAnalyzer in the latest version of 3D Slicer…</p>
<p>Best,<br>
Suji</p>

---
