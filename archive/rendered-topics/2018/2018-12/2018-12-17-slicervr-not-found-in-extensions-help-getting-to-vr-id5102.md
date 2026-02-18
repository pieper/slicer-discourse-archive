# SlicerVR not found in extensions. Help getting to VR

**Topic ID**: 5102
**Date**: 2018-12-17
**URL**: https://discourse.slicer.org/t/slicervr-not-found-in-extensions-help-getting-to-vr/5102

---

## Post #1 by @gptruncus (2018-12-17 03:01 UTC)

<p>Operating system:Mac High Sierra<br>
Slicer version:4.11.0 12-15-2018<br>
Expected behavior:<br>
Actual behavior: finding SlicerVR extension</p>
<p>Hello, I am very new to Slicer and have been using it to try to segment cardiac echocardiogram and MRI.<br>
I would like to get to the Slicer VR and get a VR headset.</p>
<p>I cannot find the Slicer VR extension listed, but have downloaded the others.<br>
I have looked through the Kitware tutorials such as <a href="https://blog.kitware.com/slicervirtualreality/" rel="nofollow noopener">https://blog.kitware.com/slicervirtualreality/</a>.</p>
<p>sincerely,<br>
Greg</p>

---

## Post #2 by @lassoan (2018-12-17 04:07 UTC)

<p>Apple is lagging quite far behind Windows in virtual reality capabilities.</p>
<ul>
<li>Apple hardware: Until very recently, there have been no virtual reality capable Macs. Now the latest high-end models are compatible, but for most of them you need to get an external GPU (that has the size and weight of a small-form-factor desktop PC and also costs about that much).</li>
<li>Compatible headsets: The only officially compatible headset is HTC Vive. It is a good headset, except it uses external trackers, which is a hassle to set up. Oculus Rift is not yet fully supported but probably it will work in a year or so. The inexpensive, highly portable Windows Mixed Reality headsets are not compatible (and probably won’t be), but maybe other headsets with comparable specs will appear in a few years.</li>
<li>Software: HTC Vive is supported in latest MacOS version at driver level and <a href="https://steamcommunity.com/app/250820/discussions/0/1692659135909712803/?ctp=2" rel="nofollow noopener">it is reported to be sort of working</a>, but there is not much virtual reality software for MacOS.</li>
</ul>
<p>Similarly to other virtual reality software providers, Slicer developers have focused their efforts on Windows, where wide range of mature virtual reality hardware and software are already available. The OpenVR interface that Slicer uses to communicate with headsets is compatible with MacOS, so in theory it should not be much time to make it work on MacOS, but we need enough interest from MacOS users and some Slicer developers will need to get access to compatible hardware.</p>
<p>If you already have a virtual reality capable MacOS computer, SteamVR works well on your system, and you would like to use Slicer in virtual reality, then <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/3" rel="nofollow noopener">add a comment on SlicerVirtualReality issue tracker</a>.</p>
<p>If you would like to explore virtual reality right now, you can get the full experience on Windows. You will need a headset (any OpenVR compatible headset will work) and a maximum few-year-old desktop computer or a recent gaming laptop. I would recommend i7 CPU and minimum Nvidia GeForce GTX1070 GPU for optimal performance (good-quality volume rendering, 4D rendering, etc).</p>

---

## Post #3 by @gptruncus (2018-12-17 04:37 UTC)

<p>thank you very much for the detailed reply.<br>
Working with Windows then, is there a straightforward setup with the SlicerVR extension, using a 3d file to connect to the VR headset?<br>
Is there a tutorial for this on the site?<br>
Sincerely,<br>
Greg</p>

---

## Post #4 by @lassoan (2018-12-17 04:39 UTC)

<p>Detailed instructions are described on <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">SlicerVirtualReality extension website</a>. If anything is missing or unclear then you can post questions here.</p>

---
