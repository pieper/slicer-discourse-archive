---
topic_id: 24913
title: "Cannot Hide Tool Bars And Module Panel"
date: 2022-08-25
url: https://discourse.slicer.org/t/24913
---

# Cannot hide tool bars and module panel

**Topic ID**: 24913
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/cannot-hide-tool-bars-and-module-panel/24913

---

## Post #1 by @nnzzll (2022-08-25 07:14 UTC)

<p>I am developing a custom app and want to hide slicer’s tool bars and module panel.<br>
Inside the <code>qXXAppMainWindowPrivate::setupUi</code> function , I added several lines at the bottom</p>
<pre><code class="lang-auto">  auto modulePanel = mainWindow-&gt;findChildren&lt;QDockWidget*&gt;();
  auto toolbars = mainWindow-&gt;findChildren&lt;QToolBar*&gt;();
  modulePanel.at(0)-&gt;setVisible(false);
  for(int i=0;i&lt;toolbars.count();i++)
  {
    toolbars.at(i)-&gt;setVisible(false);
  }
</code></pre>
<p>which should hide the module panel and toolbars, however,<br>
Every time I start the app the module panel and toolbars still exists.</p>
<p>What is the problem during startup? Since python api like <code>setToolbarsVisible</code> works fine with this.</p>
<p>Operating system: ubuntu 18.04<br>
Slicer version: v5.0.3</p>

---
