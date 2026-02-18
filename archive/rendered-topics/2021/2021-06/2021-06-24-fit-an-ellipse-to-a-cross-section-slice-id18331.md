# Fit an ellipse to a cross-section slice

**Topic ID**: 18331
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/fit-an-ellipse-to-a-cross-section-slice/18331

---

## Post #1 by @joannecallow (2021-06-24 18:31 UTC)

<p>Hello. I was wondering if there is a way to fit an ellipse to a cross section slice? I have a shape that is close to an ellipse, but not perfect. I would like to fit an ellipse to the structure and find the major and minor axes. Is this possible?</p>

---

## Post #2 by @lassoan (2021-06-24 18:44 UTC)

<p>You can get the center and principal axis directions of the ellipse (or ellipsoid, cylinder, …) using Segment Statistics module. Just enable centroid and principal axis metrics in Advanced / Labelmap statistics / Options. You can do all this programmatically in Python as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment">here</a>.</p>
<p>However, in Slicer you can do much more. You can solve not just this one step of your workflow, but most likely you can implement the entire analysis pipeline. For example, you can extract and quantify entire vascular networks (and get vessel diameter along cross-sections orthogonal to the centerline). If you describe what the clinical task and what approach you are planning to achieve it then we can give more specific advice.</p>

---

## Post #3 by @joannecallow (2021-06-24 19:11 UTC)

<p>Thank you so much for your help. I have segmented an Achilles tendon and would like to measure thickness of the tendon orthogonal to the centreline along the minor axis of the ellipse. An ellipse will not perfectly fit the tendon, but will be able to give a direction for my thickness measurement. So if there is a way to visually see the ellipse on the image, I could go in with the ruler tool and measure along the minor axis where the tendon slice begins and ends.</p>

---

## Post #4 by @joannecallow (2021-06-24 19:22 UTC)

<p>I was also wondering if there is a way to find segment statistics at multiple slices along the segment? I can do it if I have multiple different segments. But, in order to get the measurements orthogonal to the centreline I need to fill between slices, find the centreline and use the curved planar reconstruction to adjust the planes. But, if I fill between slices segment statistics just gives me a centroid of the whole segment, but I am interested in the centroid and principal axis of each individual slice going up the tendon.</p>

---

## Post #5 by @lassoan (2021-06-24 20:21 UTC)

<p>You can straighten the tendon using the transform computed by the Curved planar reformat module. This takes care of measuring in cross-sections orthogonal to the centerline.</p>
<p>Then, you can write a few-line Python script that assigns a different label to each slice of the segmentation (using basic numpy array operations), and then use Segment Statistics module to get per-slice metrics. If you need principal axis directions in the original image space then you can apply the inverse of thr straightening transform to the computed centroid and principal axes.</p>
<p>If you confirm on a few examples that this workflow is good then you can write a Python script that fully automates the workflow.</p>

---

## Post #6 by @joannecallow (2021-06-24 20:54 UTC)

<p>Thanks Andras. I am wondering how to read the principal axis directions. It gives three different points for each axis. How does this translate into a directions? And how do I find the length from this? The image below shows the distance I am interested in for each slice (red line). The image is a cross sectional slice of the tendon.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef1f361871a9c93fb12d068124d4acc806a4dbc3.png" alt="Screen Shot 2021-06-24 at 1.39.13 PM" data-base62-sha1="y7mZ5JgEzDlgsWZpMoKDQhyV8sz" width="254" height="288"></p>

---

## Post #7 by @lassoan (2021-06-26 01:39 UTC)

<p>Each triplet specify axis direction in RAS coordinate system.</p>
<p>The simplest is to use oriented bounding box axis directions and size.</p>
<p>If you go with the principal axes then you need to implement diameter measurement along those axes. For example, you can step through the voxels of the segmentation node along those directions and find the two farthest point of the segment. Or you can use Line Profile module in Sandbox extension to get samples along that line in a table and just count the number of nonzero values in the table and multiply with the sampling distance to get the diameter.</p>

---
