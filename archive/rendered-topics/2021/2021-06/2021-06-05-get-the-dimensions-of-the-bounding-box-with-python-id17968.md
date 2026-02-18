# Get the dimensions of the bounding box with python

**Topic ID**: 17968
**Date**: 2021-06-05
**URL**: https://discourse.slicer.org/t/get-the-dimensions-of-the-bounding-box-with-python/17968

---

## Post #1 by @jmhuie (2021-06-05 18:08 UTC)

<p>Hi, I am trying to create an annotation ROI that is the size of the bounding box using python. I’m envisioning two main steps but I can’t quite figure out how to do all of it (in python).</p>
<ol>
<li>Adjust the 3D bounding box to be the smallest box around everything in the scene (similar to the reposition button)</li>
<li>Create an annotationROI that matches the dimensions and position of the bounding box.</li>
</ol>
<p>I know there is code in the script repository for the reposition button but getting the dimensions of the bounding box is the biggest challenge for me right now. Any help would be appreciated. Thanks!</p>

---

## Post #2 by @lassoan (2021-06-05 18:42 UTC)

<p>You can iterate through all display nodes in the scene and get the bounds of each node that is visible in your selected view. However, it would be probably more generally usable if you allowed the user to select a subset of nodes, e.g., those in a selected folder in Data module. What do you plan to use this ROI for?</p>
<p>Annotation ROI nodes are being phased out, replaced by markups ROI nodes. I would recommend to create markups ROI nodes. Their main advantage is that they can be rotated, you can define measurements on them, you can customize their appearance and behavior.</p>

---

## Post #3 by @jmhuie (2021-06-07 21:59 UTC)

<p>Thanks Andras. The ROI would be used to “crop” and extend the boundaries of a volume using the Crop Volume module. To provide some context, for my second moment of area module a user might need to apply a linear transformation on the segment. If they are not careful, the segment may be translated outside of the bounds of the original volume and the calculations will not be done on sections of the segment that are outside. In some scenarios, if the volume itself is very small (i.e., the user cropped the volume before segmenting) then it may be impossible to fit the segment inside the bounds of the volume. In which case, extending the bounds are necessary.</p>
<p>Initially, I had the idea of setting up my module to automatically do the cropping so that the user no longer needed to worry about being inside or outside of the bounds. However, I realized that may be unnecessarily intensive from a computational perspective. Instead, I now think it might be more useful to include a button that toggles a markup ROI or some sort of box on and off to show the volume’s bounds and rely on the user to translate their segment and crop if necessary.</p>

---

## Post #4 by @lassoan (2021-06-07 22:44 UTC)

<p>Volume node can compute bounds even for non-linearly transformed volumes. Crop volume module can automatically compute the extended bounds of a ROI (both annotation ROI and markups ROI, even if rotated). Label statistics can compute rotated oriented bounding box that you can directly use as input in the new Markups ROI.</p>
<p>So, there should be no need to reimplement any ROI computations, just need to chose the one that is closest to what you need.</p>

---
