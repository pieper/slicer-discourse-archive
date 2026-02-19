---
topic_id: 6674
title: "Creating Ostomies And Repositioning Facial Fractures"
date: 2019-05-02
url: https://discourse.slicer.org/t/6674
---

# Creating ostomies and repositioning facial fractures

**Topic ID**: 6674
**Date**: 2019-05-02
**URL**: https://discourse.slicer.org/t/creating-ostomies-and-repositioning-facial-fractures/6674

---

## Post #1 by @pmostofi (2019-05-02 10:49 UTC)

<p>Hello all,</p>
<p>My colleague and I conducting research using 3D slicer along with 3D printing to print out models of our patients’ facial fractures.</p>
<p>Our goal is to reduce these facial fractures within the program before printing them out on a 3D printer so we can pre-bend mini-titanium plates on them before we use them in the operating room.</p>
<p>My questions are as follows:</p>
<ol>
<li>
<p>Does 3D Slicer have the ability to reduce fractures within the program?</p>
</li>
<li>
<p>How can we use the osteomy feature within the program to cut areas of bone for surgery pre-planning?</p>
</li>
</ol>
<p>Any input that would help direct us with these questions would be much appreciated.</p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2019-05-03 19:04 UTC)

<p>Hi -</p>
<p>There has been research in the past at trying to automatically calculate fracture reductions, but as you can imagine it’s a hard problem and I’m not aware of any usable tools.</p>
<p>But you can certainly use the <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">Segment Editor</a> to interactively define pieces and rearrange them using transforms.  The Scissors effect should allow you to make free-form osteotomies.</p>
<p>You may find that <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">SlicerVR</a> to be particularly useful for this kind of task, since it allows direct 6-degree-of-freedom manipulation and 3D visualization.</p>
<p>You can also look at <a href="http://cmf.slicer.org/" rel="nofollow noopener">SlicerCMF</a> which addresses somewhat related issues.</p>

---

## Post #3 by @lassoan (2019-05-03 19:23 UTC)

<p>See this demo video about how to position bones in virtual reality:</p>
<div class="lazyYT" data-youtube-id="VzVjvnKuBAE" data-youtube-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>The main advantage of virtual reality is not the stereo display and infinite field of view but the hand controllers, which allows you to grab and position objects in space very quickly and accurately (it is about the same experience as grabbing and positioning real physical objects, but you can scale all sizes, so you can be easily 10x more accurate than in reality).</p>

---
