# Virtual reality behaving weirdly

**Topic ID**: 6864
**Date**: 2019-05-21
**URL**: https://discourse.slicer.org/t/virtual-reality-behaving-weirdly/6864

---

## Post #1 by @sarvpriya1985 (2019-05-21 02:15 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.10.1<br>
Expected behavior:<br>
Actual behavior:<br>
Hi everyone,</p>
<p>I have been experiencing weird behaviour in virtual reality environment when performing with controllers.<br>
What is happening is exactly opposite motion when using controllers. If i try to bring it close, the model goes far. If i try to make it big it gets small. Initially, I thought it of as a batteryissue of controllers, but even after relpacing them it is behaving same.</p>
<p>Is anyone having similar issues. Any suggestions.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @cpinter (2019-05-21 17:50 UTC)

<p>Hi Sarv,</p>
<p>What VR hardware do you use?<br>
Did you try flying closer to the objects first? Sometimes “3D pinch” seems counterintuitive if you start it when still far from the closest object (farther than arm’s reach)</p>

---

## Post #3 by @lassoan (2019-05-21 18:03 UTC)

<p>I’ve experienced similar issues with Windows Mixed Reality headsets a couple of times, when I started interacting with the scene before the tracking was fully initialized. Before you start manipulating the scene, hold up the controllers in front of you and move them around until their positions are stabilized.</p>

---

## Post #4 by @sarvpriya1985 (2019-05-21 18:09 UTC)

<p>Hi Csaba</p>
<p>Thanks for getting back. I am using windows mixed reality headset. It was working fine previously but for last few days this is happening. I changed the batteries of controllers but didn’t work. The model just goes in the opposite direction of my required gesture. I didnt try anything regarding flying. The moment I try to start moving it around, the models flies away from me.</p>
<p>Sarv</p>

---

## Post #5 by @lassoan (2019-05-21 18:15 UTC)

<p>Maybe the virtual reality view is already somehow inverted (by getting some transient incorrect transforms). Try to reset the view, maybe try with a fresh scene, and only start manipulation after the controller tracking is stable. If you find that you have problem with a particular scene then it could be good if you could share it with us so that we can investigate.</p>

---
