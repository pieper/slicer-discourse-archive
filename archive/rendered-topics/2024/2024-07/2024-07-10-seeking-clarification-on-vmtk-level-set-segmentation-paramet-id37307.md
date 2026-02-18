# Seeking Clarification on VMTK Level Set Segmentation Parameters and Behavior

**Topic ID**: 37307
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/seeking-clarification-on-vmtk-level-set-segmentation-parameters-and-behavior/37307

---

## Post #1 by @tuingc159 (2024-07-10 14:47 UTC)

<p>Hi all,</p>
<p>I am currently working with VMTK for level set segmentation on ultrasound data and have encountered several issues and questions regarding parameter adjustments and their impact. I implemented my workflow in Python and used VTI format files for my data. I would appreciate any insights or clarifications from the community. Here are the details:</p>
<p><strong>1. Minimal Differences with Parameter Changes:</strong></p>
<ul>
<li>When extracting segmentations for different parameter settings after evolution, there were no significant differences in the results.</li>
<li>I adjusted parameters such as iterations, propagation, curvature, and advection, but observed minimal differences in the segmentation outcomes.</li>
<li>When using the test data and pytest provided with the package, there are differences in segmentation outcomes.</li>
</ul>
<p><strong>Question:</strong> Why do parameter adjustments seem to have little effect on my final segmentation results, despite following the same procedures that yielded varying results with the test data?</p>
<ul>
<li>For example, when using geodesic level set type and extreme derivative sigma values for the gradient feature image, relative to my voxel resolution (sigma value 1.0 compared to a voxel resolution of 1e-4), the feature image showed minimal gradients. Despite this, the segmentation results remained consistent (as when using a sigma of 1e-4).<br>
I am puzzled as to how the segmentation process can be effective under these conditions, given that it uses the feature image during evolution.</li>
</ul>
<p><strong>Question:</strong> How does the segmentation process remain effective with large sigma values relative to voxel resolution, given the minimal gradients in the feature image?</p>
<p><strong>2. Different level set types:</strong><br>
I experimented with different types of level sets (e.g., Laplacian versus geodesic gradient) without observing differences in segmentation outcomes. I couldn’t find documentation detailing these different types of level sets.</p>
<p><strong>Question</strong>: What are the differences between the various types of level sets (e.g., Laplacian versus geodesic gradient), and where can I find documentation on these?</p>
<p>Any insights or suggestions on these issues would be greatly appreciated. Thank you!</p>

---
