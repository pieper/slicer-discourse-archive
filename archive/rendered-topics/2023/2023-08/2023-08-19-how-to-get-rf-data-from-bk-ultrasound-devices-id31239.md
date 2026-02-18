# How to get RF data from BK ultrasound devices

**Topic ID**: 31239
**Date**: 2023-08-19
**URL**: https://discourse.slicer.org/t/how-to-get-rf-data-from-bk-ultrasound-devices/31239

---

## Post #1 by @Theo (2023-08-19 08:26 UTC)

<p>The slicer I developed and compiled needs to be connected to the BK ultrasound device through the cameralink mode of the plus server initiator to obtain raw RF data. I am not sure how to obtain RF data in the slicer code. Can you give me some advice? Thank you.</p>

---

## Post #2 by @lassoan (2023-08-19 09:09 UTC)

<p>You can set up PlusServer to collect RF data (there example configuration files, <del>for example <a href="https://github.com/PlusToolkit/PlusLibData/blob/d8f1456bd125bcd7e577805cd57fad1ec9cbfb70/ConfigFiles/PlusDeviceSet_Server_DAQVideoSource.xml#L6">here</a></del> - it seems there is no example config file for BK CameraLink) and then connect to PlusServer from Slicer to receive the RF data stream in real-time.</p>

---

## Post #4 by @Theo (2023-08-21 08:56 UTC)

<aside class="quote no-group quote-post-not-found" data-username="Theo" data-post="3" data-topic="31239" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/theo/48/67129_2.png" class="avatar"> Theo:</div>
<blockquote>
<p>I have read some internal documents of Plus, which mention the use of Cameralink acquisition cards and Sapera APIs. However, compared to the current content of PlusLibData, it seems that there has been an update. Do I currently need to use this device and API, and does the slicer have device model requirements for these devices? Is there a more specific tutorial, thanks.</p>
</blockquote>
</aside>
<p>I have read some internal documents of Plus, which mention the use of Cameralink acquisition cards and Sapera APIs. However, compared to the current content of PlusLibData, it seems that there has been an update. Do I currently need to use this device and API, and does the slicer have device model requirements for these devices? Is there a more specific tutorial, thanks.</p>

---

## Post #5 by @lassoan (2023-08-24 08:45 UTC)

<p>The example config file was for another CameraLink device. I had a look and it seems we don’t have an example configuration file for acquiring RF data via BK using the CameraLink card. Instead, we used the <a href="https://github.com/PlusToolkit/PlusLib/blob/master/src/PlusDataCollection/Testing/vtkBkProFocusCameraLinkVideoSourceTest.cxx">vtkBkProFocusCameraLinkVideoSourceTest</a> to view and acquire RF data from these systems. We only had limited time to test with these devices so we could not fully complete the development and testing and we have not tested this interface for a long time, but it should not take too much work to get this up and running again.</p>
<p>Do you have access to a BK machine with CameraLink interface and a data acquisition computer with a DALSA CameraLink card? Have your group acquired RF images from this BK machine using the CameraLink interface before?</p>

---

## Post #6 by @Theo (2023-08-25 06:39 UTC)

<p>Yes, we now have a BK ultrasound that can provide RF data, and we want to obtain its real-time RF data through Plus. We have also reviewed your last response and it seems that ultrasound RF data can be obtained without the need for vtkBkProFocusCameraLinkVideoSourceTest. Can it be obtained through the vtkDAQVideoSourceTest program? We are in contact with DAQ system company to purchase their camera link acquisition card in order to obtain RF data through plus.</p>
<p>What support is needed if we use vtkBkProFocusCameraLinkVideoSourceTest to obtain RF data? Do we need to obtain a DALSA CameraLink card and a development package from BK ultrasound company?</p>

---

## Post #7 by @lassoan (2023-08-25 08:27 UTC)

<p>Does your BK ultrasound has a CameraLink port? Do you have license from BK to use that port?</p>
<p>BK provided “Grabbie” library for interfacing with DALSA CameraLink card and we used that, but you could probably use a different CameraLink grabber and since DAQ grabber already has an interface in Plus, it could be a good candidate. However, you would need to adjust the DAQ grabber class in Plus to support RF data acquisition (it should not be complicated or a lot of work) and you may need to do some other changes (for example, how the data acquisition is initialized, determine image size and position within the buffer, managebuffer size changes, etc.). Also, you need to ensure that the framegrabber is compatible with BK’s CameraLink hardware requirements.</p>

---

## Post #8 by @Theo (2023-08-25 09:25 UTC)

<p>Thank you for your prompt response. I understand part of it. Does this mean that the “Grabbie” library is necessary, regardless of which camera link data acquisition card we use (such as whether the DAQ acquisition card requires this library “Grabbie” library). We are applying for support from BK ultrasound.</p>

---

## Post #9 by @lassoan (2023-08-25 13:07 UTC)

<p>Grabbie contains functions like computation of essential image metadata (such as number and length of scan lines for each imaging plane) from information queried from the OEM interface. You may be able to figure it out from the OEM interface documentation and experimentarion, but Grabbie can serve as a useful example. It seemed that Grabbie was kind of a work in progress when we worked with it (10+ years ago). Maybe they have something much better now.</p>

---
