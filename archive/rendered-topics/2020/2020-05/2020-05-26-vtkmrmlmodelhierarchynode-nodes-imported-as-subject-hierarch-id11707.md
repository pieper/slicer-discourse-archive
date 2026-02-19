---
topic_id: 11707
title: "Vtkmrmlmodelhierarchynode Nodes Imported As Subject Hierarch"
date: 2020-05-26
url: https://discourse.slicer.org/t/11707
---

# vtkMRMLModelHierarchyNode nodes imported as subject hierarchies

**Topic ID**: 11707
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/vtkmrmlmodelhierarchynode-nodes-imported-as-subject-hierarchies/11707

---

## Post #1 by @RafaelPalomar (2020-05-26 09:24 UTC)

<p>Hello,</p>
<p>I create a model hierarchy (based on vtkMRMLModelHierarchyNode objects) and save the mrml scene. When I open that scene, the model hierarchy has been turned into a subject hierarchy. Is that the expected behaviour?</p>
<p>Thanks you in advance.</p>

---

## Post #2 by @cpinter (2020-05-26 09:41 UTC)

<p>Yes, model hierarchies are considered to be deprecated, as specified in the Slicer 5 <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Model_Hierarchies">roadmap</a>.</p>
<p>We added all model hierarchy features in the subject hierarchy folder items. Please use those instead.</p>

---

## Post #3 by @RafaelPalomar (2020-05-26 10:50 UTC)

<p>Hello <a class="mention" href="/u/cpinter">@cpinter</a>, thanks for the reply.</p>
<p>I guess this opens the related question <a href="https://discourse.slicer.org/t/passing-hierarchies-to-clis/11706" class="inline-onebox">Passing hierarchies to CLIs</a>. Any clue?</p>

---
