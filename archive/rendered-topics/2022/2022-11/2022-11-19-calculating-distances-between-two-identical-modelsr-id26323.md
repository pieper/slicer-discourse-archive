---
topic_id: 26323
title: "Calculating Distances Between Two Identical Modelsr"
date: 2022-11-19
url: https://discourse.slicer.org/t/26323
---

# Calculating distances between two identical modelsr

**Topic ID**: 26323
**Date**: 2022-11-19
**URL**: https://discourse.slicer.org/t/calculating-distances-between-two-identical-modelsr/26323

---

## Post #1 by @TrascendentK (2022-11-19 17:23 UTC)

<p>Hi all,<br>
i’m new to Sclier3D and i’m actually using it to write my bachelor’s thesis, so i apologise if this is an odd question.</p>
<p>The work is aimed to evaluate the accuracy of computer-guided implant surgery, which means measuring the distance between the ideal implant position and it’s actual post-operative one in a given set of points. I have gathered the models of the implant’s planned position and it’s actual position and when imported in Slicer they correctly arrange based on their relative position.</p>
<p>Now i’m facing difficulties in programmatically getting the linear distance between the corresponding points of the two models, as i’m trying to eliminate the human errors and thus i don’t want to use human registered points to obtain such information.</p>
<p>Any idea on how i can achieve these?<br>
I’ll attach a screen of the two models imported in Slicer.</p>
<p>Thanks for your help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0daf2bde8487b096698e95965d3f9cc4ca12dab.png" data-download-href="/uploads/short-url/ymHGBVdenzt9DSatXvHLH89NeWv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0daf2bde8487b096698e95965d3f9cc4ca12dab.png" alt="image" data-base62-sha1="ymHGBVdenzt9DSatXvHLH89NeWv" width="423" height="500" data-dominant-color="9B98C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">524×618 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-12-01 07:02 UTC)

<p>You can do this in multiple stages:</p>
<ul>
<li>first align the position based on center of gravity and direction based on principal axis directions</li>
<li>fine-tune the result using ICP (using <code>Model to model registration</code> module in SlicerIGT)</li>
</ul>
<p>Alternatively, you may use Segment Registration extension (that can register the models even if they are deformed).</p>

---
