---
topic_id: 26702
title: "When Importing Data On 3Dslicer Version 5 0 The Data Display"
date: 2022-12-13
url: https://discourse.slicer.org/t/26702
---

# When importing data on 3dslicer version 5.0, the data displayed is different from the original data

**Topic ID**: 26702
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/when-importing-data-on-3dslicer-version-5-0-the-data-displayed-is-different-from-the-original-data/26702

---

## Post #1 by @FUFU (2022-12-13 07:04 UTC)

<p>For example, when I imported dicom data on 3dslicer on version 4.8, it would show the mark traces of layers 162 to 167.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24145e4e71d7894fc2e2a62be082f4076e23fb43.jpeg" data-download-href="/uploads/short-url/59aPkPg1pahTvQK8e7pO9iatOfx.jpeg?dl=1" title="8954f66e098e4966b8c00c02ec284ad" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24145e4e71d7894fc2e2a62be082f4076e23fb43_2_690x470.jpeg" alt="8954f66e098e4966b8c00c02ec284ad" data-base62-sha1="59aPkPg1pahTvQK8e7pO9iatOfx" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24145e4e71d7894fc2e2a62be082f4076e23fb43_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24145e4e71d7894fc2e2a62be082f4076e23fb43_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24145e4e71d7894fc2e2a62be082f4076e23fb43.jpeg 2x" data-dominant-color="9A9A9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8954f66e098e4966b8c00c02ec284ad</span><span class="informations">1286×876 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But if I run the same dicom data on version 5.0, it only shows traces of data from layers 163 to 167.That means the mark 162 is not visible<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c47d2421ad996131747da5b82a6b089a098bbf24.jpeg" data-download-href="/uploads/short-url/s2dHgzWNsrFjJ0XjL3oDMVHwn2Y.jpeg?dl=1" title="3cf6a11a5601be38efc22248e267efe" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c47d2421ad996131747da5b82a6b089a098bbf24_2_690x466.jpeg" alt="3cf6a11a5601be38efc22248e267efe" data-base62-sha1="s2dHgzWNsrFjJ0XjL3oDMVHwn2Y" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c47d2421ad996131747da5b82a6b089a098bbf24_2_690x466.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c47d2421ad996131747da5b82a6b089a098bbf24_2_1035x699.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c47d2421ad996131747da5b82a6b089a098bbf24_2_1380x932.jpeg 2x" data-dominant-color="929192"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3cf6a11a5601be38efc22248e267efe</span><span class="informations">1479×999 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Another problem also occurred: When running on version 5.0, the 156th layer name appeared twice and the 155th layer name was omitted, which would not have occurred with the same dicom data running on version 4.8.The following two figures show the problems above version 5.0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a159fcec614cd35c8323b794e4aeb6273392b14.jpeg" data-download-href="/uploads/short-url/lZ5Rkz2YNtG1TidMNPRNwmlGeJS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a159fcec614cd35c8323b794e4aeb6273392b14_2_638x500.jpeg" alt="image" data-base62-sha1="lZ5Rkz2YNtG1TidMNPRNwmlGeJS" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a159fcec614cd35c8323b794e4aeb6273392b14_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a159fcec614cd35c8323b794e4aeb6273392b14_2_957x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a159fcec614cd35c8323b794e4aeb6273392b14.jpeg 2x" data-dominant-color="8A8B8B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1151×902 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52d0685c581941630d4db89eb9ed5c7057ed31f2.jpeg" data-download-href="/uploads/short-url/bOBFa8psnLv0pYiMgemGvPgdMtQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52d0685c581941630d4db89eb9ed5c7057ed31f2_2_642x500.jpeg" alt="image" data-base62-sha1="bOBFa8psnLv0pYiMgemGvPgdMtQ" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52d0685c581941630d4db89eb9ed5c7057ed31f2_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52d0685c581941630d4db89eb9ed5c7057ed31f2_2_963x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52d0685c581941630d4db89eb9ed5c7057ed31f2.jpeg 2x" data-dominant-color="878888"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1143×890 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This page count problem came up a few times, but I checked that the renaming in my folder was OK<br>
Although this problem is sometimes small, but the problem is a few pages at a time, it is still affected.Thank you all.</p>

---

## Post #2 by @pieper (2022-12-13 13:15 UTC)

<p>I’m not sure what you mean by ‘mark traces’. Can you clarify?  It would be best if you could share a deidentified example to get the best advice.</p>

---

## Post #3 by @FUFU (2022-12-14 01:15 UTC)

<p>This is the doodle trace of the segmenteditor paint function.</p>

---

## Post #4 by @lassoan (2022-12-14 06:49 UTC)

<p>Have you loaded DICOM data using the DICOM module?</p>

---

## Post #5 by @FUFU (2022-12-15 07:06 UTC)

<p>yes I use DICOM module</p>

---

## Post #6 by @lassoan (2022-12-15 14:08 UTC)

<p>We are not aware of any issues regarding loading of clinical CT images. If there is any difference compared to previous versions, then most likely Slicer-5.2.1 provides the correct result.</p>
<aside class="quote no-group" data-username="FUFU" data-post="1" data-topic="26702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/50afbb/48.png" class="avatar"> FUFU:</div>
<blockquote>
<p>Another problem also occurred: When running on version 5.0, the 156th layer name appeared twice and the 155th layer name was omitted,</p>
</blockquote>
</aside>
<p>This is the correct behavior when slice spacing is varying throughought the image (either because it was acquired with varying slice spacing to save dose; or because a few files were corrupted or misplaced).</p>
<p>Have you received any message about varying slice spacing when you loaded the image? Is there a <code>... acquisition transform</code> in the scene after you loaded the image?</p>

---
