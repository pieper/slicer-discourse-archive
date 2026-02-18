# Segmentation_atlas_template

**Topic ID**: 15780
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/segmentation-atlas-template/15780

---

## Post #1 by @sara_sharifi (2021-02-01 19:01 UTC)

<p>Operating system:7<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:<br>
Hi<br>
I  am looking for a method called Template or Atlas method that I can use in 3D Slicer software or ITK Snap software to segment kidney images in CT scan . Please help me and introduce me to other software for segmenting CT images and its algorithms<br>
(<a href="mailto:sharifisara7373@gmail.com">sharifisara7373@gmail.com</a>)<br>
Thank you</p>

---

## Post #2 by @lassoan (2021-02-02 04:09 UTC)

<p>This documentation page is a good starting point for image segmentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a>.</p>
<p>Nowadays classic atlas based methods are being replaced by neural networks. If you segment a few hundred images with manual/semi-automatic tools then you can use those to train a network that will segment similar images fully automatically (using for example <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#nvidia-ai-assisted-annotation-aiaa-for-3d-slicer">AIAA Segment Editor plugin</a>). Check out <a href="https://monai.io/">monai framework</a> for details and examples.</p>

---

## Post #3 by @sara_sharifi (2021-02-02 05:41 UTC)

<p>thanks,<br>
Thanks, now I have reset the 3D slicer program by mistake and now I can’t find any module. I installed some items in the extension section, but it didn’t work and I only see the Event Broker module. How should I fix it?</p>

---

## Post #4 by @lassoan (2021-02-02 13:50 UTC)

<p>Probably you need to delete your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">application settings</a>. If you know which extension caused the trouble then let us know and we can have a look.</p>

---
