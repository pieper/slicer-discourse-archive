# What type of landmarking should I use?

**Topic ID**: 19531
**Date**: 2021-09-06
**URL**: https://discourse.slicer.org/t/what-type-of-landmarking-should-i-use/19531

---

## Post #1 by @lccmyers (2021-09-06 19:29 UTC)

<p>I’m working on a project on vertebral morphology, and would like to use landmarking to compare morphology across my sample. However, I’m not sure the best way to approach the landmarking, because I’m only interested in specific regions of the vertebrae that do not have a morphology that allows repeatable and comparable placement of landmarks across all of the vertebrae in my sample.</p>
<p>If you’re up on your vertebral morphology: I’m trying to compare zygapophyseal (articular facet) shape in caudal vertebrae across my sample, and the zygapophyses don’t have either a) diagnostic morphological points that I can confidently place landmarks on across my sample or b) uniformity as far as ‘lateralmost extent’ or ‘superiormost extent’ that I am comfortable placing landmarks on. It seems like some form of semilandmarks would be my best bet here, but I’m having trouble coming up with the best way to place semilandmarks <em>only</em> within the zygapophyses, and not over the entire vertebra, as I’m not interested in the rest of the vertebra (at the moment). Anyone have any ideas? I’d appreciate any help I can get.</p>

---

## Post #2 by @muratmaga (2021-09-07 01:51 UTC)

<p>If drawing an outline of your articular surfaces are sufficient for your purposes, you can use the curves markup and use a resampling to generate semi-landmarks. Here is a tutorial that shows the basics of how to do semi-landmarking in Slicer. <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Markups_2" rel="noopener nofollow ugc">https://github.com/SlicerMorph/Tutorials/tree/main/Markups_2</a></p>
<p>Whether you want to do this via open curves (as shown in tutorial) or closed curves depends on how many points you can identify as “homologous” landmarks across your samples. Resampling tool in the Slicer will treat only the very first and last point on the open curve as fixed. So if you have multiple points that you can use as “anchor” points (or hard landmarks), you can string a series of open curves to outline a closed polygon and finally merge them into a single set of points using the MergeMarkups tool of SlicerMorph.<a href="https://github.com/SlicerMorph/Tutorials/tree/main/MergeMarkups" rel="noopener nofollow ugc">https://github.com/SlicerMorph/Tutorials/tree/main/MergeMarkups</a></p>

---

## Post #3 by @lccmyers (2021-09-19 16:59 UTC)

<p>Thanks for the response!! I think an outline will be helpful, but I’d also like to include measures of the depth and curvature of the surface itself. Is there a way to add more landmarks to the interior of an outline of semilandmarks, without requiring a fixed landmark on the surface itself? I think I’ll be able to designate somewhat homologous points along the outline of the surface, but there isn’t one within the surface itself.</p>

---
