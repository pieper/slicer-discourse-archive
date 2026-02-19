---
topic_id: 8280
title: "Openigtif Trajectory Message"
date: 2019-09-03
url: https://discourse.slicer.org/t/8280
---

# OpenIGTIF Trajectory Message

**Topic ID**: 8280
**Date**: 2019-09-03
**URL**: https://discourse.slicer.org/t/openigtif-trajectory-message/8280

---

## Post #1 by @burnhamd (2019-09-03 18:21 UTC)

<p>Does the OpenIGTIF extension have support to receive and send trajectory messages?  I cant seem to find mention of it.</p>

---

## Post #2 by @burnhamd (2019-09-04 14:31 UTC)

<p>I am attempting to send a trajectory using a annotation.  I placed a ruler annotation in the scene.  But when I try to add this to my connector node, slicer crashes without an error message.</p>

---

## Post #3 by @lassoan (2019-09-04 14:48 UTC)

<p>Which Slicer version do you use?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> There seems to be a <a href="https://github.com/openigtlink/OpenIGTLinkIF/blob/master/MRML/vtkIGTLToMRMLTrajectory.cxx" rel="nofollow noopener">converter for ruler-&gt;trajectory</a> could you have a look why it may fail?</p>

---

## Post #4 by @Sunderlandkyl (2019-09-04 15:11 UTC)

<p>That’s the old repository, there is no such converter in <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">SlicerOpenIGTLink</a>, or in <a href="https://github.com/IGSIO/OpenIGTLinkIO/tree/master/Converter" rel="nofollow noopener">OpenIGTLinkIO</a>.</p>
<p>.</p>

---

## Post #5 by @lassoan (2019-09-04 15:18 UTC)

<p><a class="mention" href="/u/burnhamd">@burnhamd</a> Since trajectory message is not supported now, I would recommend to use transform message instead. You can compute a transform from position of the two endpoints of the ruler.</p>

---

## Post #6 by @burnhamd (2019-09-04 15:24 UTC)

<p>I decided to use the string message and send the same data that way for now.  This approach is working well.  I assume it is a bug then that the annotation shows up in the available data list for sending of MRMLNodes?  Seems that this should be removed from the UI at least to avoid crashes when someone attempts to send them.</p>
<p>Thanks for your help!</p>

---

## Post #7 by @lassoan (2019-09-04 15:29 UTC)

<p>I agree, we should not show nodes that cannot be transferred (or at least not crash but log an error). I’ve added a ticket to track this: <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/96" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink/issues/96</a></p>

---
