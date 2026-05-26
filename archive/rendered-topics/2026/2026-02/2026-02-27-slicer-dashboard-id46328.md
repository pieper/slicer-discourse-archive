---
topic_id: 46328
title: "slicer dashboard"
date: 2026-02-27
url: https://discourse.slicer.org/t/46328
last_bumped: 2026-05-01T03:58:02.055Z
---

# slicer dashboard

**Topic ID**: 46328
**Date**: 2026-02-27
**URL**: https://discourse.slicer.org/t/slicer-dashboard/46328

---

## Post #1 by @Fatima.k (2026-02-27 14:38 UTC)

<p>Hi there, Is there any way/possibility that I can use slicer viewer in web-dashboard as well as import/call some of the extension into the dashboard without needing to install and import whole slicer app into the dashboard? Thank you.</p>

---

## Post #2 by @cpinter (2026-03-03 11:20 UTC)

<p>There have been many posts about deployment of Slicer in the cloud, please do a search here on the forum.</p>
<p>I think lately the two options that people find most interesting are SlicerTrame and RDP-based streaming.</p>

---

## Post #3 by @Fatima.k (2026-04-07 14:57 UTC)

<p>Hi, Thank you very much for your help. I moved forward with SlicerTrame and tested the examples which looks the way I want to employ slicer. Just wondering if you that it is possible to employ the slicer modules and extensions selectively? I started to do so and tested this for RT extension or Track lesion extension but I wasn’t successful yet. I appreciate if you have any idea to share how to employ them. Best,</p>

---

## Post #4 by @Thibault_Pelletier (2026-04-08 08:42 UTC)

<p>Hi <a class="mention" href="/u/fatima.k">@Fatima.k</a>,</p>
<p>SlicerTrame doesn’t support most extensions yet as the framework is quite young.</p>
<p>Since it doesn’t use Qt for its UI, some work is required to make the extensions available:</p>
<ul>
<li>Isolate the module’s logic relying on Qt from the rest of the code</li>
<li>Instantiate the logic in your SlicerTrame application context</li>
<li>Hook the logic to the SlicerTrame UI or add in the trame UI for the specific module</li>
</ul>
<p>The effort required for the migration is very dependent on the extension’s implementation.<br>
Depending on your use-case, it may be worthwhile to cherry pick the logic to integrate in your application.</p>
<p>Best,<br>
Thibault</p>

---

## Post #5 by @Fatima.k (2026-04-30 15:24 UTC)

<p>Hello <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a> ,</p>
<p>Thank you very much for your help. I’ve been working on MultiVolume viewer to add into my application. following is the map of the work:</p>
<p>trame-slicer-main/<br>
├── Dash-SlicerTrame.py<br>
└── examples/<br>
├── multi_volume_viewer_app.py<br>
├── segmentation_app.py<br>
└── viewer_lib/<br>
I deployed the MultiVolume viewer in the dashboard by following your advice to separate the extension’s Qt-dependent UI from the reusable logic, then re-expose the needed MultiVolumeExplorer behavior through a web-compatible Panel/trame interface. Instead of trying to embed the original Slicer Qt module directly, the dashboard launches a dedicated trame/Slicer viewer process from <code>Dash-SlicerTrame.py</code>, initializes the Slicer-style viewer logic inside that process, and embeds the running viewer back into the Panel dashboard through an iframe. The dashboard-side Panel controls act as the replacement for the original Qt module panel: it let the user start/stop the viewer, load local DICOM or volume folders, assign background and foreground volumes, adjust opacity and window/level, and select comparison layouts. A small file-based bridge connects the Panel dashboard and the trame viewer, so commands from the dashboard are passed to the viewer while the viewer publishes its loaded-volume state back to Panel. In this way, I did not fully port the original Qt MultiVolumeExplorer widget; I reimplemented its practical workflow for the dashboard by isolating the visualization logic, launching it in a Slicer/trame context, and controlling it from custom web UI components. with all being said, this multivolume module still doesn’t work properly as the same way in slicer. I’d appreciate any thought on this that how can I make changes to make it works?</p>
<p>Thanks,</p>
<p>Fatemeh</p>

---

## Post #6 by @Thibault_Pelletier (2026-05-01 03:58 UTC)

<p>Hi <a class="mention" href="/u/fatima.k">@Fatima.k</a>,</p>
<p>Thx for the update, glad to hear that you are moving forward with this!</p>
<p>To help you further, could you clarify what kind of problems you are currently facing (difference between the Slicer behavior and the trame behavior) and what doesn’t currently work?</p>
<p>At some point, it may also be necessary to have a look at your code.<br>
If you have pushed your work in progress somewhere (for instance on github), then I can further help.</p>
<p>Best,<br>
Thibault</p>

---
