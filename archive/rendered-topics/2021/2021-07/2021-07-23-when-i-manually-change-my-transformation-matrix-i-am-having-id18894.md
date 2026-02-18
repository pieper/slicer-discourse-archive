# When I manually change my Transformation Matrix, I am Having some problem. I want to know the logic or reason behind it. know the logic 

**Topic ID**: 18894
**Date**: 2021-07-23
**URL**: https://discourse.slicer.org/t/when-i-manually-change-my-transformation-matrix-i-am-having-some-problem-i-want-to-know-the-logic-or-reason-behind-it-know-the-logic/18894

---

## Post #1 by @Amit_1993 (2021-07-23 12:24 UTC)

<p>I have two images, one is CT image and another one is a functional image (SPECT).  First to align the center of both images I have manually adjusted the transformation matrix. Then I want to do the scaling so that I have to change the diagonal member of the transformation matrix which I also have done manually. The problem actually rise here, when I do scaling my images again got translated which I do not want. Can anybody tell me the solution? Thanks !</p>

---

## Post #2 by @lassoan (2021-07-23 16:05 UTC)

<p>Scaling always happens around the origin, so what you see it the expected behavior. You could use multiple transforms (one to move the fixed point to the origin and then another transform to apply scaling), but it is much faster and more accurate if you perform semi-automatic <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">point-based registration</a>.</p>

---
