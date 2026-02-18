# Get oriented bounding boxes for each segment

**Topic ID**: 19796
**Date**: 2021-09-21
**URL**: https://discourse.slicer.org/t/get-oriented-bounding-boxes-for-each-segment/19796

---

## Post #1 by @jumbojing (2021-09-21 22:58 UTC)

<p>是不是可以开发自动boundingbox功能呢?如果能够 oriented bounding <em>box</em> 就太好了…</p>
<blockquote>
<p>Is it possible to develop an automatic boundingbox function? It would be great if it could be oriented bounding <em>box</em>…</p>
</blockquote>

---

## Post #2 by @lassoan (2021-09-22 00:38 UTC)

<p>This feature is already available in Segment Statistics module. See complete example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment">here</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63d764c1f909a0860b9dd3284818f95b5d9abde9.jpeg" data-download-href="/uploads/short-url/efeKo5nx72AhFF0EH7hPjrjQjG1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d764c1f909a0860b9dd3284818f95b5d9abde9_2_690x420.jpeg" alt="image" data-base62-sha1="efeKo5nx72AhFF0EH7hPjrjQjG1" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d764c1f909a0860b9dd3284818f95b5d9abde9_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d764c1f909a0860b9dd3284818f95b5d9abde9_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d764c1f909a0860b9dd3284818f95b5d9abde9_2_1380x840.jpeg 2x" data-dominant-color="484748"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1169 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @jumbojing (2021-09-22 00:42 UTC)

<p>That is Great! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> Thanks</p>

---

## Post #4 by @jumbojing (2022-07-18 12:09 UTC)

<p>我用这个示例做了pedicle的obb，又用以下代码crop volume：</p>
<blockquote>
<p>I used this example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment" rel="noopener nofollow ugc">here </a>to make the obb of the pedicle, and also used the following code to crop the volume:</p>
</blockquote>
<p><code>cropLogic = slicer.modules.cropvolume.logic() crop_module = slicer.vtkMRMLCropVolumeParametersNode() crop_module.SetROINodeID(roi.GetID()) crop_module.SetInputVolumeNodeID(volume.GetID()) crop_module.SetVoxelBased(True) cropLogic.Apply(crop_module) </code></p>
<p>却得到了下面我不想要的结果（注意：红色的是得到的obb）：</p>
<blockquote>
<p>But I get the following result that I don’t want(Note: the red one is the obb):</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c693a5f87890110d6566734f3cc04203e350b68.png" data-download-href="/uploads/short-url/ft312An1ai3ElhmUWLrLx0VinKE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c693a5f87890110d6566734f3cc04203e350b68_2_407x500.png" alt="image" data-base62-sha1="ft312An1ai3ElhmUWLrLx0VinKE" width="407" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c693a5f87890110d6566734f3cc04203e350b68_2_407x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c693a5f87890110d6566734f3cc04203e350b68_2_610x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c693a5f87890110d6566734f3cc04203e350b68.png 2x" data-dominant-color="1D1716"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">666×818 56.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>What’s wrong?</p>
</blockquote>

---

## Post #5 by @jumbojing (2022-07-18 12:45 UTC)

<p>好吧，解决了。。。</p>
<blockquote>
<p>Well, I’ve solved.  .  .</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48e3fd7f51089a292529418c9c1126dd023238e0.png" data-download-href="/uploads/short-url/aoOQmVy22ctQcldeYhzQSkSiVpu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48e3fd7f51089a292529418c9c1126dd023238e0_2_265x500.png" alt="image" data-base62-sha1="aoOQmVy22ctQcldeYhzQSkSiVpu" width="265" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48e3fd7f51089a292529418c9c1126dd023238e0_2_265x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48e3fd7f51089a292529418c9c1126dd023238e0_2_397x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48e3fd7f51089a292529418c9c1126dd023238e0_2_530x1000.png 2x" data-dominant-color="1D1714"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×1120 46.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
