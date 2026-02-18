# What units does the reformat module use?

**Topic ID**: 1268
**Date**: 2017-10-23
**URL**: https://discourse.slicer.org/t/what-units-does-the-reformat-module-use/1268

---

## Post #1 by @Masteling (2017-10-23 17:49 UTC)

<p>Hi all,</p>
<p>Our goal is to rotate the coronal plane to a specific angle X in relation to the axial plane. We would like to use the Reformat Module.</p>
<p>Our question is: what are the units used in the Rotation Segment? If we want to rotate the coronal plane in 40º what should be put in the LR bar?</p>
<p>Thanks in advance,<br>
Mariana Masteling</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be73a48ce83323f8f15eb62866eadeafbbe34e46.png" alt="Slicer_reformat_units" data-base62-sha1="raOtWdMP6bXjMm2BEcCdABtnvsa" width="401" height="429"></p>

---

## Post #2 by @pieper (2017-10-23 18:03 UTC)

<p>Those entries are in degrees - typing in 40 appears to work for me.  Does it not give what you expect?</p>

---

## Post #3 by @Masteling (2017-10-23 20:11 UTC)

<p>We thought it was in degrees too. But after rotating it to 57º, using AnglePlanes Plugin and rotating to the same angle using Reformat, the results aren’t similar.</p>
<p><strong>57º rotation using AnglePlanes Plugin</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d4eaf9c5d588c0eba51a748a5333b5c7fb91de4.png" data-download-href="/uploads/short-url/djqZivuDpA7q8Hd6E8BnyZB7O6M.png?dl=1" title="28_3d_57_angleplanes_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d4eaf9c5d588c0eba51a748a5333b5c7fb91de4_2_690x338.png" alt="28_3d_57_angleplanes_2" data-base62-sha1="djqZivuDpA7q8Hd6E8BnyZB7O6M" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d4eaf9c5d588c0eba51a748a5333b5c7fb91de4_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d4eaf9c5d588c0eba51a748a5333b5c7fb91de4_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d4eaf9c5d588c0eba51a748a5333b5c7fb91de4.png 2x" data-dominant-color="9C9DD3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">28_3d_57_angleplanes_2</span><span class="informations">1254×616 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>57º rotation using reformat</strong> (this angle is 32º not 57º)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d50be637d83a12eda22623eb671c6b6c0582f4.png" data-download-href="/uploads/short-url/inHz6t7mhHaFgI1tveCro3kyLAM.png?dl=1" title="28_3d_57_reformat_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80d50be637d83a12eda22623eb671c6b6c0582f4_2_690x422.png" alt="28_3d_57_reformat_2" data-base62-sha1="inHz6t7mhHaFgI1tveCro3kyLAM" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80d50be637d83a12eda22623eb671c6b6c0582f4_2_690x422.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80d50be637d83a12eda22623eb671c6b6c0582f4_2_1035x633.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80d50be637d83a12eda22623eb671c6b6c0582f4_2_1380x844.png 2x" data-dominant-color="9B9ED2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">28_3d_57_reformat_2</span><span class="informations">1395×855 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The same DICOMs were used to create the previous plots, they are just not shown.</p>

---

## Post #4 by @pieper (2017-10-23 20:41 UTC)

<p>Did you try the negative rotation?</p>
<p>Here’s what I did that worked:</p>
<ul>
<li>download MRHead Sample Data</li>
<li>use the Reformat module to rotate the Green plane by 40 degrees</li>
<li>go to the Transforms module and create a Linear Transform applied to the MRHead</li>
<li>set the rotation around LR to be -40</li>
</ul>
<p>The resulting coronal view of the rotated data looks right.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab39a7b495b05f690051724396bcd53def9ad6f5.jpeg" data-download-href="/uploads/short-url/oqJaIJp6hsOV5aPLDBJrKGeqUy9.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ab39a7b495b05f690051724396bcd53def9ad6f5_2_690x373.jpg" alt="image" data-base62-sha1="oqJaIJp6hsOV5aPLDBJrKGeqUy9" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ab39a7b495b05f690051724396bcd53def9ad6f5_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ab39a7b495b05f690051724396bcd53def9ad6f5_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ab39a7b495b05f690051724396bcd53def9ad6f5_2_1380x746.jpg 2x" data-dominant-color="AFAFBD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×746 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2017-10-23 21:24 UTC)

<p>I confirm that it is rotation in degrees. Note that rotations are incremental: if you rotate around multiple axes, the previous rotation slider is always reset to 0.</p>
<aside class="quote no-group" data-username="Masteling" data-post="3" data-topic="1268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masteling/48/13587_2.png" class="avatar"> Masteling:</div>
<blockquote>
<p>57º rotation using reformat (this angle is 32º not 57º)</p>
</blockquote>
</aside>
<p>These angles may refer to the same rotation -  they are just different angles of the same triangle: 57deg = 90deg - 32deg (-1deg probably measurement error).</p>

---

## Post #6 by @Masteling (2017-10-27 14:02 UTC)

<p>Thank you all for your clarifications <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
