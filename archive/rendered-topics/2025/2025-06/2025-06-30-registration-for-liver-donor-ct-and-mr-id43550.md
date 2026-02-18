# Registration for liver donor CT and MR 

**Topic ID**: 43550
**Date**: 2025-06-30
**URL**: https://discourse.slicer.org/t/registration-for-liver-donor-ct-and-mr/43550

---

## Post #1 by @MinHo_Shin (2025-06-30 19:26 UTC)

<p>Dear community,</p>
<p>I am a hepatobiliary surgeon using 3D Slicer for preoperative planning. Until now, I have been segmenting the portal vein, hepatic vein, and liver parenchyma from the <em>delayed phase</em> of a CT scan for liver resection.</p>
<p>Currently, I am preparing for living liver donor surgeries and would like to perform 3D reconstruction of the liver hilum using:</p>
<ul>
<li>Arterial and portal phases of CT (same session)</li>
<li>T2-weighted MR image acquired on a different date (to delineate the biliary structures)</li>
</ul>
<p>However, registration has been extremely challenging, likely due to differing origin points and voxel spacing between the CT and MRI scans. I am not necessarily looking for an automatic registration method — I don’t mind a time-consuming or manual process — I just need a reliable way to align the CT and MRI so they can exist on the same coordinate system and allow accurate reconstruction.</p>
<p>Could anyone share a recommended workflow or technique in 3D Slicer (or any module/tool) to achieve this?</p>
<p>Thank you very much in advance for your help.</p>
<p>Best regards,</p>

---

## Post #2 by @pieper (2025-06-30 23:19 UTC)

<p>I’m not sure what you’ve tried so far, but if the patient is in close to the same position in both the MR and CT scan then you should get a reasonable registration with something like these steps (images and files are from some data from the SampleData module for illustration).</p>
<ul>
<li>
<p>In the Data module, right click one of the volumes, say the CT</p>
</li>
<li>
<p>Select “register this” in the context menu<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0d72aa32e39883d6c10ed670522576acb2712e8.png" data-download-href="/uploads/short-url/pep1FPBRckx6tNUgF3QGGgQm4QM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d72aa32e39883d6c10ed670522576acb2712e8_2_690x416.png" alt="image" data-base62-sha1="pep1FPBRckx6tNUgF3QGGgQm4QM" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d72aa32e39883d6c10ed670522576acb2712e8_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0d72aa32e39883d6c10ed670522576acb2712e8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0d72aa32e39883d6c10ed670522576acb2712e8.png 2x" data-dominant-color="ECF0EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">862×520 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>then right click on the MR and in the registration menu pick rigid registration<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f7c990ac7dde24aece58983e68168ee1d62cf77.jpeg" data-download-href="/uploads/short-url/mKSRMhZzFmBQKNuSF1lvUE9lq6P.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f7c990ac7dde24aece58983e68168ee1d62cf77_2_690x226.jpeg" alt="image" data-base62-sha1="mKSRMhZzFmBQKNuSF1lvUE9lq6P" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f7c990ac7dde24aece58983e68168ee1d62cf77_2_690x226.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f7c990ac7dde24aece58983e68168ee1d62cf77_2_1035x339.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f7c990ac7dde24aece58983e68168ee1d62cf77_2_1380x452.jpeg 2x" data-dominant-color="B8BEC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1536×504 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>This will take you to General Registration with the volumes pre-selected and a transform created</p>
</li>
<li>
<p>Pick one of the alignment options, probably Geometry Align if the livers are roughly in the model of the scans.</p>
</li>
<li>
<p>Click apply and in a few seconds it should</p>
</li>
<li>
<p>To check, go back to the Data module.  Click on “eye” column for the CT so it will be displayed in all slice views<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33b7f0bb046837e6c39f8472e73a9d8aebe6145b.png" alt="image" data-base62-sha1="7nwrmFWLu99LunAgPSIeiT56xNV" width="60" height="62"></p>
</li>
<li>
<p>Right click on the “eye” for the MR and pick “show in slice views as foreground”</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18e14269285004805be77a6281cf9bfd5ec5ecf6.png" data-download-href="/uploads/short-url/3y64FHQenJe56hnItUTuU4ELAAC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18e14269285004805be77a6281cf9bfd5ec5ecf6_2_690x147.png" alt="image" data-base62-sha1="3y64FHQenJe56hnItUTuU4ELAAC" width="690" height="147" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18e14269285004805be77a6281cf9bfd5ec5ecf6_2_690x147.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18e14269285004805be77a6281cf9bfd5ec5ecf6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18e14269285004805be77a6281cf9bfd5ec5ecf6.png 2x" data-dominant-color="C7CACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">722×154 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This should show you the images aligned.</p>
<p>If they don’t line up well, one common issue is too few samples.  You can go back to the General Registration and change the Percentage from the default to a larger number.  Maybe just going to 0.02 is enough but even going to 1% or more will not add too much compute time and can really improve the results.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/530a31e69dc9fd0e7db823004b1dc791264c661e.png" alt="image" data-base62-sha1="bQBtizy9fRiMcE1G62V3F5t0Syq" width="690" height="46" data-dominant-color="E7E7E7"></p>
<p>If the livers are very differently shaped in the two scans due to breathing or patient pose, you might try a nonlinear transform.  The steps are basically the same.</p>

---
