# "Paging File is Too Small" error

**Topic ID**: 27379
**Date**: 2023-01-20
**URL**: https://discourse.slicer.org/t/paging-file-is-too-small-error/27379

---

## Post #1 by @MattAWard (2023-01-20 14:35 UTC)

<p>Operating system: Windows Server 2019 (Virtual Machine)<br>
Slicer version: 5.2.1<br>
Expected behavior: Total segmentation of abdominal CT using TotalSegmentator extension<br>
Actual behavior: OSError [WinError 1455] The paging file is too small for this operation to complete</p>
<p>I’ve tried in vain to increase the paging file size but nothing seems to work. The VM has 16Gb of allocated RAM so I’m not sure what the issue is. Attached is a screenshot of the paging settings.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/490babd0d8f352577d623a2599d74530b0119d7d.png" data-download-href="/uploads/short-url/aqbRmrHku1Kk2o3vkxPnEx8proF.png?dl=1" title="paging_settings" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/490babd0d8f352577d623a2599d74530b0119d7d_2_690x497.png" alt="paging_settings" data-base62-sha1="aqbRmrHku1Kk2o3vkxPnEx8proF" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/490babd0d8f352577d623a2599d74530b0119d7d_2_690x497.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/490babd0d8f352577d623a2599d74530b0119d7d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/490babd0d8f352577d623a2599d74530b0119d7d.png 2x" data-dominant-color="EAEDEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">paging_settings</span><span class="informations">880×634 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-01-20 14:41 UTC)

<p>Try turning off “Automatically manage…” and set custom size 32000MB. You can then gradually decrease the memory and see what is the minimum requirement.</p>

---

## Post #3 by @MattAWard (2023-02-02 11:48 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. This seemed to remove the paging file error (I had to create some extra room in the VM), though I’m now dealing with a low CUDA memory error. I’ll be doing some more tuning of the CPU/ GPU resources of our VM, so hopefully I’ll be able to clear that up and get it working.</p>

---
