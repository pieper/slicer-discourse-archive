# ALPACA "What is the Target landmark set used for?"

**Topic ID**: 39648
**Date**: 2024-10-11
**URL**: https://discourse.slicer.org/t/alpaca-what-is-the-target-landmark-set-used-for/39648

---

## Post #1 by @Chuan (2024-10-11 08:43 UTC)

<p>Hi,<br>
I have a question regarding on the option of “Target landmark set (Optional)”,<br>
does anyone know what is this used for?<br>
Since ALPACA can generate new landmark on Target model, why there is this option that allowing user to put target landmark set?</p>
<p>Basically, I need the wrapped source model instead of caring about the landmarks. Do you think whether I input target landmark set here or not will influence the final wrapped source model during the “morphing” stage from source model towards target model?</p>
<p>Best regards,<br>
Chuan</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea426048abeff36f90991aa1eddfb19ec1a4b4ce.png" alt="image" data-base62-sha1="xqlWaBshldprjcozBxoGcMT9Z2S" width="554" height="482"></p>

---

## Post #2 by @muratmaga (2024-10-11 15:36 UTC)

<p>If you create do have a target landmark set, you can set that as a reference in this field and ALPACA will calculate the root mean square between that reference and the estimated landmark position.</p>
<p>RMS can be helpful when you are trying to optimize ALPACA parameters in an objective way.</p>

---

## Post #3 by @Chuan (2024-10-11 18:19 UTC)

<p>I see, thank you very much!</p>

---
