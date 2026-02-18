# How to Load a Volume in Slicer

**Topic ID**: 23348
**Date**: 2022-05-09
**URL**: https://discourse.slicer.org/t/how-to-load-a-volume-in-slicer/23348

---

## Post #1 by @emma1201 (2022-05-09 15:05 UTC)

<p>Hi everyone, am a student who is just starting out with Slicer. I have a really basic question and am frustrated that I cannot find out what is wrong - I am unable to load any input Volumes. I have created a volume ‘DTI volume’ from my dicom images into an nrrd file. In this example I included the sample data from MRHead and Brain Tumor. All the volumes have loaded in the ‘Volumes’ and the ‘Data’ tab shows these volumes exist (first picture) but when I try to load an input volume into ‘Volume Rendering’ or any other tab (such as Registration) they do not exist and only the sample data exists (second picture). Is there an error in the way I load the volumes?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4f17b6b74a7010b27a5051b500988b6ca6ca77d.png" alt="image" data-base62-sha1="pOHjHhEJ2vHXgfKBgEKVSqwUd1b" width="532" height="347"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/177e457562a7ae11c13a1458107b893c4c9f4748.jpeg" data-download-href="/uploads/short-url/3lPw2TbLyVU2ZABHDgQoKRY6NS0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/177e457562a7ae11c13a1458107b893c4c9f4748_2_690x481.jpeg" alt="image" data-base62-sha1="3lPw2TbLyVU2ZABHDgQoKRY6NS0" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/177e457562a7ae11c13a1458107b893c4c9f4748_2_690x481.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/177e457562a7ae11c13a1458107b893c4c9f4748_2_1035x721.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/177e457562a7ae11c13a1458107b893c4c9f4748_2_1380x962.jpeg 2x" data-dominant-color="AFABAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1340 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have already tried restarting Slicer. Thanks so much for your help. Apologies for the very basic question.</p>

---

## Post #2 by @pieper (2022-05-09 17:21 UTC)

<p>The DTI volume cannot be directly volume rendered, so it doesn’t show up on the list.  You can install SlicerDMRI and get the module to convert from tensor to scalars (for example, Fractional Anisotropy) and then use that for volume rendering.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://aacrjournals.org/cancerres/article/77/21/e101/662618/SlicerDMRI-Open-Source-Diffusion-MRI-Software-for">
  <header class="source">
      <img src="https://aacr.silverchair-cdn.com/data/SiteBuilderAssetsOriginals/Live/Images/umbrella/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://aacrjournals.org/cancerres/article/77/21/e101/662618/SlicerDMRI-Open-Source-Diffusion-MRI-Software-for" target="_blank" rel="noopener">American Association for Cancer Research</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:376/500;"><img src="https://aacr.silverchair-cdn.com/aacr/content_public/journal/cancerres/issue/77/21/1/m_canres_77_21_cover.png?Expires=1714842915&amp;Signature=XqUbtYphOIlTKWwmOh8pDZzCZYJqbHvF1gKutQivTqedjwjS2XleTS7Fs7PNJab6vZIoosup4ahUBc2LPGZoi9irNm-KMGVPLu2I~sPmnFMQOG02UeOtQ0dO-W9W1NE5OSFZx1YsflX9cMw9jCDzWF9Di6GMaInTOuhrkgYUuE-siz787dgBsqDzdl6BYQ3YHtKKem3KsUapQO8OauWtnx42HL8~MLfS2MgGlZ1ph1WmRqkGRkgA8Kx2hwA7a6S4k29-Y9iaK41AJECzy3Q3GZ80Ojw90gFtVKYsSnSrWrHc3mR0Q1rsagpFe~2TYrz3fqxtWtQLKerYsl85RT3VTA__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" class="thumbnail" width="376" height="500"></div>

<h3><a href="https://aacrjournals.org/cancerres/article/77/21/e101/662618/SlicerDMRI-Open-Source-Diffusion-MRI-Software-for" target="_blank" rel="noopener">SlicerDMRI: Open Source Diffusion MRI Software for Brain Cancer Research</a></h3>

  <p>Abstract. Diffusion MRI (dMRI) is the only noninvasive method for mapping white matter connections in the brain. We describe SlicerDMRI, a software suite that enables visualization and analysis of dMRI for neuroscientific studies and patient-specific...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @emma1201 (2022-05-10 14:06 UTC)

<p>Thank you for the reply Steve, that worked! What about a regular T1-weighted MRI, how do I convert these to show up for volume rendering? How can I process it first to show up?</p>

---

## Post #4 by @pieper (2022-05-10 19:18 UTC)

<p>You shouldn’t need to do anything for the T1 to be available for volume rendering.  Check in the Volumes module to confirm that you T1 is recognized as a Scalar volume (in the Volume Information tab).  In Volume Rendering, select the T1 and make it visible with the eye icon.  You may need to reset the view to make it appear (Center button in <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">this interface</a>).</p>

---

## Post #5 by @emma1201 (2022-05-21 09:14 UTC)

<p>Hi Steve, thanks so much for your help! I’ve realised the problem has to do with SlicerDMRI - when I have this extension installed, all my DICOM images load as DWI (even if they are not originally DWI) and I am unable to use it. Is there any work around this? (First image shows the files loaded as a regular T1 with the SlicerDMRI extension disabled, second image shows how it is loaded as a DWI image when SlicerDMRI is installed and enabled.)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9f6466bb02a63f4ebebd69fddae9646ba7c9d49.png" alt="image" data-base62-sha1="zFgwZgSpxlE3FNuMNwCLe1tGsyZ" width="394" height="266"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6ce6979558953b9d89775f44cb668dba3db9bb0.png" alt="image" data-base62-sha1="nNDuJMAo7wdTuOpknrJICZZXeM0" width="409" height="297"></p>

---

## Post #6 by @pieper (2022-05-21 15:46 UTC)

<p>Yes, this can happen because a DWI series can be difficult to detect without deep inspection of all the instances, so the DWI plugin can have false positives.  You can go into the DICOM Plugins section of the DICOM module to disable diffusion when you load the T1 series.</p>

---
