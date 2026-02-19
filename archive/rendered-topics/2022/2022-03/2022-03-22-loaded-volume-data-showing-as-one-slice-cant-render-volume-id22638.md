---
topic_id: 22638
title: "Loaded Volume Data Showing As One Slice Cant Render Volume"
date: 2022-03-22
url: https://discourse.slicer.org/t/22638
---

# Loaded volume data showing as one slice, cant render volume

**Topic ID**: 22638
**Date**: 2022-03-22
**URL**: https://discourse.slicer.org/t/loaded-volume-data-showing-as-one-slice-cant-render-volume/22638

---

## Post #1 by @Rhythm (2022-03-22 14:02 UTC)

<p>Hello I am loading a full body MRI dataset from a GE Signa 1.5T machine.  The data appears as only one slice of a 31 slice sequence.  I am able to select volume rendering but no volume image appears.  I am able to view the entire sequence in the Impax viewer.  Screen shot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3298d82f6fdbbfe7fb24ef8927d2bd7b3ee0ee29.png" data-download-href="/uploads/short-url/7dBl9WIBfdmQAzwIrbsHL3xhOZP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3298d82f6fdbbfe7fb24ef8927d2bd7b3ee0ee29_2_690x388.png" alt="image" data-base62-sha1="7dBl9WIBfdmQAzwIrbsHL3xhOZP" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3298d82f6fdbbfe7fb24ef8927d2bd7b3ee0ee29_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3298d82f6fdbbfe7fb24ef8927d2bd7b3ee0ee29_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3298d82f6fdbbfe7fb24ef8927d2bd7b3ee0ee29_2_1380x776.png 2x" data-dominant-color="64646C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-03-22 17:13 UTC)

<p>If the data is in dicom be sure to load via the dicom module.  If it’s in the legacy GE format you may need to uncheck the SingleFile option in the file load.  Probably we haven’t tried reading the legacy format in a very long time so bugs might have snuck into the I/O stack.</p>

---

## Post #3 by @Rhythm (2022-03-22 17:50 UTC)

<p>Thank you Steve.  I’m not sure if the data is DICOM or legacy, is there a way to tell?  Using the load data function, some of the slices default to Single File, but not all.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad32b5fa157fcfd2fe693b9ec51b01d090e39d02.png" data-download-href="/uploads/short-url/oIbfuwDvxpqfzZ3Scmsth257FIu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad32b5fa157fcfd2fe693b9ec51b01d090e39d02_2_690x388.png" alt="image" data-base62-sha1="oIbfuwDvxpqfzZ3Scmsth257FIu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad32b5fa157fcfd2fe693b9ec51b01d090e39d02_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad32b5fa157fcfd2fe693b9ec51b01d090e39d02_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad32b5fa157fcfd2fe693b9ec51b01d090e39d02_2_1380x776.png 2x" data-dominant-color="CFCFD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I uncheck the slices that default to Single File, and this is the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07c6b6e0436babdbb8aad00b3a47860bbbe15322.jpeg" data-download-href="/uploads/short-url/16N5jZe9raemPV2ocl5mTztw0kq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07c6b6e0436babdbb8aad00b3a47860bbbe15322_2_690x388.jpeg" alt="image" data-base62-sha1="16N5jZe9raemPV2ocl5mTztw0kq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07c6b6e0436babdbb8aad00b3a47860bbbe15322_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07c6b6e0436babdbb8aad00b3a47860bbbe15322_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07c6b6e0436babdbb8aad00b3a47860bbbe15322_2_1380x776.jpeg 2x" data-dominant-color="6A6B72"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b702a1b9fed6ab2937c6d4f768451e8b36eb2538.png" data-download-href="/uploads/short-url/q6Z0XSLcF6myb9M5IpVG7T3Qx9m.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b702a1b9fed6ab2937c6d4f768451e8b36eb2538_2_690x388.png" alt="image" data-base62-sha1="q6Z0XSLcF6myb9M5IpVG7T3Qx9m" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b702a1b9fed6ab2937c6d4f768451e8b36eb2538_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b702a1b9fed6ab2937c6d4f768451e8b36eb2538_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b702a1b9fed6ab2937c6d4f768451e8b36eb2538_2_1380x776.png 2x" data-dominant-color="686970"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Each slice shows as a separate volume.</p>

---

## Post #4 by @pieper (2022-03-22 18:00 UTC)

<p>It looks like the old format.  It might work to select just one file and uncheck SingleFile and the others in the same directory should be checked if they meet some similarity rules (obscure legacy format rules - you’d need to look at the code to know for sure).</p>
<p>If they are dicom, try the dicom module and see if it works.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html</a></p>
<p>If they are dicom (load in the database) but still don’t load right in the views, you might try the troubleshooting section of that page.</p>

---

## Post #5 by @Rhythm (2022-03-22 18:32 UTC)

<p>Hi Steve<br>
I have tried the Load directory function in the DICOM module.<br>
I have also tried selecting just one file and uncheck SingleFile and the others in the same directory are checked.<br>
I’m not a coder, is there a way to extract the legacy format rules from the code?</p>

---

## Post #6 by @pieper (2022-03-22 18:36 UTC)

<p>I’m afraid that if you are dealing with legacy data you will need to dig around and find a tool that works with it.  There are probably converters but if the data isn’t working with Slicer they I’m not sure what to suggest.  We used to use those GE signa machines a lot so I would have thought the reader would be working.  If you are able to post the data maybe someone could try and give suggestions.</p>

---

## Post #7 by @Rhythm (2022-03-22 18:47 UTC)

<p>Thank you Steve I will post some data in the community forum.</p>

---
