# Rotate the 3D View

**Topic ID**: 26435
**Date**: 2022-11-25
**URL**: https://discourse.slicer.org/t/rotate-the-3d-view/26435

---

## Post #1 by @f1oNae (2022-11-25 09:01 UTC)

<p>I know I can rotate the 3D view through the code.</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDView = layoutManager.threeDWidget(0).threeDView()
threeDView.yaw()
</code></pre>
<p>But how can I rotate 3D view at any angle I need?For example,I need to rotate it 7.2 degrees.</p>
<p>I really need your help!Deeply grateful!</p>

---

## Post #2 by @rbumm (2022-11-25 11:38 UTC)

<p>For your case (7.2 deg to the right) you could use:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDView = layoutManager.threeDWidget(0).threeDView()
threeDView.yawDirection = threeDView.YawRight
threeDView.setPitchRollYawIncrement(7.2)
threeDView.yaw()
</code></pre>
<p>Kind regards</p>

---
