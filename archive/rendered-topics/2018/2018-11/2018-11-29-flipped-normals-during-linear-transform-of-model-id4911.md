# Flipped normals during linear transform of model

**Topic ID**: 4911
**Date**: 2018-11-29
**URL**: https://discourse.slicer.org/t/flipped-normals-during-linear-transform-of-model/4911

---

## Post #1 by @dominicwhite (2018-11-29 15:36 UTC)

<p>I’m importing a 3d model created in another program and trying to align it with the same model created in Slicer, and I’m running into a problem with the normals of the model.</p>
<p>Here’s the model after import:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f15acfe592ab55e04e3fae63576b6cc0ebd6867.jpeg" data-download-href="/uploads/short-url/bhC9W27jFdYJr1wbuNF7yQjDJ9d.jpeg?dl=1" title="01%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f15acfe592ab55e04e3fae63576b6cc0ebd6867_2_682x500.jpeg" alt="01%20AM" data-base62-sha1="bhC9W27jFdYJr1wbuNF7yQjDJ9d" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f15acfe592ab55e04e3fae63576b6cc0ebd6867_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f15acfe592ab55e04e3fae63576b6cc0ebd6867_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f15acfe592ab55e04e3fae63576b6cc0ebd6867_2_1364x1000.jpeg 2x" data-dominant-color="8284A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01%20AM</span><span class="informations">1578×1156 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here’s the same model after a reflection using the Transforms module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b7011fcc3c009a13e567a143ca2c442cfefd52c.jpeg" data-download-href="/uploads/short-url/8tOhn2CinIuvyXdugj4J0gObS4k.jpeg?dl=1" title="47%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b7011fcc3c009a13e567a143ca2c442cfefd52c_2_679x500.jpeg" alt="47%20AM" data-base62-sha1="8tOhn2CinIuvyXdugj4J0gObS4k" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b7011fcc3c009a13e567a143ca2c442cfefd52c_2_679x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b7011fcc3c009a13e567a143ca2c442cfefd52c_2_1018x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b7011fcc3c009a13e567a143ca2c442cfefd52c_2_1358x1000.jpeg 2x" data-dominant-color="7F81A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">47%20AM</span><span class="informations">1540×1134 395 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This appears to be a problem with the normals - I can reverse it with Surface Toolbox’s flipped normals.</p>
<p>However, is there a way to do a reflection which doesn’t flip the normals?</p>
<p>Here are my Linear Transform settings to reproduce this effect:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33bf96ee4e0fbaaba9ee5d01a5ebc501037204cf.png" data-download-href="/uploads/short-url/7nMPrBpl9NtzXTFCNvDAscm1XFt.png?dl=1" title="55%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33bf96ee4e0fbaaba9ee5d01a5ebc501037204cf_2_356x500.png" alt="55%20AM" data-base62-sha1="7nMPrBpl9NtzXTFCNvDAscm1XFt" width="356" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33bf96ee4e0fbaaba9ee5d01a5ebc501037204cf_2_356x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33bf96ee4e0fbaaba9ee5d01a5ebc501037204cf_2_534x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33bf96ee4e0fbaaba9ee5d01a5ebc501037204cf_2_712x1000.png 2x" data-dominant-color="F4F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">55%20AM</span><span class="informations">1140×1598 63.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-11-29 16:07 UTC)

<aside class="quote no-group" data-username="dominicwhite" data-post="1" data-topic="4911">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dominicwhite/48/2364_2.png" class="avatar"> dominicwhite:</div>
<blockquote>
<p>However, is there a way to do a reflection which doesn’t flip the normals?</p>
</blockquote>
</aside>
<p>If you turn the model inside out (apply a linear transform with a matrix that has negative determinant) then the surface normals will be reversed, too. Using Surface Toolbox module is a good solution. Is there any specific reason you would only want to turn the surface inside out but not flip the normals?</p>

---

## Post #3 by @dominicwhite (2018-11-29 16:53 UTC)

<p>Andras</p>
<p>My linear algebra is pretty rusty, so I may be missing something here, but I’m not trying to turn the model inside out.</p>
<p>What I want to do is flip the model around one of the axes (i.e. map every x coordinate to -x, while keeping y &amp; z coordinates the same).</p>
<p>I was following the instructions in the Wiki FAQ for this question: <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ#How_do_I_fix_incorrect_axis_directions.3F_Can_I_flip_an_image_.28left.2Fright.2C_anterior.2Fposterior_etc.29_.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/FAQ#How_do_I_fix_incorrect_axis_directions.3F_Can_I_flip_an_image_.28left.2Fright.2C_anterior.2Fposterior_etc.29_.3F</a></p>
<p>It just seems counter-intuitive to me that reflecting the model through a plane would also flip the normals (but see above re: math &amp; rusty). Hence my original question, is there a Transform matrix to do a reflection without also flipping the normals?</p>

---

## Post #4 by @lassoan (2018-11-29 20:09 UTC)

<aside class="quote no-group" data-username="dominicwhite" data-post="3" data-topic="4911">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dominicwhite/48/2364_2.png" class="avatar"> dominicwhite:</div>
<blockquote>
<p>Hence my original question, is there a Transform matrix to do a reflection without also flipping the normals?</p>
</blockquote>
</aside>
<p>There is not. Inverting direction of axis turns the model inside out (the inside surface of the non-transformed model becomes outside surface in the transformed model).</p>

---

## Post #5 by @steffen-o (2018-12-03 09:01 UTC)

<p>You could do the flipping in <a href="http://www.meshlab.net/" rel="nofollow noopener">Meshlab</a> (it’s also free) before you import it into Slicer.<br>
There you can flip the axis (Filters-&gt;Normals Curvature Orientation -&gt;Transform, flip swap axis) and invert the faces orientation (Filters-&gt;Normals Curvature Orientation -&gt; Invert faces orientation).</p>

---

## Post #6 by @dominicwhite (2018-12-06 16:41 UTC)

<p>Thanks, <a class="mention" href="/u/steffen-o">@steffen-o</a> . I’m trying to build a script to import files from another program into Slicer, so I’d prefer to do it all “in-house”.</p>
<p>In case anyone has the same problem in future, I was eventually able to flip surface models without inverting normals using the “Surface Toolbox” module’s Mirror operation.</p>

---

## Post #7 by @lassoan (2018-12-07 00:52 UTC)

<p>Surface toolbox is a Python scripted module, which exposes a few VTK filters on the GUI. Of course you can use those VTK filters directly in your script.</p>

---
