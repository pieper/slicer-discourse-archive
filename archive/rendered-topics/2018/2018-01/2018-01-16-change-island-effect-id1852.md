---
topic_id: 1852
title: "Change Island Effect"
date: 2018-01-16
url: https://discourse.slicer.org/t/1852
---

# Change island effect 

**Topic ID**: 1852
**Date**: 2018-01-16
**URL**: https://discourse.slicer.org/t/change-island-effect/1852

---

## Post #1 by @opetne (2018-01-16 12:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.9.0<br>
Expected behavior: Change a color code to another<br>
Actual behavior: Delete all the color codes</p>
<p>I did air sac segmentation with the Editor module some years ago. For a statistical analysis I have to compare selected parts (diverticles) of the air sac system but my old color codes are not perfect, I have to change some parts of the diverticles. After clicking on the desired area, all the color codes are set to background (deleted, I think). What could be the reason for it?</p>
<p>Best,</p>
<p>Ors</p>

---

## Post #2 by @pieper (2018-01-16 12:34 UTC)

<p>Hi -</p>
<p>Hmm, hard to tell.  It could help troubleshoot if you let us know if you are using the old Editor or the new Segment Editor to change the islands?  Did you check the error log?  Is this something you can reproduce with the sample data?  Is the data sharable so we can try the operation?</p>
<p>-Steve</p>

---

## Post #3 by @opetne (2018-01-16 14:24 UTC)

<p>Dear Steve,</p>
<p>I’m using the old Editor module, since for this kind of segmentation I have<br>
to make a lot of manual editing.  I can share the files for checking.</p>
<p>Ors</p>

---

## Post #4 by @pieper (2018-01-16 20:02 UTC)

<p>Okay, sure - if you can share a dataset that replicates the issue I can take a look - use dropbox or something similar to send the files.</p>
<p>-Steve</p>

---

## Post #5 by @opetne (2018-01-16 20:21 UTC)

<p>Dear Steve,</p>
<p>You’ll receive the files vie wetransfer. Thank you for your help.</p>
<p>Ors</p>

---

## Post #6 by @opetne (2018-01-16 20:22 UTC)

<p>Sorry, I will share a google drive.</p>
<p>Ors</p>

---

## Post #7 by @opetne (2018-01-16 20:26 UTC)

<p>Dear Steve,</p>
<p>Which email adress should I use?</p>
<p>"We’re sorry, but your email message to [“slicer@discoursemail.com”]<br>
(titled 3 HASON 2-label.zip) didn’t work.</p>
<p>None of the destination email addresses are recognized, or the Message-ID<br>
header in the email has been modified. Please make sure that you are<br>
sending to the correct email address provided by staff."</p>

---

## Post #8 by @pieper (2018-01-16 20:43 UTC)

<p>ah, yes, makes sense - I’m pieper at <a href="http://isomics.com">isomics.com</a></p>
<p>-Steve</p>

---

## Post #9 by @lassoan (2018-01-16 20:45 UTC)

<p>I think you should be able to send private message to other users by clicking on the username then click on “Message”. But maybe it does not show up a while for new users (for spam protection).</p>

---

## Post #10 by @opetne (2018-01-16 20:46 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="1852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>pieper at <a href="http://isomics.com" rel="noopener nofollow ugc">isomics.com</a></p>
</blockquote>
</aside>
<p>Dear Steve,</p>
<p>sharing sent.</p>
<p>Ors</p>

---

## Post #11 by @pieper (2018-01-17 00:37 UTC)

<p>Hi Ors -</p>
<p>Thanks for sharing the data - that helped.  The issue is that your label map volume is of type ‘unsigned short’, but the change island tool only works with data type ‘short’ (slicer creates ‘short’ by default but maybe this was imported from another system?).</p>
<p>If you don’t really need the “island” part of this, you could just use the ChangeLabelEffect that would turn all voxels of a certain value to another.</p>
<p>Or if you need the island feature you can run your labelmap through the Filtering-&gt;Arithmetic-&gt;Cast Scalar Volume and switch to type short.  (If you create a new volume as the output you can change it to a labelmap in the Volumes module).</p>
<p>Or you could import the label into the new Segment Editor but I’m not sure there’s an exact replacement for the ChangeIslandEffect (<a class="mention" href="/u/lassoan">@lassoan</a> may have suggestions).</p>
<p>-Steve</p>

---

## Post #12 by @lassoan (2018-01-17 01:00 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="1852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>there’s an exact replacement for the ChangeIslandEffect</p>
</blockquote>
</aside>
<p>You can find ChangeIslandEffect feature in Segment Editor in “Islands” effect. Choose “Add selected island” and then if you click on an island in any of the viewers, then that island is added to the currently selected segment.</p>
<p>I think all features of the legacy Editor are available in Segment Editor and there are of course many improvements and fixes.</p>

---

## Post #13 by @opetne (2018-01-17 08:17 UTC)

<p>Dear Steve,</p>
<p>Thank you for your help. All the labels were created with Slicer with the<br>
same system.<br>
The solution you suggested worked. My problem was that I labeled a kind of<br>
air sac diverticle with a bad color code and I wanted to change it. The<br>
ChangeLabel Effect worked properly for this. In my mind a label is a<br>
complete label which contains all the color codes and this is why I didn’t<br>
try this effect but that was I wanted to do exactly.</p>
<p>Best,</p>
<p>Ors</p>

---

## Post #14 by @pieper (2018-01-17 12:54 UTC)

<p>Sounds good Ors - glad you are back on track.</p>
<p>Longer term, as Andras mentioned, the Segment Editor is more powerful and we’ll be putting our efforts there.</p>

---
