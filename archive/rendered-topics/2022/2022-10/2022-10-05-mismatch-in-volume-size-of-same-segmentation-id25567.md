# Mismatch in volume size of same segmentation

**Topic ID**: 25567
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/mismatch-in-volume-size-of-same-segmentation/25567

---

## Post #1 by @Young_Wang (2022-10-05 23:20 UTC)

<p>Hi there,</p>
<p>I’m working on a registration-related project. While I was working on this project, I noticed something interesting after performing the following steps:</p>
<ol>
<li>created a segmentation from one volume</li>
<li>shifted the original volume via a linear transformation</li>
<li>created a second segmentation from the transformed volume</li>
<li>performed segment comparison</li>
</ol>
<p>I noticed that the reference volume and the compare volumes are different in size under the Dice similarity metrics. I wonder if I misunderstood how to use the segment comparison module or if there is a bug that needs to be addressed.</p>
<p>I attached a screenshot of what I have just described and a screenshot. I can send you a copy of what I did(I tried to include the source file here but I can’t upload it from here)<br>
Thanks in advance for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33cd5b4b8cab3306ca5802249ee14814b774da03.jpeg" data-download-href="/uploads/short-url/7ogkbjOXl9Y365qDpc6yniG0jn5.jpeg?dl=1" title="Screen Shot 2022-10-05 at 20.06.43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cd5b4b8cab3306ca5802249ee14814b774da03_2_690x396.jpeg" alt="Screen Shot 2022-10-05 at 20.06.43" data-base62-sha1="7ogkbjOXl9Y365qDpc6yniG0jn5" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cd5b4b8cab3306ca5802249ee14814b774da03_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cd5b4b8cab3306ca5802249ee14814b774da03_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cd5b4b8cab3306ca5802249ee14814b774da03_2_1380x792.jpeg 2x" data-dominant-color="ABA4A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-05 at 20.06.43</span><span class="informations">4064×2334 738 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @ebrahim (2022-10-06 13:02 UTC)

<p>Could the difference be due to the discrete regular grid?</p>
<p>Depending on your policy for when to include or exclude voxels that are only partially in the target region, segmentation might not commute with rigid rotation. Exaggerated example rotating a square and getting larger segmentation:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3170f6875516594ad7ecce0e1212cd1fb4177e39.png" alt="image" data-base62-sha1="73npVriY0BJGph1FYxM17R5KaaB" width="341" height="157"></p>

---

## Post #3 by @Young_Wang (2022-10-07 19:31 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> thank you for your reply. I found out the issue by doing the following:</p>
<ol>
<li>created a segmentation from one volume</li>
<li>clone the original volume</li>
<li>shifted the cloned volume via a linear transformation</li>
<li>created a second segmentation from the cloned volume</li>
<li>performed segment comparison</li>
</ol>
<p>With that change, the reference volume and the compare volume now have the same size.</p>

---
