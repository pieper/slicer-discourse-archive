# OpenIGTlinkIF Transform references

**Topic ID**: 8097
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/openigtlinkif-transform-references/8097

---

## Post #1 by @burnhamd (2019-08-19 19:33 UTC)

<p>I am using openigtif extenstion to get streaming data from my tracker.  Is there a way to get a reference to the transforms created by openigtif extenstion before they are created?</p>
<p>I want a object to be set to a default position (identity) until the slicerIGTIF updates this transform.<br>
I have tried creating a transform node with the same name as the transform coming in, but I just get duplicates instead.</p>

---

## Post #2 by @burnhamd (2019-08-19 19:36 UTC)

<p>Update to my own question.</p>
<p>I am thinking of going down the path of having an observer that watches the scene to see if a node with the correct name was added.  Is this the best method?</p>

---

## Post #3 by @lassoan (2019-08-21 16:38 UTC)

<p>OpenIGTlinkIF module looks up nodes by name (that matches the device name in OpenIGTLink message).</p>
<p>We usually create the node by the appropriate name <em>before</em> we establish the OpenIGTLink connection. This way OpenIGTLinkIF module finds that node and updates it in real-time.</p>
<p>If you prefer OpenIGTLinkIF to create the nodes for you then looking them up by name is correct, too. The only slight additional complexity is that you need to add the scene observers to detect when the nodes are added.</p>

---

## Post #4 by @burnhamd (2019-08-23 13:11 UTC)

<p>I assumed that the openigtlinkif module looked nodes up by name.  And I created a node with the same name prior to creating the openigt link.  However, I get another node with the same name when the connection is established rather than the node that I previously created being used.</p>
<p>Here is the screenshot.  The first one in the list is the one I created.  The second is the one that was added by openigtlinkif after establishing the connection.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc954e02b7cdf7c1ad2b09c6eb74197262011183.png" alt="image" data-base62-sha1="A2scND7RtymzpNgkyBMrEIF2jYL" width="321" height="59"></p>

---

## Post #5 by @lassoan (2019-08-23 16:10 UTC)

<p>Please try with latest Preview Release of Slicer and let us know if this is still the case.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Do you remember having a problem that OpenIGTLinkIF created new nodes instead of reusing existing nodes by the same name&amp;type?</p>

---

## Post #6 by @Sunderlandkyl (2019-08-23 16:24 UTC)

<p>When it was originally split into the SlicerOpenIGTLink module it had that problem, but as I recall I fixed it shortly after.</p>

---

## Post #7 by @Sunderlandkyl (2019-08-23 16:27 UTC)

<p>I just tested it with the latest nightly version of Slicer, and it found the existing nodes with the same name.</p>

---

## Post #8 by @burnhamd (2019-08-23 16:56 UTC)

<p>Found the issue.</p>
<p>I was using a TransformNode.<br>
Once I used the LinearTransformNode, it works as expected.</p>

---

## Post #9 by @lassoan (2019-08-23 17:00 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you update OpenIGTLinkIF so that it can update vtkMRMLTransformNode types as well?</p>

---

## Post #10 by @Sunderlandkyl (2019-08-23 18:16 UTC)

<p>Integrated in <a href="https://github.com/openigtlink/SlicerOpenIGTLink/commit/36041a4d6a7a247fc8ed783485524e60bb340f0f" rel="nofollow noopener">36041a4</a>.</p>
<p>It should be included in tomorrows nightly build.</p>

---
