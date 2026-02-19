---
topic_id: 25458
title: "Where To Call Logic Functions Of Module"
date: 2022-09-28
url: https://discourse.slicer.org/t/25458
---

# Where to call logic functions of module

**Topic ID**: 25458
**Date**: 2022-09-28
**URL**: https://discourse.slicer.org/t/where-to-call-logic-functions-of-module/25458

---

## Post #1 by @michabermoy (2022-09-28 06:09 UTC)

<p>Hi, I have created my own module that displays segments. To accomplish this, I added some functions to the logic class of the module, all of which I call in the setup() function of the widget class. While this works well for most functions, I have to reload the module several times for other functions to work. For example, one of the functions I have defined resets all view and slice node FOVs. This function does not do its job at startup of the module unlike other functions, i.e. the FOVs are not reset at the start of the module. Rather, I have to hit ‘reload’ for the function to take effect and reset the FOVs. Is there a way to fix this issue for all functions? Where should I move my logic function calls so that I don’t need to repeatedly reload the module?</p>

---
