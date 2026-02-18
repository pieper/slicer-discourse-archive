# Segment part deletion like osirix bone delete function

**Topic ID**: 36415
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/segment-part-deletion-like-osirix-bone-delete-function/36415

---

## Post #1 by @mvergnat (2024-05-27 11:02 UTC)

<p>Dear 3Dslicer community:<br>
As congenital heart surgeon, I use massively 3dslicer (mostly MRI chest).<br>
To work, I use always segmentation, it makes my work easier.<br>
I don’t need perfect segmentation, otherwise it will take me too long, I just use simple technique</p>
<p>For example, I have a CT chest, I use<br>
Segmentation threshold<br>
Then I use hollow<br>
With this, I have a segment that I can easily inspect on computer.</p>
<p>My question:<br>
I want to delete specifically some part of the segment BUT without using the scissors:<br>
I explain:<br>
Some certainly know the old fashioned osirix:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a07cbc8227ed13f1eb3bc88e2f05270924d896d3.jpeg" alt="image" data-base62-sha1="mTJDMFmAL5SHUjHjZrpotjlsa1t" width="448" height="281"><br>
In 3d there was instrument called bone delete <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20cfc6e4dc4037e5275e1a982840517abf6f7cd2.jpeg" alt="image" data-base62-sha1="4GgrdNoULNHFnu1NblGfIeENbou" width="417" height="183"><br>
In my volume I want to delete a part of the segment that is not in contact with the rest of the segment, for example, the ribs:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed5c443a13654bc1ea3a827e9ae257682b33a599.jpeg" alt="image" data-base62-sha1="xRMQ7cV1TnfEYyIx309ibcIq3dT" width="373" height="379"></p>
<p>The function asked is:<br>
only selective delete what is in continuation with the location where I click.</p>
<p>The advantage:<br>
for example, it will massive speed up my rib/bone deletion in chest imaging.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce9526aa0b750dd2b1f3b85e51df3ff1c89aa7ad.jpeg" alt="image" data-base62-sha1="ttvUDACUTJ83gpC8vzQ5cmzt7Y1" width="431" height="281"></p>
<p>Any idea?</p>
<p>Many thx</p>
<p>Always pleasure to word with 3dslicer and interact with the community!!</p>
<p>mathieu</p>

---

## Post #2 by @Sunderlandkyl (2024-05-27 15:10 UTC)

<p>You can use the Islands effect to remove a selected island:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787b1b5be1aa53ea165328a31a9413990b736f57.png" alt="image" data-base62-sha1="hbP3cLtpZdBuxrUskdrnY3G72En" width="662" height="136"></p>
<p>It doesn’t work in 3D so you will have to click on the segment in the slice views.</p>
<p>You might also be interested in the “Keep selected island option” which will remove everything that isn’t connected to a specific location.</p>

---

## Post #3 by @mvergnat (2024-05-27 15:48 UTC)

<p>Kyle,<br>
this is a perfect match.<br>
Very good advice, I like it.<br>
Many Many thx!!!</p>

---

## Post #4 by @mvergnat (2024-05-27 15:51 UTC)

<p>an the keep selected island was even more good idea!<br>
<img src="https://emoji.discourse-cdn.com/twitter/heart_hands.png?v=12" title=":heart_hands:" class="emoji only-emoji" alt=":heart_hands:" loading="lazy" width="20" height="20"></p>

---
