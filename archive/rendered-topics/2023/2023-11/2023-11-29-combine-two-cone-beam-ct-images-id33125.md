# Combine two cone-beam CT images

**Topic ID**: 33125
**Date**: 2023-11-29
**URL**: https://discourse.slicer.org/t/combine-two-cone-beam-ct-images/33125

---

## Post #1 by @tenzin_kunkyab (2023-11-29 21:10 UTC)

<p>Hi Developers,</p>
<p>I think this is a new specific case problem, which is why I created another thread.</p>
<p>I have an object of size about less than 5 mm that I scanned with our linac-integrated cone-beam CT with image acquisition parameter of 0.5 mm in axial resolution and 1 mm in slice thickness resolution. In axial dimension, the resolution suffices. but in slice thickness direction, we observe partial volume effect. One possible solution that we came up with could be shifting the object, may be 0.5 mm direction either way and then scan it once again. So we are left with two cone-beam CT images, I was wondering if there is slicer functionality that can some how interweave those two CBCT images such that we have effective slice thickness resolution of about 0.5 mm? So overall resolution of the scan would 0.5 by 0.5 by 0.5 mm.</p>
<p>Looking forward to hearing from you!</p>

---

## Post #2 by @pieper (2023-11-29 23:54 UTC)

<p>If you can carefully control the 0.5mm translation without tilting the specimen then this might work, otherwise it might just add noise or blur.  You might just add the two volumes together and get a reasonable result.  Or you could write a short script to interleave the two acquisitions into a single volume.</p>

---

## Post #3 by @tenzin_kunkyab (2023-11-30 02:37 UTC)

<p>Thank you very much for your comment, yes the translational capability on the machines we are using is fairly accurate. I’d like to ask a couple of follow-up questions though.</p>
<p>1.) Add two volumes together? is there a slicer functionality that does this easily? If so what modules am I looking for?</p>
<p>2.) If option 1 doesn’t yield a good result, I would perhaps go for option two. in regards to what coding language or library would you suggest for me to look more into this?</p>
<p>Thank you for your swift response.</p>

---

## Post #4 by @pieper (2023-11-30 22:53 UTC)

<aside class="quote no-group" data-username="tenzin_kunkyab" data-post="3" data-topic="33125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tenzin_kunkyab/48/3916_2.png" class="avatar"> tenzin_kunkyab:</div>
<blockquote>
<p>1.) Add two volumes together? is there a slicer functionality that does this easily? If so what modules am I looking for?</p>
</blockquote>
</aside>
<p>I meant you could try the Add Scalar Volume.  Since these are cone beam the units probably aren’t calibrated so this would be basically the same as averaging the two.</p>
<aside class="quote no-group" data-username="tenzin_kunkyab" data-post="3" data-topic="33125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tenzin_kunkyab/48/3916_2.png" class="avatar"> tenzin_kunkyab:</div>
<blockquote>
<p>2.) If option 1 doesn’t yield a good result, I would perhaps go for option two. in regards to what coding language or library would you suggest for me to look more into this?</p>
</blockquote>
</aside>
<p>You would need to write a small python script.  You could ask an AI for details, something like this: <a href="https://g.co/bard/share/8a3fd1068580">https://g.co/bard/share/8a3fd1068580</a></p>
<p>Note that some steps could be refined, but this looks pretty close.</p>

---

## Post #5 by @tenzin_kunkyab (2023-12-04 19:00 UTC)

<p>Hi! Thank you for this, I was just trying a simple example, which generated the following error, I reinstalled the latest and stable version, both generated the same error.</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: module ‘slicer.util’ has no attribute ‘getIData’</p>
<p>Is there a way to fix this?</p>

---

## Post #6 by @tenzin_kunkyab (2023-12-05 00:36 UTC)

<p>I just tried adding two volumes method based on two slight different CT images, unfortunately it adds two adjacent slices up using that method, so thats no good.</p>

---
