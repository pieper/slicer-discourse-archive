---
topic_id: 11979
title: "Modify Stl Files"
date: 2020-06-10
url: https://discourse.slicer.org/t/11979
---

# modify STL files

**Topic ID**: 11979
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/modify-stl-files/11979

---

## Post #1 by @jtwalther (2020-06-10 12:29 UTC)

<p>Hi all, I am pretty new to Slicer so I am not sure about all the functionality.<br>
I want do develop an extension so that I can load an STL file (which was created with Blender) into slicer, modify some parameters such as diameter, size(…) and export the new file as stl again. Has anyone an idea what might be the best way to do so? Maybe transform first into DICOM or nrrd format?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-06-10 12:32 UTC)

<p>This is certainly very doable, but there are so many options that we can only suggest “best” way to do it if we understand what you are trying to achieve. Can you be a bit more specific? Which body part, disease, etc. you are working with and what is the clinical goal? How do you decide in Slicer how to modify the model - by registering to an image? What kind of image?</p>

---

## Post #3 by @timeanddoctor (2020-06-11 02:49 UTC)

<p>If you just want change the size and place in slicer, you can apply the transform module and then hard it to export finally.</p>

---

## Post #4 by @jtwalther (2020-06-12 09:02 UTC)

<p>hey! thanks for the help.<br>
I am not working on a special disease. I am more interested in 3D printing. It is a research project. I have a stl model of lets say a cube with a hole through which shall one day be implemented to a pacient. I want to adjust the hole to a patients specific artery for example. Or change the edge length of the cube. Or if it is a round part change the diameter. So far I loaded the stl as segmentation into slicer and created a master volume in the segment editor. When I want to use the effects/tools in the segment editor I have to convert the file to binary labelmap. During that process slicer crushes and doesn’t respond any more. I am working with slicer 4.10.2 and tried it on an ubuntu and on a windows machine. Do you have an idea why?<br>
I will have a look at the transform module. I don’t know exactly how to use it yet but I will have a look at your tutorials<br>
Thanks!</p>

---

## Post #5 by @lassoan (2020-06-12 16:39 UTC)

<p>If you just need to position the model then there is no need to import it into a segmentation. Probably the easiest is to position it with landmarks: place markups fiducial points on the model; and corresponding points on the patient image, then use Fiducial registration wizard module (provided by SlicerIGT extension) to compute a transform that positions the model.</p>
<p>If you want to modify the model size then probably the easiest is to construct it in Slicer, by combining a few polydata sources.</p>
<p>You may find this example useful, it shows how to create a parametric model using VTK sources and even some simple positioning using fiducial points: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---
