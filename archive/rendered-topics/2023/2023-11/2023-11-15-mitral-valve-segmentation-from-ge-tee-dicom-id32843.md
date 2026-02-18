# Mitral valve segmentation from Ge TEE Dicom

**Topic ID**: 32843
**Date**: 2023-11-15
**URL**: https://discourse.slicer.org/t/mitral-valve-segmentation-from-ge-tee-dicom/32843

---

## Post #1 by @KatellD (2023-11-15 19:25 UTC)

<p>Hi all,<br>
I am trying to segment a mitral valve from 3D TEE for reseach purposes and the software seems to not recognize the different axis (axial, sagittal, coronal).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4847e0cc1dfa42eeb407c89056f4410fbdd8805c.jpeg" data-download-href="/uploads/short-url/ajqnjqI5DlzyKxdhz0GNULiBZfK.jpeg?dl=1" title="Capture d'écran 2023-11-15 132855" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4847e0cc1dfa42eeb407c89056f4410fbdd8805c_2_690x337.jpeg" alt="Capture d'écran 2023-11-15 132855" data-base62-sha1="ajqnjqI5DlzyKxdhz0GNULiBZfK" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4847e0cc1dfa42eeb407c89056f4410fbdd8805c_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4847e0cc1dfa42eeb407c89056f4410fbdd8805c_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4847e0cc1dfa42eeb407c89056f4410fbdd8805c_2_1380x674.jpeg 2x" data-dominant-color="2F2F36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d'écran 2023-11-15 132855</span><span class="informations">1916×937 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After multiple attempts to restore the Dicom frame in their original axis with SlicerHeart, I found this old topic (<a href="https://discourse.slicer.org/t/issue-with-3d-tee-from-ge-vivid-e95-in-3d-slicer/13642" class="inline-onebox">Issue With 3D TEE from GE Vivid E95 in 3D Slicer</a>) where the advices were either to install Image3dAPI or check if the Dicom were correctly exported. I exported the DICOM directly from the US system (GE Vivid95) with the only way possible to make sure of the input and I also install Image3dAPI. As I am waiting for the response of the Ge’s team for the license needed to use Image3DAPI, I wanted to make sure that is was due to the fact that the Dicom aren’t in CartesianDicom and that it could be fixed with this extension.<br>
Do you know if it’s possible to convert Ge dicom into cartesian dicom with Image3DAPI or with another sofware in order to extract a .stl fil of a mitral valve?</p>
<p>Thank you in advance for you help !</p>

---

## Post #2 by @lassoan (2023-11-15 19:30 UTC)

<p>The images that you loaded contain just a screen capture (2D video) of the rendering. These pictures do not contain any 3D information.</p>
<p>Once you manage to export images that contain 3D data (in a way that is compatibel with Image3dAPI) you can load that into Slicer, visualize in 3D, and create .stl of the mitral valve. It really all just depends on the GE software having the right export options.</p>

---

## Post #3 by @KatellD (2023-11-15 21:33 UTC)

<p>Thank you for you answer !<br>
However, I was wondering if in any case you would know how to extract 3d data from Ge US Machine as I export them as Dicom via the Dicom Usb channel and I checked multiple times and I didn’t found any other export options.</p>

---
