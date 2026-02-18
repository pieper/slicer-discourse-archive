# Problem when uploading volumes for registration

**Topic ID**: 24582
**Date**: 2022-07-31
**URL**: https://discourse.slicer.org/t/problem-when-uploading-volumes-for-registration/24582

---

## Post #1 by @Valeria_Onofrj (2022-07-31 19:03 UTC)

<p>Operating system:MAC<br>
Slicer version:4.13<br>
Expected behavior:I have uploaded DWI and FLAIR and I should be able to coregister FLAIR on DWI</p>
<p>Actual behavior:The Brainregistration plug in does not recognise the DWI, therefore I can not upload it and can’t coregister the 2 volumes</p>

---

## Post #2 by @pieper (2022-08-01 17:56 UTC)

<p>If the DWI was loaded as a diffusion volume you’ll need to extract a scalar from it.  E.g.estimate the tensor and use the baseline image or create a scalar map like FA (you can do these steps with SlicerDMRI).</p>

---

## Post #3 by @Valeria_Onofrj (2022-08-02 15:05 UTC)

<p>I tried but DMRI does not open the DWI</p>
<p>Valeria</p>

---

## Post #4 by @pieper (2022-08-02 15:11 UTC)

<p>Check the <code>Volume type</code> field of the <code>Volume Information</code> tab of the <code>Volumes</code> module.  It should be <code>Scalar</code> to work with the registration tools.  If not you need to convert it, e.g. with the Vector to Scalar Volume module, depending on the type.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9915a964d38e70b75f81290bf9ae172a27154f6e.png" data-download-href="/uploads/short-url/lQfsHyUmecEIlCxpQbJClfEoyMC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9915a964d38e70b75f81290bf9ae172a27154f6e_2_606x500.png" alt="image" data-base62-sha1="lQfsHyUmecEIlCxpQbJClfEoyMC" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9915a964d38e70b75f81290bf9ae172a27154f6e_2_606x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9915a964d38e70b75f81290bf9ae172a27154f6e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9915a964d38e70b75f81290bf9ae172a27154f6e.png 2x" data-dominant-color="E7E6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">620×511 46.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Valeria_Onofrj (2022-08-09 11:54 UTC)

<p>If I open the Image on volume I see it’s a MRMLMulti in the volume type section.<br>
I still can’t do the registration.</p>

---

## Post #6 by @pieper (2022-08-09 13:41 UTC)

<p>That means your DWI was loaded as a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer">MultiVolume</a> and you can either use the MultiVolume modules to extract a frame from it for registration.  Or you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html?highlight=multivolume#convert-multivolume-node-to-sequence-node">convert it to a Sequence</a> and use that newer infrastructure.</p>

---

## Post #7 by @Valeria_Onofrj (2022-08-09 14:10 UTC)

<p>I tried to use the multivolume but I keep having thé same problem: i can not use thé dei images for registration</p>
<p>Valeria</p>

---

## Post #8 by @pieper (2022-08-09 15:10 UTC)

<p>What I mean is that you need to extract a frame as a single scalar volume from the multivolume and then you can use that frame for registration.</p>

---
