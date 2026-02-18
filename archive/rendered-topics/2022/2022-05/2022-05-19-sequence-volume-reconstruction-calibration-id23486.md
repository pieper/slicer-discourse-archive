# Sequence volume reconstruction calibration

**Topic ID**: 23486
**Date**: 2022-05-19
**URL**: https://discourse.slicer.org/t/sequence-volume-reconstruction-calibration/23486

---

## Post #1 by @Karl-Philippe (2022-05-19 12:10 UTC)

<p>Hello,</p>
<p>I am trying to reconstruct a 3D ultrasound volume with the slicer volume reconstruction module. I can correctly apply the calibration matrix (image to probe) specified in the plus server configuration file (used to replay the .mha sequence file containing the tracked images) to reconstruct a volume. However, I observe some undersampling with live reconstruction (many iterations are needed to compose all the images in the volume). Considering this, I want to use the reconstruction of the recorded sequence to reconstruct the 3D ultrasound volume. However, the image-probe calibration matrix (specified in the aquisition and replay PLUS configuration files) is not applied in the .mha sequence metafile.</p>
<p>So my question is: how to apply the calibration matrix (image to probe) to a sequence metafile (.mha) to reconstruct a volume using the recorded sequence reconstruction mode of the Slicer volume reconstruction module?</p>
<p>Thank you,</p>
<p>Here is attached an example (Elbow example from IGT sample data) of the volume reconstruction from a sequence file where the calibration matrix is not applied.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d653e07e44b8a69da54ac36342483d648aa81163.png" data-download-href="/uploads/short-url/uA1SOIK7vHCgP0xgFPXoOFCLGin.png?dl=1" title="3D_reconstruction_from_sequence_example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653e07e44b8a69da54ac36342483d648aa81163_2_690x373.png" alt="3D_reconstruction_from_sequence_example" data-base62-sha1="uA1SOIK7vHCgP0xgFPXoOFCLGin" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653e07e44b8a69da54ac36342483d648aa81163_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653e07e44b8a69da54ac36342483d648aa81163_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653e07e44b8a69da54ac36342483d648aa81163_2_1380x746.png 2x" data-dominant-color="2A292C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_reconstruction_from_sequence_example</span><span class="informations">1920×1040 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2022-05-19 15:30 UTC)

<p>ImageToProbe calibration transforms are not normally recorded in sequence metafiles by Plus. You can copy and paste the calibration matrix into a new transform and use that for the parent transform of the image.</p>
<ul>
<li>
<p>Copy:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a21cb62fcf5cdd86d8fbf5607349e045cc413714.png" alt="image" data-base62-sha1="n86RBOpO7pxqHG4tvGPIVlyS0x6" width="170" height="190"></p>
</li>
<li>
<p>Paste:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9841572f6361cb35ed64ace59ae5633d94ea26e.png" alt="image" data-base62-sha1="sKGXvkYb7PbSPjAKPIHfc8DzDRA" width="529" height="424"></p>
</li>
</ul>

---
