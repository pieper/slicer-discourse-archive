# How to import the nifti file of HCP842 Tractography Atlas to 3DSlicer as label maps?

**Topic ID**: 7102
**Date**: 2019-06-10
**URL**: https://discourse.slicer.org/t/how-to-import-the-nifti-file-of-hcp842-tractography-atlas-to-3dslicer-as-label-maps/7102

---

## Post #1 by @shahrokh (2019-06-10 10:31 UTC)

<p>Dears 3DSlicer developers:</p>
<p>How can I use <strong>HCP842 Tractography Atlas</strong> to extract “fiber bundles” in DWI images.<br>
I want to use 80 regions segmented in this atlas as “Label Maps” in UKF Tractography.</p>
<p>I must mentioned that I get this atlas HCP842 Tractography from the folder with the name of <strong>Atlas</strong> in <strong>DSI Studio software</strong> (<strong>HCP842_tractography.nii.gz</strong>). In this file, the brain is segmented in 80 regions:<br>
0	Acoustic_Radiation_L<br>
1	Acoustic_Radiation_R<br>
2	Cortico_Striatal_Pathway_L<br>
3	Cortico_Striatal_Pathway_R<br>
4	Cortico_Spinal_Tract_L<br>
5	Cortico_Spinal_Tract_R<br>
…<br>
77	CNVIII_R<br>
78	CNX_L<br>
79	CNX_R</p>
<p><strong>My ultimate goal is that</strong> I want to do all the steps tractography in “DSI Studio” software in 3DSlicer which includes in the following steps:</p>
<p>1- Import DWI images.</p>
<p>2- Normalize these images with Tractography atlases such as HCP842.</p>
<p>3- Exact fiber bundles based on the regions segmented in this atlas.</p>
<p>4- Get these fiber bundles registered with DWI images.</p>
<p>Thanks a lot.<br>
Shahrokh.</p>

---

## Post #2 by @shahrokh (2019-06-11 15:03 UTC)

<p>Hi<br>
Is there any way to solve this problem?<br>
Please guide me.<br>
Shahrokh.</p>

---

## Post #3 by @pieper (2019-06-11 20:48 UTC)

<p>Hi Shahrokh -</p>
<p>That all seems reasonable.  Are you comfortable with the features of <a href="http://dmri.slicer.org/" rel="nofollow noopener">SlicerDMRI</a>?  If you can import your DWI and the atlas grayscale you should be able to register them and resample the atlas labels into your subject space and then use the labels as seeds for tractography.</p>
<p>Have you been able to give it a try?  What step’s not working?</p>
<p>-Steve</p>

---
