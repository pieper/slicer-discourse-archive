---
topic_id: 27947
title: "Can I Block 3D Slicers Ability To Save Data"
date: 2023-02-21
url: https://discourse.slicer.org/t/27947
---

# Can I block 3d slicer's ability to save data?

**Topic ID**: 27947
**Date**: 2023-02-21
**URL**: https://discourse.slicer.org/t/can-i-block-3d-slicers-ability-to-save-data/27947

---

## Post #1 by @dsa934 (2023-02-21 11:51 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi , slicer users</p>
<p>I was wondering if it is possible to block the 3d slicer’s save function to process data that needs to be secure.</p>
<p>Is it possible in the same way as commenting out the save function?</p>
<p>It may sound like an absurd question, but it’s necessary to prevent data leaks. Is it possible?</p>

---

## Post #2 by @RafaelPalomar (2023-02-21 13:02 UTC)

<p>I’m not sure this is possible in Slicer. IO is driven by MRML storage nodes and qSlicerReaders/Writers. Slicer does not seem to have implemented methods to unregister any of these components once they have been registered.</p>
<p>I would’t go down the road of commenting out the registration of these components. I would probably try to search for an OS mechanism to launch Slicer on isolation. I’m not very acquainted with Windows but Windows Sandboxes sounds relevant for this case (<a href="https://uk.pcmag.com/migrated-3765-windows-10/140650/windows-sandbox-how-to-safely-test-software-without-ruining-your-computer" class="inline-onebox" rel="noopener nofollow ugc">Windows Sandbox: How to Safely Test Software Without Ruining Your Computer</a>)</p>

---

## Post #3 by @dsa934 (2023-02-21 14:43 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="2" data-topic="27947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>I’m not sure this is possible in Slicer. IO is driven by MRML storage nodes and qSlicerReaders/Writers. Slicer does not seem to have implemented methods to unregister any of these components once they have been registered.</p>
</blockquote>
</aside>
<p>I thought it would be possible to turn off the save widget, but it’s a pity.</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="2" data-topic="27947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Windows Sandboxes sounds relevant for this case (<a href="https://uk.pcmag.com/migrated-3765-windows-10/140650/windows-sandbox-how-to-safely-test-software-without-ruining-your-computer" rel="noopener nofollow ugc">Windows Sandbox: How to Safely Test Software Without Ruining Your Computer</a>)</p>
</blockquote>
</aside>
<p>Thank you for your quick response. I’m off work now, so I’ll check again tomorrow.</p>

---

## Post #4 by @jcfr (2023-02-22 23:17 UTC)

<p>The complete Slicer workflow can indeed be customized through multiple approaches</p>
<p>You could for example create an <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">Application startup file</a> that would take care of accommodating to your use case by removing menu entries, disabling modules, …</p>
<p>Alternatively, you could consider creating an extension encapsulating your workflow as well as a custom Slicer-based application bundling it.</p>
<p>References:</p>
<ul>
<li><a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></li>
<li><a href="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/">https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/</a></li>
<li><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">https://github.com/KitwareMedical/SlicerCustomAppTemplate</a></li>
</ul>

---

## Post #5 by @dsa934 (2023-02-23 09:13 UTC)

<p>Thank you for the reply.</p>
<p>Is it correct to say that the 3d slicer program itself can be customized? (e.g. Slicer version_1.0 which cannot save the used mesh MRML model file)</p>

---
