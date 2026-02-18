# Customizing Slicer 3d toolbar

**Topic ID**: 13545
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/customizing-slicer-3d-toolbar/13545

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-18 13:24 UTC)

<p>How to customize slicer in-built toolbar?<br>
I want to hide some in=built buttons in toolbar and add custom buttons into it?</p>

---

## Post #2 by @lassoan (2020-09-18 13:41 UTC)

<p>In general, you would hide all toolbars except your custom toolbar, using <code>slicer.util.setToolbarsVisible(False, [myToolbar1, myToolbar2])</code>. You can add your custom toolbar and actions to it using standard Qt calls.</p>

---

## Post #3 by @Chintha_Siva_Prasad (2020-09-18 14:08 UTC)

<p>Can I hide certain widgets like(marksups) in the built-in toolbar,without hiding the whole toolbar I just want to hide some of them?</p>

---

## Post #4 by @lassoan (2020-09-18 14:14 UTC)

<p>This is all just standard Qt API, so you should find answers by googling <code>qt hide toolbar button</code>. If you have any specific issue then let us know.</p>

---

## Post #5 by @Chintha_Siva_Prasad (2020-09-18 14:19 UTC)

<p>How can I get the toolbar instances?</p>

---

## Post #6 by @jamesobutler (2020-09-18 14:59 UTC)

<p>This would also be part of standard Qt API. Widgets have children and parents.  So you will need to familiarize yourself with <a href="https://doc.qt.io/qt-5/qobject.html#findChild" rel="noopener nofollow ugc">https://doc.qt.io/qt-5/qobject.html#findChild</a> and <a href="https://doc.qt.io/qt-5/qobject.html#findChildren" rel="noopener nofollow ugc">https://doc.qt.io/qt-5/qobject.html#findChildren</a> type calls for finding various Qt objects through the application.</p>

---

## Post #7 by @Xiaojie_Guo (2026-01-30 03:56 UTC)

<pre><code class="lang-auto">import slicer

mainToolBar = slicer.util.findChild(slicer.util.mainWindow(), 'ModuleToolBar')

allActions = mainToolBar.actions()

for action in allActions:
    if action.text == 'Markups':
        actionWidget = mainToolBar.widgetForAction(action)
        if actionWidget:
            actionWidget.setVisible(False)
            print('success')
</code></pre>
<p>I use these codes to hide 'Markups" in toolbar. It does not work. What is wrong?</p>

---

## Post #8 by @Xiaojie_Guo (2026-01-30 06:15 UTC)

<p>Got it. I found the wrong toolbar.</p>

---
