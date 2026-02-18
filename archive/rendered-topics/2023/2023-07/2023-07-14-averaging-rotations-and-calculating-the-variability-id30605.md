# Averaging rotations and calculating the variability

**Topic ID**: 30605
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/averaging-rotations-and-calculating-the-variability/30605

---

## Post #1 by @Melanie (2023-07-14 14:06 UTC)

<p>Hi,</p>
<p>I use the model registration module to register bones and calculate the 3-d displacements.<br>
My aim is to define the axis of rotation (finite helical axis).<br>
I would like to calculate a mean rotation for all transforms (I can leave the translations for the minute) and then calculate the variability. (Ultimately to calculate the mean rotation axis and the variability around the mean axis)</p>
<p>What’s the best way to do this pls</p>

---

## Post #2 by @lassoan (2023-07-14 14:21 UTC)

<p>This topic has been discussed on this forum:</p>
<aside class="quote quote-modified" data-post="17" data-topic="15871">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/13edae/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/calculate-axis-of-rotation/15871/17">Calculate axis of rotation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for kind support <a class="mention" href="/u/lassoan">@lassoan</a> 
Found this, after some research 
"Similarly we can also calculate backwards and find the intantanous axis of rotation at some distance 
− 
⃗ 
r 
from any point if we know the linear velocity of the point and the angular velocity. This is given by: 
[\begin{equation} \label{eq:2} -\vec{r}= \frac{\vec{\omega} \times \vec{v}_P }{ \vec{\omega}\cdot\vec{\omega} } \end{equation}] 
Thus if know the position of a point 
⃗ 
r 
P 
, its linear velocity 
⃗ 
v 
P 
we can fi…
  </blockquote>
</aside>

<p>An algorithm is provided for computing axis of rotation for a single pair of transforms and a perfect rotation around a single axis. Nobody volunteered to develop a more robust algorithm that could approximate the rotation axis from many imperfect measurements, so you would need to figure it out.</p>
<p>It may not be very hard, as there are not too many unknowns (you only have to determine position and orientation of the rotation axis and for each pair of transforms a rotation angle, so if you have 4 pair of transforms then in total you have 10 unknowns) and you may be able to get an approximate initial guess based on anatomical knowledge. You need to specify some error metric (such as residual position error of some anatomical landmark points) and then you can compute the uknowns using any non-linear optimizer.</p>

---
