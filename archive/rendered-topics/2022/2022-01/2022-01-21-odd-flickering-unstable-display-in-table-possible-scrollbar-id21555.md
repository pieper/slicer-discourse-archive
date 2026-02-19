---
topic_id: 21555
title: "Odd Flickering Unstable Display In Table Possible Scrollbar"
date: 2022-01-21
url: https://discourse.slicer.org/t/21555
---

# Odd 'flickering' (unstable display) in table: possible scrollbar issue

**Topic ID**: 21555
**Date**: 2022-01-21
**URL**: https://discourse.slicer.org/t/odd-flickering-unstable-display-in-table-possible-scrollbar-issue/21555

---

## Post #1 by @DIV (2022-01-21 05:43 UTC)

<p>Using the latest Preview version of 3D Slicer (4.13.0 2022-01-19) in the <strong>Segment Editor</strong> I encountered some weird behaviour in the table of segments.<br>
I had eight (8) segments defined, and I clicked the Threshold tool and scrolled down.<br>
The table entries perpetually flicked between two states, at a frequency of ~once every 3–4 seconds,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e35562304f7fc068eba722710e85bfc1ee0750.png" data-download-href="/uploads/short-url/ze4w5xGysdaTrys79jxy6E34w12.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e35562304f7fc068eba722710e85bfc1ee0750.png" alt="image" data-base62-sha1="ze4w5xGysdaTrys79jxy6E34w12" width="574" height="500" data-dominant-color="E6E9ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">593×516 40.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d358811fdfe76714ec71daf404db48e94e9be44b.png" data-download-href="/uploads/short-url/u9EmH6iJN3eaZyOMg46PkGH5wVR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d358811fdfe76714ec71daf404db48e94e9be44b.png" alt="image" data-base62-sha1="u9EmH6iJN3eaZyOMg46PkGH5wVR" width="574" height="500" data-dominant-color="EAEBEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">593×516 39.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My best guess is that there might be two conflicting instructions in the underlying code for the table:</p>
<ul>
<li>one saying “a scrollbar needs to be added”,</li>
<li>the other saying “a scrollbar is not needed”,</li>
</ul>
<p>I speculate that the problem arises because</p>
<ul>
<li>when the scrollbar <em>is</em> present the vertical spacing of the list of segment is compressed, meaning that a scrollbar is <em>not</em> needed;  but</li>
<li>when the scrollbar is <em>not</em> present the vertical spacing of the list of segment is expanded, meaning that a scrollbar <em>is</em> needed.</li>
</ul>
<p>—DIV</p>

---

## Post #2 by @DIV (2022-01-21 05:45 UTC)

<p>Upon further consideration, I don’t think <s>clicking the Threshold effect or</s> scrolling down had anything to do with it.  The behaviour likely commenced after adding the eighth segment.</p>
<p>Adding a ninth segment stopped the flickering.<br>
Surprisingly, <em>removing</em> the same ninth segment did <em>not</em> cause the flickering to instantly resume.</p>
<p>Later on I applied the Threshold effect, causing its dialogue to be dismissed.  And then I clicked <em>again</em> on the Threshold effect:  this <em>did</em> actually cause the flickering to start (with <em>eight</em> segments)!  Cancelling the Threshold effect caused the flickering to stop.</p>

---
