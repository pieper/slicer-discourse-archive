# How can I load a default segment color config from customized file,like export from itk-snap

**Topic ID**: 24988
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/how-can-i-load-a-default-segment-color-config-from-customized-file-like-export-from-itk-snap/24988

---

## Post #1 by @SlicerIsGood (2022-08-30 01:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25b47ad8488a7042d0a0394ef82785f43c26b72d.png" data-download-href="/uploads/short-url/5nylfrXiJTdk2naz0ajTAwnArRr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25b47ad8488a7042d0a0394ef82785f43c26b72d.png" alt="image" data-base62-sha1="5nylfrXiJTdk2naz0ajTAwnArRr" width="418" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">766×915 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>like this, itk-snap has a eport label description file funciton, so I want load this file to slicer to perform segmentation with color described in file, how can I do this?</p>

---

## Post #2 by @pieper (2022-08-30 20:47 UTC)

<p>One option is just to use the segment editor to make a segmentation with the names/colors you want to have but no segmentations and save it as a .seg.nrrd that you can use as a template.  Then reload it for each case you want to segment and add the actual segmentations (setting the master volume and adjusting the segmentation geometry if needed).</p>

---

## Post #3 by @jay1987 (2022-08-31 01:57 UTC)

<p>one code piece i copy from module brain parcellation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/611cb6def8ed617107a86914c2625b6f45671c58.png" alt="image" data-base62-sha1="dR5PL3EAr0nvZHBqM8PJeleFQeI" width="522" height="148"><br>
and the GIFNiftyNet2.ctbl file format<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e98d342e3d02ea49477e7086f5f622804bd7921.png" data-download-href="/uploads/short-url/2586Tgy3iSNNgp1YiG2taCJxrDX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e98d342e3d02ea49477e7086f5f622804bd7921.png" alt="image" data-base62-sha1="2586Tgy3iSNNgp1YiG2taCJxrDX" width="373" height="500" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">480×643 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-08-31 02:44 UTC)

<p>I’ve added a reader for this ITK-Snap Label Description file format (<code>*.txt</code> or <code>*.label</code>), in the Sandbox extension. If you install this extension then you can-drag-and drop these label description files to make Slicer load them as a color table. This color table can then be used when you load a segmentation to set segment names and colors. See some more description <a href="https://github.com/PerkLab/SlicerSandbox#ImportItkSnapLabel">here</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d0da8f1073141b27d4e1f6751063c044e0f37d6.png" data-download-href="/uploads/short-url/fyJjfIcHhJNDxAZRVEl0rkK95EW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d0da8f1073141b27d4e1f6751063c044e0f37d6_2_690x244.png" alt="image" data-base62-sha1="fyJjfIcHhJNDxAZRVEl0rkK95EW" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d0da8f1073141b27d4e1f6751063c044e0f37d6_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d0da8f1073141b27d4e1f6751063c044e0f37d6_2_1035x366.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d0da8f1073141b27d4e1f6751063c044e0f37d6_2_1380x488.png 2x" data-dominant-color="393938"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1401×497 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e494579ef82cefed8b77927edf2ff792d2842633.png" data-download-href="/uploads/short-url/wC6GtyCJxyGArNChjH9kKDhB4eT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e494579ef82cefed8b77927edf2ff792d2842633_2_690x221.png" alt="image" data-base62-sha1="wC6GtyCJxyGArNChjH9kKDhB4eT" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e494579ef82cefed8b77927edf2ff792d2842633_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e494579ef82cefed8b77927edf2ff792d2842633_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e494579ef82cefed8b77927edf2ff792d2842633.png 2x" data-dominant-color="3F3E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×442 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Liam_Swiggard (2024-06-07 20:54 UTC)

<p>Hi There,When using your ITK snap Label Description software, I noticed that if the Label Transparency is set to any value different than 0 or 1 (i.e 0.5), Sandbox will not detect the labels file as a ITK-SnAP Label Description File. Spesifically, I have two Text Files: Anat_labels.txt and Anat_labels_Altered.txt. Anat_labels reads as an ITK-SnAP Label Description File, where as Anat_labels_Altered does not. The only difference between them is that Anat_labels_Altered has Label Transparency values between 0 and 1. However, if I change all the Label Transparency values to be either 0 or 1, Sandbox recognizes it as an ITK-SnAP Label Description File. What do you suggest I do?</p>

---

## Post #7 by @lassoan (2024-06-09 03:51 UTC)

<p>Please provide a sample file and I’ll have a look.</p>

---
