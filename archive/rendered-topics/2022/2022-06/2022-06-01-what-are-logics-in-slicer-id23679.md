# What are 'logics' in Slicer

**Topic ID**: 23679
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/what-are-logics-in-slicer/23679

---

## Post #1 by @gzt036 (2022-06-01 21:55 UTC)

<p>I am new to Slicer and I am confused with the class names, could someone help to explain what is ‘loadable’, what is ‘logics’ in plain language? I mean, what is the idea using ‘Logics’ as class name?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2022-06-01 22:05 UTC)

<p>PerkLab has a Slicer bootcamp that has materials that could be helpful for you. Download the <a href="https://github.com/PerkLab/PerkLabBootcamp/raw/master/Doc/day3_2_SlicerProgramming.pptx" rel="noopener nofollow ugc">day3_2_SlicerProgramming</a> powerpoint.</p>
<p>The “loadable” part is likely referring to the fact that the these modules are “loaded” whenever Slicer is started. Modifying these modules would require restarting Slicer to re-load the modules. The various module types are explained in more detail in the linked PerkLab powerpoint.</p>
<p>“Logic” is referring to everything that is not user interface related. It is the internal processing for a module. More is explain in the linked PerkLab powerpoint.</p>

---
