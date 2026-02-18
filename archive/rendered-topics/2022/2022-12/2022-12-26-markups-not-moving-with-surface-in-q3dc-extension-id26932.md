# Markups not moving with surface in Q3DC extension

**Topic ID**: 26932
**Date**: 2022-12-26
**URL**: https://discourse.slicer.org/t/markups-not-moving-with-surface-in-q3dc-extension/26932

---

## Post #1 by @Annett (2022-12-26 21:21 UTC)

<p>In the new 5.2 version, when using Q3DC extension there is a problem.<br>
I have to take measurements on an .stl file.<br>
When you enter points for taking measurements, if you then use “transform” to move the object, the points don’t stay on the surface. Only the object moves and not the points. With version 4.2 I didn’t have this problem.<br>
How can I solve it? Is it a bug?</p>

---

## Post #2 by @lassoan (2022-12-26 21:25 UTC)

<p>I don’t know if this change was intentional or not, but you can probably make the markup node move together with the model by dragging the markup under the same transform as the model (in Data module, “Transform hierarchy” tab).</p>

---

## Post #3 by @FilippoFV (2022-12-26 21:19 UTC)

<p>Hello everybody, I need some help please with the new release 5.2.1</p>
<p>I use the Q3DC panel to add some landmarks on my model flagging the on surface option both on connected and selected landmarks. Now I see my landmarks on the model.<br>
After that I go to the transform panel to move my model in reference to the Y,G and R planes.<br>
But I see now that the landmarks don’t stick to the model but they move on their own loosing their position on my model.</p>
<p>What do I do wrong? I want to be able to move my model with the lendmarks permanent on it.</p>
<p>Thank you!</p>

---

## Post #4 by @Annett (2022-12-27 10:19 UTC)

<p>I tried but unfortunately points don’t move together with the mesh… I can’t understand why</p>

---
