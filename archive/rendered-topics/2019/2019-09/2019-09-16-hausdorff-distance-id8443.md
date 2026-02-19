---
topic_id: 8443
title: "Hausdorff Distance"
date: 2019-09-16
url: https://discourse.slicer.org/t/8443
---

# Hausdorff Distance

**Topic ID**: 8443
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/hausdorff-distance/8443

---

## Post #1 by @MFS-YES (2019-09-16 10:05 UTC)

<p>Hello!<br>
I compute Dice and Hausdorff Distance, you can see the result. So, I know that Dice similarity ranged from 0 to 1. How Hausdorff distance was ranged?  Consequently, how to interpret this result. Any explanation will be helpful. Thanks!<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a11f564140c946ade8775e5feeaa801b780f82d.png" alt="mmexport1568627962647" data-base62-sha1="hpSJ6eAA08f0FHheX45ijvxCkgZ" width="408" height="434"></p>

---

## Post #2 by @cpinter (2019-09-16 13:43 UTC)

<p>Hausdorff distance is millimeters.</p>
<p>Here’s the wikipedia page for the Hausdorff distance that explains the concept with a helpful figure<br>
<aside class="onebox wikipedia">
  <header class="source">
      <a href="https://en.wikipedia.org/wiki/Hausdorff_distance" target="_blank" rel="nofollow noopener">en.wikipedia.org</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:128/128;"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Hausdorff_distance_sample.svg/250px-Hausdorff_distance_sample.svg.png" class="thumbnail"></div>

<h3><a href="https://en.wikipedia.org/wiki/Hausdorff_distance" target="_blank" rel="nofollow noopener">Hausdorff distance</a></h3>

<p>In mathematics, the Hausdorff distance, or Hausdorff metric, also called Pompeiu–Hausdorff distance, measures how far two subsets of a metric space are from each other. It turns the set of non-empty compact subsets of a metric space into a metric space in its own right. It is named after Felix Hausdorff.
 Informally, two sets are close in the Hausdorff distance if every point of either set is close to some point of the other set. The Hausdorff distance is the longest distance you can be forced to...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Here is the doxygen page from the Plastimatch Hausdorff algorithm with equations (this is what the module uses, need to scroll down a bit)<br>
<a href="http://plastimatch.org/doxygen/classHausdorff__distance.html" class="onebox" target="_blank" rel="nofollow noopener">http://plastimatch.org/doxygen/classHausdorff__distance.html</a></p>
<p>By the way this last link is referenced from the module documentation<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison</a></p>
<p>It is generally a good idea to look at the documentation, as many times you will find useful information there.</p>

---

## Post #3 by @MFS-YES (2019-09-17 04:02 UTC)

<p>Thank!<img title="Emoji" alt="Emoji" height="16" src="https://s.yimg.com/nq/yemoji_assets/latest/yemoji_assets/1f44d.png" width="16"></p>

---

## Post #4 by @John_Agapito (2021-09-14 20:00 UTC)

<p>on a related note…does anyone have any information on whether the plastimatch Hausdorff or DICE calculations have been validated against any other viable option?</p>

---

## Post #5 by @gcsharp (2021-09-14 20:05 UTC)

<p>Yes, we validated it against analytic solids prior to using it to score the MICCAI 2015 H&amp;N Grand Challenge.  That means comparing translated and resized cubes, spheres, and cylinders, and comparing against the analytic solution.</p>

---

## Post #6 by @John_Agapito (2021-09-15 12:29 UTC)

<p>Thanks Greg - are there any publications or links to details available anywhere?<br>
We’d like to use slicerRT to assess AI contouring quality in a research project.</p>

---

## Post #7 by @gcsharp (2021-09-17 19:34 UTC)

<p>Hi John.  I checked, but that information was not included in the paper.  I guess you could cite as “Personal communication”.  Sorry.</p>

---

## Post #8 by @John_Agapito (2021-09-18 11:25 UTC)

<p>Thanks for checking Greg. Much obliged.</p>

---
