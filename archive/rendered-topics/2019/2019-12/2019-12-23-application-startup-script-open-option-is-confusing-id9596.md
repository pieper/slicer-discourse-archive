---
topic_id: 9596
title: "Application Startup Script Open Option Is Confusing"
date: 2019-12-23
url: https://discourse.slicer.org/t/9596
---

# Application startup script open option is confusing

**Topic ID**: 9596
**Date**: 2019-12-23
**URL**: https://discourse.slicer.org/t/application-startup-script-open-option-is-confusing/9596

---

## Post #1 by @muratmaga (2019-12-23 23:03 UTC)

<p>I find the application startup script setting confusing.</p>
<p>The default behavior is to try to open .slicerrc.py file with the editor registered for .py extension. If the user never actually done anything with .py extension, the click doesn’t do anything, but throw an error:</p>
<p>ShellExecute ‘file:///C:/Users/Murat/.slicerrc.py’ failed (error 31), even if the file exists.</p>
<p>As a user, I was expecting the open icon not actually try to open and edit the file, but give me a file browser that I can navigate to and choose to use with Slicer. We are distributing a .slicerrc.py file that we find useful for working with large datasets (disable compression etc…) that other can benefit from. But most of our users are never going to actually edit a python code. So the intention is that they simply navigate to it.</p>
<p>Can this be altered?</p>

---

## Post #2 by @lassoan (2019-12-24 00:11 UTC)

<p>I agree, the “open” icon may be misleading. Probably we should replace it by an “edit” icon but right now we don’t have such icon in Slicer core. If you can create one or find one that allows unrestricted usage and modification without attribution then please send it to us.</p>
<p>Path of rc file can be overridden in ‘SLICERRC’ environment variable. I don’t see how or why it should be possible to override in the application.</p>
<p>I would not recommend to distribute .slicerrc.py file to people who have never edited a Python file. Instead, you can register custom options in Application Settings. See for example how a  custom “settingspanel” is added in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L80">DICOM module</a>.</p>

---
