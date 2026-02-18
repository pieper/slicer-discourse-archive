# Sending fiducial points via OpenIGTLinkIF

**Topic ID**: 5614
**Date**: 2019-02-01
**URL**: https://discourse.slicer.org/t/sending-fiducial-points-via-openigtlinkif/5614

---

## Post #1 by @Chai_Chun_Lok (2019-02-01 22:45 UTC)

<p>Hi, I have some questions regarding “OpenIGTLinkIF”. I can see that it can used to send linear transforms in Slicer with an OpenIGTLink example (TrackerServer). However, I found that the I/O configuration can only choose linear transform only. When I try to run other examples from OpenIGTLink (PointServer and PointClient), but Slicer can’t receive any point in the form of PointMessage even the connector status is ‘ON’. Is there a way to send fiducial points into Slicer similar to the stated example(TrackerServer)?</p>

---

## Post #2 by @lassoan (2019-02-02 02:11 UTC)

<p>I don’t think sending of markup points is currently supported (<a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you confirm)?</p>
<p>It should not be difficult to add (probably a few days of work), would you be interested to contribute? We can help you to get started.</p>

---

## Post #3 by @Chai_Chun_Lok (2019-02-02 03:38 UTC)

<p>It would be nice if I could add this support. I’m still a novice at programming. Is it OK?</p>

---

## Post #4 by @lassoan (2019-02-02 14:03 UTC)

<p>We don’t have immediate plans to implement this, so if you want this to happen soon then you would need to contribute in some way. You can submit an issue to SlicerOpenIGTLink extension’s issue tracker to record this request and follow its status.</p>

---

## Post #5 by @Chai_Chun_Lok (2019-02-02 14:23 UTC)

<p>I will submit an issue about this. Thanks for the information!</p>

---

## Post #6 by @lassoan (2019-02-04 18:49 UTC)

<p>For reference, here is the GitHub issue tracking this feature request: <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/67" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink/issues/67</a></p>

---

## Post #7 by @zhenyu1995 (2019-02-13 03:50 UTC)

<p>Hi Sir,</p>
<p>We had successfully send the transform files (.h5) via IGTLink and we are working on converting those transform nodes into fiducial nodes. I had successfully convert one transform node to fiducial node using coding below:</p>
<pre><code>myNode = slicer.util.getNode('Point1')
transformMatrix = vtk.vtkMatrix4x4()
myNode.GetMatrixTransformToWorld(transformMatrix)
x = transformMatrix.GetElement(0,3)
y = transformMatrix.GetElement(1,3)
z = transformMatrix.GetElement(2,3)
slicer.modules.markups.logic().AddFiducial(x, y, z)
</code></pre>
<p>However, we have 8 transform nodes (Point 1, Point2, Point3, … , Point8) so i am trying to develop a looping coding to convert all transform nodes into fiducial nodes in one go. May I know how can we do this? I’ve tried using ‘for’ loop together with myNode = slicer.util.getNode(‘Point’,n) where n varies from 1 to 8. But this cannot work. Thank you very much</p>

---

## Post #8 by @lassoan (2019-03-13 14:36 UTC)

<aside class="quote no-group" data-username="zhenyu1995" data-post="7" data-topic="5614">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/47e85d/48.png" class="avatar"> zhenyu1995:</div>
<blockquote>
<p>slicer.util.getNode(‘Point’,n)</p>
</blockquote>
</aside>
<p>You can use <code>'Point'+str(n)</code> or <code>'Point%d' % n</code> to append a number to the end of a string and a number.</p>

---

## Post #9 by @zhenyu1995 (2019-03-14 02:48 UTC)

<p>This had worked well. Thank you very much!</p>

---

## Post #10 by @lassoan (2021-04-18 05:10 UTC)

<p>A post was merged into an existing topic: <a href="/t/i-cant-find-the-trackerserver-exe-in-openigtlinkif-module/17055/10">I can’t find the TrackerServer.exe in OpenIGTLinkIF module</a></p>

---
