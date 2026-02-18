# Import Folder Structure in Windows Explorer to Subject Hierarchy

**Topic ID**: 12796
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/import-folder-structure-in-windows-explorer-to-subject-hierarchy/12796

---

## Post #1 by @Ryan_Morrison (2020-07-30 19:27 UTC)

<p>Is there a way to import a bunch of models into the subject hierarchy while maintaining their folder structure? It would be nice to not have to manually create the folder structure in slicer.</p>
<p>Windows explorer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6edcb4d39ad69038a50d5d50a7eeebb8580a3a05.png" data-download-href="/uploads/short-url/fOJnJZl305FzZehppi2OXheQ7gF.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6edcb4d39ad69038a50d5d50a7eeebb8580a3a05.png" alt="Capture" data-base62-sha1="fOJnJZl305FzZehppi2OXheQ7gF" width="542" height="500" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">550×507 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer Hierarchy:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2626b60e3e01d3a1aa092b7a32e350775bacf6b1.png" data-download-href="/uploads/short-url/5rv55L9Ke6tCbfw7rl9IawuUCyZ.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2626b60e3e01d3a1aa092b7a32e350775bacf6b1_2_362x500.png" alt="Capture2" data-base62-sha1="5rv55L9Ke6tCbfw7rl9IawuUCyZ" width="362" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2626b60e3e01d3a1aa092b7a32e350775bacf6b1_2_362x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2626b60e3e01d3a1aa092b7a32e350775bacf6b1_2_543x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2626b60e3e01d3a1aa092b7a32e350775bacf6b1_2_724x1000.png 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1065×1467 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-07-30 19:32 UTC)

<p>To create subject hierarchy folders corresponding to location of files in the file system, right-click on an empty (white) area in the Subject hierarchy tree view and then choose “Create hierarchy from loaded directory structure”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32efd65113c296a40c5e922ed48507c9476cf34b.png" data-download-href="/uploads/short-url/7gBIMw8KBNoMWScMELoysG1SjIT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32efd65113c296a40c5e922ed48507c9476cf34b_2_669x500.png" alt="image" data-base62-sha1="7gBIMw8KBNoMWScMELoysG1SjIT" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32efd65113c296a40c5e922ed48507c9476cf34b_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32efd65113c296a40c5e922ed48507c9476cf34b_2_1003x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32efd65113c296a40c5e922ed48507c9476cf34b_2_1338x1000.png 2x" data-dominant-color="F5EFE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1339×1000 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Ryan_Morrison (2020-07-30 19:48 UTC)

<p>You’ve come to the rescue once again Andras! I really cannot thank you enough.</p>

---

## Post #4 by @cpinter (2020-07-30 20:02 UTC)

<p>I didn’t know if anybody ever used this after I implemented it years ago. Good to know someone does <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> It seems we keep it!</p>

---

## Post #5 by @lassoan (2020-07-30 20:11 UTC)

<p>I’ve just pointed it out. It was <a class="mention" href="/u/cpinter">@cpinter</a> who implemented it.</p>
<p>We should make it easier to discover.</p>

---

## Post #6 by @Ryan_Morrison (2020-07-30 20:15 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>! It’s hugely helpful. It would be nice if it was done automatically when one drags/drops a folder with many subfolders into slicer. The feature is a bit hidden.</p>

---

## Post #7 by @cpinter (2020-07-30 20:23 UTC)

<p>I agree. I thought about this back then but don’t have a good solution for making it more accessibe.</p>

---
