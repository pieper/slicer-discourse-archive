# Segmentations export

**Topic ID**: 31043
**Date**: 2023-08-08
**URL**: https://discourse.slicer.org/t/segmentations-export/31043

---

## Post #1 by @zhuyingying1234 (2023-08-08 12:12 UTC)

<p>Dear slicer experts<br>
I have a problem， In segmentations, I want to convert the stru-5 export to lable-5, the result is that the two ranges are not the same after exporting, what is the problem？ In segmentations, nothing has changed, it is the default state.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc29c3fe8126c1d7c37f411d7e16371959c005eb.jpeg" data-download-href="/uploads/short-url/qQzfiPy6ERTUcMi8WSp6mugoFGr.jpeg?dl=1" title="截屏2023-08-08 17.12.52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc29c3fe8126c1d7c37f411d7e16371959c005eb_2_690x431.jpeg" alt="截屏2023-08-08 17.12.52" data-base62-sha1="qQzfiPy6ERTUcMi8WSp6mugoFGr" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc29c3fe8126c1d7c37f411d7e16371959c005eb_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc29c3fe8126c1d7c37f411d7e16371959c005eb_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc29c3fe8126c1d7c37f411d7e16371959c005eb_2_1380x862.jpeg 2x" data-dominant-color="2E2F2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-08-08 17.12.52</span><span class="informations">1920×1200 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e821ae6feb139045618645675ce94d2f3870d3cc.jpeg" data-download-href="/uploads/short-url/x7wVYUviE8IyCuzVeLgtMiQIYfq.jpeg?dl=1" title="截屏2023-08-08 17.12.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e821ae6feb139045618645675ce94d2f3870d3cc_2_690x431.jpeg" alt="截屏2023-08-08 17.12.36" data-base62-sha1="x7wVYUviE8IyCuzVeLgtMiQIYfq" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e821ae6feb139045618645675ce94d2f3870d3cc_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e821ae6feb139045618645675ce94d2f3870d3cc_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e821ae6feb139045618645675ce94d2f3870d3cc_2_1380x862.jpeg 2x" data-dominant-color="2B2E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-08-08 17.12.36</span><span class="informations">1920×1200 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f429b7565e735ce972c05e41646a3439b664cf4.png" data-download-href="/uploads/short-url/6K595aTmlnNyi7iFM0F9q9XuVH6.png?dl=1" title="截屏2023-08-08 20.08.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f429b7565e735ce972c05e41646a3439b664cf4_2_365x500.png" alt="截屏2023-08-08 20.08.46" data-base62-sha1="6K595aTmlnNyi7iFM0F9q9XuVH6" width="365" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f429b7565e735ce972c05e41646a3439b664cf4_2_365x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f429b7565e735ce972c05e41646a3439b664cf4_2_547x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f429b7565e735ce972c05e41646a3439b664cf4_2_730x1000.png 2x" data-dominant-color="393D40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-08-08 20.08.46</span><span class="informations">1036×1418 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looking forward to your reply. Thank you.</p>

---

## Post #2 by @AJ_ZHU (2023-08-08 12:34 UTC)

<p>Hi<br>
Kind-of I did encounter the same issue inside this “Export” there since this module has a “smart” way while exporting: the exported part is cropped based on the boundary box of segments (that’s why the output size is being changed.).<br>
Better to do some of your own python modules, using the function ==&gt;<br>
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)</p>
<p>so the output of “labelmapVolumeNode” will take dimensions of the ref. vol. node</p>

---

## Post #3 by @AJ_ZHU (2023-08-08 12:48 UTC)

<p>addition, the above module need have a defined ref. vol.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c63e12148972fcf3fb628c4a4bbb208e1011a282.png" data-download-href="/uploads/short-url/shJwxwOi51K080UAIwSNfr2EqKS.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c63e12148972fcf3fb628c4a4bbb208e1011a282.png" data-base62-sha1="shJwxwOi51K080UAIwSNfr2EqKS" alt="image.png" width="563" height="344" data-dominant-color="F4F2F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">720×440 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @zhuyingying1234 (2023-08-09 22:27 UTC)

<p>Thank you very much your answer.</p>

---
