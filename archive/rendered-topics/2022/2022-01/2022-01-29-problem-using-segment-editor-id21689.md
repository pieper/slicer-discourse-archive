# Problem using Segment editor

**Topic ID**: 21689
**Date**: 2022-01-29
**URL**: https://discourse.slicer.org/t/problem-using-segment-editor/21689

---

## Post #1 by @Keivan_Ahmadi (2022-01-29 14:59 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 4.11</p>
<p>Dear all,</p>
<p>Currently, I have created a segmentation of the rat head model. I saved the following files of the segmentation for future modification.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc6cd691f7a2e3742807f7a1043d805a87d07e1.png" data-download-href="/uploads/short-url/8Ov3AlJfs0HZmV6ITEheT4dNzQR.png?dl=1" title="Screenshot 2022-01-29 133503" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc6cd691f7a2e3742807f7a1043d805a87d07e1.png" alt="Screenshot 2022-01-29 133503" data-base62-sha1="8Ov3AlJfs0HZmV6ITEheT4dNzQR" width="690" height="187" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-01-29 133503</span><span class="informations">868×236 9.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But after I load files again, I am not able to change anything. As you can see in the following screenshot I am not able to create any change in the previous segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9388c420e7f57ec4fc185ea86c65c5c7f393034.jpeg" data-download-href="/uploads/short-url/xhap2zvtqmSXglJL6BpAEiCWFSI.jpeg?dl=1" title="Screenshot 2022-01-29 134202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9388c420e7f57ec4fc185ea86c65c5c7f393034_2_690x365.jpeg" alt="Screenshot 2022-01-29 134202" data-base62-sha1="xhap2zvtqmSXglJL6BpAEiCWFSI" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9388c420e7f57ec4fc185ea86c65c5c7f393034_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9388c420e7f57ec4fc185ea86c65c5c7f393034_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9388c420e7f57ec4fc185ea86c65c5c7f393034_2_1380x730.jpeg 2x" data-dominant-color="84748D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-01-29 134202</span><span class="informations">1920×1017 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would appreciate that if someone have any idea regarding this issue. I just want to create some changes using the paint tools of the segment editor, then create a new mask.</p>
<p>Thank you in advance.</p>

---

## Post #2 by @rbumm (2022-01-29 15:26 UTC)

<p>Go further down in the effect tab and check what you have got here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8393b889500908b78bae732ef3226b43c7ed6cd.png" alt="image" data-base62-sha1="zpT22h8K08UVOAUa4NM9zCaPHeR" width="381" height="274"></p>

---

## Post #3 by @Keivan_Ahmadi (2022-01-29 15:53 UTC)

<p>Dear Rudolf,</p>
<p>Thank you very much for the reply. I checked all options in there, but nothing changed. When I try to remove some part of segmentation with the help of paint tools in the segment editor nothing changes. It seems that my file is kind of uneditable. I wonder is there any way to change that. I have attached some files concerning this problem.</p>
<p>As an example, I have plan to remove the downer part of the green segment in the following slice with the help of paint<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42194f08beabe689703e20a586267bf5180f496c.jpeg" data-download-href="/uploads/short-url/9qJJG3zpR4RwcepfV59DfUjo1nC.jpeg?dl=1" title="Screenshot 2022-01-29 164328" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42194f08beabe689703e20a586267bf5180f496c_2_690x366.jpeg" alt="Screenshot 2022-01-29 164328" data-base62-sha1="9qJJG3zpR4RwcepfV59DfUjo1nC" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42194f08beabe689703e20a586267bf5180f496c_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42194f08beabe689703e20a586267bf5180f496c_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42194f08beabe689703e20a586267bf5180f496c_2_1380x732.jpeg 2x" data-dominant-color="84758D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-01-29 164328</span><span class="informations">1920×1021 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After using the paint tool, I reach the following result (dark red part in the following screen)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9202c394854794e72c6608d8848c11b853007e36.jpeg" data-download-href="/uploads/short-url/kPFDdjwVglYoU8hOICzylBdMYui.jpeg?dl=1" title="Screenshot 2022-01-29 164510" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9202c394854794e72c6608d8848c11b853007e36_2_690x367.jpeg" alt="Screenshot 2022-01-29 164510" data-base62-sha1="kPFDdjwVglYoU8hOICzylBdMYui" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9202c394854794e72c6608d8848c11b853007e36_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9202c394854794e72c6608d8848c11b853007e36_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9202c394854794e72c6608d8848c11b853007e36_2_1380x734.jpeg 2x" data-dominant-color="A17C8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-01-29 164510</span><span class="informations">1916×1020 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After I saved this change and reload the files, I did not see any change. I would like to modify the loading file, but it seems that it is not possible and I don’t know what is the problem.</p>

---

## Post #4 by @rbumm (2022-01-29 20:00 UTC)

<p>You can put one online for download (bundle them as MRB) and post the link here.</p>

---
