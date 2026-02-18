# Create an online segmentation mask from navigation data

**Topic ID**: 35518
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/create-an-online-segmentation-mask-from-navigation-data/35518

---

## Post #1 by @Davide_Scorza (2024-04-16 08:51 UTC)

<p>Dear Slicer community,</p>
<p>I am developing a module which includes a navigation step of a surgical robot (it is related to an <a href="https://discourse.slicer.org/t/update-3d-visualization-programmatically/30158">older topic</a> posted by a colleague some time ago) , and I would like to update the visualization of where we have already passed, with respect to a reference volume. We are currently mapping OPCUA position to slicer through an OpenIGTLink node as suggested in the linked topic, and we use the position to update a model.</p>
<p>Basically, what I am trying to achieve is the following behaviour, for visualization purposes:</p>
<ul>
<li>Activate the navigation of the system</li>
<li>Navigate the system through a reference volume</li>
<li>If the system is inside a predefined ROI, then colour the pixel to green value</li>
<li>if the system pass the predefined ROI, then colour the pixel to a red value</li>
</ul>
<p>The green and red values could be represented as a segmentation node displayed in the label layer (exactly as the Segmentation volumes).<br>
I believe the answer rely on the Segmentation Editor module, because the type of interaction that I am thinking it is similar to the paint brush, but I would like to activate it programmatically within a python module.<br>
I am assuming that I can do the processing without blocking the application.</p>
<p>I would appreciate any help or indication that you could provide.<br>
Thanks in advance.<br>
Davide</p>

---
