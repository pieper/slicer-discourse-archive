# Load FreeSurfer data set as DICOMRT

**Topic ID**: 12886
**Date**: 2020-08-07
**URL**: https://discourse.slicer.org/t/load-freesurfer-data-set-as-dicomrt/12886

---

## Post #1 by @loubna (2020-08-07 08:13 UTC)

<p>Hi,</p>
<p>I have used SlicerFreeSurfer extension to import FreeSurfer data into slicer ( TutorialData/diffusion_recon/Diff001) as shown in figure1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a958bd5ddd66cf42d3181e35e7eeed61504e269b.png" data-download-href="/uploads/short-url/oa6OCuwSStmbyA7qQ2IjGyHdhCr.png?dl=1" title="fig1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a958bd5ddd66cf42d3181e35e7eeed61504e269b_2_690x307.png" alt="fig1" data-base62-sha1="oa6OCuwSStmbyA7qQ2IjGyHdhCr" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a958bd5ddd66cf42d3181e35e7eeed61504e269b_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a958bd5ddd66cf42d3181e35e7eeed61504e269b_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a958bd5ddd66cf42d3181e35e7eeed61504e269b_2_1380x614.png 2x" data-dominant-color="9790A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig1</span><span class="informations">1905×850 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have then created new study to export Dicom and some segments as DICOM RT. The model is not well reconstructed (FIG 2) .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdd39d424628d88e41fe88f85f88bc4f34056048.jpeg" data-download-href="/uploads/short-url/tmPgiRMijRn9gEf3fhFUQDx2Q1q.jpeg?dl=1" title="fig2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdd39d424628d88e41fe88f85f88bc4f34056048_2_690x312.jpeg" alt="fig2" data-base62-sha1="tmPgiRMijRn9gEf3fhFUQDx2Q1q" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdd39d424628d88e41fe88f85f88bc4f34056048_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdd39d424628d88e41fe88f85f88bc4f34056048_2_1035x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdd39d424628d88e41fe88f85f88bc4f34056048_2_1380x624.jpeg 2x" data-dominant-color="A89EB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig2</span><span class="informations">1906×863 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are there any transformation that must be taken into account before exporting data.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @Sunderlandkyl (2020-08-07 13:41 UTC)

<p>If you change the 3D representation of the segmentation to Planar Contours, are the contours well defined?</p>

---

## Post #3 by @loubna (2020-08-07 13:59 UTC)

<p>Yes, it seems that contours are well  defined (see attached figure) . But I have got some errors when loading data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d530539fc3c175c646f1f93ee51867b94dc706da.png" data-download-href="/uploads/short-url/upXeUPi2bAv7Broh48v18AKCi3E.png?dl=1" title="fig3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d530539fc3c175c646f1f93ee51867b94dc706da_2_690x299.png" alt="fig3" data-base62-sha1="upXeUPi2bAv7Broh48v18AKCi3E" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d530539fc3c175c646f1f93ee51867b94dc706da_2_690x299.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d530539fc3c175c646f1f93ee51867b94dc706da_2_1035x448.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d530539fc3c175c646f1f93ee51867b94dc706da_2_1380x598.png 2x" data-dominant-color="AFA9BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig3</span><span class="informations">1892×821 335 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc3bbb981b4cb79700dacb50983ac555570939cc.png" data-download-href="/uploads/short-url/qRbJXLVHzXIdDhmgacmhXqebzE8.png?dl=1" title="fig4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc3bbb981b4cb79700dacb50983ac555570939cc.png" alt="fig4" data-base62-sha1="qRbJXLVHzXIdDhmgacmhXqebzE8" width="690" height="357" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig4</span><span class="informations">980×508 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Sunderlandkyl (2020-08-07 15:42 UTC)

<p>There is likely an issue with the planar contour to closed surface conversion.</p>
<p>You can circumvent this conversion step by clicking on the update button beside the closed surface representation and using the Planar contour -&gt; Ribbon model -&gt; Binary labelmap -&gt;Closed Surface conversion path.</p>

---

## Post #5 by @lassoan (2020-08-08 15:08 UTC)

<p>I don’t think it is possible to store such intricate surfaces in DICOM RT structure set (it would be almost impossible to get all the keyholes generated correctly for arbitrarily complex geometry). You can store the segmentation as a DICOM Segmentation Object instead, which stores segmentation as a labelmap. A DICOM Surface Segmentation object could be used as well (which stores a triangle mesh), but Slicer currently does not have an importer/exporter for that.</p>

---

## Post #6 by @loubna (2020-08-08 15:20 UTC)

<p>Thank you for reply, but what about storing these intricate surfaces as DICOM RT and then reconstruct them using the other conversion Rule Planar contour -&gt; Ribbon model -&gt; Binary labelmap -&gt;Closed Surface. Because It seems that it works fine. In other words what are advantages of ribbon models compared to contours and how it deals with keyholes problems.</p>
<p>Thank’s in advance</p>

---

## Post #7 by @lassoan (2020-08-08 15:22 UTC)

<p>Ribbon models have no advantages. We had to introduce them because of poor design decision of DICOM RT working group decades ago to represent segmentation as a series of 2D contours instead of a 3D representation.</p>

---
