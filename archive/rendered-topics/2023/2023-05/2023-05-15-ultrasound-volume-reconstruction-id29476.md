# Ultrasound volume reconstruction

**Topic ID**: 29476
**Date**: 2023-05-15
**URL**: https://discourse.slicer.org/t/ultrasound-volume-reconstruction/29476

---

## Post #1 by @Callie_Dunkel (2023-05-15 14:38 UTC)

<p>Hello everyone,</p>
<p>I am interested in reconstructing the volume of joints using ultrasound machines available at my school. So far, I have been able to set up the ultrasound simulator in Slicer. I have Konica Minolta HS2, Fujifilm PX and Edge II ultrasound machines at my disposal. I plan on using one of the optical trackers our lab has as well. Before I dive into trying to make this work, I just want to make sure Plustoolkit and Silcer are able to be configured with the hardware devices I had. These machines were not listed on Plus’ website but is there a way to set them up (with limited programming experience!). Thank you in advance and thanks for all the work everyone has put into this amazing application!</p>

---

## Post #2 by @tomekcz (2023-05-17 17:57 UTC)

<p>PLUS should be the package you need, but you’re right that it doesn’t look like any of the ultrasound scanners you have are supported out-of-the-box. If you have access to the API/SDK of these ultrasound systems (provided by the manufacturer), you can attempt to code up your own class (see <a href="https://plustoolkit.github.io/devicecode" class="inline-onebox" rel="noopener nofollow ugc">Adding a Device</a>). This does require a fair amount of comfort with C++, but you can use the other devices as a template for your code (e.g. <a href="https://github.com/PlusToolkit/PlusLib/blob/master/src/PlusDataCollection/Interson/vtkPlusIntersonVideoSource.cxx" rel="noopener nofollow ugc">PlusLib/vtkPlusIntersonVideoSource.cxx</a>).</p>
<p>If you dont have access to SDKs, you can investigate using a frame grabber that will essentially record the stream from the ultrasound display and send those frames to Slicer over the IGTLink server (see <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceEpiphan.html" rel="noopener nofollow ugc">Epiphan frame grabber</a>). More information on Data collection devices can be found here <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html" rel="noopener nofollow ugc">Device set configuration</a>. Hope this helps!</p>

---
