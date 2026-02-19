---
topic_id: 7715
title: "I Cant Open Slicer With Guidelet Module"
date: 2019-07-23
url: https://discourse.slicer.org/t/7715
---

# I can't open Slicer with Guidelet module

**Topic ID**: 7715
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/i-cant-open-slicer-with-guidelet-module/7715

---

## Post #1 by @Zhao_Su (2019-07-23 03:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c823c75932e364f5b837c79c37e20c3bf8ca0e94.png" data-download-href="/uploads/short-url/syw9h6zwcDkC3n0fv0ML6KtNlvS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c823c75932e364f5b837c79c37e20c3bf8ca0e94.png" alt="image" data-base62-sha1="syw9h6zwcDkC3n0fv0ML6KtNlvS" width="690" height="35" data-dominant-color="0C0C0C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">774×40 1.31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d043f87f72a2be35b4ee7b834aef5a26d8eb50ec.png" data-download-href="/uploads/short-url/tIoWiSv3hG8t77hpfcem5Zbn4Kw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d043f87f72a2be35b4ee7b834aef5a26d8eb50ec_2_690x493.png" alt="image" data-base62-sha1="tIoWiSv3hG8t77hpfcem5Zbn4Kw" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d043f87f72a2be35b4ee7b834aef5a26d8eb50ec_2_690x493.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d043f87f72a2be35b4ee7b834aef5a26d8eb50ec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d043f87f72a2be35b4ee7b834aef5a26d8eb50ec.png 2x" data-dominant-color="A8A8AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">851×609 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2019-07-23 13:54 UTC)

<p>I think you need to enter a space after --python-code.</p>
<p>By the way the Guidelet module is a template that contains a base class that you need to subclass and implement to do anything. Or have you simply repurposed the class and developed an actual Guidelet in it?</p>

---
