---
topic_id: 13208
title: "Alpaca Module Doesnt Correctly Register Models Of Different"
date: 2020-08-28
url: https://discourse.slicer.org/t/13208
---

# ALPACA module doesn't correctly register models of different size

**Topic ID**: 13208
**Date**: 2020-08-28
**URL**: https://discourse.slicer.org/t/alpaca-module-doesnt-correctly-register-models-of-different-size/13208

---

## Post #1 by @Dave_Matthews (2020-08-28 03:31 UTC)

<p>I’ve segmented out the premaxilla of several guppies that I CT scanned. I place landmarks on one of the models and am trying to use ALPACA to transfer these landmarks to other models. This works well when I use two models that are very similar, but does not work to transfer landmarks between males and females (females are about twice as big as males).<br>
I have tried changing the alpha and beta values but this doesn’t fix the problem.</p>
<p>I’m wondering if ALPACA is able to deal with similar structures that are different sizes? Does either registration step account for size or do they only account for position and local shape change?</p>
<p>Thanks for any help!</p>

---

## Post #2 by @muratmaga (2020-08-28 03:35 UTC)

<p><a class="mention" href="/u/dave_matthews">@Dave_Matthews</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> and <a class="mention" href="/u/agporto">@agporto</a> are working on that. It should be fixed in the next couple days…</p>

---

## Post #3 by @smrolfe (2020-08-28 03:37 UTC)

<p>We’re just testing now, and will be updated shortly!</p>

---

## Post #4 by @Dave_Matthews (2020-08-28 04:56 UTC)

<p>Thanks very much for the quick reply!</p>

---

## Post #5 by @Chuan (2023-11-16 08:38 UTC)

<p>Hi Smrolfe,</p>
<p>Recently I also meet the similar problem, do you have an answer now?</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #6 by @Chuan (2023-11-16 08:40 UTC)

<p>Hi Muratmaga,</p>
<p>Do you have any suggestion now? Or is there any similar post about transfer landamrks in Slicer?</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #7 by @muratmaga (2023-11-16 15:50 UTC)

<p>That has been fixed sometime ago, and there is now a scaling option built-in (you can disable it by choosing skip scaling).</p>
<p>If it is still not working right for you, please share the two models and the LMs you want to transfer.</p>

---
