---
topic_id: 13795
title: "Slicer Unity Bridge Interest"
date: 2020-10-01
url: https://discourse.slicer.org/t/13795
---

# Slicer/Unity bridge, interest?

**Topic ID**: 13795
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/slicer-unity-bridge-interest/13795

---

## Post #1 by @adamrankin (2020-10-01 14:05 UTC)

<p>Hello all,</p>
<p>Our research group has some funds available for VR infrastructure development, and we are exploring the value of building a Slicer/Unity bridge.</p>
<p>Our primary goal is to enable Slicer on the HoloLens (and HoloLens 2) by streaming position data to Slicer, and streaming stereo rendered views back to HoloLens.</p>
<p>My first question is, has anyone started exploring this approach?</p>
<p>My second question is, is there interest from the community that investing in this area is worthwhile?</p>
<p>Thank you all for any feedback you have. Additionally, if you see this post and know of a research group who might be interested in this discussion, could you send them a link to this post?</p>
<p>Kind regards,<br>
Adam</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/franklinwk">@franklinwk</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #2 by @pieper (2020-10-01 14:43 UTC)

<p>That could be very cool, yes, I’d be interested in looking into this.  We did something <a href="https://www.na-mic.org/wiki/VR_Radiology">somewhat similar that a while back</a>, where we served rendered images to use as texture maps in VR, but not the whole rendering.</p>
<p>The biggest question to me in this approach is minimizing latency to avoid simulator sickness issues.  <a class="mention" href="/u/adamrankin">@adamrankin</a> have you investigated what the best case framerate would be just for the data transfer (i.e. head motion -&gt; tracking data from hololens -&gt; slicer -&gt; render -&gt; transfer image -&gt; display image).  If we know that’s possible then we can look into any optimizations required.</p>
<p>I’m interested in this not just for VR, but for the general topic of real-time render servers (e.g. for cloud).</p>

---

## Post #3 by @adamrankin (2020-10-01 16:09 UTC)

<p>Another alternative might be an OpenXR backend for VTK. Although this doesn’t bypass all the UWP requirements for running on HoloLens 1/2.</p>

---

## Post #4 by @adamrankin (2020-10-01 19:21 UTC)

<p>Or perhaps holographic remoting</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://docs.microsoft.com/en-us/windows/mixed-reality/develop/platform-capabilities-and-apis/add-holographic-remoting" target="_blank" rel="noopener nofollow ugc">docs.microsoft.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://docs.microsoft.com/en-us/windows/mixed-reality/develop/platform-capabilities-and-apis/add-holographic-remoting" target="_blank" rel="noopener nofollow ugc">Add holographic remoting - Mixed Reality</a></h3>

<p>Explains how to use Holographic Remoting to render holograms to a HoloLens over the network.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @dzenanz (2020-10-01 21:46 UTC)

<p><a class="mention" href="/u/agirault">@agirault</a> Is there already some connection between VTK and Unity? Wasn’t there some work based on <a href="https://gitlab.com/3dheart_public/vtktounity" rel="noopener nofollow ugc">vtktounity</a>?</p>

---

## Post #6 by @agirault (2020-10-02 13:22 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a>, yes, the link you shared is a nice open-source effort, though the last time I looked, it required a lot of hacks to make it work with VTK.</p>
<p>The latest work I’m aware of would be using <a href="https://www.kitware.eu/activiz/" rel="noopener nofollow ugc">ActiviZ 9.0</a> (C# wrapping of VTK) which the Kitware Europe team have integrated into Unity as a <a href="https://assetstore.unity.com/packages/essentials/tutorial-projects/vtkunity-activiz-163686" rel="noopener nofollow ugc">paid Unity module</a>. There is a <a href="https://assetstore.unity.com/packages/essentials/tutorial-projects/vtkunity-medicalviewer-162395" rel="noopener nofollow ugc">free plugin</a> to demonstrate medical imaging capabilities. None of this is open-source though.</p>

---

## Post #7 by @pieper (2020-10-02 13:33 UTC)

<p>From a quick look at the vtk unity connections it appears they work by sharing an opengl context, but as I understand it this would not work for hololens.</p>

---

## Post #8 by @adamrankin (2020-10-02 13:34 UTC)

<p>More importantly, it’s not just VTK that has to work. HoloLens requires UWP apps, which would require modifications to <strong>all</strong> underlying libraries.</p>

---

## Post #9 by @abhiazadz (2022-02-19 11:38 UTC)

<p>Hey, I am trying to find a way to send Fiducials from Unity to Slicer through OpenIGTLink, can you please tell me how I can do it? I have never done cross-platform connections before.</p>

---
