# Issues with “open a dialog”

**Topic ID**: 43377
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/issues-with-open-a-dialog/43377

---

## Post #1 by @doc-xie (2025-06-17 04:10 UTC)

<p>Hi everyone,<br>
In the “DICOM patcher” or “Diffusion-weighted DICOM Import (DICOM2niixGUI)” of Slicer(version-4.11.0), after click the button “open a dialog”, there is no any response or any dialog windows appeared. Moreover, there is not any error information in the “log message”.<br>
The details are list in the attachement.<br>
How to fix the issues?<br>
Thans,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e9894922c41829793ec696164176d6710fb5580.png" data-download-href="/uploads/short-url/8VKvjuIMr6DGk0BwQ1GngEatpN6.png?dl=1" title="截屏2025-06-17 11.45.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e9894922c41829793ec696164176d6710fb5580_2_690x337.png" alt="截屏2025-06-17 11.45.29" data-base62-sha1="8VKvjuIMr6DGk0BwQ1GngEatpN6" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e9894922c41829793ec696164176d6710fb5580_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e9894922c41829793ec696164176d6710fb5580_2_1035x505.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e9894922c41829793ec696164176d6710fb5580_2_1380x674.png 2x" data-dominant-color="EEEEF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2025-06-17 11.45.29</span><span class="informations">1668×816 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd365014a4cd2715e50e72b9d19fc14749bcbc1e.png" data-download-href="/uploads/short-url/thofg3gy4rMEM8B1S8w7zeUqAdU.png?dl=1" title="截屏2025-06-17 11.45.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd365014a4cd2715e50e72b9d19fc14749bcbc1e_2_690x349.png" alt="截屏2025-06-17 11.45.59" data-base62-sha1="thofg3gy4rMEM8B1S8w7zeUqAdU" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd365014a4cd2715e50e72b9d19fc14749bcbc1e_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd365014a4cd2715e50e72b9d19fc14749bcbc1e_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd365014a4cd2715e50e72b9d19fc14749bcbc1e_2_1380x698.png 2x" data-dominant-color="EBEBEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2025-06-17 11.45.59</span><span class="informations">1668×844 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf2581db45952be9c14e73a4ba17231d9bccbda.png" data-download-href="/uploads/short-url/xFhqo4iGiQiHFYNSWZ6kKj6kDuq.png?dl=1" title="截屏2025-06-17 12.09.05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebf2581db45952be9c14e73a4ba17231d9bccbda_2_379x500.png" alt="截屏2025-06-17 12.09.05" data-base62-sha1="xFhqo4iGiQiHFYNSWZ6kKj6kDuq" width="379" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebf2581db45952be9c14e73a4ba17231d9bccbda_2_379x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf2581db45952be9c14e73a4ba17231d9bccbda.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf2581db45952be9c14e73a4ba17231d9bccbda.png 2x" data-dominant-color="C6DAE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2025-06-17 12.09.05</span><span class="informations">560×738 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2025-06-17 07:25 UTC)

<p>It reminds me of <a href="https://github.com/commontk/CTK/commit/92988fed9e620eb8161c60f915546229b8202565" class="inline-onebox" rel="noopener nofollow ugc">BUG: avoid app freeze on mac · commontk/CTK@92988fe · GitHub</a> which was quite a long time ago.</p>
<p>To try and fix the issue, please install latest Slicer stable 5.8.1 from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>. You are currently using a 4.11 version which is quite old and that has been numerous fixes and improvements since then.</p>

---
