---
topic_id: 19211
title: "How To Initialize Module Widget At Application Startup"
date: 2021-08-16
url: https://discourse.slicer.org/t/19211
---

# How to initialize module widget at application startup

**Topic ID**: 19211
**Date**: 2021-08-16
**URL**: https://discourse.slicer.org/t/how-to-initialize-module-widget-at-application-startup/19211

---

## Post #1 by @keri (2021-08-16 14:06 UTC)

<p>Thank you, good to know.</p>
<p>What is a best way to initialize a module’s <strong>widget</strong> when Slicer CAT is started?</p>
<p>For example I have a <code>qSlicerStackLoadModule</code> and <code>qSlicerStackLoadModuleWidget</code> classes. I can see that <code>qSlicerStackLoadModule</code> is initialized when Slicer is launched. But the <code>qSlicerStackLoadModuleWidget</code> is initialized when the module is manually chosen in Slicer’s module toolbar via function <code>qSlicerStackLoadModule::createWidgetRepresentation()</code>.</p>
<p>I’m looking for a way to instantiate <code>qSlicerStackLoadModuleWidget</code> when <code>qSlicerStackLoadModule</code> is initialized (or more generally when the app is launched). I have tried some things but they either don’t work (Slicer stops launching) or have some lacks.</p>

---

## Post #2 by @lassoan (2021-08-16 14:28 UTC)

<p>Modules should be functional without any GUI, to make sure that they work correctly when used for batch processing (then there may be no application GUI at all) or when used from other modules.</p>
<p>If there are any features that must be initialized at startup then those should be implemented in the module logic. If there are special “always-on” GUI elements, such as a toolbar then those can be initialized from the module class (which is a Qt class).</p>

---
