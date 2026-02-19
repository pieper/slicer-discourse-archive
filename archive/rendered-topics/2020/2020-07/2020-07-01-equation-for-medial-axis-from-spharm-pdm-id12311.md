---
topic_id: 12311
title: "Equation For Medial Axis From Spharm Pdm"
date: 2020-07-01
url: https://discourse.slicer.org/t/12311
---

# Equation for medial axis from SPHARM-PDM

**Topic ID**: 12311
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/equation-for-medial-axis-from-spharm-pdm/12311

---

## Post #1 by @christinah (2020-07-01 01:57 UTC)

<p>Operating system: MacOS Catalina<br>
Slicer version: 4.10.2</p>
<p>Hi there,</p>
<p>I’ve been using SPHARM-PDM and first want to say a really, truly huge thank you – both for the tool and for the extremely helpful Google slide tutorial, great answers to posts on here, and other documentation.  I’m a cell biologist and have managed to use the tool to analyze the shape of tomograms of single parasitic cells, which is pretty amazing!  I’ve also been able to import the meshes that SPHARM generated into FEM software for some fluid dynamics simulations.  I tried so many things (and kept failing) before I stumbled on Slice and SPHARM… so you can imagine how grateful I feel to your team!</p>
<p>Second, I have a quick question. Is there some clever way to extract the medial axis line as a list of x, y, z coordinates?  For the FEM simulations I mentioned above, I’d like to find an equation for the medial axis so that I can use it to define a coordinate system. I might fit a curve to x, y, z coordinates in matlab, for example.  (If not, maybe I need to work harder to figure out how to do this starting with the .vtk file.)</p>
<p>Thanks so much for any advice!  Apologies if this question is eye-rolling-ly simple <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Best,<br>
Christina</p>

---

## Post #2 by @christinah (2020-07-02 23:50 UTC)

<p>Quick update: as an alternative to extracting details about the medial axis and using that to set up a coordinate system for subsequent FEM simulations, maybe I could figure out how to use the mapped spherical coordinates already used for SPHARM’s central algorithm.  Is there a way to access those, if the original idea in the post above is not possible?</p>
<p>There are text files with a long 1D list of phi’s and theta’s in the output folder from SPHARM mesh generation, which I know are used as color maps in the Shape Population viewer, but I’m not sure how to make use of those. Is there a way to obtain the actual spherical mapping information used during the SPHARM process?</p>
<p>Again, thank you very, very much for any help or tips!  I am pretty stuck.</p>
<p>Best,<br>
Christina</p>

---

## Post #3 by @bpaniagua (2020-07-03 12:37 UTC)

<p>Hi Christina</p>
<p>For the medial axis you can use the parameterization derived medial axis that is produced as part of SPHARM, please <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3630372/">check this paper</a> and  <a href="https://docs.google.com/presentation/d/1ZZ6UpONwTl_GKk66Kde9Brq0PIDujw2pKavm1RD1SBo/present?slide=id.p40">slide 40</a> in the tutorial.</p>
<p>These files containing 1D vectors of the spherical parameterizations are a legacy file that we used on a Shape Population Viewer look alike program before. If you are using the SPHARM-PDM module within SlicerSALT (SPHARM-PDM generator) the phi and theta 1D color maps will be automatically mapped into the mesh and the unit sphere. If you want to do the mapping, you will have to use <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Modules/CLI/MetaMeshTools/MeshMath.cxx">MeshMath</a>, specifically the KWMToPolyData function.</p>
<pre><code>MeshMath &lt;vtkIn&gt; &lt;vtkOut&gt; -KWMtoPolyData &lt;txtFileIn&gt; &lt;nameScalarField&gt;   Writes a KWM scalar field (N Dimensions) into a PolyData Field Data Scalar to visualize in Slicer"

MeshMath fileIn.vtk fileOut.vtk -KWMtoPolyData phi.txt PhiFieldName
</code></pre>
<p>MeshMath is currently compiled within Slicer when you install the SPHARM-PDM extension, and available in the SALT package, please let me know if you need instructions on how to use it from there!</p>
<p>HTH<br>
Bea</p>
<p>ps. I almost miss your question! Please post SPHARM-PDM questions into the <a href="https://discourse.slicer.org/c/community/slicer-salt">SALT subforum the next time</a>, so me or somebody else within the SALT team can help you <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"> .</p>

---

## Post #4 by @christinah (2020-07-03 19:20 UTC)

<p>Dear Beatriz,</p>
<p>Thank you very much for your reply. Also, thanks for letting me know that I should be posting in the SALT subforum!  Will do next time.</p>
<p>For the medial axis: thanks so much, yes, I have the .vtk file for the parameterization derived medial axis from SPHARM. I’m interested in obtaining the xyz coordinates of that axis (and finding an analytic equation to describe it, which I can use to generate a coordinate system for fem simulations). If that makes sense, do you have any advice about extracting the medial axis coordinates?  Thank you very, very much!  Possibly this is a very simple question, and I’m missing something… maybe the info is already in the vtk datafile below, and I just don’t know how to read it?</p>
<p>“ASCII<br>
DATASET POLYDATA<br>
POINTS 100 float<br>
-100.422 -310.532 34.3645 -100.303 -310.377 34.5271 -99.9777 -309.886 34.9144<br>
-99.4429 -309.069 35.4893 -98.6939 …”</p>
<p>On the second topic of extracting the actual spherical mapping matrix (which maps a given phi, theta on a sphere to its corresponding x, y, z in “real space”): thank you for point me to MeshMath!  I’ll work on understanding the code and see if I can figure out how to get the mapping matrix/algorithm out using it.</p>
<p>Many thanks for your help. Have a great holiday weekend,<br>
Christina</p>

---

## Post #5 by @bpaniagua (2020-07-06 13:58 UTC)

<p>Hi Christina,</p>
<p>The POINTS field in that vtk file should include 300 float values that are the x,y,z tuples for all your coordinates.</p>
<p>You can either use <a href="https://vtk.org/Wiki/VTK/Examples/Cxx/PolyData/PolyDataGetPoint">vtk functions</a> to read those points, or just parse the ascii polydata manually.</p>
<p>HTH<br>
Bea</p>

---
