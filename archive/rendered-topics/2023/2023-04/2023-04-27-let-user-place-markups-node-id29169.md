---
topic_id: 29169
title: "Let User Place Markups Node"
date: 2023-04-27
url: https://discourse.slicer.org/t/29169
---

# Let user place markups node

**Topic ID**: 29169
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/let-user-place-markups-node/29169

---

## Post #1 by @devD (2023-04-27 09:17 UTC)

<p>I am trying to make a simple script.</p>
<p>I have created a button which the user can press. When the button is pressed, the user should then be prompted to place one markups node, when this node is placed the user should then be prompted to place another node and then no more (so two markups nodes should be placed). And then i want to get the coordinates for these nodes.</p>
<p>I have tried to do this by using the function</p>
<pre><code class="lang-auto">placeModePersistence = 1
slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)
</code></pre>
<p>and a while loop that should let the user to place two nodes. However the issue is that the code creates the markups node before the user has a chance to place it on the image. What is the right way to do this?</p>
<p>(I also tried using the interaction nodes but got the same problem)</p>
<p>Thank you</p>

---

## Post #2 by @RafaelPalomar (2023-05-02 10:36 UTC)

<p>I’m not sure if it is a good idea to have a <code>while loop</code> like this; my feeling is that this will have problems with the Slicer application’s event loop.</p>
<p>Assuming you want this integrated in a scripted module. Instead of asking the user directly, I would set a “Remaining points: &lt;# number of points&gt;” label in the user interface. If the user should not proceed without adding all the fiducials, you can disable the rest of the user interface of the module until the count is fulfilled.</p>
<p>If you don’t want this integrated in a module, you could have a look at the templated markups (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#creating-template-landmarks" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a>), which can help you placing markups in a workflow.</p>

---
