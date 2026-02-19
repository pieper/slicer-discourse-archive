---
topic_id: 8231
title: "Qt Enum Access From Slicer Using Python"
date: 2019-08-29
url: https://discourse.slicer.org/t/8231
---

# Qt enum access from Slicer using Python?

**Topic ID**: 8231
**Date**: 2019-08-29
**URL**: https://discourse.slicer.org/t/qt-enum-access-from-slicer-using-python/8231

---

## Post #1 by @mikebind (2019-08-29 20:55 UTC)

<p>I’m working on a custom module and want to use a QTableWidget filled with QTableWidgetItems.  I have that working, but as I work on it, I keep coming across Qt enums being used to set various policies or flags.  For example, to control how QTableWidgetItems can be interacted with, I need to use QTableWidgetItems.setFlags().  Qt documentation examples explain that this function takes a logical combination of enums like this</p>
<pre><code class="lang-auto">QTableWidgetItem *item = new QTableWidgetItem();
item-&gt;setFlags(Qt::ItemIsSelectable|Qt::ItemIsEnabled);
</code></pre>
<p>Is there any way to access these enums from a python slicer module?  My workaround is currently to dig in the Qt documentation to find out what integers the enums correspond to (e.g. <a href="https://doc.qt.io/qt-5/qt.html#ItemFlag-enum" rel="nofollow noopener">https://doc.qt.io/qt-5/qt.html#ItemFlag-enum</a>) and use that number.  So far, that works fine, but is much uglier and less clear than the named enum approach.</p>
<p>The equivalent version I have working is</p>
<pre><code>item = qt.QTableWidgetItem()
item.setFlags(33) # 33 because selectable is 1 and enabled is 32 and to combine them you add them up
</code></pre>
<p>I’ve tried searching the slicer source on github and exploring the autocomplete methods and properties under qt.Q… and a couple qt.QAbstract… classes, but have not found any leads.  Some of these enums show up in .ui files, but not in anything python that I’ve found. Thanks for any help you can provide.</p>

---

## Post #2 by @Sunderlandkyl (2019-08-29 21:09 UTC)

<p>Yes, you can access the enums in the Qt namespace like this:</p>
<pre><code>qt.Qt.ItemIsEnabled</code></pre>

---

## Post #3 by @mikebind (2019-08-29 22:05 UTC)

<p>Thank you!  I felt like there should be something like that, but did not find it!</p>

---
