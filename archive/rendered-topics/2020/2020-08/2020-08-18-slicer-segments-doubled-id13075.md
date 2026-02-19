---
topic_id: 13075
title: "Slicer Segments Doubled"
date: 2020-08-18
url: https://discourse.slicer.org/t/13075
---

# Slicer segments doubled

**Topic ID**: 13075
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/slicer-segments-doubled/13075

---

## Post #1 by @skentis (2020-08-18 15:31 UTC)

<p>Hello!</p>
<p>When I opened my data in slicer today the segments were doubled so when I turn off visibility for a segment or erase part of it there’s still another layer of the segment underneath. I attached an image of trying to erase part of the segment. Any idea how to fix this?</p>
<p>Thanks!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a69cdedd457514b74d906bf96e15bfea7cea70.png" alt="Screen Shot 2020-08-18 at 11.30.31 AM" data-base62-sha1="jdaWJhVPYfu7AB4kDiw7XLDWFby" width="388" height="300"></p>

---

## Post #2 by @lassoan (2020-08-18 15:41 UTC)

<p>Probably you loaded all the files in the output folder. The folder contains a scene file (.mrml) and various data files (image, segmentation, etc.).</p>
<p>It is enough to load the scene file (.mrml), which loads all the other files, that were in the scene when you saved it.</p>
<p>If you also load individual data files then you will end up loading everything twice.</p>

---

## Post #3 by @skentis (2020-08-18 15:47 UTC)

<p>Thanks for the quick response! I tried several times to just load the .mrml (screen shot attached) but it keeps loading twice. Could it have accidentally been saved as double/is there a way to undo that?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8aca11dc3f1a6d1595a92d0017453d9be692a4de.png" data-download-href="/uploads/short-url/jNMP39vCFuJKkgjoFqpdCVCaxPg.png?dl=1" title="Screen Shot 2020-08-18 at 11.44.37 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aca11dc3f1a6d1595a92d0017453d9be692a4de_2_690x175.png" alt="Screen Shot 2020-08-18 at 11.44.37 AM" data-base62-sha1="jNMP39vCFuJKkgjoFqpdCVCaxPg" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aca11dc3f1a6d1595a92d0017453d9be692a4de_2_690x175.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8aca11dc3f1a6d1595a92d0017453d9be692a4de_2_1035x262.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8aca11dc3f1a6d1595a92d0017453d9be692a4de.png 2x" data-dominant-color="282829"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-18 at 11.44.37 AM</span><span class="informations">1166×296 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-08-18 15:48 UTC)

<p>You con go to Data module to review what you have in the scene and delete what you don’t need.</p>

---

## Post #5 by @skentis (2020-08-18 15:54 UTC)

<p>Oh awesome! So just to make sure I don’t mess anything up I should just click delete on this top “Segmentation”?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d4061a593768b92448fb69796a37c1c17bebcbc.png" data-download-href="/uploads/short-url/diWla5Kle7EQLrakTKR6rgvfCkk.png?dl=1" title="Screen Shot 2020-08-18 at 11.52.21 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d4061a593768b92448fb69796a37c1c17bebcbc_2_690x116.png" alt="Screen Shot 2020-08-18 at 11.52.21 AM" data-base62-sha1="diWla5Kle7EQLrakTKR6rgvfCkk" width="690" height="116" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d4061a593768b92448fb69796a37c1c17bebcbc_2_690x116.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d4061a593768b92448fb69796a37c1c17bebcbc_2_1035x174.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d4061a593768b92448fb69796a37c1c17bebcbc.png 2x" data-dominant-color="2E3E54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-18 at 11.52.21 AM</span><span class="informations">1218×206 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-08-18 15:56 UTC)

<p>That segmentation does not have segments, so I don’t think it would make a difference, but you can delete it. You may either have more segmentations (or duplicate segment in the same segmentation) or an exported labelmap in the scene.</p>

---

## Post #7 by @skentis (2020-08-18 15:56 UTC)

<p>Deleting it fixed the issue I think! Thanks so much for your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
