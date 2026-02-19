---
topic_id: 9423
title: "Copying Seeds From One Frame To Other Frames"
date: 2019-12-07
url: https://discourse.slicer.org/t/9423
---

# Copying seeds from one frame to other frames

**Topic ID**: 9423
**Date**: 2019-12-07
**URL**: https://discourse.slicer.org/t/copying-seeds-from-one-frame-to-other-frames/9423

---

## Post #1 by @sarvpriya1985 (2019-12-07 13:18 UTC)

<p>Hi everyone,<br>
I am trying to copy seeds place in one frame to rest of the cardiac frames. However, when i try to copy the seeds, it keeps on adding multiple seeds in that particular frame, and by the time i copy all the seeds, the last frame has multiple copies of the same seed.<br>
I am attaching step by step screenshots of what I did.<br>
Due to multiple copies of seeds, the “initialize option” of grow from seeds is seen only in the original frame and the rest of the frames show only update option.</p>
<p>Would appreciate all help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a4ef83f22bbb2bc12bab3fa110bb563d5992973.jpeg" data-download-href="/uploads/short-url/farNPpMD6T3x4MG7ojNAYeacBdV.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a4ef83f22bbb2bc12bab3fa110bb563d5992973_2_690x384.jpeg" alt="Capture" data-base62-sha1="farNPpMD6T3x4MG7ojNAYeacBdV" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a4ef83f22bbb2bc12bab3fa110bb563d5992973_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a4ef83f22bbb2bc12bab3fa110bb563d5992973_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a4ef83f22bbb2bc12bab3fa110bb563d5992973_2_1380x768.jpeg 2x" data-dominant-color="8B8C94"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1905×1061 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e71425ee511a660040dad6690a449556b4dfb962.jpeg" data-download-href="/uploads/short-url/wYdsHtIXR0uzJLZwkHBFOnynCy6.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e71425ee511a660040dad6690a449556b4dfb962_2_690x395.jpeg" alt="Capture1" data-base62-sha1="wYdsHtIXR0uzJLZwkHBFOnynCy6" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e71425ee511a660040dad6690a449556b4dfb962_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e71425ee511a660040dad6690a449556b4dfb962_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e71425ee511a660040dad6690a449556b4dfb962_2_1380x790.jpeg 2x" data-dominant-color="8B8B92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1916×1097 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17ac8f5e790efafb476f0c4cf20c7755e039f76b.jpeg" data-download-href="/uploads/short-url/3nqGMk8RlTk8mpqzZLONq5fIInV.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17ac8f5e790efafb476f0c4cf20c7755e039f76b_2_690x396.jpeg" alt="Capture2" data-base62-sha1="3nqGMk8RlTk8mpqzZLONq5fIInV" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17ac8f5e790efafb476f0c4cf20c7755e039f76b_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17ac8f5e790efafb476f0c4cf20c7755e039f76b_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17ac8f5e790efafb476f0c4cf20c7755e039f76b_2_1380x792.jpeg 2x" data-dominant-color="898991"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1914×1100 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1db11250707f276c200621cd1d9329510a9967ce.jpeg" data-download-href="/uploads/short-url/4eFdGfgVCEUwmBJL69Rz0INLjwG.jpeg?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1db11250707f276c200621cd1d9329510a9967ce_2_690x397.jpeg" alt="Capture3" data-base62-sha1="4eFdGfgVCEUwmBJL69Rz0INLjwG" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1db11250707f276c200621cd1d9329510a9967ce_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1db11250707f276c200621cd1d9329510a9967ce_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1db11250707f276c200621cd1d9329510a9967ce_2_1380x794.jpeg 2x" data-dominant-color="898A91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">1918×1106 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ed4d5ff9065fe8852d62e3de783a4a1ab7630ce.jpeg" data-download-href="/uploads/short-url/4oKk1A6ijKWLrcPQvbAK4vV02JM.jpeg?dl=1" title="Capture4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ed4d5ff9065fe8852d62e3de783a4a1ab7630ce_2_690x379.jpeg" alt="Capture4" data-base62-sha1="4oKk1A6ijKWLrcPQvbAK4vV02JM" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ed4d5ff9065fe8852d62e3de783a4a1ab7630ce_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ed4d5ff9065fe8852d62e3de783a4a1ab7630ce_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ed4d5ff9065fe8852d62e3de783a4a1ab7630ce_2_1380x758.jpeg 2x" data-dominant-color="8D8E94"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture4</span><span class="informations">1916×1055 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1461ccb721058a92840c8140a34b5af0abc8b1fd.jpeg" data-download-href="/uploads/short-url/2Uj5dNm5BD7vir06PiqRQs409DD.jpeg?dl=1" title="Capture5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1461ccb721058a92840c8140a34b5af0abc8b1fd_2_690x386.jpeg" alt="Capture5" data-base62-sha1="2Uj5dNm5BD7vir06PiqRQs409DD" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1461ccb721058a92840c8140a34b5af0abc8b1fd_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1461ccb721058a92840c8140a34b5af0abc8b1fd_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1461ccb721058a92840c8140a34b5af0abc8b1fd_2_1380x772.jpeg 2x" data-dominant-color="8A8B93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture5</span><span class="informations">1940×1086 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc25fe9008e61c19a2e2daf765d03f39d8781ace.jpeg" data-download-href="/uploads/short-url/qQram6bGEPvQhiYvoTX8tqxYIRo.jpeg?dl=1" title="Capture6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc25fe9008e61c19a2e2daf765d03f39d8781ace_2_690x376.jpeg" alt="Capture6" data-base62-sha1="qQram6bGEPvQhiYvoTX8tqxYIRo" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc25fe9008e61c19a2e2daf765d03f39d8781ace_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc25fe9008e61c19a2e2daf765d03f39d8781ace_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc25fe9008e61c19a2e2daf765d03f39d8781ace_2_1380x752.jpeg 2x" data-dominant-color="8C8D95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture6</span><span class="informations">1951×1064 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-01-15 02:50 UTC)

<p>Is the segmentation a sequence?</p>

---

## Post #3 by @sarvpriya1985 (2020-01-15 03:20 UTC)

<p>Hi Andras</p>
<p>Yes segmentation is a sequence. I was using copy seeds from segmentation but it just kept on adding the seeds. By the time I was on last frame it had added all the seeds to it.</p>
<p>Thanks<br>
Sarv</p>

---

## Post #4 by @lassoan (2020-01-15 04:22 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="3" data-topic="9423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>it just kept on adding the seeds</p>
</blockquote>
</aside>
<p>Copying seeds will always add the seeds. You can copy the content from the added segments using Logical operators / Copy (or just delete the old empty seeds to avoid multiple copies). Also note that the first time you go to a new time point, the content of the segmentation is initialized from the previous time point, so if you define the seed contents first and then iterate through the sequence then you’ll get a copy of the seeds in all time points automatically.</p>

---

## Post #5 by @sarvpriya1985 (2020-01-16 18:45 UTC)

<p>Thanks Andras. Does copying seeds from logical operator allow pasting them to next time point.</p>
<p>Thanks</p>

---
