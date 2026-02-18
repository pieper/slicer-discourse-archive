# Symmetric scissor effect issue

**Topic ID**: 1210
**Date**: 2017-10-12
**URL**: https://discourse.slicer.org/t/symmetric-scissor-effect-issue/1210

---

## Post #1 by @hherhold (2017-10-12 12:30 UTC)

<p>The size range in the scissor slice cut symmetric effect is specified in mm, but the number appears to be the number of slices. If I pick 20mm, regardless of the range in my data set, it will do +/- 10 slices from where I draw my scissor region.</p>
<p>This is in a recent nightly build.</p>

---

## Post #2 by @lassoan (2017-10-12 14:28 UTC)

<p>I confirm that it is in slices. Could you please enter a bug report at <a href="http://issues.slicer.org">issues.slicer.org</a>? If you could submit a pull request with the fix then it would be even better.</p>

---

## Post #3 by @hherhold (2017-10-12 23:20 UTC)

<p>I’ll try fixing it - might have a couple of questions along the way. I know C/C++ and a little python, but I’m very new at the innards of slicer.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2017-10-13 02:47 UTC)

<p>I had a look and the issue and it was simple enough so I went ahead and <a href="https://github.com/Slicer/Slicer/commit/16719ef6cfc45e881db5e661ba766499a8a60f28">fixed it</a>. It’ll be available in the nightly release on Saturday.</p>
<p>Thank you for reporting the issue and offering your help to fix it!</p>

---

## Post #5 by @hherhold (2017-10-13 12:18 UTC)

<p>Wow, thank you!</p>
<p>I’d gotten as far as figuring out how much I didn’t know (which was extensive, to say the least), so reading through your fix will be a very useful tutorial for me.</p>
<p>Thanks again!</p>

---
