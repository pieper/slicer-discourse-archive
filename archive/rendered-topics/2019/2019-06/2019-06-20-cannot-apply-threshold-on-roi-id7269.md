---
topic_id: 7269
title: "Cannot Apply Threshold On Roi"
date: 2019-06-20
url: https://discourse.slicer.org/t/7269
---

# Cannot apply Threshold on ROI

**Topic ID**: 7269
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/cannot-apply-threshold-on-roi/7269

---

## Post #1 by @Apex (2019-06-20 21:57 UTC)

<p>Operating system: Windows, Linux, and Mac<br>
Slicer version:4.10.2<br>
Expected behavior: Issue 1: <strong>To “apply” “Threshold” on ROI</strong><br>
Issue 2: <strong>Can apply “Threshold”, but it is automatically reduced to a smaller region when I pressed “apply”.</strong><br>
Actual behavior:<br>
<strong>Issue 1:</strong><br>
Threshold:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b6c11f22434f9dac26e92fb0b2592eb92cfcc4.jpeg" data-download-href="/uploads/short-url/zudXEpVAkNs1lcRvGavdTFNfQtS.jpeg?dl=1" title="pasted%20image%200" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8b6c11f22434f9dac26e92fb0b2592eb92cfcc4_2_690x388.jpeg" alt="pasted%20image%200" data-base62-sha1="zudXEpVAkNs1lcRvGavdTFNfQtS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8b6c11f22434f9dac26e92fb0b2592eb92cfcc4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8b6c11f22434f9dac26e92fb0b2592eb92cfcc4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8b6c11f22434f9dac26e92fb0b2592eb92cfcc4_2_1380x776.jpeg 2x" data-dominant-color="B0B3B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pasted%20image%200</span><span class="informations">1600×900 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Apply:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9320d35f1a0fd6a9aa9624b11a740c8885f732fc.jpeg" data-download-href="/uploads/short-url/kZyw2GUMBD48iciOkPCOFlZUdJO.jpeg?dl=1" title="pasted%20image%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9320d35f1a0fd6a9aa9624b11a740c8885f732fc_2_690x388.jpeg" alt="pasted%20image%201" data-base62-sha1="kZyw2GUMBD48iciOkPCOFlZUdJO" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9320d35f1a0fd6a9aa9624b11a740c8885f732fc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9320d35f1a0fd6a9aa9624b11a740c8885f732fc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/9320d35f1a0fd6a9aa9624b11a740c8885f732fc_2_1380x776.jpeg 2x" data-dominant-color="A8A8AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pasted%20image%201</span><span class="informations">1600×900 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Issue 2</strong><br>
Threshold: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4346312b760b3cf5e1fd0f03fd39dff3f36860e5.png" data-download-href="/uploads/short-url/9B8nkDdRABD8PwVLSz1ZIJkPpJj.png?dl=1" title="pasted%20image%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346312b760b3cf5e1fd0f03fd39dff3f36860e5_2_690x388.png" alt="pasted%20image%202" data-base62-sha1="9B8nkDdRABD8PwVLSz1ZIJkPpJj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346312b760b3cf5e1fd0f03fd39dff3f36860e5_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346312b760b3cf5e1fd0f03fd39dff3f36860e5_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346312b760b3cf5e1fd0f03fd39dff3f36860e5_2_1380x776.png 2x" data-dominant-color="A6B4AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pasted%20image%202</span><span class="informations">1600×900 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Apply: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/125269f16787518a073f266b85d9303a0bdfdeda.jpeg" data-download-href="/uploads/short-url/2C5afqVx6C5snBBhFXVnlsqAojw.jpeg?dl=1" title="pasted%20image%203" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125269f16787518a073f266b85d9303a0bdfdeda_2_690x388.jpeg" alt="pasted%20image%203" data-base62-sha1="2C5afqVx6C5snBBhFXVnlsqAojw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125269f16787518a073f266b85d9303a0bdfdeda_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125269f16787518a073f266b85d9303a0bdfdeda_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/125269f16787518a073f266b85d9303a0bdfdeda_2_1380x776.jpeg 2x" data-dominant-color="8C8E92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pasted%20image%203</span><span class="informations">1600×900 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Though the threshold is working in the majority of cases, there are few on which it is not working.<br>
Can anyone help me to resolve this?<br>
Thank you</p>

---

## Post #2 by @lassoan (2019-06-20 22:04 UTC)

<p>Preview is shown on the entire image visible in the view. When you apply the threshold, it is applied to the region specified in the segmentation node’s geometry.</p>
<p>Segmentation node’s geometry is defined by default by the first selected master node. If you switch master nodes, maximum extent of the segmentation will not change. You need to click on “Specify geometry” button to change the extent of the segmentation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d726ba2dc21621909757eb5448d8a4b909e595.png" alt="image" data-base62-sha1="zdEpRMPMXQIMYP0XcfSqruzuxjT" width="599" height="328"></p>

---

## Post #3 by @Apex (2019-06-21 05:57 UTC)

<p>Thank you very much for the support. Now its working.</p>

---

## Post #4 by @Apex (2019-06-21 10:22 UTC)

<p>Thank you for your response</p>

---
