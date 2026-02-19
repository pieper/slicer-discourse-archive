---
topic_id: 14874
title: "How Can I Make All 6 Views Link Together"
date: 2020-12-04
url: https://discourse.slicer.org/t/14874
---

# How can I make all 6 views Link together

**Topic ID**: 14874
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/how-can-i-make-all-6-views-link-together/14874

---

## Post #1 by @Tesla2678 (2020-12-04 05:13 UTC)

<p>Hello there,</p>
<p>I have 2 files in layout. I want to make all 6 views link together, So when I move the mouse while the Shift key is pressed, all the other 5 views will move at the same time.</p>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2020-12-04 05:18 UTC)

<p>Views that have the same <a href="http://apidocs.slicer.org/master/classvtkMRMLAbstractViewNode.html#a896bad470fb25f642165eb6305eee4fc">View group</a> are linked. You can set it from Python or using View Controllers module’s Advanced section.</p>

---

## Post #3 by @Tesla2678 (2020-12-08 01:48 UTC)

<p>Thank you very much~</p>

---

## Post #5 by @jcfr (2021-05-18 19:03 UTC)

<blockquote>
<p>Is there a way to link the views in Python? We need to be able to zoom all 3 views at the same time. I &gt; imagine it would be like pushing the “Link button” in the view tool bar.</p>
</blockquote>
<p>See entry <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-all-slice-views-linked-by-default">Set all slice views linked by default</a> from the script repository</p>

---

## Post #6 by @spycolyf (2021-05-19 17:54 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
Is there a way to reset, reinitialize or recreate a 3D view after it contains a rendering. In other words, dispose or delete the rendering or view and create a new one in the same view window?</p>
<p>Thanks</p>

---

## Post #7 by @pieper (2021-05-19 18:01 UTC)

<p><a class="mention" href="/u/spycolyf">@spycolyf</a> - the way it works in Slicer is that the views observe the scene and display whatever meets their display criteria (i.e. if matches their view ID or doesn’t specify a view ID).  So for example if a model node has multiple model display nodes, each one of which will have a list of zero or more view IDs.  The view will then display the model using the display properties for the matching display node or nodes.  Clearing the view would mean making sure none of the display nodes match what the view ID.</p>

---

## Post #8 by @spycolyf (2021-05-19 20:03 UTC)

<p>OK, my apologies. I should show you what I’m trying to do.</p>
<p>I currently have a MIP displayed. How do I replace it with a transparent rendering?</p>
<p>Here’s the MIP…<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9c59f2a7b428438409d2c9df02b5919ffa83803.png" alt="image" data-base62-sha1="v4v0QJ7rxKeS2Aoy0x9klwMqF7Z" width="255" height="262"></p>
<p>And when I try to replace it with a render, here’s what I get. The MIP wont go away…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6df010330de73ca12097b654da2296968be498c.png" alt="image" data-base62-sha1="snik1iBuJZQoCy510yXN7QSoasY" width="248" height="231"></p>
<p>I’m trying to switch from the MIP to this…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37b01042db2f3d3da6cba2ee23d7d3c7b60ebd19.png" alt="image" data-base62-sha1="7WDtsLSyag80H7KgmFwCB8dedOF" width="218" height="215"></p>

---

## Post #9 by @pieper (2021-05-19 20:57 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="8" data-topic="14874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>And when I try to replace it with a render, here’s what I get. The MIP wont go away…</p>
</blockquote>
</aside>
<p>What step do you do when you try to replace the MIP?</p>

---

## Post #11 by @spycolyf (2021-05-20 14:43 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<p>Sorry about all of that code <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=9" title=":expressionless:" class="emoji" alt=":expressionless:"></p>
<p>Here’s what get executed after to replace the MIP with the rendered…</p>
<pre><code>def showVolumeRendering self, volumeNode):
    volRenLogic = slicer.modules.volumerendering.logic()
    displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
    displayNode.SetVisibility(True)
    scalarRange = volumeNode.GetImageData().GetScalarRange()
    if scalarRange[1]-scalarRange[0] &lt; 1500:
      # Small dynamic range, probably MRI
      displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName("MR-Default"))
    else:
      # Larger dynamic range, probably CT
      displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName("CT-Chest-Contrast-Enhanced"))</code></pre>

---

## Post #13 by @pieper (2021-05-20 18:22 UTC)

<p>Probably you are ending up with multiple display nodes so changing one leaves the other in place.  You should be able to replace all the display nodes with a new version with the settings you want (or change the settings of the existing ones)</p>

---

## Post #14 by @spycolyf (2021-05-21 14:42 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. But, how? What code am I missing?</p>

---

## Post #15 by @pieper (2021-05-21 15:00 UTC)

<p>I couldn’t say for sure - debugging is half the fun, so you’ll need to do some digging.</p>
<p>A good way to better understand what’s going on is to use the Data module’s <code>All nodes</code> tab, and open the <code>Node information</code> box and enable showing of hidden nodes and MRML ids.  Then as you interact with the scene you can see all the details of node values and what nodes reference each other by ID.  All this node information is what gets saved and restored in the scene, and also what controls communication across the app.  Once you get a good handle on what happens there you will have a much better understanding of how to write and debug Slicer code.</p>

---

## Post #16 by @lassoan (2021-05-21 17:11 UTC)

<p>It seems that you haven’t switched back the rendering technique in the view from MIP to composite rendering. See my answer to this question <a href="https://discourse.slicer.org/t/slicerqr-development/15954/161">here</a>. It would be easier to keep track of discussions if we kept the topics short and focused on one question.</p>

---
