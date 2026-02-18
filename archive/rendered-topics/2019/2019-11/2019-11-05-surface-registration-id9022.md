# Surface registration

**Topic ID**: 9022
**Date**: 2019-11-05
**URL**: https://discourse.slicer.org/t/surface-registration/9022

---

## Post #1 by @erin_hong (2019-11-05 01:04 UTC)

<p>Operating system:MAC<br>
Slicer version: Slicer 4.0 Slicer CMF<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935cbab7e0f3dec5e44f35e74c667948800a5265.jpeg" data-download-href="/uploads/short-url/l1CRjuVFMHZ4rj3LgyuFgJ5Ah0h.jpeg?dl=1" title="04%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935cbab7e0f3dec5e44f35e74c667948800a5265_2_567x500.jpeg" alt="04%20PM" data-base62-sha1="l1CRjuVFMHZ4rj3LgyuFgJ5Ah0h" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935cbab7e0f3dec5e44f35e74c667948800a5265_2_567x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935cbab7e0f3dec5e44f35e74c667948800a5265_2_850x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935cbab7e0f3dec5e44f35e74c667948800a5265_2_1134x1000.jpeg 2x" data-dominant-color="837F74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20PM</span><span class="informations">1354×1194 350 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Expected behavior:  surface registration<br>
Actual behavior:<br>
have not been successful to register the images that I segmented (a half of mandible without defect then with periodontal bone defects)  Since I am trying to register areas that are either very thin crestal bone or absent, I am not able to register so then color maps give me unreliable colored map.</p>
<ol>
<li>Do you think your company’s slicer CMF has an ability to create registration when there is not enough cortical thickness?</li>
<li>Is there a manual way to register?</li>
</ol>
<p>I have included a few images for you to understand what I am trying to do.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fb9b1a6e462c8caf6d1157b49318d20b58eeef9.jpeg" data-download-href="/uploads/short-url/95JVxBApgA6KF4S0gyB95qd17vj.jpeg?dl=1" title="15%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb9b1a6e462c8caf6d1157b49318d20b58eeef9_2_569x500.jpeg" alt="15%20PM" data-base62-sha1="95JVxBApgA6KF4S0gyB95qd17vj" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb9b1a6e462c8caf6d1157b49318d20b58eeef9_2_569x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb9b1a6e462c8caf6d1157b49318d20b58eeef9_2_853x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb9b1a6e462c8caf6d1157b49318d20b58eeef9_2_1138x1000.jpeg 2x" data-dominant-color="B0C4B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15%20PM</span><span class="informations">1376×1208 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @bpaniagua (2020-01-10 20:19 UTC)

<p><a class="mention" href="/u/erin_hong">@erin_hong</a> please feel free to follow up in this post with any specific questions you might have.</p>

---

## Post #3 by @manjula (2020-01-10 20:35 UTC)

<p>Hi,</p>
<p>Sometime  back i had the same problem and tried several options including other software like geomagic and cloudcompare. I got the best results for my problem with CMF ROI registration.  I validated the results of superimposition with Model to Model distance and shape population viewer.</p>
<p>I think if you go through the following link you will find useful inputs from many here.</p>
<aside class="quote quote-modified" data-post="1" data-topic="9424">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/revisiting-rigid-mesh-registration/9424">Revisiting Rigid Mesh Registration</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    I first posted the problem few months back and Prof: Lassoan help me with it. Now i have had time to read about this topic and play around I would like to have a better understanding of the problem as i am not 100% happy with the results that i am getting with CMF surface registraion module and IGT fiducial registration wizard.  i am no mathematician or programmer and many parts of this will be copy pasted from other published work whici i read. 
Original Problem : We have a STL files from surfa…
  </blockquote>
</aside>

<p>We have done similar things with 3D Slicer and i do not think it is related to the thickness of the cortical bone.</p>
<p>Also why are you segmenting and registering at the first place ? Is it not best to simply do Image registration ?</p>

---
