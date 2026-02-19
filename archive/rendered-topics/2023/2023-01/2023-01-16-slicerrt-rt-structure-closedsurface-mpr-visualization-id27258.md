---
topic_id: 27258
title: "Slicerrt Rt Structure Closedsurface Mpr Visualization"
date: 2023-01-16
url: https://discourse.slicer.org/t/27258
---

# SlicerRt RT Structure ClosedSurface MPR visualization

**Topic ID**: 27258
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/slicerrt-rt-structure-closedsurface-mpr-visualization/27258

---

## Post #1 by @sani1486 (2023-01-16 09:27 UTC)

<p>Hello,<br>
I am trying to visualize RT structure data as a Closed Contour representation in my own application in a Three 2D view, and i checked SlicerRT implementation on it,  So basically i copied the</p>
<blockquote>
<p>vtkPlanarContourToClosedSurfaceConversionRule.cxx</p>
</blockquote>
<p>codes, passed my RT structures polydata into the Convert function of the file, and it did give me the target representation, which i believe should be a closed surface representation, And i also checked in Slicer this representation is displayed using a vtkPlaneCutter , Now my problem is when i use my original poly data and pass it to vtkPlaneCutter it visualizes the polydatas exactly the way slicer does, (with lots of little dots with different colors), but when i pass the target representation polydata to vtkPlaneCutter , vtk throws an error saying there is no output from vtkPlaneCutter. I would like to know , is this how Slicer does it? Pass the target represntation to the vtkPlanecutter? I tried to debug and find out , but failed to set up debugging,. Any insight on how the closed surface is visualized in slicer ? i tried to check the code in segmentation module and saw vtkImageData is also being used , but i think its for labelmap representation. not the default closed surface representation. so should i do any other post processing after i get the target representation from convert function, and then pass it to vtkplanecutter ?</p>

---

## Post #2 by @cpinter (2023-01-16 11:09 UTC)

<p>Please use the infrastructure. We spent an immense amount of time developing it (answering hundreds of questions during the work just like your question), so better make use of it rather then reimplementing parts of it.</p>
<p>Load the RTStruct using SlicerRT, then you’ll immediately get a closed surface representation in the segmentation node that is created.</p>
<p>See some info on segmentation nodes here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a><br>
More details in paper: <a href="https://www.sciencedirect.com/science/article/pii/S0169260718313038?casa_token=5dhe33DcA54AAAAA:kHkW3LYAViKRXp_MQ_q8PYMPPezpik6yC2-5t5gNO5iwHNdqqchufpVjHv-6QRwfz5Dhi12SXg" class="inline-onebox">Polymorph segmentation representation for medical image computing - ScienceDirect</a><br>
Even more details in thesis: <a href="https://qspace.library.queensu.ca/handle/1974/26422" class="inline-onebox">Dynamic Representation of Anatomical Structures in Radiation Therapy Treatment Planning and Evaluation</a><br>
Please note that the paper and the thesis do not contain some new features such as layer support in binary labelmaps.</p>

---
