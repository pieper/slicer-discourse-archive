# The segmentation statistics with Lung Ct Anlizer does not show the results correctly.

**Topic ID**: 34336
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/the-segmentation-statistics-with-lung-ct-anlizer-does-not-show-the-results-correctly/34336

---

## Post #1 by @Marcelo_Sanchez (2024-02-14 23:07 UTC)

<p>I recently installed 3d slicer 5.6.1 and noticed that the LungCTAnlizar results are not displaying well, the lung segmentation data is exactly the same, so, in the different lung segments shows the same results, how can I correct this data, what am I doing wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b8349802bd1e17f201b5864cd1d7f3c812c569.jpeg" data-download-href="/uploads/short-url/tVgrSwBxecv1JhK8phElaDQggCl.jpeg?dl=1" title="test" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1b8349802bd1e17f201b5864cd1d7f3c812c569_2_388x500.jpeg" alt="test" data-base62-sha1="tVgrSwBxecv1JhK8phElaDQggCl" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1b8349802bd1e17f201b5864cd1d7f3c812c569_2_388x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1b8349802bd1e17f201b5864cd1d7f3c812c569_2_582x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1b8349802bd1e17f201b5864cd1d7f3c812c569_2_776x1000.jpeg 2x" data-dominant-color="E7E9E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test</span><span class="informations">798×1027 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2024-02-15 12:07 UTC)

<p>This looks like a bug, I will check the sources and keep you updated …</p>

---

## Post #3 by @rbumm (2024-02-15 15:47 UTC)

<p>Ok it is not a bug, but a weakness of LungCTAnalyzer which runs a  “Lobe analysis” when checked even on a lung segmentation with only two lungs and no lobes segmented.<br>
This is the reason why you get the “false” results.<br>
Please use one of the AI tools that are offered in LungCTSegmenter (lungmaskLCRTLobes or Totalsegmentator basic) to create lobe segmentations and then run LungCTAnalyzer again.<br>
We will implement a detection of the missing lobe segmentatons in LCTA to avoid confusion to the user.<br>
Thank you for the report !</p>

---

## Post #4 by @Marcelo_Sanchez (2024-02-18 16:19 UTC)

<p>Dear,</p>
<p>Thank you very much for your quick answer, I am sending you a picture with the results after the analysis with Lung CT Analyzer, I did it after following your advice.</p>
<p>Regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/664dc172c83a199c0046912b0b8118d666de13da.jpeg" data-download-href="/uploads/short-url/eB1i9bXIHW3TUSegdCgKN7W76B4.jpeg?dl=1" title="LCTA" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/664dc172c83a199c0046912b0b8118d666de13da_2_354x500.jpeg" alt="LCTA" data-base62-sha1="eB1i9bXIHW3TUSegdCgKN7W76B4" width="354" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/664dc172c83a199c0046912b0b8118d666de13da_2_354x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/664dc172c83a199c0046912b0b8118d666de13da.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/664dc172c83a199c0046912b0b8118d666de13da.jpeg 2x" data-dominant-color="EAEAE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LCTA</span><span class="informations">491×692 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @rbumm (2024-02-18 16:23 UTC)

<p>Does this look ok now? Please confirm …</p>

---

## Post #6 by @Marcelo_Sanchez (2024-02-18 22:53 UTC)

<p>Im sorry, yes, it works perfect and the analysis is very good.</p>
<p>Thanks again.</p>
<p>Marcelo.</p>

---
