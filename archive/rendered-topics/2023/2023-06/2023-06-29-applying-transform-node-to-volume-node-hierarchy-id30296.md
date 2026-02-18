# Applying transform node to volume node hierarchy

**Topic ID**: 30296
**Date**: 2023-06-29
**URL**: https://discourse.slicer.org/t/applying-transform-node-to-volume-node-hierarchy/30296

---

## Post #1 by @bongo_kat (2023-06-29 10:32 UTC)

<p>Hello,</p>
<p>I’m trying to change the transform hierarchy of my scene.<br>
When I load my MHA file as a Sequence Meta File it gives me a volume node and a transform node:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7bfc370a7e4d98b750ffd9db5fb4fda5f1f0ad4.png" alt="image" data-base62-sha1="x4996QVRpI2GT7oJWggh743HhJi" width="163" height="80"><br>
I would like to apply the transform node to my volume node:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6028c7387e533d217c8077506b19cd8cbe215731.png" alt="image" data-base62-sha1="dIFcEqEq5O4hS5yupPN7MMXeWDn" width="166" height="77"></p>
<p>Here is my code, could someone please tell me what’s wrong with it or what’s missing ? I can load the file but adding the transform to the volume is not working.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/536d7a875f71446c65a5693cc4022069ae5ff8cc.png" alt="image" data-base62-sha1="bU2bAxLiIt4ylBrY9Ojl3kMQoOM" width="545" height="197"><br>
Thank you very much!</p>

---

## Post #2 by @lassoan (2023-06-30 12:26 UTC)

<p><code>GetNthDataNode</code> gives you a reference to the data node in the internal scene. Instead, you need to get the proxy transform node and volume node by calling <code>GetProxyNode</code>.</p>

---
