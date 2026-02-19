---
topic_id: 16571
title: "Factory Extensions With Built Custom Slicerapp Application N"
date: 2021-03-16
url: https://discourse.slicer.org/t/16571
---

# Factory extensions with built custom SlicerApp_APPLICATION_NAME

**Topic ID**: 16571
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/factory-extensions-with-built-custom-slicerapp-application-name/16571

---

## Post #1 by @fbordignon (2021-03-16 13:23 UTC)

<p>Hi guys, we’ve finally surrendered and started to build Slicer for our application (GeoSlicer - petrophysics area). I’ve had success in building it with Windows and adding the customizations needed on the source code. We’ve cloned the oficial repo and based our changes on the commits of the stable releases i.e., we’ve created a branch from  <a href="https://github.com/Slicer/Slicer/commit/002be18086c3054bb834dd674401ba624629e4f6" rel="noopener nofollow ugc">002be18</a> for the 4.11.20200930 build<br>
I’ve forced the slicer revision to be able to download the factory extensions with</p>
<p><code>Slicer_FORCED_REVISION "29402"</code></p>
<p>I believe it is Ok to do that, as long as we keep the changes mostly aesthetical and/or small modifications we could use the factory extensions with no problem. The problem arose when I tried to use a custom App name:</p>
<p><code>set(SlicerApp_APPLICATION_NAME "GeoSlicer")</code></p>
<p>We had a problem with SlicerJupyter, for example. The extension could not load because of some paths containing GeoSlicer instead of Slicer. I’ve added some paths to the .ini file and could load the extensions, but had some other issues down the road.</p>
<p>It would be nice to have the extensions available for users, no matter the appname, but we can understand if compiling them is the only option. Do you have any other idea that can make it work?<br>
Thanks</p>

---

## Post #2 by @Sam_Horvath (2021-03-16 13:59 UTC)

<p>Quick question:</p>
<p>Did you use the <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">custom application template</a> to create your custom app, or did you modify Slicer directly?</p>
<p>Also, if you could share some error messages indicating the paths that are not loading correctly, that would be great.</p>

---

## Post #3 by @fbordignon (2021-03-16 14:05 UTC)

<p>I’ve modified Slicer directly. I guess I was asking for trouble. Let me try SlicerCAT and report back. Thanks</p>

---

## Post #4 by @Sam_Horvath (2021-03-16 14:23 UTC)

<p>So the custom app template is the recommended method, but it is also possible that we need to make some modification to SlicerJupyter to have it work nicely with a custom app.</p>

---
