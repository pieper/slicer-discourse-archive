# C++ segmentation Module building fails with Qt5 - compatibility with Qt4/Qt5 of ui files?

**Topic ID**: 2661
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/c-segmentation-module-building-fails-with-qt5-compatibility-with-qt4-qt5-of-ui-files/2661

---

## Post #1 by @Eloise (2018-04-23 10:05 UTC)

<p>Hi all,</p>
<p>I have developed a C++ segmentation module in Slicer in a previous environment (Slicer 4.9 on Mac Os El Capitan 10.11, using Qt4), and I am now trying to build it in a new Slicer environment (Slicer 4.9 on Mac OS Sierra 10.12, using Qt5.10). I encountered difficulties in building this new Slicer with Qt4 so I used Qt5 as it was recommended as the most maintained/tested now and it worked, but the building of my segmentation modules failed in the ui files, and more especially in the qSlicerModuleNameFooBarWidget.ui (copied below), indicating an RCC Parse Error <em>Line: 2 Column: 18 [unexpected tag: ui]</em>, and I can’t find any help on such error.<br>
Did someone ever have this error ?  The ui file is very basic and I have read that there was a compatibility from Qt4 to Qt5 for the ui files ?</p>
<pre><code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;ui version="4.0"&gt;
 &lt;class&gt;qSlicerSeedSegmentation3FooBarWidget&lt;/class&gt;
 &lt;widget class="QWidget" name="qSlicerSeedSegmentation3FooBarWidget"&gt;
  &lt;property name="geometry"&gt;
   &lt;rect&gt;
    &lt;x&gt;0&lt;/x&gt;
    &lt;y&gt;0&lt;/y&gt;
    &lt;width&gt;103&lt;/width&gt;
    &lt;height&gt;32&lt;/height&gt;
   &lt;/rect&gt;
  &lt;/property&gt;
  &lt;property name="windowTitle"&gt;
   &lt;string&gt;Foo bar&lt;/string&gt;
  &lt;/property&gt;
  &lt;layout class="QVBoxLayout" name="verticalLayout"&gt;
   &lt;property name="margin"&gt;
    &lt;number&gt;0&lt;/number&gt;
   &lt;/property&gt;
   &lt;item&gt;
    &lt;widget class="QPushButton" name="FooBarButton"&gt;
     &lt;property name="text"&gt;
      &lt;string&gt;Foo Bar&lt;/string&gt;
     &lt;/property&gt;
    &lt;/widget&gt;
   &lt;/item&gt;
  &lt;/layout&gt;
 &lt;/widget&gt;
 &lt;resources/&gt;
 &lt;connections/&gt;
&lt;/ui&gt;
</code></pre>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2018-04-23 13:19 UTC)

<aside class="quote no-group" data-username="Eloise" data-post="1" data-topic="2661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eloise/48/3948_2.png" class="avatar"> Eloise:</div>
<blockquote>
<p>qSlicerModuleNameFooBarWidget</p>
</blockquote>
</aside>
<p>There is no such file in the Slicer source code. If the file is in your own module, then I would recommend to create a new module skeleton using Slicer’s Extension Wizard module and compare the differences to your own module. Or, you can have a look at <a href="https://github.com/Slicer/Slicer/commits/master/Utilities/Templates/Modules/Loadable">changes to the extension template</a> since you generated your module and apply the same changes to your module manually.</p>

---
