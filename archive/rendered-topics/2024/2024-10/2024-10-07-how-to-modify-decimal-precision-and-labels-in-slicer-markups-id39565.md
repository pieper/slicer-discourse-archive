---
topic_id: 39565
title: "How To Modify Decimal Precision And Labels In Slicer Markups"
date: 2024-10-07
url: https://discourse.slicer.org/t/39565
---

# How to Modify Decimal Precision and Labels in Slicer Markups

**Topic ID**: 39565
**Date**: 2024-10-07
**URL**: https://discourse.slicer.org/t/how-to-modify-decimal-precision-and-labels-in-slicer-markups/39565

---

## Post #1 by @Deep_Learning (2024-10-07 12:58 UTC)

<p>I’m wondering how to change the number of decimal points displayed in markup text—for example, adjusting the length of a line markup from two decimal points to one.</p>
<p>Additionally, is it possible to remove the markup name in the 3D view and only display the length?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @pieper (2024-10-07 14:11 UTC)

<p>Good question - I don’t see that this is exposed in the GUI.</p>
<p>Also I would have thought that something like this would work, but it seems the PrintFormat doesn’t change.  Perhaps someone with more knowledge about how the Markups are implemented can comment.</p>
<pre><code class="lang-auto">l = getNode("L")
ll = l.GetMeasurement("length")
ll.SetPrintFormat("%g")
</code></pre>

---

## Post #3 by @Deep_Learning (2024-10-08 09:53 UTC)

<p>I would be happy to script it…   I found something called precision, but I do not think that it is related to the display.   I always get 2 decimal points displayed in the 3D View.</p>
<aside class="quote" data-post="1" data-topic="6157">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-change-the-default-precision-of-fiducials/6157">How to change the default precision of fiducials?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
I’d like to add more significant digits to fiducial points when saving to a FCSV file. I can set the values I want using Python, but the Markups table and the output FCSV file show the default precision. I have tried changing the precision under Application Settings-&gt; Units but this doesn’t impact the fiducial points. Is there a way to do this? 
Thank you for your help. 
Sara
  </blockquote>
</aside>


---

## Post #4 by @pieper (2024-10-08 14:37 UTC)

<p>In the Application Settings → Units you can set the precision.</p>
<p>Right now the inclusion of the node name and colon character are hard coded, so some C++ code would be need (or a workaround with and extra markup point with custom label or something).</p>

---

## Post #5 by @Deep_Learning (2024-10-19 11:35 UTC)

<p>Thanks for your reply… very helpful.<br>
A few notes for others.   Precision seems to be the number of total digits.   This worked for me, but if set to 2, one would get 1.2mm, 9.9mm and 24mm. (no decimal on the &gt;=10).<br>
I can get rid of the Markupnode labels, by changing the name.  Changing to “” (empty string) works, but on saving/loading the mrb, A generic name is given to the missing names.   changing the names to  " " (space)  gives some persistence.</p>

---
