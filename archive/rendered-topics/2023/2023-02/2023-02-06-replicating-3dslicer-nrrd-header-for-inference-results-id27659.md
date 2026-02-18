# Replicating 3Dslicer nrrd header for inference results

**Topic ID**: 27659
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/replicating-3dslicer-nrrd-header-for-inference-results/27659

---

## Post #1 by @m_takahashi (2023-02-06 13:46 UTC)

<p>Hello all</p>
<p>I have created an AI model for organ segmentation. The models input and output are a 2D CT slice and a 2D mask array. These 2D arrays are then joined into a 3D array for the whole CT series.</p>
<p>I used 3D Slicer to generate the annotations which were used for training (seg.nrrd).</p>
<p>Now I would like to view my inferences on 3D slicer along with the original input (the CT series) so I can eventually edit them.</p>
<p>I have managed to rudimentary replicate the seg.nrrd  header and create nrrds that work well with slicer for most series. Some of them however will not register perfectly. The way I managed to fix this so far was oppening the series in 3D slicer, creating a mock seg.nrrd and then copying the important header information (space origin and others) and this fixes my problem.</p>
<p>My question is, is there any way to automatically replicate what the 3dslicer software does to create the seg.nrrd file?<br>
I have been searching through simpleitk and <a href="http://slicer.io" rel="noopener nofollow ugc">slicer.io</a> but have not found the answer for this yet.<br>
I did try getting some information from simpleitk GetOrigin and get GetSpacing functions (calling it on the loaded complete series) but outputs were different from the 3DSlicer software header.</p>
<p>Thank you very much</p>

---

## Post #2 by @lassoan (2023-02-08 11:49 UTC)

<p>Image geometry is specified by origin, spacing, and axis directions. You need to make all these match in the image and segmentation.</p>

---
