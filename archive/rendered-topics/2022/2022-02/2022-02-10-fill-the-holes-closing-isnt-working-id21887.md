# Fill the holes(Closing) isn't working

**Topic ID**: 21887
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/fill-the-holes-closing-isnt-working/21887

---

## Post #1 by @jo1 (2022-02-10 10:33 UTC)

<p>Hi<br>
I used local threshold in order to get artery.<br>
It works well but there are some holes…<br>
So I also used Smoothing after this process but it doesn’t work.<br>
(it isn’t working, actually. but in this case, doesn;t work at all)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2448acf81c2198163c806a4574a2400d0a578efc.png" alt="image" data-base62-sha1="5aYTxxkziWKYGF8bu0yXor29FCI" width="425" height="271"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/397f6a0c01334f246f02c8b879aafe8d01d11a3b.png" alt="image" data-base62-sha1="8cEcnb1aaqmc5Bj3wOyQffvRE1R" width="530" height="355"></p>

---

## Post #2 by @chir.set (2022-02-10 10:57 UTC)

<p>These are <em>huge</em> holes, not even holes but rather an insufficient segmentation. Fill holes works well on holes <em>inside</em> a closed surface segment. Increase the kernel size according to the size of the inner holes. If this gets too big, smoothing may be a very long process. So it’s really best to segment better.</p>

---

## Post #3 by @jo1 (2022-02-10 11:22 UTC)

<p>Thank you for the fase reply!!! I found another way to improve this work.<br>
3D brush with threshold works well.</p>

---
