# How to change the application name of Slicer?

**Topic ID**: 13521
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/how-to-change-the-application-name-of-slicer/13521

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-17 10:08 UTC)

<p>I changed the appllicationName, applicationDisplayName by slicer.util module.<br>
But the window title is not changing, its still Slicer(version).</p>

---

## Post #2 by @lassoan (2020-09-17 11:24 UTC)

<p>A clone of the Slicer.exe launcher and SlicerLauncherSettings.ini settings file can be created with a different name (for example, MyModuleName.exe and bin/MyModuleNameLauncherSettings.ini). See example <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">here</a>.</p>

---

## Post #3 by @slicer365 (2023-10-05 12:01 UTC)

<p>A problem with me about this topic</p>
<p>If I  change the soft’s name to Japanese characters, I will not be able to start the software！</p>

---

## Post #4 by @lassoan (2023-10-05 12:38 UTC)

<p>Since the code page of the console and operating system may not be UTF8 on most Windows systems, it could be problematic to use special characters on the command line (in application name or command-line arguments). This may change in the next couple of years but until then I would recommend to use only latin characters in the application name.</p>
<p>The application shortcut’s name (that appears in the Start menu) should be easy to change, by modifying the nsis install script. The title of the application’s main window can also be changed easily after the application has started; but various popup windows may still use the application name in their window title.</p>

---
