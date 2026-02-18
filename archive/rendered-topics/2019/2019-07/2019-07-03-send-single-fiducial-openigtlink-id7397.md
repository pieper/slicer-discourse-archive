# Send single Fiducial- OpenIGTLink

**Topic ID**: 7397
**Date**: 2019-07-03
**URL**: https://discourse.slicer.org/t/send-single-fiducial-openigtlink/7397

---

## Post #1 by @ChiaraTe (2019-07-03 15:56 UTC)

<p>Hi,<br>
I am writing an User Interface with Python Qt and SlicerDesigner and I am using OpenIGTLink for communication with external device.<br>
I send the whole Fiducial List with :<br>
connectorNode.RegisterOutgoingMRMLNode(FiducialList), but can I send only one fiducial of the list?</p>
<p>I don’t know how to access the position of the single fiducial and send it as VTK object.</p>
<p>Thank you</p>

---

## Post #2 by @Sunderlandkyl (2019-07-03 19:37 UTC)

<p>Which version of Slicer are you using?</p>
<p>In Slicer &lt;= 4.8.1 OpenIGTLinkIF had the ability to send/receive points using a vtkMRMLMarkupsFiducialNode.</p>
<p>The current version of OpenIGTLink in Slicer does not currently support point messages.</p>

---

## Post #3 by @ChiaraTe (2019-07-03 20:08 UTC)

<p>I noticed this problem with Slicer 4.10.<br>
In 4.8 I can send points with OpenigtlinkIF but all the points of the markupsList. For example if I have a fiducialList with three points: p0,p1,p2 how can I send only  p2?</p>

---

## Post #4 by @Sunderlandkyl (2019-07-03 20:26 UTC)

<p>Looking at the implementation of the old OpenIGTLinkIF, it doesn’t look like it’s possible.</p>
<p>You could implement a workaround by attaching an observer to the fiducial node and sending the position as a transform message for the time being.</p>

---

## Post #5 by @Sunderlandkyl (2019-07-03 20:41 UTC)

<p>I see you’ve already commented on it but for the sake of others, here is the SlicerOpenIGTLink issue on GitHub:<br>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/67" target="_blank" rel="nofollow noopener">github.com/openigtlink/SlicerOpenIGTLink</a>
  </header>
  <article class="onebox-body">
    <a href="https://github.com/chaicl95" rel="nofollow noopener">
<img src="https://avatars1.githubusercontent.com/u/47264962?v=2&amp;s=96" class="thumbnail onebox-avatar" width="60" height="60">
</a>

<h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/67" target="_blank" rel="nofollow noopener">Issue: [Feature Request] Sending fiducial points/Markup points via OpenIGTLinkIF</a></h4>

<div class="date" style="margin-top:10px;">
	<div class="user" style="margin-top:10px;">
	opened by <a href="https://github.com/chaicl95" target="_blank" rel="nofollow noopener">chaicl95</a>
	on <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/67" target="_blank" rel="nofollow noopener">2019-02-02</a>
	</div>
	<div class="user">
	closed by <a href="https://github.com/leochan2009" target="_blank" rel="nofollow noopener">leochan2009</a>
	on <a href="https://github.com/openigtlink/SlicerOpenIGTLink/issues/67" target="_blank" rel="nofollow noopener"></a>
	</div>
</div>

<pre class="content" style="white-space: pre-wrap;">I would like to request a new feature where the module can send and receive fiducial points/markup points via OpenIGTLinkIF. I...</pre>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #6 by @ChiaraTe (2019-07-08 13:23 UTC)

<p>Hi,<br>
I have solved putting each fiducial in a new list where there is only that point.<br>
Thank you</p>

---
