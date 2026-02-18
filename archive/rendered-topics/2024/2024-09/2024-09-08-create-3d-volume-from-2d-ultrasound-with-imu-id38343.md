# Create 3D volume from 2D ultrasound with IMU

**Topic ID**: 38343
**Date**: 2024-09-08
**URL**: https://discourse.slicer.org/t/create-3d-volume-from-2d-ultrasound-with-imu/38343

---

## Post #1 by @Sekeun_Kim (2024-09-08 18:17 UTC)

<p>Thank you for your sharing.</p>
<p>I am trying to do same project that you mentioned generating 3D vol from 2D.<br>
Could you share your experience on that ?<br>
Especially, did you used IMU for location information and probe as image acquisition ?<br>
What organs that you generated from 2D?</p>

---

## Post #2 by @lassoan (2024-09-12 02:57 UTC)

<p>3D volume reconstruction from 2D slices using an IMU works well. See example in this topic:</p>
<aside class="quote" data-post="1" data-topic="33061">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/dfb087/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/clarius-live-via-plus-imu-data/33061">Clarius Live via Plus IMU Data</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, is it possible to transfer the IMU position data of the Clarius C3HD3 to Slicer? The connection via Plus works and live images can also be displayed. How can the position data be used to display the ultrasound image live in the 3D view? 
Thank you!
  </blockquote>
</aside>

<aside class="quote no-group" data-username="Sekeun_Kim" data-post="1" data-topic="38343">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sekeun_kim/48/77865_2.png" class="avatar"> Sekeun_Kim:</div>
<blockquote>
<p>did you used IMU for location information and probe as image acquisition ?</p>
</blockquote>
</aside>
<p>You can only only track rotating motion (not translation).</p>
<aside class="quote no-group" data-username="Sekeun_Kim" data-post="1" data-topic="38343">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sekeun_kim/48/77865_2.png" class="avatar"> Sekeun_Kim:</div>
<blockquote>
<p>What organs that you generated from 2D?</p>
</blockquote>
</aside>
<p>IMU is well-suited for tracking endocavity ultrasound probes (for imaging prostate, uterus, cervix, etc.), as rotating them can cover a large 3D region.</p>
<p>If the probe is outside the body then the size of the 3D region that can be reached by rotating motion is quite limited. For these applications a 6-degree-of-freedom optical or electromagnetic tracker may be a better choice.</p>

---
