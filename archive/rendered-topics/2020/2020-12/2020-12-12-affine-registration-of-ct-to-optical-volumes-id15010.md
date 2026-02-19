---
topic_id: 15010
title: "Affine Registration Of Ct To Optical Volumes"
date: 2020-12-12
url: https://discourse.slicer.org/t/15010
---

# Affine Registration of CT to Optical Volumes

**Topic ID**: 15010
**Date**: 2020-12-12
**URL**: https://discourse.slicer.org/t/affine-registration-of-ct-to-optical-volumes/15010

---

## Post #1 by @Matteo_Bonsignore (2020-12-12 01:59 UTC)

<p>Hello all,</p>
<p>I have just started using 3D slicer this month, I am new to image processing. I am trying to register the CT of a 3d-printed (Powder Bed Fusion) metal cylinder (very simple geometry, diameter = 2mm, with indents every 2mm height-wise to facilitate feature identification for registration) to the optical stack of the same part (taken with a DSLR camera during operation of the 3d printer).</p>
<p>The camera takes images of the powder bed in the printer (after the laser has melted it) every 30 micron, thus building a stack of slices with resolution (7 x 7 x 30 micron); the CT has resolution (2.5 x 2.5 x 2.5 micron).</p>
<p>To prepare for the registration I first crop all unwanted regions from both stacks (e.g. slices containing CT artifacts), rotate the CT 180° to more or less match the direction of the optical stack, and perform a first fiducial registration (Fiducial Registration module) using 10 fiducials placed at various heights on the coronal view (see screenshot).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5160861b30abec6b9e01f31023de5c865db548dc.jpeg" data-download-href="/uploads/short-url/bBTtxGO2M6FT7R3Ew8rzdwE8yug.jpeg?dl=1" title="Screenshot 2020-12-12 at 02.51.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5160861b30abec6b9e01f31023de5c865db548dc_2_690x438.jpeg" alt="Screenshot 2020-12-12 at 02.51.27" data-base62-sha1="bBTtxGO2M6FT7R3Ew8rzdwE8yug" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5160861b30abec6b9e01f31023de5c865db548dc_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5160861b30abec6b9e01f31023de5c865db548dc_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5160861b30abec6b9e01f31023de5c865db548dc.jpeg 2x" data-dominant-color="43434D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-12-12 at 02.51.27</span><span class="informations">1375×874 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At this point the stacks match in height, but the cross-section area (i.e. each slice) of the CT is clearly larger than that of the optical stack. The final step would ideally be a registration that allows the CT to be rescaled in x and y to match the optical stack exactly, but I am not sure how to do this. I have mostly been attempting affine and b-spline registrations with a variety of modules for this, but to no avail.</p>
<p>Having very little experience with image registration I am unsure of the reasons for which none of these methods work. Does 3d slicer have a module that allows for obtaining this final registration step with relative ease?</p>
<p>Thank you very much,<br>
Matteo</p>

---

## Post #2 by @lassoan (2020-12-12 03:42 UTC)

<p>There are dozens of registration tools for Slicer, but we highlighted a few that we generally recommend here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">https://slicer.readthedocs.io/en/latest/user_guide/registration.html</a></p>
<p>You can start the registration with an affine landmark transformation, and fine-tune it at the end with intensity based automatic image registration.</p>
<p>Affine landmark transformation is needed very rarely (most common are rigid and bspline, sometimes similarity), therefore this option is not exposed in most registration modules to not clutter the user interface. Currently, I think the only landmark registration module that offers affine transformation is “Landmark registration” in Slicer core. It is not very convenient for large volume differences because it automatically places the corresponding point in the corresponding image and it is tedious to move it to the correct position, but it should be still usable. Fiducial registration wizard module would be easier to use, but affine option is not exposed on its interface. Probably you only need to add 20-30 lines of code to add this option, so if you are willing to build Slicer and you understand a little C++ then it should be quite easy to add (we can help you getting started).</p>
<p>After you have your initial alignment (hardened the landmark transform on the moving image), I would recommend to get a refined registration using “General registration (Elastix)” module (provided by SlicerElastix extension), because it usually works with default parameter set, without any tuning.</p>

---

## Post #3 by @Matteo_Bonsignore (2020-12-12 19:02 UTC)

<p>It (almost) works, thank you so much!</p>
<p>In the end the fiducial registration wizard’s interface options were sufficient, all it took was two sets of fiducials in the axial view (one set at an indent and another set at the next indent) and the warping transformation achieved a fairly accurate result. The final registration using Elastix almost achieved a perfect registration.</p>
<p>I just had two more questions, if I may:</p>
<ol>
<li>The final Elastix registration has a few misalignments, I suspect this is due to the “bubbles” in the CT volume (see screenshot below), which in reality are fused metal powder particles that do not form part of the printed part and should therefore be removed.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef0b10a91c23eebfe6b77f9871b443ff4c03fe4.jpeg" data-download-href="/uploads/short-url/28amyNvWbeOZDnpa2J1PQqaHQLG.jpeg?dl=1" title="Screenshot 2020-12-12 at 19.58.40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ef0b10a91c23eebfe6b77f9871b443ff4c03fe4_2_690x431.jpeg" alt="Screenshot 2020-12-12 at 19.58.40" data-base62-sha1="28amyNvWbeOZDnpa2J1PQqaHQLG" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ef0b10a91c23eebfe6b77f9871b443ff4c03fe4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ef0b10a91c23eebfe6b77f9871b443ff4c03fe4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef0b10a91c23eebfe6b77f9871b443ff4c03fe4.jpeg 2x" data-dominant-color="C7C6CF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-12-12 at 19.58.40</span><span class="informations">1324×828 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have tried adding a mask to the volume such that the mask only encompasses the actual volume and not the bubbles, I can achieve this for one slice but I was hoping there might be a semi-automatic way of extending the mask to all slices (approx. 2400 in total, manually doing each would take too long).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/395fc3de65ac50db9249f6a1531fc1aba334d06e.jpeg" data-download-href="/uploads/short-url/8byohozvrNN9DxSvOwmbo2xtCuG.jpeg?dl=1" title="Screenshot 2020-12-12 at 19.57.51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395fc3de65ac50db9249f6a1531fc1aba334d06e_2_690x312.jpeg" alt="Screenshot 2020-12-12 at 19.57.51" data-base62-sha1="8byohozvrNN9DxSvOwmbo2xtCuG" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395fc3de65ac50db9249f6a1531fc1aba334d06e_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395fc3de65ac50db9249f6a1531fc1aba334d06e_2_1035x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/395fc3de65ac50db9249f6a1531fc1aba334d06e_2_1380x624.jpeg 2x" data-dominant-color="414348"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-12-12 at 19.57.51</span><span class="informations">1920×870 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>The CT file (the moving image) is pretty large (&gt; 1 GB) and Elastix registration requires approx. 2 hrs to complete on my laptop. Is there any way of improving the registration time? Are there any alternatives to simply downsampling the CT stack?</li>
</ol>
<p>Thank you very much for your help.</p>

---

## Post #4 by @Matteo_Bonsignore (2020-12-12 19:05 UTC)

<p>Apologies, I forgot to mention, I am using the Level Tracing function to semi-automatically mask the slices, since it seems to work quite well (but only for individual slices).</p>

---

## Post #5 by @lassoan (2020-12-14 04:23 UTC)

<p>For affine registration, it should be enough to have a few hundred points along each axis (you would get the same registration results as on the full-resolution data set). Apply some Gaussian smoothing and then use Crop volume module with a spacing scale of 5 to 10. This will make everything about 100x faster.</p>
<p>To get rid of the bubbles, you can use Grow from seeds or Watershed effects to segment only the dense core of the material. You can also try Smoothing effect.</p>

---
