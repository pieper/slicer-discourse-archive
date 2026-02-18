# 3D Connexion space mouse

**Topic ID**: 4077
**Date**: 2018-09-12
**URL**: https://discourse.slicer.org/t/3d-connexion-space-mouse/4077

---

## Post #1 by @opetne (2018-09-12 08:37 UTC)

<p>I tried to search for a solution but without a success. How can I connect and use the Connexion 3D space mouse with the 3D Slicer?</p>
<p>Ors</p>

---

## Post #2 by @ihnorton (2018-09-12 17:34 UTC)

<p>The <a href="https://plustoolkit.github.io/">Plus toolkit</a> supports Connexion:</p>
<p><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Device3dConnexion.html" class="onebox" target="_blank">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Device3dConnexion.html</a></p>
<p>There is a Slicer example at the bottom of that page.</p>

---

## Post #3 by @opetne (2018-09-12 18:16 UTC)

<p>Dear Isaiah,</p>
<p>I found this page but I didn’t understand where the PlusServer is. Sorry for being that dumb.</p>
<p>Ors</p>
<p>Isaiah Norton <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> ezt írta (időpont: 2018. szept. 12., Sze 19:45):</p>

---

## Post #4 by @opetne (2018-09-13 09:27 UTC)

<p>Dear Isaiah,</p>
<p>I’ve found the PlusServer and did the steps written in the link you provided. I removed the driver for the 3D connexion and started the PlusServer as written in the link but no movement was made using the 3D mouse.<br>
Here is a log:<br>
|INFO|000.205000| Software version: Plus-2.6.0.63ba551d - Win64| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(102)</p>
<p>|INFO|000.205000| Logging at level 3 to file: C:/Users/petnehazy ors/PlusApp-2.6.0.20180310-Win64/data/091318_111629_PlusLog.txt| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(103)</p>
<p>|INFO|000.207000| Supported devices: - 3dConnexion (ver: Plus-2.6.0) - AuroraTracker (ver: NDICAPI-1.7) - BkProFocusOem (ver: Plus-2.6.0) - ChRobotics (ver: Plus-2.6.0) - Epiphan (ver: Plus-2.6.0) - FakeTracker (ver: Plus-2.6.0) - GenericSerialDevice (ver: Plus-2.6.0) - ICCapturing (ver: The Imaging Source UDSHL-3.4) - ImageProcessor (ver: Plus-2.6.0) - IntelRealSenseTracker (ver: ) - Microchip (ver: Plus-2.6.0) - MmfVideo (ver: Plus-2.6.0) - NDITracker (ver: NDICAPI-1.7) - NoiseVideo (ver: Plus-2.6.0) - OpenIGTLinkTracker (ver: OpenIGTLink v3.1.0) - OpenIGTLinkVideo (ver: OpenIGTLink v3.1.0) - OptiTrack (ver: Plus-2.6.0) - OpticalMarkerTracker (ver: Plus-2.6.0) - PhidgetSpatial (ver: Plus-2.6.0) - PolarisTracker (ver: NDICAPI-1.7) - SavedDataSource (ver: Plus-2.6.0) - UsSimulator (ver: Plus-2.6.0) - VFWVideo (ver: Plus-2.6.0) - VirtualBufferedCapture (ver: Plus-2.6.0) - VirtualCapture (ver: Plus-2.6.0) - VirtualDiscCapture (ver: Plus-2.6.0) - VirtualMixer (ver: Plus-2.6.0) - VirtualSwitcher (ver: Plus-2.6.0) - VirtualVolumeReconstructor (ver: Plus-2.6.0) | in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(107)</p>
<p>|INFO|000.210000| Server host name: DESKTOP-57CUE9I| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(127)</p>
<p>|INFO|000.221000| Server IP addresses: 169.254.241.236, 169.254.18.34, 169.254.49.1, 10.10.10.246, 127.0.0.1| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(147)</p>
<p>|INFO|000.221000| Start remote control server at port: 18904| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(156)</p>
<p>|INFO|018.768000| Connect using configuration file: C:\Users\petnehazy ors\PlusApp-2.6.0.20180310-Win64\config\PlusDeviceSet_Server_3dConnexion.xml| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(314)</p>
<p>|INFO|018.769000| Server process command line: "C:/Users/petnehazy ors/PlusApp-2.6.0.20180310-Win64/bin/PlusServer.exe" --config-file="C:\Users\petnehazy ors\PlusApp-2.6.0.20180310-Win64\config\PlusDeviceSet_Server_3dConnexion.xml" --verbose=3| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(205)</p>
<p>|INFO|018.959000|SERVER&gt; System start timestamp: 1834</p>
<p>|INFO|018.959000|SERVER&gt; Software version: Plus-2.6.0.63ba551d - Win64</p>
<p>|INFO|018.959000|SERVER&gt; Logging at level 3 (INFO) to file: C:/Users/petnehazy ors/PlusApp-2.6.0.20180310-Win64/data/091318_111648_PlusLog.txt</p>
<p>|INFO|018.959000|SERVER&gt; Server status: Reading configuration.</p>
<p>|INFO|018.959000|SERVER&gt; Server status: Connecting to devices.</p>
<p>|INFO|019.468000| Server process started successfully| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(213)</p>
<p>|INFO|019.963000|SERVER&gt; Server status: Starting servers.</p>
<p>|INFO|019.979000|SERVER&gt; Server status: Server(s) are running.</p>
<p>|INFO|019.980000|SERVER&gt; Press Ctrl-C to quit.</p>
<p>|INFO|019.983000|SERVER&gt; Plus OpenIGTLink server listening on IPs: 169.254.241.236, 169.254.18.34, 169.254.49.1, 10.10.10.246, 127.0.0.1 – port 18944</p>
<p>|INFO|109.806000|SERVER&gt; Received new client connection (client 1 at 127.0.0.1:18944). Number of connected clients: 1</p>
<p>|INFO|109.867000|SERVER&gt; OpenIGTLink broadcasting started. No data was available between 0-89.872sec, therefore no data were broadcasted during this time period.</p>

---

## Post #5 by @ungi (2018-09-13 14:33 UTC)

<p>Plus just relays the coordinate transformation. It reads it from the mouse and sends to Slicer, where it is converted to a transform node by the OpenIGTLinkIF module. What you do with the transform is up to you. You may be able to move the 3D view camera or a surface model with the transform, or use it in a custom module to control other things as well.</p>

---

## Post #6 by @juanmaverde (2022-11-23 06:57 UTC)

<p>Hello all,</p>
<p>Did you manage to solve this issue? I’m facing the same problem with the space mouse.</p>
<p>Summary:</p>
<ul>
<li>I can connect and start the client using openIGTL</li>
<li>transform is static</li>
</ul>
<p>Thanks for helping</p>

---

## Post #7 by @Marijn_H (2023-07-05 12:05 UTC)

<p>Hi!</p>
<p>I have the same issue with the spacemouse as <a class="mention" href="/u/juanmaverde">@juanmaverde</a>. Did you find a solution yet?</p>
<p>I can connect with plus and openIGTLink to Slicer, but the transform remains an identity matrix when manipulating the spacemouse. I tried both with and without the 3DX driver installed.</p>
<p>Thanks for your help!</p>

---

## Post #8 by @henrykrumb (2023-07-05 17:18 UTC)

<p>Heyho,</p>
<p>I’m currently working on a standalone Linux bridge from libspacenav (<a href="https://spacenav.sourceforge.net/" rel="noopener nofollow ugc">https://spacenav.sourceforge.net/</a>) to Slicer via OpenIGTLink: <a href="https://github.com/henrykrumb/spacenav-igt" class="inline-onebox" rel="noopener nofollow ugc">GitHub - henrykrumb/spacenav-igt: Use 3DConnexion SpaceMouse devices in 3D Slicer (IGTLink)</a></p>
<p>It doesn’t make use of PlusLib at the moment, but the same functionality could be integrated into the 3DConnexion class there as well (you’d need to distinguish between OS’s though, and the Windows driver works completely different).</p>
<p>If Linux is an option for you, you could try it out and maybe give me some feedback if it worked <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2023-07-06 14:12 UTC)

<p><a class="mention" href="/u/henrykrumb">@henrykrumb</a> Thank you for sharing!</p>
<p>We have played with this device a bit but it did not end up using much, as it was not very easy or intuitive to position objects with it. How do you use it? How is your experience so far?</p>

---

## Post #10 by @henrykrumb (2023-08-04 09:07 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , no problem <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I use the SpaceMouse to position and rotate the camera in the 3D view by directly associating the Camera with the transform in the transform hierarchy. This is quite convenient to inspect 3D objects from all sides, e.g. directly after segmenting a volume.</p>
<p>However, I went through a similar experience at first that the positioning was not super intuitive. I basically needed to tweak some of the values that directly fall out of the driver, such as the sensitivity which I had to reduce significantly. I also had to change the signs and order of the components in translation and rotation vectors, because the SpaceMouse coordinate frame did not directly align with RAS. Adjusting all of that, I now find the device quite usable for my purposes <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
