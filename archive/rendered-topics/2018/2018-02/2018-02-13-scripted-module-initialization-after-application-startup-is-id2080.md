---
topic_id: 2080
title: "Scripted Module Initialization After Application Startup Is"
date: 2018-02-13
url: https://discourse.slicer.org/t/2080
---

# Scripted module initialization after application startup is completed

**Topic ID**: 2080
**Date**: 2018-02-13
**URL**: https://discourse.slicer.org/t/scripted-module-initialization-after-application-startup-is-completed/2080

---

## Post #1 by @lassoan (2018-02-13 16:15 UTC)

<p>Modules that relied on using a singleshot timer to perform additional initialization steps after Slicer startup is completed, in Slicer-4.9 (recent trunk versions) must switch to use the application’s <code>startupCompleted()</code> signal instead. See details in Slicer <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/VTK7-Qt4-to-VTK9-Qt5#Slicer_scripted_module_initialization_steps_after_application_startup">migration guide</a>.</p>

---
