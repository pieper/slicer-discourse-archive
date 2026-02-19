---
topic_id: 29136
title: "How To Test My Own Data In Totalsegmentator"
date: 2023-04-26
url: https://discourse.slicer.org/t/29136
---

# How to test my own data in TotalSegmentator

**Topic ID**: 29136
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/how-to-test-my-own-data-in-totalsegmentator/29136

---

## Post #1 by @whu (2023-04-26 11:04 UTC)

<p>After installed the TotalSegmentator extensions successfully, the example dataset was good.<br>
But when using the WH-2019 dataset(<a href="https://zmiclab.github.io/zxh/0/mmwhs/" class="inline-onebox" rel="noopener nofollow ugc">Multi-Modality Whole Heart Segmentation Challenge</a>), one of the test ct data,<br>
the result is like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ac368dc4dfb31da235b67aa59c6fa22f0f0a7e3.png" data-download-href="/uploads/short-url/3OL4Nv4meWeWESR2BKuBPVsLl8T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ac368dc4dfb31da235b67aa59c6fa22f0f0a7e3_2_690x351.png" alt="image" data-base62-sha1="3OL4Nv4meWeWESR2BKuBPVsLl8T" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ac368dc4dfb31da235b67aa59c6fa22f0f0a7e3_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ac368dc4dfb31da235b67aa59c6fa22f0f0a7e3_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ac368dc4dfb31da235b67aa59c6fa22f0f0a7e3_2_1380x702.png 2x" data-dominant-color="9A9598"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1867×951 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
seemed not as the CTA example dataset in Slicer.<br>
Here, what about the common CT data loaded in Slicer, how to set the parameters in order to get the correct results?<br>
thanks.</p>

---

## Post #2 by @whu (2023-05-12 12:58 UTC)

<p>Nobody care this ? <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=12" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @ATAKAN_Isik (2023-05-13 13:15 UTC)

<p>Hi,<br>
As far i know totalsegmentator use nn-UNET. You can use this network on pyhton for testing your own data<br>
<a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a> is the github repo for this network .</p>

---

## Post #4 by @rbumm (2023-05-14 18:09 UTC)

<p>Are all of the test data giving you a problem? Or just this single one from a bigger dataset?<br>
If it is just this only series you may want to find out the reason in what way these data are different. You could start in the Volume module under “Advanced” and compare.</p>

---
