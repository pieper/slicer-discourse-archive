---
topic_id: 1046
title: "Dir Cost Function Value Modification"
date: 2017-09-13
url: https://discourse.slicer.org/t/1046
---

# DIR: Cost function value modification

**Topic ID**: 1046
**Date**: 2017-09-13
**URL**: https://discourse.slicer.org/t/dir-cost-function-value-modification/1046

---

## Post #1 by @pwang (2017-09-13 22:24 UTC)

<p>Operating system: Windows7<br>
Slicer version:4.7.0<br>
My current goal is to get a better deformable image registration (DIR). The settings for Percentage Of Samples, Maximum Step Length and Minimum Step Length are: 1, 0.005 and 0.001 respectively. I think I have no other choice than modifying the Cost Function Convergence Factor (CFCF). My assumption is if I decrease the CFCF, my registration will improve, i.e. finer features register better. (Please let me know if my assumption is wrong.) Below is the CFCF I talk about:<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eaa165b70406fd8c1532ba1ff4e33d29dadf1ad.png" alt="image" data-base62-sha1="bdTEuBVccykAme8S0jm5xJskmp7" width="606" height="158">. Is there any tutorial talking about how to modify the CFCF value? Thanks a lot.</p>

---

## Post #2 by @lassoan (2017-09-14 03:58 UTC)

<p>Optimizing “General Registration (BRAINS)” module’s parameters requires <em>lots</em> of experimentation. If you can find a registration problem similar to yours in the <a href="https://na-mic.org/wiki/Projects:RegistrationDocumentation:UseCaseInventory">Registration case library</a> then you can use that as a starting point.</p>
<p>You may also try SlicerElastix extension, which uses <a href="http://elastix.isi.uu.nl/">Elastix library</a> for registration. Based on my experience, Elastix gives good registration results with default parameters, without any tuning (of course tuning may further improve results or decrease calibration time).</p>
<p>If you write more about your end goal then we can give more specific advice.</p>

---

## Post #3 by @pwang (2017-09-15 16:22 UTC)

<p>Thank you Lassoan for your advice. I tried Plastimatch plug in and it give me good result. But I have another problem. Let me open another topic. Thx.</p>

---
