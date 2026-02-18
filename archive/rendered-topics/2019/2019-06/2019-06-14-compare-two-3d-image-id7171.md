# Compare two 3d image

**Topic ID**: 7171
**Date**: 2019-06-14
**URL**: https://discourse.slicer.org/t/compare-two-3d-image/7171

---

## Post #1 by @safa (2019-06-14 16:45 UTC)

<p>Is there a way to compare two nifti images, to find the difference in them ?</p>

---

## Post #2 by @lassoan (2019-06-14 17:48 UTC)

<p>There are many tools in Slicer that can help you in comparing volumes.</p>
<p>You can also set one volume as foreground, the other as background and fade between them (Ctrl + Mouse-click-and-drag up/down).</p>
<p>You may find “Layer Reveal Cursor” in Compare Volumes useful.</p>
<p>If you segment one of the image with a simple global thresholding in Segment Editor module and show that over the other image then you get a very clear view of what moved and how much. If you segment objects of interest, you can compute quantitative metrics about their displacement by using Segment Comparison module in SlicerRT extension.</p>
<p>You may register the two volumes (using “General Registration (BRAINS)” module or SlicerElastix extension) and visualize the resulting transform using Transforms module.</p>

---

## Post #3 by @safa (2019-06-15 01:19 UTC)

<p>when I compare between these two images I want obtain a result as histogram form or a table or …<br>
that shows where is  exactly the difference between these two images</p>

---

## Post #4 by @lassoan (2019-06-15 02:01 UTC)

<p>To see where, what directions, and how much structures have moved perform spatial registration and use Transforms module to visualize the displacement.</p>
<p>For quantitative analysis, you can segment the structures of interest and use Segment comparison module in SlicerRT extension.</p>

---

## Post #5 by @kevin.x (2020-10-01 01:26 UTC)

<p>Hi Iassoan,</p>
<p>Could you explain more about the comparison and visualisation of two 3d volume? I’m new to 3d slicer and am not familiar with the operations of the modules.<br>
Actually, I segmented a 3D CT image and now I have 3 volumes: the original CT image (A), the labelled ground truth (B), and the segmentation image ©. I want to compare (B) and © and visualize them within one window. It will be better if different colours can be assigned to True Positive, False Positive, True Negtive and False Negtive voxels. Is it possible??</p>
<p>Much appreciated!</p>

---

## Post #6 by @lassoan (2020-10-08 22:10 UTC)

<p>For visual comparison, see <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#interacting-with-views">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#interacting-with-views</a></p>
<p>For quantitative metrics, you can convert the labelmap volume to segmentation and compare using Segment Comparison module (provided by SlicerRT extension).</p>

---
