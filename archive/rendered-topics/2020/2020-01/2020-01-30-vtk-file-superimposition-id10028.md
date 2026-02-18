# vtk file superimposition

**Topic ID**: 10028
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/vtk-file-superimposition/10028

---

## Post #1 by @nayansi.jha (2020-01-30 14:30 UTC)

<p>How can we save two vtk superimposed files( as a single file)?<br>
For example- right condyle models of the same patient taken at two different time points.</p>

---

## Post #2 by @timeanddoctor (2020-01-30 14:39 UTC)

<p>Yes, there are many methods:<br>
1、you can use the merge models module<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47d3f811695954af5712bfc531142dd6d3604281.png" data-download-href="/uploads/short-url/afq2B9xFfM4sSMs9vxRt4ZiCn5v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d3f811695954af5712bfc531142dd6d3604281_2_690x274.png" alt="image" data-base62-sha1="afq2B9xFfM4sSMs9vxRt4ZiCn5v" width="690" height="274" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d3f811695954af5712bfc531142dd6d3604281_2_690x274.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d3f811695954af5712bfc531142dd6d3604281_2_1035x411.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d3f811695954af5712bfc531142dd6d3604281_2_1380x548.png 2x" data-dominant-color="838283"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1402×557 35.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2、you can import the models to a segmentation and then have a operation</p>

---

## Post #3 by @timeanddoctor (2020-01-30 14:50 UTC)

<p>If you want to alin the different models you can use the ‘fiducial registration’ in IGT and analyse the different with the ‘model to model distance’ module</p>

---
