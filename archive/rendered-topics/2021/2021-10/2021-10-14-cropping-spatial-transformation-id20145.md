# Cropping spatial transformation

**Topic ID**: 20145
**Date**: 2021-10-14
**URL**: https://discourse.slicer.org/t/cropping-spatial-transformation/20145

---

## Post #1 by @Ndzimbong_William_Br (2021-10-14 07:19 UTC)

<p>Hi,</p>
<p>Please, is it possible to get (and save) to spatial transformation applied when cropping a volume ?<br>
I mean, as the cropping is a spatial transformation, is it possible the get (save) in any form (matrix, parameters, …) the information about the this transformation?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-10-14 20:02 UTC)

<p>I’m not quite sure what you are asking - after you’ve cropped a volume the cropped volume is in RAS space so there is no transform involved.  What transform are you looking for?</p>

---

## Post #3 by @muratmaga (2021-10-14 20:39 UTC)

<aside class="quote no-group" data-username="Ndzimbong_William_Br" data-post="1" data-topic="20145">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ndzimbong_william_br/48/8047_2.png" class="avatar"> Ndzimbong_William_Br:</div>
<blockquote>
<p>s it possible the get (save) in any form (matrix, parameters, …) the information about the this transformation</p>
</blockquote>
</aside>
<p>İf you mean cropping while under a transform, that’s the transformation. You already know what that is. İf it’s a linear transform, it is also saved under the image header and displayed in volumes module after cropping.</p>

---
