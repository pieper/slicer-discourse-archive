# LPS/RAS to voxel

**Topic ID**: 29256
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/lps-ras-to-voxel/29256

---

## Post #1 by @kulasbart (2023-05-02 18:48 UTC)

<p>Hello,</p>
<p>I am trying to convert a set of RAS coordinates (.fcsv) exported from slicer, into voxel units. Ideally, I would like to do this on python as part of a workflow…</p>
<p>I’m using matmul with the coordinates [X,Y,Z] and the affine from the .nii file header of my registered image…</p>
<p>voxel_coords = [np.round(np.linalg.inv(affine) @ np.array(ras_coord).T) for ras_coord in ras_vals]</p>
<p>The coordinates are correctly spaced and seem to even be on the same plane , but there is some misalignment with the original image. Seems to be a translational problem, I’m thinking it has to do with the last row of my affine matrix, or a field of view issue? Or did I miss a step?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46f87e5f82ff7680e5fede5cfc89bf23083e42fb.png" data-download-href="/uploads/short-url/a7POIOzK9PKDbvFwbcbSfjOmHuX.png?dl=1" title="Screen Shot 2023-05-02 at 11.42.24 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46f87e5f82ff7680e5fede5cfc89bf23083e42fb_2_605x499.png" alt="Screen Shot 2023-05-02 at 11.42.24 AM" data-base62-sha1="a7POIOzK9PKDbvFwbcbSfjOmHuX" width="605" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46f87e5f82ff7680e5fede5cfc89bf23083e42fb_2_605x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46f87e5f82ff7680e5fede5cfc89bf23083e42fb_2_907x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46f87e5f82ff7680e5fede5cfc89bf23083e42fb.png 2x" data-dominant-color="444444"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-05-02 at 11.42.24 AM</span><span class="informations">1024×846 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,<br>
Bart</p>

---

## Post #2 by @lassoan (2023-05-02 18:58 UTC)

<p>See the Python code snippet that does this [here] (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" class="inline-onebox">Script repository — 3D Slicer documentation</a>). If you do this outside Slicer then there will be no transformation on the volume.</p>
<p>Pay attention to the coordinate system used in the file. In current Slicer versions it is LPS by default, so you can directly use it with the IJK to LPS matrix that is stored in the image header. If markup points are in RAS then you need to convert.</p>
<p>I would not recommend using fcsv files. They are not standard CSV. Best is to save as markup json instead, as you can reead/parse the file with a single line of code and you get easy access to all point coordinates a d all metadata in a Python object. If you want to process using Excel macros (not recommended) you can save as proper CSV by exporting the markups to a table node first (in Markups module).</p>

---

## Post #3 by @kulasbart (2023-05-02 22:02 UTC)

<p>Hi Andras. Appreciate your help on this. I will export as .json</p>
<p>My markups are in LPS format, I used the inv(affine) matrix which I got from the nifti file — nib.load(‘file.nii’).affine — is this the image header matrix you are referring to? This gave me the offset result in the screenshot</p>
<p>Regarding the script snippet you linked me: how do I create a volumeNode object in python? I have been looking around and it looks like I may need to use slicer.ScriptedLoadableModule or slicer.utils in this step? I assume I need to pass the .nii file</p>
<p>It would be helpful to know volumeNode.GetRASToIJKMatrix(volumeRasToIjk)</p>
<p>Best,<br>
Bart</p>

---

## Post #4 by @kulasbart (2023-05-02 22:06 UTC)

<p>I can also try to be more clear on what I’m trying to do here:</p>
<ul>
<li>I’ve labeled a set of markup coordinates on a CT image (.nii)</li>
<li>Using the markups export file (LPS format), I’m trying to get the coordinates of the markups in the voxel space of the CT</li>
</ul>

---

## Post #5 by @lassoan (2023-05-03 00:10 UTC)

<p>NIFTI format is very problematic. There are two ways to define IJK to LPS transformation (sform and qform) and not always clear which one should be used and how. Also, NIFTI uses RAS internally, so depending on what library you use to read the header and what options, you might get IJK to RAS.</p>
<p>To eliminate one source of error, I would recommend to save as NRRD format instead.</p>
<p>You can get IJK from LPS in a NRRD file using Python (outside Slicer’s Python environment) as shown <a href="https://discourse.slicer.org/t/building-the-ijk-to-ras-transform-from-a-nrrd-file/1513/2">here</a>.</p>

---

## Post #6 by @kulasbart (2023-05-03 17:44 UTC)

<p>Thanks Andras, very resourceful.</p>
<p>I will look into using NRRD format.</p>
<p>Temporarily, a simple fix was flipping the x,y coordinates from RAS to LPS to match the seega output.</p>

---
