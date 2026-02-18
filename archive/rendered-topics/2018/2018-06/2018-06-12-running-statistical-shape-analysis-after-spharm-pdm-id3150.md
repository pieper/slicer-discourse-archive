# Running statistical shape analysis after SPHARM-PDM

**Topic ID**: 3150
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/running-statistical-shape-analysis-after-spharm-pdm/3150

---

## Post #1 by @doganarda (2018-06-12 13:13 UTC)

<p>Hello everyone,</p>
<p>I am using SPHARM-PDM to represent several subcortical structures (mainly Hippocampus and Caudate) and use the SPHARM coefficients in SVM classification. However, I would really like to apply some statistical analysis after the structures are reconstructed using SPHARM parametrization (meshfiles from ParaToSPHARMMesh) and I was looking through various papers that has utilized SPHARM representations in their shape analyses (Gerig et. al. 2001a, Styner et. al. 2004, Styner et. al. 2006, Geardin et. al. 2017) and it seems to me that SPHARM-PDM toolbox offers the calculation of statistical maps through StatNonParamTestPDM or ShapeAnalysisMANCOVA.</p>
<p>However, the problem is I cannot find a way of how to use and I am mainly interested in StatNonParamTestPDM. I am using Slicer 3D for Shape Analysis Toolbox and perfectly happy with its ability to calculate SPHARM coefficients and ellipse aligned PDM-reconstructed mesh files but I cannot find anything in Slicer 3D as to how to run statistical analysis. I have done a somewhat extensive google search and still was unable to find any useful information.</p>
<p>I have seen a topic in the old forum about comparison between StatNonParamTestPDM and ShapeAnalysisMANCOVA (<a href="https://www.nitrc.org/forum/message.php?msg_id=12180" rel="nofollow noopener">https://www.nitrc.org/forum/message.php?msg_id=12180</a>) and I looked through all messages which contained no info whatsoever regarding actually how to use. In addition, I came accross a forum post titled download and installation of MANCOVA (<a href="https://www.nitrc.org/forum/message.php?msg_id=12890" rel="nofollow noopener">https://www.nitrc.org/forum/message.php?msg_id=12890</a>) which was talking about SPHARM-PDM toolbox and some packages inside - from there I found download links (<a href="https://www.nitrc.org/frs/?group_id=308#" rel="nofollow noopener">https://www.nitrc.org/frs/?group_id=308#</a>, <a href="https://www.nitrc.org/projects/shape_mancova/" rel="nofollow noopener">https://www.nitrc.org/projects/shape_mancova/</a>) both saying that StatNonParamTestPDM and ShapeAnalysisMANCOVA are contained in SPHARM-PDM toolbox. I dont know exactly what this toolbox is or how to get it and if I have it or not with Slicer 3D (I have Slicer Salt too but could not find any statistical analysis module there either). After downloading SPHARM-PDM v1.3, as well as BatchMake Bmm files and StatParamTestPDM, I could not see how I can do anything about the files that I downloaded (I use linux so I downloaded accordingly). Even though they seem as executable files, I cannot run them, clicking on them do nothing.</p>
<p>Finally, I found ShapeAnalysisMANCOVA-master file which contained cpp files like converting vtk to itk and StatNonParamTestPDM as well as ShapeAnalysisMANCOVA. Even thought at first they seemed right files and I just needed to run those cpp files through my terminal, there were missing headers and as a person who is not really experienced with cpp I could not solve it (I tried to run vtk to itk conversion so that I can try StatNonParamTestPDM but it said that in the header file that is called from the main cpp code, there is another header missing namely vtkPoints.h which was indeed included in the header file). I tried to run the cmake txt file with cmake, but I got few errors there too.</p>
<p>So long story short, I was trying really hard to carry out statistical analysis after getting the SPHARM-PDM reconstructed mesh files from SPHARM coefficients but I could not figure out a way of how to use StatNonParamTestPDM (my main aim is to use this) or MANCOVA, nor was I able to find any useful help/guide in google. Can anyone please help me with how to carry out these statistical analysis? Just how to run the programs.</p>
<p>Thank you very much in advance,<br>
Sorry for the long post,<br>
Best regards,<br>
Arda</p>

---

## Post #2 by @Kailiang_Wang (2018-06-20 02:21 UTC)

<p>Dear experts:<br>
i have the same question!!!<br>
I have performed the analysis of SPHARM-PDM 3D-slicer4.8 using the ShapeAnalysis_Data_Example in MCA_OS. But I can’t find any valid tool to go on comparing these two groups in slicer of MAC_OS, and I don’t know what to do! Can you help me! I am beginner to SPHARM-PDM in MCA_OS. Many thanks in advance!</p>

---

## Post #3 by @lassoan (2018-06-20 03:31 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> could you help with this?</p>

---
