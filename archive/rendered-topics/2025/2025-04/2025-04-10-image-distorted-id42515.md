---
topic_id: 42515
title: "Image Distorted"
date: 2025-04-10
url: https://discourse.slicer.org/t/42515
---

# Image Distorted

**Topic ID**: 42515
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/image-distorted/42515

---

## Post #1 by @amelia.eastham (2025-04-10 08:38 UTC)

<p>Does anyone know why this has suddenly happened to one of my files please?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dc1c542779c1c60dfaa9815f31291659812c42c.png" data-download-href="/uploads/short-url/1XHmerbDMQagP2REanRYpoPWiGo.png?dl=1" title="Distorted Image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc1c542779c1c60dfaa9815f31291659812c42c_2_690x393.png" alt="Distorted Image" data-base62-sha1="1XHmerbDMQagP2REanRYpoPWiGo" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc1c542779c1c60dfaa9815f31291659812c42c_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc1c542779c1c60dfaa9815f31291659812c42c_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dc1c542779c1c60dfaa9815f31291659812c42c.png 2x" data-dominant-color="E4DDE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Distorted Image</span><span class="informations">1140×650 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57fe1f33cdf4af49feae80deb702b44bc9cf632a.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db441b55aebe54d9e1fa6f5474f245d7cc6da0c.png" data-video-base62-sha1="cypZBdYSwnIDM0oJmp4SVRIZwxQ.mp4">
  </div><p></p>

---

## Post #2 by @pieper (2025-04-10 11:07 UTC)

<p>It looks like the background image geometry got changed (image width).  Let us know what file formats you used, what operations you performed, what versions of software you are using, etc to get more specific help.</p>

---

## Post #3 by @amelia.eastham (2025-04-10 16:12 UTC)

<p>Thank you for the reply.</p>
<p>I now have issues with two of my files! The first shows that it was saved at 15:33 today (as expected), but when I open it there are no images or segmentations there:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa6462d0e0ad754e7762eb586676e2898817c100.png" data-download-href="/uploads/short-url/ojmffA1rryeOG9PZtX0RGXEyA9O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa6462d0e0ad754e7762eb586676e2898817c100_2_690x133.png" alt="image" data-base62-sha1="ojmffA1rryeOG9PZtX0RGXEyA9O" width="690" height="133" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa6462d0e0ad754e7762eb586676e2898817c100_2_690x133.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa6462d0e0ad754e7762eb586676e2898817c100_2_1035x199.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa6462d0e0ad754e7762eb586676e2898817c100_2_1380x266.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1568×303 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The second is showing this error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d96670f7e7ab42652031605c0c0b62c706b986.png" data-download-href="/uploads/short-url/g6jfLRHpjUALMpPBBcthiLe86fc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70d96670f7e7ab42652031605c0c0b62c706b986_2_690x446.png" alt="image" data-base62-sha1="g6jfLRHpjUALMpPBBcthiLe86fc" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70d96670f7e7ab42652031605c0c0b62c706b986_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70d96670f7e7ab42652031605c0c0b62c706b986_2_1035x669.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70d96670f7e7ab42652031605c0c0b62c706b986_2_1380x892.png 2x" data-dominant-color="F0EEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1618×1046 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am using dicom files, segmenting using the segment editor, version 5.8.0, and then just saving the files to my chosen directory.</p>

---

## Post #4 by @lassoan (2025-04-10 18:52 UTC)

<p>It looks like the files are corrupted. Most likely you have run out of space but it may be due to using a network/cloud drive or external drive. Have you received any error messages when you saved the scene? If you run a disk check does it find any problems?</p>

---

## Post #5 by @amelia.eastham (2025-04-11 10:42 UTC)

<p>There is plenty of space on the USB. I ran a disk check and now the file has been deleted:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6057bb338199d264bbf0baa356cd6058ef45fa19.png" data-download-href="/uploads/short-url/dKhND9NoKYDLb18ZEqpekBo6NQd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6057bb338199d264bbf0baa356cd6058ef45fa19_2_690x121.png" alt="image" data-base62-sha1="dKhND9NoKYDLb18ZEqpekBo6NQd" width="690" height="121" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6057bb338199d264bbf0baa356cd6058ef45fa19_2_690x121.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6057bb338199d264bbf0baa356cd6058ef45fa19_2_1035x181.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6057bb338199d264bbf0baa356cd6058ef45fa19_2_1380x242.png 2x" data-dominant-color="F9FAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1614×284 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is still no fix with this error either:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33f541d5a858ee2a5e50b1bd7f9e2a1c20599d0f.png" data-download-href="/uploads/short-url/7pDOlvTSHrxqkSs6f6JfYPmML5t.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33f541d5a858ee2a5e50b1bd7f9e2a1c20599d0f_2_690x446.png" alt="image" data-base62-sha1="7pDOlvTSHrxqkSs6f6JfYPmML5t" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33f541d5a858ee2a5e50b1bd7f9e2a1c20599d0f_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33f541d5a858ee2a5e50b1bd7f9e2a1c20599d0f_2_1035x669.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33f541d5a858ee2a5e50b1bd7f9e2a1c20599d0f_2_1380x892.png 2x" data-dominant-color="EFEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×892 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any further advice, please?</p>

---

## Post #6 by @lassoan (2025-04-11 18:54 UTC)

<aside class="quote no-group" data-username="amelia.eastham" data-post="5" data-topic="42515">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/278dde/48.png" class="avatar"> amelia.eastham:</div>
<blockquote>
<p>I ran a disk check and now the file has been deleted:</p>
</blockquote>
</aside>
<p>This indicates that this USB drive is not working reliably. Maybe you accidentally touched the USB connector while it was writing files, or maybe you unplugged the USB cable without detaching the drive, etc. You can avoid such issues if you work on an internal drive and copy files to the USB drive when you are done.</p>
<p>The file that you get the error for is corrupted. If disk repair did not fix it then probably you cannot recover its content.</p>

---

## Post #7 by @amelia.eastham (2025-04-14 09:18 UTC)

<p>I saved this file a couple of months ago and have opened/accessed it many times since. The error message has occurred all of a sudden with no changes to the files etc.</p>

---

## Post #8 by @lassoan (2025-04-14 12:21 UTC)

<p>The <code>_nrrdEncoeingGzip_read: error reading from gzFile</code> is a very low level error message, which means that the file is corrupted. If you had successfully read this file before but not anymore then most likely the corruption is caused by a problem with your storage device.</p>
<p>The disk check result (errors were found, files were deleted) also indicates malfunction of the storage device.</p>

---

## Post #9 by @amelia.eastham (2025-04-14 12:46 UTC)

<p>I have now resolved this issue. Thank you for any responses</p>

---
