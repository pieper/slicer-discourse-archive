# Volume Rendering when SetUseDepthPeeling(True) disappeared in Windows OS

**Topic ID**: 26278
**Date**: 2022-11-17
**URL**: https://discourse.slicer.org/t/volume-rendering-when-setusedepthpeeling-true-disappeared-in-windows-os/26278

---

## Post #1 by @StephenLeePeng (2022-11-17 09:54 UTC)

<p>Hello, everyone, recently I find a situation abount different volume rendering performance between Windows and Linux OS.</p>
<p>I would to realize volume rendering in the 3d view, sometimes I would display surface rendering and volume rendering at the same time. To confirm the depth information correctly, I would use the setting parameters, SetUseDepthPeeling(True).</p>
<p>But the difference occurs, If in Linux system, the volume rendering will be displayed as expected. But in Windows system, the volume rendering will not display, eventhough I move the mouse on the 3d View.</p>
<p>Then I switch to “View Controllers” module, unchecked “Use depth peeling” , then the volume rendering will displayed as expected. After that, even I checked the “Use depth peeling” again, the volume rendering will displayed all time.</p>
<p>So to my confusion, why in Windows system, when SetUseDepthPeeling(True), the volume rendering will not displayed as expected, but in Linux, all is right.</p>

---

## Post #2 by @StephenLeePeng (2022-11-17 12:11 UTC)

<p>here is the View Controllers module, and the Use depth peeling checkbox.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8e77d88224bea7cfffe3d6bf04c8dd5e3ed1f80.png" alt="viewControllers" data-base62-sha1="uWP6abd47ecfLZsxXLLdKj0hNDO" width="485" height="239"></p>
<p>Any advice will be appreciated!<br>
And thanks to <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> in advance, expect to your<br>
professional answer and advices.</p>

---

## Post #3 by @lassoan (2022-11-17 20:18 UTC)

<p>I remember encountering this issue (you need to disable and re-enable depth peeling for volume rendering to work). If you can reproduce it with the latest Slicer Preview Release then please submit a bug report to <a href="https://issues.slicer.org">https://issues.slicer.org</a>. Thank you!</p>

---

## Post #4 by @StephenLeePeng (2022-11-18 02:30 UTC)

<p>Thanks, now I used Slicer version is Slicer-4.13.0-2022-01-16-linux-amd64, and windows version is built by source codes one years ago.</p>
<p>I want to know the problem is occured by different GPU version, such as in Linux, I use Nvidia 1080 GPU, bu t in Windows, I use intel UHD Graphics driver, or any other reason.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/459092263f37cce80cf3f55e655258dc0dda140a.png" alt="inter-graphics" data-base62-sha1="9VoGBvBHWjqflS3RTMbz8wI02w2" width="274" height="264"></p>
<p>And I will use the latest Slicer Preview Release as you recommend and try to reproduce this bug.</p>

---
