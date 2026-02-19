---
topic_id: 25597
title: "Could Not Load 303 Hrct Expiration As A Scalar Volume Hrct C"
date: 2022-10-07
url: https://discourse.slicer.org/t/25597
---

# Could not load: 303: HRCT EXPIRATION as a Scalar Volume _ HRCT chest

**Topic ID**: 25597
**Date**: 2022-10-07
**URL**: https://discourse.slicer.org/t/could-not-load-303-hrct-expiration-as-a-scalar-volume-hrct-chest/25597

---

## Post #1 by @ishankaw (2022-10-07 19:14 UTC)

<p>Hi,<br>
I have tried to load a HRCT Chest DICOM series using Slicer V. 5.0.3. I get the following error message.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e23c09c763122db033eed37452a903d874037f85.png" data-download-href="/uploads/short-url/whmxs6mN5KT7lg0dC0fzVbIRsj3.png?dl=1" title="error log" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e23c09c763122db033eed37452a903d874037f85_2_690x326.png" alt="error log" data-base62-sha1="whmxs6mN5KT7lg0dC0fzVbIRsj3" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e23c09c763122db033eed37452a903d874037f85_2_690x326.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e23c09c763122db033eed37452a903d874037f85_2_1035x489.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e23c09c763122db033eed37452a903d874037f85_2_1380x652.png 2x" data-dominant-color="2B3137"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error log</span><span class="informations">1417×670 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I tried the dicompatcher but didn’t work.</p>
<p>OS : Windows 11<br>
Slicer version : 5.0.3</p>

---

## Post #2 by @pieper (2022-10-07 20:44 UTC)

<p>That data is in a proprietary format so it’s not readable by Slicer.  You should go back to  the source of the data and ask that they export it in standard dicom format.</p>

---

## Post #3 by @ishankaw (2022-10-12 04:43 UTC)

<p>Thank you very much for the comment. I will try this.</p>

---
