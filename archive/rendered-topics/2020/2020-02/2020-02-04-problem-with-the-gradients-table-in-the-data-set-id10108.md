---
topic_id: 10108
title: "Problem With The Gradients Table In The Data Set"
date: 2020-02-04
url: https://discourse.slicer.org/t/10108
---

# Problem with the gradients table in the data set

**Topic ID**: 10108
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/problem-with-the-gradients-table-in-the-data-set/10108

---

## Post #1 by @Santiago_Cutiller (2020-02-04 15:50 UTC)

<p>Hi!<br>
I am Santiago and I am working on a research project on epilepsy and diffusion tensor.<br>
I have a problem with the gradients table in the data set.<br>
When i trying use difussion brain masking I get the following error:<br>
Diffusion Brain Masking standard error:  C:/Users/Usuario/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli- modules/DiffusionWeightedVolumeMasking.exe: Error parsing Diffusion information, no B0 images.<br>
I checked the data. Gradient values ​​are strange<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1870e5fa7216b603ea70045881bc819e608e738a.jpeg" data-download-href="/uploads/short-url/3udlg5IgtCM37BjksMYVT5bOPx0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1870e5fa7216b603ea70045881bc819e608e738a_2_690x388.jpeg" alt="image" data-base62-sha1="3udlg5IgtCM37BjksMYVT5bOPx0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1870e5fa7216b603ea70045881bc819e608e738a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1870e5fa7216b603ea70045881bc819e608e738a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1870e5fa7216b603ea70045881bc819e608e738a.jpeg 2x" data-dominant-color="A8A8B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1069×602 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This error occurs only with data from a manufacturer. Is there a way to correct it?</p>
<p>Thanks!</p>

---

## Post #2 by @zhangfanmark (2020-02-04 16:14 UTC)

<p>Hi,</p>
<p>Yes, the gradient table is strange. It looks all the directions are the same for the first few DW images. What module did you use to convert the data? I guess DWIConvert as you are using 4.10.<br>
You can try our new Dcm2niixGUI extension to convert the dicom data to nrrd, and see how it works. The new module is avaible in the nightly via the extension manager.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @Santiago_Cutiller (2020-02-05 20:34 UTC)

<p>Hello! Thanks for answering<br>
I can’t use Dcm2nii GUI but I think I identified the problem<br>
First I converted the DICOM files to FSL and examine the bvec file and check that there is definitely a problem with the gradient table:</p>
<p><em>0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934 0.5607954357719934</em></p>
<p><em>-0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721 -0.5770928835459721</em></p>
<p><em>0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226 0.5936937619496226</em></p>
<p>All values are equal</p>
<p>Also in the bval file I saw that there is a problem with the b values</p>
<p><em>-4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18 -4.6116860184273879e+18</em></p>
<p>I searched in a forum for gradient tables for philips. Apparently in philips there are 3 modes: low, medium and high resolution according to the number of gradients and in turn each of them can have the “overplus” function activated or deactivated. Therefore there are six possible gradient tables. I tried several of them and got a good result with this:</p>
<p><em>0 -0.499998 -0.499998 0.707107 -0.653288 -0.208664 0.019658 0.421225 0.689925 -0.653495 -0.292882 0.294515 0.514993 0.707102 -0.707102 -0.472486 0.555492 0.707102 -0.707107 -0.707102 0.707102 0.472486 -0.707085 -0.636392 -0.706047 -0.292882 0.292882 0.707085 0.707102 -0.706260 0.034719 0.707060 0.707107 100.000.000</em></p>
<p><em>0 -0.499998 -0.499998 -0.707107 -0.270606 -0.675630 -0.706829 -0.567950 -0.154927 -0.270675 -0.707102 -0.706411 -0.486072 -0.292882 -0.472486 -0.707102 -0.643950 -0.472486 -0.707107 -0.472486 -0.472486 -0.707102 -0.707085 -0.425181 -0.706047 -0.707102 -0.707102 -0.707085 -0.292882 -0.706260 -0.706256 -0.707060 -0.000000 100.000.000</em></p>
<p><em>0 -0.707110 0.707110 0.000000 -0.707098 -0.707095 -0.707112 -0.707109 -0.707108 -0.706880 -0.643604 -0.643619 -0.706056 -0.643604 -0.526084 -0.526084 -0.526077 -0.526084 -0.000212 0.526084 0.526084 0.526084 0.007849 0.643604 0.054730 0.643604 0.643604 0.007849 0.643604 0.048932 0.707105 0.011526 0.707107 100.000.000</em></p>
<p>with that data I generated a bvec file, also generate a bval file:</p>
<p><em>0 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000</em></p>
<p>Then with DWIconverter I transformed the FSL into nrrd, I created brain masking and I made the tensor estimate with good results</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4bf5b98cf675a26c495d1e35f3148c6f4c2ae1e.png" alt="image" data-base62-sha1="um3cLBk5qe8Fl0R8A7WGj8iSknc" width="174" height="205"></p>
<p>I made the anisotropic fraction map that showed reasonable values</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35122d11c5e4e4825914df12a17dee3b2ca28296.png" alt="image" data-base62-sha1="7zufn6BK2GpCbeKujA8WhcEfBpI" width="183" height="195"></p>
<p>However, when I do the tractography (with the same parameters I always use) the results are not good. The tracts are aberrant.</p>
<p>for example in this reconstruction the roi is put in the internal capsule</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/143edd29d442acb9f798a962166cf86b452aabfc.png" alt="image" data-base62-sha1="2T6eyk0KzDyoJQeZTbt0y2TLdr6" width="135" height="147"></p>
<p>something similar happens in the corpus callosum</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f1109c252c84c325f59f071a22386e53d450c8.png" alt="image" data-base62-sha1="Zplk9jiJv2J1JL7wjlXi5K1n0Q" width="150" height="133"></p>
<p>I have read that philips gradient tables acquired with the “overplus” option sometimes require a transformation procedure but I don’t know how to do it</p>
<p>I’d appreciate the answer</p>

---

## Post #4 by @zhangfanmark (2020-02-05 21:07 UTC)

<p>Hi, it looks like an orientation issue, but I am not sure exactly. Perhaps you can look up the fsl website for information about flipping the orientations: <a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils" rel="nofollow noopener">https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils</a></p>

---
