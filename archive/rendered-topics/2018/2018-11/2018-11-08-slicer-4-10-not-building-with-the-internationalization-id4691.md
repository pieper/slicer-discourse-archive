---
topic_id: 4691
title: "Slicer 4 10 Not Building With The Internationalization"
date: 2018-11-08
url: https://discourse.slicer.org/t/4691
---

# Slicer 4.10 not building with the internationalization

**Topic ID**: 4691
**Date**: 2018-11-08
**URL**: https://discourse.slicer.org/t/slicer-4-10-not-building-with-the-internationalization/4691

---

## Post #1 by @carlos-luque (2018-11-08 23:12 UTC)

<p>I’ve built the 3D Slicer 4.10 with Internalization and  the compilation crashed.  I chose  building in release, internationalization and remaining variables are default.</p>
<p>The compilation error is:</p>
<pre><code class="lang-auto">Error        Cannot open C:/D/Slicer/Libs/MRML/Widgets/Resources/Translations/qMRMLWidgets_fr.ts:  
The system can not find in the specified path. 
[C:\B\S410RI18n\Slicer-build\Libs\MRML\Widgets\qMRMLWidgets.vcxproj]    Slicer    C:\B\S410RI18n\CUSTOMBUILD    1
</code></pre>
<p>where the <code>c:/D/Slicer</code> is the code folder and the c:/B/S410RI18n is the building folder</p>
<p>I think I forgot setting up some variables because the folder <code>Translations</code> does not exist in the source code (Slicer/Libs/MRML/Widgets)</p>
<p>Could someone give me some tips to solve this issue?</p>
<p>Thanks in the advance</p>

---

## Post #2 by @Tung_Macty (2019-01-23 08:48 UTC)

<p>When you download 3D Slicer source codes. There is no Translations directory under  ~/Slicer/Libs/MRML/Widgets/Resources/ . So you must use make Translations directory and then build</p>

---

## Post #3 by @jcfr (2019-01-31 17:24 UTC)

<p>This should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27950" rel="nofollow noopener">r27950</a></p>

---
