# Transforming a data node on to linear transform

**Topic ID**: 8232
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/transforming-a-data-node-on-to-linear-transform/8232

---

## Post #1 by @Jainey (2019-08-30 03:05 UTC)

<p>hi all,<br>
apologies for all this non-software persons queries.<br>
I have done registration of models and created linear transform files. (from 3 to 10)<br>
The I have created a mark ups node applying mark ups on my first model which I used to register.<br>
Then I transformed it on to individual transformation matrix (from3 - 10)<br>
Does this approach work to get me point coordinates of the mark up s on the subsequent models please. I want to make sure that the mark up s stay at the same location I have put them on model one. When the model displaces I want the mark ups to stay in the exact position and give me the coordinates<br>
Thanks</p>

---

## Post #2 by @lassoan (2019-08-30 23:27 UTC)

<p>If you apply the same transforms to multiple nodes (images, models, markups, etc) then they should all move together.</p>
<p>In Markups module, you can choose to see the original or transformed point coordinates. If you save point coordinates to file or copy to clipboard then always the original coordinates are used (transform has no effect). You need to harden the transform on the markups node to get transformed point coordinates in saved file or clipboard.</p>

---

## Post #3 by @Jainey (2019-08-30 23:34 UTC)

<p>Thanks Prof <a class="mention" href="/u/lassoan">@lassoan</a><br>
I get multiple transformation files like - linear transform -3, then -4  and 5 etc., when I register models. Can I apply my F node to each one of these, and expect that they represent the next movement.</p>
<p>like my model 2, displaces from 1 (I get LT _3 for registering that) , Then I register model 2 to 3, I get LT_4 for that. Can I create one F node on first model and transform that with LT_3 and 4 and thereafter and expect that to reflect the displacement of models.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2019-08-30 23:53 UTC)

<p>You can change the parent transform of a node any time and it does not matter what parent transforms were used previously.</p>
<p>If you <em>harden</em> a transform on a node then it permanently changes the node. So, if you later apply a different transform then it will be applied on top of the hardened transform.</p>

---

## Post #5 by @Jainey (2019-09-05 12:52 UTC)

<p>Thank you ever so much Prof <a class="mention" href="/u/lassoan">@lassoan</a><br>
I am trying this</p>

---
