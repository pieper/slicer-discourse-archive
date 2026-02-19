---
topic_id: 11858
title: "Configuration Of Active Color Of Vtkslicermarkupswidgetrepre"
date: 2020-06-04
url: https://discourse.slicer.org/t/11858
---

# Configuration of active color of vtkSlicerMarkupsWidgetRepresentation

**Topic ID**: 11858
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/configuration-of-active-color-of-vtkslicermarkupswidgetrepresentation/11858

---

## Post #1 by @Fangwen_Zhai (2020-06-04 09:17 UTC)

<p>In the current implementation of vtkSlicerMarkupsWidgetRepresentation, active and invalid colors are hard coded as gray and bright green respectively. Since the selected and unselected colors of control points can be configured for each markup node, I think it is better to make them also configurable, maybe leave it as an entry in the application setting panel?</p>

---

## Post #2 by @lassoan (2020-06-05 02:22 UTC)

<p>There are already so many options to control how markups are displayed that probably exposing a few more would not make things any worse. It would be great if you could add a pull request that adds an “ActiveColor” property to vtkMRMLMarkupsDisplayNode, which is used in the displayable managers instead of a hardcoded value.</p>
<p>I’m not sure what you mean by “invalid” colors. If you mean the color that is used when no display node is generated then I think we can leave that as is. I would expect that markups would not be displayed at all without a valid display node (and if they do then it is probably a bug).</p>

---

## Post #3 by @Fangwen_Zhai (2020-06-05 02:58 UTC)

<p>Thanks for the response. I’ll be glad to add this feature when I’m free. Besides, I don’t know the usage of invalid color either and never met such condition that an invalid point appeared. I mentioned it because invalidColor is defined in the code.</p>

---
