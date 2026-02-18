# Passing hierarchies to CLIs

**Topic ID**: 11706
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/passing-hierarchies-to-clis/11706

---

## Post #1 by @RafaelPalomar (2020-05-26 09:20 UTC)

<p>Hello.</p>
<p>I’m trying to develop a CLI module which takes a set of models as input and gives a set of models as output. It seems to be possible to use vtkMRMLModelHierarchy nodes for this, but is it possible to use vtkMRMLSubjectHierarchy nodes instead?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @cpinter (2020-05-26 11:19 UTC)

<p>First, I’d like to clarify something from the question that is incorrect. We cannot use vtkMRMLSubjectHierarchy nodeS, because subject hierarchy node is (now in its 2.0 form) a singleton, and contains the whole hierarchy. The elements in subject hierarchy are called items, and are internal to the one node. So making it work with CLIs the same way the old fashioned hierarchy nodes worked is not possible.</p>
<p>Unfortunately CLI support of subject hierarchy in this sense is not implemented yet (what is implemented is that it can put outputs to the same folder as the input was). One solution I can imagine for now is adding an application setting for skipping the auto-conversion from hierarchy nodes to SH items. What do you think <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> ?</p>

---

## Post #3 by @jcfr (2020-05-26 13:39 UTC)

<p>I added this as a discussion topic for the upcoming hangout, see <a href="https://discourse.slicer.org/t/2020-05-26-hangout/11700" class="inline-onebox">2020.05.26 Hangout</a></p>

---
