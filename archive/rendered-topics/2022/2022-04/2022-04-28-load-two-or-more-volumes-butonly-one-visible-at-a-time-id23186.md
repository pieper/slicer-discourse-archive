# Load two or more volumes butonly one visible at a time

**Topic ID**: 23186
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/load-two-or-more-volumes-butonly-one-visible-at-a-time/23186

---

## Post #1 by @maxaerosat.co.za (2022-04-28 19:34 UTC)

<p>Using Fedora linux -<br>
Had to install Slicer on new computer from scratch (4.8) , other later versions have problems to run .<br>
things look fine .<br>
However if i load two or more volumes , only one show at a time even if both “eyes”  are open<br>
is it a hardware problem , or am i missing something . - how can i fix it<br>
it mean i cannot superimpose one volume on another .<br>
please give advice</p>

---

## Post #2 by @muratmaga (2022-04-28 19:53 UTC)

<p>First you are using a version that is not supported anymore. So, you may want to spend sometime on how to get the newer versions working your computer.</p>
<p>Are these two volumes acquired at the same exam (e.g., T1 &amp; T2 images) or are they co-registered already.</p>
<p>If so, you can set one as the foreground volume and the other as the background volume and visualize them together, by changing the opacity (alpha) channel.<br>
See this for more detail:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data</a></p>

---
