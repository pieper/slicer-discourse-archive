# Color difference

**Topic ID**: 8877
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/color-difference/8877

---

## Post #1 by @prorai (2019-10-23 14:55 UTC)

<p>i’m exporting a 3d segmentation using closed surface representation method, with that i’m passing a RGB value for color. but the output and even in slicer 3D view i’m getting different color than the actual color.</p>
<p>example:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b0abfc0b388508641f117ec4ac61f6bde054e85.png" alt="image" data-base62-sha1="fgW7nzXMhK1yg7oE6Fkekdjcwsd" width="381" height="370"></p>
<p>model should look like the left one (i have created a material with same RBG value and other setting and attached to the model to check the difference)<br>
but the output is the right one</p>

---

## Post #2 by @pieper (2019-10-23 15:12 UTC)

<p>Lots of lighting and material property parameters can impact the final rendered color, so I wouldn’t expect an exact match.  Not sure what tool you are rendering with, but maybe it interprets things differently.</p>

---

## Post #3 by @prorai (2019-10-24 11:42 UTC)

<p>Yeah i agree about the lighting and material thing so i tried to use same properties for both models , but i saw that the RBG color i’m entering doesn’t look like the real one in 3D view window too. are there any limitations?</p>

---

## Post #4 by @pieper (2019-10-24 11:54 UTC)

<aside class="quote no-group" data-username="prorai" data-post="3" data-topic="8877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>are there any limitations?</p>
</blockquote>
</aside>
<p>What limitations did you have in mind?  You can play with the shading parameters in slicer and see how the various material properties interact.  Not sure what other software you are using so can’t really say what’s different.</p>

---
