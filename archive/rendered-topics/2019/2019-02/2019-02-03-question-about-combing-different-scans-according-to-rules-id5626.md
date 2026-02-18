# Question about combing different scans according to rules

**Topic ID**: 5626
**Date**: 2019-02-03
**URL**: https://discourse.slicer.org/t/question-about-combing-different-scans-according-to-rules/5626

---

## Post #1 by @rowan_miller (2019-02-03 05:18 UTC)

<p>I have DWI and T2 axial images. I’d like to create a new set of images through combining those. However i’d like the combination to occur according to a set of rules:</p>
<p>if dwi dark + t2 dark -&gt; dark<br>
if dwi dark + t2 bright -&gt; dark<br>
if dwi light + t2 light -&gt; dark<br>
if dwi light + t2 dark -&gt; hot pink!</p>
<p>could anyone point me to some modules or suggest a way to get started on this?</p>
<p>regards,</p>

---

## Post #2 by @pieper (2019-02-05 14:54 UTC)

<p>Sounds like you can do that by writing a small python script that applies a formula from the two input volumes to calculate the output value.  Then apply a color table to make the bright parts pink.  Note that you may need to resample the dwi into the t2 space before doing numpy array options.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Developers/Python_scripting#Start_Here" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Developers/Python_scripting#Start_Here</a></p>

---
