---
topic_id: 20872
title: "Visual Representation Of Control Point In Icons"
date: 2021-12-01
url: https://discourse.slicer.org/t/20872
---

# Visual representation of control point in icons

**Topic ID**: 20872
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/visual-representation-of-control-point-in-icons/20872

---

## Post #1 by @jamesobutler (2021-12-01 22:48 UTC)

<p>When using the Markups module and looking at icons to determine functionality, I have observed that there seems to be different visual representations of a “control point”. These different visual representations make it seem like the buttons act on/utilize different objects when in fact they act on/utilize the same type of objects (control points).</p>
<h2><a name="p-70545-starburst-glyph-representation-1" class="anchor" href="#p-70545-starburst-glyph-representation-1" aria-label="Heading link"></a>Starburst Glyph representation</h2>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c6fef56dbf2856b4dacf9a30804d90d9765f816.png" alt="image" data-base62-sha1="aUc6E7GWdkSpPO4MN7eDGsNLXgO" width="484" height="45"></p>
<h2><a name="p-70545-sphere3d-glyph-representation-2" class="anchor" href="#p-70545-sphere3d-glyph-representation-2" aria-label="Heading link"></a>Sphere3D Glyph representation</h2>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfe78c22df43ac5d9f5b783319227209758ab9eb.png" alt="image" data-base62-sha1="rnFhF6GkcqDzhlKlH8YB12ZLNSX" width="147" height="42"></p>
<h2><a name="p-70545-square-blue-outline-glyph-representation-3" class="anchor" href="#p-70545-square-blue-outline-glyph-representation-3" aria-label="Heading link"></a>Square blue outline Glyph representation</h2>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b77f350572f0c1a3295dff0ae2e771d50b6e9df.png" alt="image" data-base62-sha1="mbl029WI70ozuG6VMaXKM5n9Ser" width="157" height="34"></p>
<p>It would be helpful if an icon is referring to a Markups “control point” that they all use the same visual representation. This applies even to module icon like the Markups module because it is using control points in the icon.</p>
<p>If these icons are updated, should the control point visualization match the Slicer default display of control points? Do the Slicer defaults need to be updated? Current defaults are below:</p>
<ul>
<li>Glyph: Sphere3D</li>
<li>Color: <span class="hashtag-raw">#ff8080</span> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cea7b9664ea9c70af9f0f72f8d6b5c725bfee0f6.png" alt="image" data-base62-sha1="tu9HNmIAoQBeSGJcmyFbSoaNOWa" width="31" height="34"></li>
</ul>
<p>My guess is that Starburst2D used to be the default glyph and it was changed at some point for some reason? This resulting in the split of various representations in the icons.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4862bb6ea9c025e03c18985ae3c04232d52f41b3.png" alt="image" data-base62-sha1="aklUs85LL7zDlEfmTPa7zcLgmBR" width="84" height="44"></p>
<p>I believe there was also previous discussion about making the default control point color match the color in the icon. Therefore it should either be the more salmon color as in the Starburst2D representations, or the more deep red color as in the Sphere3D representations.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85aae6dfa3f3eee56d2e98704a2834840c722775.png" alt="image" data-base62-sha1="j4tERyHyKUcJbPkmAuYYaX66S5n" width="82" height="34"></p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @pieper (2021-12-01 22:55 UTC)

<p>Yes, in the Slicer3 era the starburst was the default shape for a fiducial (point) in the 2D views.</p>
<p>+1 for unifying the visual representation.</p>

---

## Post #3 by @lassoan (2021-12-02 19:13 UTC)

<p>Agreed, it would be nice to harmonize these icons.</p>
<p>I find that crosshair with a dot is very good for accurate positioning in slice views, while in 3D usually the sphere glyph looks the most natural. The sphere glyph is usually good enough in slice views as well, so keeping the current sphere glyph as default - and use that in all the markups module icons - makes sense.</p>
<p>To have crisp icons at all resolutions, we would need create SVGs that are pixel-perfect at the size of 24x24 pixels, using colors that work over both light and dark background (just to avoid the need of dynamically recoloring/replacing icons when switching between light/dark mode), preferably in Inkscape.</p>
<p>Kitware designers (Steve Jordan) offered their help for this. If we put together a small set of well-described icons (name, description, previous appearance) then he can design them. Markups icons could be a good collection - not too many, closely related icons that would greatly benefit from a redesign.</p>

---

## Post #4 by @mikebind (2021-12-02 22:12 UTC)

<p>I find that anything other than a sphere seems odd in the 3D views. I think either cross-hair with a dot or a circle works OK in 2D.  I like being able to see more of the image with the cross-hair, but it’s also helpful that the representation is similar between the 2D and 3D views for the circle/sphere.  Overall, I would vote for the circle/sphere pairing as the default (and what’s shown on icons).  One option would be to use a cross-hair when <em>placing</em> new control points, and a circle/sphere for <em>placed</em> points. I’m not sure how well that functionality would fit into how markups work under the hood, though, so maybe it’s not very feasible.</p>

---
