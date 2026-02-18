# CBCT superimposition

**Topic ID**: 36925
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/cbct-superimposition/36925

---

## Post #1 by @MARIA_Santos (2024-06-20 19:53 UTC)

<p>Hello! I am new to 3D slicer and although I have read some topics about CBCT superimposition I cannot seem to get it right. What I want to do is superimpose 2 facial CBCTs (pre and post orthognatic surgery) and measure the distance between some teeth before and after the surgery.<br>
Can someone please explain in a very simple way how to do this??<br>
THANK YOU SO MUCH!</p>

---

## Post #2 by @lassoan (2024-06-22 12:04 UTC)

<p>Have you been able to register the two CBCT images?</p>

---

## Post #3 by @MARIA_Santos (2024-06-23 09:57 UTC)

<p>No… Can you tell me how i can do that, please?<br>
Thank you so much</p>

---

## Post #4 by @muratmaga (2024-06-23 18:00 UTC)

<p>You can use the Registration tools within Slicer. Please read the section on automatic image registration in Slicer:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration</a></p>

---

## Post #5 by @MARIA_Santos (2024-06-23 19:00 UTC)

<p>I was able to register using Elastic. How should I save the volume? And what are the next steps?<br>
Again thank you very much for the help!! I really appreciate it!</p>

---

## Post #7 by @muratmaga (2024-06-24 20:17 UTC)

<aside class="quote no-group" data-username="MARIA_Santos" data-post="1" data-topic="36925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maria_santos/48/77049_2.png" class="avatar"> MARIA_Santos:</div>
<blockquote>
<p>measure the distance between some teeth before and after the surgery</p>
</blockquote>
</aside>
<p>The way you phrase your question suggest to me you need to measure the outcome of the surgical operation.</p>
<p>So unless this is a jaw of a growing child, I am not sure if you need to register pre/post CBCT. If you measure this distance using another landmark that is not affected by the surgery, you can directly measure them both on both CBCT and difference should give you how much surgery change this distance.</p>
<p>Is this not what you want to do?</p>

---

## Post #8 by @MARIA_Santos (2024-06-24 20:37 UTC)

<p>Yes I could do that but it would be hard to find the exact same point to measure in both CBCTs. I want to know, for example, how much the left upper canine tooth advanced in the surgery (and measure for different points, the front/back and the upper/down movement of some teeth)</p>

---

## Post #9 by @MARIA_Santos (2024-06-26 14:07 UTC)

<p>Anyone knows please?? I am in a bit of an hurry</p>

---
