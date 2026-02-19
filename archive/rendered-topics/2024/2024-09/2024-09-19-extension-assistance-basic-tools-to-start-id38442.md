---
topic_id: 38442
title: "Extension Assistance Basic Tools To Start"
date: 2024-09-19
url: https://discourse.slicer.org/t/38442
---

# Extension assistance - basic tools to start

**Topic ID**: 38442
**Date**: 2024-09-19
**URL**: https://discourse.slicer.org/t/extension-assistance-basic-tools-to-start/38442

---

## Post #1 by @Shirly_Someck (2024-09-19 11:56 UTC)

<p>I’ve started using 3D slicer, and managed to get a manual protocol for my project (probe view for DBS surgeries). It really is an amazing tool!<br>
Now I want to create an extension by using python, but am struggling greatly. I only need to use existing modules (not any new algorithms), but I feel that I don’t have the basic functions I need to know in order to write the wrapping code. For example:<br>
I want to create markup angle by user input; or I need to make sure my scanned are not “reformatted”, but I couldn’t find the orientation of the scan via GetOrientation.<br>
I read the Perk Lab bootcamp tutorials, I saw the tutorial videos, and looked at the script repository. Is there a page with the default basic functions (similarly to matlab)? Is there a service where I can just sit down with an expert for a couple of hours?</p>
<p>Thanks in advance for any answer!</p>

---

## Post #2 by @jcfr (2024-09-19 16:31 UTC)

<blockquote>
<p>I’ve started using 3D slicer, and managed to get a manual protocol for my project (probe view for DBS surgeries). It really is an amazing tool!</p>
</blockquote>
<p>Thanks for sharing your experience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/sparkles.png?v=12" title=":sparkles:" class="emoji" alt=":sparkles:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>I want to create markup angle by user input</p>
</blockquote>
<p>The <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">Markups</a> module documentation should provide you with useful details.</p>
<blockquote>
<p>or I need to make sure my scanned are not “reformatted”</p>
</blockquote>
<p>We would need to more details and possibly screenshot to better understand the “issue”</p>
<blockquote>
<p>I need to make sure my scanned are not “reformatted”</p>
</blockquote>
<p>Without more details, reading about the “Acquisition geometry regularization” in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">DICOM</a> module page may be of interested. (Panels and their use → Basic usage → DICOM module settings)</p>
<blockquote>
<p>Is there a page with the default basic functions (similarly to matlab)?</p>
</blockquote>
<p>Starting with the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html">Developer Guide</a> may be helpful,</p>
<blockquote>
<p>Is there a service where I can just sit down with an expert for a couple of hours?</p>
</blockquote>
<p>See  <a href="https://www.slicer.org/commercial-use.html">https://www.slicer.org/commercial-use.html</a></p>

---

## Post #3 by @Shirly_Someck (2024-09-19 17:47 UTC)

<p>First, thank you for your answer.</p>
<p>Regarding the markups, I figured out how to do it manually, but I can’t seem to make a button to add an angle markup in my extension. I looked in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html" rel="noopener nofollow ugc">developer guide</a> but couldn’t find it…</p>
<p>What I meant in regard to reformatted files, is that when I load my DICOM I sometimes get the slices in “reformat” orientation, and not the canonical (axial/coronal/sagittal):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af494e65ac380fa70a079c85c366a2ee40e44cdd.png" alt="image" data-base62-sha1="p0EC8UpxDhCXqWnl08XYx3wMv8h" width="605" height="276"><br>
and I would like that in my extension the orientation will be automatically changed to the canonical (in each slice view, i.e. red, green and yellow).</p>
<p>I will search in the developer guide and the forum for my other questions, thanks!</p>

---
