# Heat Map for multiple segmentations

**Topic ID**: 23782
**Date**: 2022-06-09
**URL**: https://discourse.slicer.org/t/heat-map-for-multiple-segmentations/23782

---

## Post #1 by @zells (2022-06-09 06:02 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dfcf174e722a78772b656255f470a335cfbe565.png" alt="" data-base62-sha1="b7UGZQPn5lQWOUhDXsiCN47DOf3" role="presentation" width="505" height="418"><br>
I have a bunch of lesions here (with organs) but I want the colors of the lesions to be denoted in a manner that if they are overlapping with other lesions it changes color. ie if the two yellow lesions (in the middle of the screen) have a overlap in the middle the color would be say red.</p>
<p>Basically creating a heat map of common points within the lesion. Anyone know of an extension package or a way to take care of this? Any recommendations are appreciated</p>

---

## Post #2 by @mau_igna_06 (2022-06-09 13:06 UTC)

<p>You can code your segments with prime numbers. That makes them decodeable after they are multiplied. Ot’s a costly iperation but you can have a look up table for it.</p>
<p>Please ask if you have any questions and if you’d be willing tondevelop this for Slicer</p>

---

## Post #3 by @hherhold (2022-06-09 13:20 UTC)

<p>There are likely many data structures that would allow you to do this, another one would be to make a volume bitmap. Each bit is for a lesion, and any element in the volume with more than one bit set is an overlap. (If that makes sense.) This could probably be done in python without too much effort.</p>

---

## Post #4 by @lassoan (2022-06-09 16:31 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="23782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>one would be to make a volume bitmap.</p>
</blockquote>
</aside>
<p>I agree, this would be a very easy way to find how many structures overlap at each location. You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">get each segment as a numpy array</a> and simply add the arrays to get a “heat map”. You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">put the result into a volume node</a> and then view it in slice views or volume rendering.</p>

---

## Post #5 by @zells (2022-06-09 16:35 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> <a class="mention" href="/u/lassoan">@lassoan</a> Thank you both for suggestions! Thank you for the links as well. I will give this a try. Thank you</p>

---
