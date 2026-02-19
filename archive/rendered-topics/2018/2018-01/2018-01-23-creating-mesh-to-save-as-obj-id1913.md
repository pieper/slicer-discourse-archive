---
topic_id: 1913
title: "Creating Mesh To Save As Obj"
date: 2018-01-23
url: https://discourse.slicer.org/t/1913
---

# Creating mesh to save as .obj

**Topic ID**: 1913
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/creating-mesh-to-save-as-obj/1913

---

## Post #1 by @nirotu (2018-01-23 16:13 UTC)

<p>Operating system: MAC<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello:</p>
<p>Iam a new comer to Slice. I would like to create a mesh of vessel (from MRI data) and would like to save as .obj file for export in to modeling software.  Can someone help me how I can go about creating mesh and save as .obj?</p>
<p>Thank you in advance!<br>
nirotu</p>

---

## Post #2 by @Frederic (2018-01-23 16:34 UTC)

<p>Hi Nirotu,<br>
This <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">page</a> could help you.<br>
Best.</p>

---

## Post #3 by @lassoan (2018-01-23 16:48 UTC)

<p>You can also use VMTK extension’s <code>Vesselness filtering</code> module for enhancing vessel visibility on the images. You may be able to extract vessels by simple thresholding of the vesselness image (followed by speckle removal using Islands effect / Keep largest island options; and Smoothing effect).</p>
<p>Once you are done with segmentation, you can export the segment to a Model node (using Segmentations module), which can be saved as an .obj file.</p>

---

## Post #4 by @nirotu (2018-01-23 18:17 UTC)

<p>Hi Andres:</p>
<p>Thank you so very much.  Is there a tutorial that walks me through VMTK routine?</p>
<p>Thanks</p>
<p>Anil N. Shetty, Ph.D.<br>
Associate Professor<br>
Division of Maternal Fetal Medicine<br>
Baylor College of Medicine<br>
TCH Pavilion for Women<br>
6651 Main Street, Suite 1020-04<br>
Houston, TX 77030</p>
<p>832-826-7312 (Off)<br>
832-825-9351 (Fax)</p>

---

## Post #5 by @cpinter (2018-01-23 19:08 UTC)

<p>There’s this tutorial. It’s quite old and it shows an overly simple case, but it shows you how it’s done<br>
</p><div class="lazyYT" data-youtube-id="DJ2032yo5Co" data-youtube-title="SlicerVmtk4 in action: Lung CT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
