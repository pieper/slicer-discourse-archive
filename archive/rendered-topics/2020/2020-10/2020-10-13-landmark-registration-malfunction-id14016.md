---
topic_id: 14016
title: "Landmark Registration Malfunction"
date: 2020-10-13
url: https://discourse.slicer.org/t/14016
---

# Landmark registration malfunction

**Topic ID**: 14016
**Date**: 2020-10-13
**URL**: https://discourse.slicer.org/t/landmark-registration-malfunction/14016

---

## Post #1 by @nvanvuren (2020-10-13 16:10 UTC)

<p>Hello,</p>
<p>I am using the Landmark Registration module to perform registration of a post mortem ex vivo hemisphere on MRI on a normal brain MRI atlas to correct for the distortion that occurs due to absence of the skull in post mortem ex vivo scanning. As I am using brains with Alzheimer’s disease, the brains show a lot of atrophy and a lot of distortion.</p>
<p>After performing the landmark registration, it looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05d9f38b8a7d13c34f891c7f07542c6612804535.jpeg" data-download-href="/uploads/short-url/PLlrSmePbQ5ZSqTYtNFY5MjHtX.jpeg?dl=1" title="Afbeelding1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9f38b8a7d13c34f891c7f07542c6612804535_2_690x431.jpeg" alt="Afbeelding1" data-base62-sha1="PLlrSmePbQ5ZSqTYtNFY5MjHtX" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9f38b8a7d13c34f891c7f07542c6612804535_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9f38b8a7d13c34f891c7f07542c6612804535_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05d9f38b8a7d13c34f891c7f07542c6612804535.jpeg 2x" data-dominant-color="585857"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Afbeelding1</span><span class="informations">1144×715 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To save the transformed hemisphere, I need to use the Harden transform button. However, when I click it the transformation changes and the registration becomes totally inaccurate.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/543b5431694ee1c6220a187958e3e9eb4564cf4e.png" data-download-href="/uploads/short-url/c19dA2RbgId6dMZQgHSDaBCCpqe.png?dl=1" title="Afbeelding2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/543b5431694ee1c6220a187958e3e9eb4564cf4e_2_690x430.png" alt="Afbeelding2" data-base62-sha1="c19dA2RbgId6dMZQgHSDaBCCpqe" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/543b5431694ee1c6220a187958e3e9eb4564cf4e_2_690x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/543b5431694ee1c6220a187958e3e9eb4564cf4e_2_1035x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/543b5431694ee1c6220a187958e3e9eb4564cf4e.png 2x" data-dominant-color="565656"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Afbeelding2</span><span class="informations">1140×712 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you explain what the Harden transform button does exactly? Any ideas how to avoid this change of transformation?</p>

---
