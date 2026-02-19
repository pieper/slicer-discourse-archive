---
topic_id: 5023
title: "Documentation Of Qt Element Connect Strings"
date: 2018-12-10
url: https://discourse.slicer.org/t/5023
---

# Documentation of qt element connect strings

**Topic ID**: 5023
**Date**: 2018-12-10
**URL**: https://discourse.slicer.org/t/documentation-of-qt-element-connect-strings/5023

---

## Post #1 by @brhoom (2018-12-10 10:47 UTC)

<p>Hi,<br>
where to find the first parameter of connect for  Qt GUI elements e.g. qt.QLineEdit(). I am using qt documentation to find them e.g. <a href="http://doc.qt.io/qt-5/qlineedit.html#textChanged" rel="nofollow noopener">this one</a> .</p>
<p>In Slicer interactor I tried:</p>
<pre><code> t = qt.QLineEdit("some text !!")     
 t.show()
 def tChg(self):
       print(t.text)
 t.connect("textChanged(str)", tChg)
</code></pre>
<p>but it didn’t work,</p>

---

## Post #2 by @brhoom (2018-12-10 10:56 UTC)

<p>It works now, my mistake. I should use QString instead of str as the documentation says.</p>

---

## Post #3 by @jamesobutler (2018-12-10 14:42 UTC)

<p>I actually prefer new-style connections which would be <code>t.textChanged.connect(tChg)</code></p>

---

## Post #4 by @jcfr (2018-12-10 16:04 UTC)

<p>Generally speaking, I would also suggest to use more explicit name for slots. Prefer <code>lineEditTextChanged</code> instead of <code>tChg</code></p>

---

## Post #5 by @brhoom (2018-12-10 17:22 UTC)

<blockquote>
<p>t.textChanged.connect(tChg)</p>
</blockquote>
<p>cool! now I know where to find these events.</p>
<blockquote>
<p>I would also suggest to use more explicit name for slots</p>
</blockquote>
<p>Sure, a code must be readable.</p>

---
