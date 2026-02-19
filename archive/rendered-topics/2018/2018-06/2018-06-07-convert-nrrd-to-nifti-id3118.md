---
topic_id: 3118
title: "Convert Nrrd To Nifti"
date: 2018-06-07
url: https://discourse.slicer.org/t/3118
---

# Convert Nrrd To Nifti

**Topic ID**: 3118
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/convert-nrrd-to-nifti/3118

---

## Post #1 by @Hikmat (2018-06-07 20:58 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>I am attempting to convert a Nrrd file (.nrrd) to a Nifti file (.nii.gz).<br>
I am aware of the DWIConvert module but I couldn’t understand how to get that to work as the U/I was confusing.</p>
<p>One could run this module from the Python interactor as well but I struggled with the syntax of this instruction and could find no apparent documentation.</p>
<p>So I tried this snippet of Python code (with the appropriate adjustments) and it seemed to work:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfa0f12767a9178c760620bbda0a9a1806403f23.png" alt="image" data-base62-sha1="tCLEuiCtRESwT5AdSgd3Iio6O3h" width="570" height="297"></p>
<p>However, upon loading the newly created Nifti file in Slicer, the images are of the incorrect type.<br>
That is to say, I get the Sagittal slice loaded in the Axial slice view and other such mishaps.<br>
In addition, my Sagittal slice has been rotated by 180.</p>
<p>Nrrd File:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e86ffb4af7f61a552090d1ad6845659b7994ac71.jpeg" data-download-href="/uploads/short-url/xaeGWwbu5QsImOxr42VHQx4wIh3.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86ffb4af7f61a552090d1ad6845659b7994ac71_2_690x374.jpg" alt="image" data-base62-sha1="xaeGWwbu5QsImOxr42VHQx4wIh3" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86ffb4af7f61a552090d1ad6845659b7994ac71_2_690x374.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e86ffb4af7f61a552090d1ad6845659b7994ac71_2_1035x561.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e86ffb4af7f61a552090d1ad6845659b7994ac71.jpeg 2x" data-dominant-color="383836"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×617 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Results of Conversion (Niftii File):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b324309c5a021cbb942e3bb95bf3d34496526581.jpeg" data-download-href="/uploads/short-url/pyL0e9KSKFg2ALCgoti2H92rCoN.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b324309c5a021cbb942e3bb95bf3d34496526581_2_690x375.jpg" alt="image" data-base62-sha1="pyL0e9KSKFg2ALCgoti2H92rCoN" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b324309c5a021cbb942e3bb95bf3d34496526581_2_690x375.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b324309c5a021cbb942e3bb95bf3d34496526581_2_1035x562.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b324309c5a021cbb942e3bb95bf3d34496526581.jpeg 2x" data-dominant-color="1C1B1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1137×618 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would appreciate any insight into this matter.</p>
<p>Thanks.</p>

---

## Post #2 by @ihnorton (2018-06-07 21:23 UTC)

<p>For non-DWI images you can use the normal File-&gt;Save. Slicer correctly loads and round-trips the <a href="https://nifti.nimh.nih.gov/nifti-1/data">NIfTI test data</a>. If you need to script the operation, see <a href="https://nifti.nimh.nih.gov/nifti-1/data">here</a> – set the file extension to .nii and Slicer IO will do the rest. e.g. using the MRHead sample dataset:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; n = getNode("MRHead")
&gt;&gt;&gt; saveNode(n, "/tmp/foo/test1.nii")
True
</code></pre>
<p>HTH</p>

---
