---
topic_id: 20255
title: "How To Set The Customized Layout Whenever I Switch To The De"
date: 2021-10-20
url: https://discourse.slicer.org/t/20255
---

# How to set the customized layout whenever I switch to the developed module?

**Topic ID**: 20255
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/how-to-set-the-customized-layout-whenever-i-switch-to-the-developed-module/20255

---

## Post #1 by @wpgao (2021-10-20 04:51 UTC)

<p>Hi Guys,</p>
<p>I had defined a customized layout with a module. When the module was activated, the layout work. However, after I switch to other module and then get back, the customized layout doesn’t work. So how to  set the customized layout whenever I switch to this module. I think there should be a function to realize it but I have no idea about that. Any suggestion?<br>
Thanks</p>
<p>Wenpeng</p>

---

## Post #2 by @lassoan (2021-10-20 05:01 UTC)

<p>If you mean that you have <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">registered a custom view layout</a> then you should register it in the application startup completed signal handler and not re-register it again if you enter the module.</p>

---
