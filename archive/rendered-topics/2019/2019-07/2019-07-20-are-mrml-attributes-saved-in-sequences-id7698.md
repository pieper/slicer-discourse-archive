---
topic_id: 7698
title: "Are Mrml Attributes Saved In Sequences"
date: 2019-07-20
url: https://discourse.slicer.org/t/7698
---

# Are MRML attributes saved in Sequences?

**Topic ID**: 7698
**Date**: 2019-07-20
**URL**: https://discourse.slicer.org/t/are-mrml-attributes-saved-in-sequences/7698

---

## Post #1 by @ungi (2019-07-20 22:29 UTC)

<p>Hi,</p>
<p>Are MRML node attributes saved and loaded by Sequences? My suspicion is that they are not. I tried adding attributes to an image and scrolling the Sequence Browser to new images. But the attributes stayed. I also tried recording a sequence of images with attributes, but as I’m replaying the sequence the attributes in the proxy node seem to remain unchanged.</p>
<p>What I wanted to do is record a sequence of segmentations (for a sequence of ultrasound images) and make note in the recorded nodes which original sequence index corresponded to them. I wanted to avoid duplicate segmentations by checking if the original sequence index has been saved in the segmentation sequence, and overwrite the segmentation if that same index already existed.<br>
If attributes are not saved/loaded with sequences, what other option do I have to tag MRML nodes in a sequence?</p>
<p>Thanks,<br>
Tamas</p>

---

## Post #2 by @adamrankin (2019-07-20 23:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Is this possibly the read/write issue that tricked us when changing segmentations with each frame of video?</p>
<p><a class="mention" href="/u/ungi">@ungi</a> You may try playing with the checkboxes in the sequence browser or sequences module.</p>

---

## Post #3 by @lassoan (2019-07-21 00:59 UTC)

<p>It seems that attributes have not been copied to/from the proxy node. I’ve <a href="https://github.com/SlicerRt/Sequences/commit/54f33bc4f6f588e0196562d0d76733d9a215ec27" rel="nofollow noopener">fixed this now</a>, so tomorrow you can try if it works as you would expect.</p>

---

## Post #4 by @ungi (2019-07-21 02:29 UTC)

<p>Thank you! I will test it tomorrow.</p>

---

## Post #5 by @ungi (2019-07-21 14:30 UTC)

<p>Today, attributes values are saved and replayed with sequences. Thank you!<br>
However, I think there are two use case that is not handled correctly yet.</p>
<ol>
<li>
</li>
</ol>
<p>Attributes are not restored after saving and loading the scene.<br>
I’ve created a sequence with different attribute values, and they were nicely replayed. Then I saved the scene, restarted Slicer, and reloaded the scene. The attribute value remained what it was when the scene was saved, but never changed anymore when the sequence was replayed.</p>
<ol start="2">
<li>
</li>
</ol>
<p>If a proxy node has a new attribute, which did not exist when previous instances were saved in a sequence, I expect that attribute to be deleted when previous instances are replayed. Today, those attributes remain unchanged with replay, keeping “random” values from previous instances.<br>
E.g. when I segment a recorded ultrasound sequence, I tag already segmented images with attributes before recording them in another sequence. I was planning to check if that attribute exists, to decide if the image has been previously segmented or not. But when I step to brand new instances (never segmented) in the input sequence, the attribute and its value remains in the proxy node, making it appear as if the image was already segmented.</p>

---

## Post #6 by @lassoan (2019-07-22 04:39 UTC)

<aside class="quote no-group" data-username="ungi" data-post="5" data-topic="7698">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>Attributes are not restored after saving and loading the scene.</p>
</blockquote>
</aside>
<p>I’ve tested this and it worked fine for me. If you change the attribute after you created the snapshot then you need to enable “Save node changes” (that’s what <a class="mention" href="/u/adamrankin">@adamrankin</a> referred to above). If it still does not work then let me know.</p>
<aside class="quote no-group" data-username="ungi" data-post="5" data-topic="7698">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>If a proxy node has a new attribute, which did not exist when previous instances were saved in a sequence, I expect that attribute to be deleted when previous instances are replayed.</p>
</blockquote>
</aside>
<p>I’ve fixed this, it should work well in Sequences extension installed/updated on Monday or later.</p>

---

## Post #7 by @ungi (2019-07-22 22:46 UTC)

<p>We have reviewed this with Andras offline. Turns out attributes are not saved in sequences when the proxy node is an image, because image sequences are saved in nrrd format. On the long run, probably all MRML node sequences should be able to preserve attributes when changed. But for now, we need to make sure attributes are only used in sequences that can preserve them. E.g. a sequence of segmentations is fine.</p>

---
