# Tip for manual downloading of Extensions

**Topic ID**: 1556
**Date**: 2017-11-29
**URL**: https://discourse.slicer.org/t/tip-for-manual-downloading-of-extensions/1556

---

## Post #1 by @JohnK (2017-11-29 17:57 UTC)

<p>I really like 3DSlicer but since I am at a hospital environment IT can be very frustrating even though I have Admin privileges on my Win workstation. The standard Install Extensions is blocked by our hospital Proxy server and I get:</p>
<p><strong>You must be authenticated to access this URL.</strong><br>
<strong>URL: <a href="http://slicer.kitware.com/midas3/slicerappstore?layout=empty&amp;os=win&amp;arch=amd64&amp;revision=26654" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore?layout=empty&amp;os=win&amp;arch=amd64&amp;revision=26654</a></strong></p>
<p>I didn’t see any help on the forum so here is what I have learned to get around this.<br>
Open a web browser to<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore/" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore/</a><br>
Click the download of the extension and then save to a local drive you have full privileges.<br>
Open the Extension Manager in 3DSlicer, click the  ‘install Extensions’ tab<br>
Click the wrench icon with arrowhead and pick install extension from file<br>
Navigate and select that file you just downloaded.<br>
Wait for a bit  (you may not get a message that the extension has been installed …)<br>
restart 3DSlicer<br>
You can delete the  file you just downloaded if you want.<br>
done!</p>

---

## Post #2 by @lassoan (2017-11-29 18:41 UTC)

<p>Thanks you for sharing this.</p>
<p>This question has come up a couple of times on the forum (for example <a href="https://discourse.slicer.org/t/cannot-download-extensions/584">Cannot download extensions</a>), it’s interesting that it is not easy to find these posts. Googling “slicer manual download of extension” brings up the relevant page, too.</p>

---

## Post #3 by @JohnK (2017-11-29 19:28 UTC)

<p>Yep, the method here did not work for me.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F4" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F4</a></p>
<p>of course could be user error… Thanks for great support!</p>

---

## Post #4 by @lassoan (2017-11-29 19:55 UTC)

<p>I think the necessary instructions were already described on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension_without_network_connection">page</a> but it was not obvious to find it (the page is quite long). I’ve now added a link from the “How to manually install an extension package?” section to the relevant section above to make the instructions easier to find.</p>

---

## Post #5 by @Saima (2021-09-21 04:04 UTC)

<p>I cant access the webpage. how to get authentication</p>

---

## Post #6 by @Saima (2021-09-21 04:06 UTC)

<p>Hi JohnK,<br>
I do not see any extension on the link provided.</p>
<p>Please share how can I have access to download extensions as the ectension manager not working.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #7 by @Saima (2021-09-21 04:07 UTC)

<p>Hi Andras,<br>
Extension manager in 3D Slicer not working. how to install extensions.<br>
for me this link not working<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore/" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/slicerappstore/ </a></p>
<p>ANy help.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #8 by @lassoan (2021-09-21 12:23 UTC)

<p>The extensions manager works now in latest Slicer Stable Release and latest Slicer Preview Release.</p>
<p>The old extensions server had to be shut down due to security vulnerabilities. You can now download extension packages manually from <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705484">here</a>.</p>

---

## Post #9 by @Saima (2021-09-23 05:18 UTC)

<p>Hi Andras,<br>
I wrote a module which was working fine in the older version slicer 4.11.0.2020.02.__. The new stable version of slicer is reporting a problem</p>
<p>Processing started<br>
error: [/home/saima/Downloads/Downloads/slicer/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>It crashes when I click apply button. I do not understand whats happening.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #10 by @lassoan (2021-09-23 16:00 UTC)

<p>Have you built Slicer and your extension on the same computer?</p>

---

## Post #11 by @Saima (2021-09-23 22:13 UTC)

<p>Hi Andras,<br>
Its loadable scripted module. Doesnt need to build. I gave path in the modules to access it.</p>
<p>Could you please help.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #12 by @lassoan (2021-09-23 22:30 UTC)

<p>Can you send a link to the line of your module that made the application crash? You can run your module line by line in the <a href="https://github.com/SlicerRt/SlicerDebuggingTools">Python debugger</a>.</p>

---

## Post #13 by @lassoan (2021-09-26 04:55 UTC)

<p>4 posts were split to a new topic: <a href="/t/tetrahedralmeshgenerator-crash/19860">TetrahedralMeshGenerator crash</a></p>

---

## Post #17 by @lassoan (2021-09-26 04:52 UTC)

<p>A post was split to a new topic: <a href="/t/show-processing-progress-information-in-a-module-gui/19859">Show processing progress information in a module GUI</a></p>

---
