---
topic_id: 19313
title: "Why Qmrmlthreedwidget Is Not Supposed To Be Inherited"
date: 2021-08-23
url: https://discourse.slicer.org/t/19313
---

# Why `qMRMLThreeDWidget` is not supposed to be inherited

**Topic ID**: 19313
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/why-qmrmlthreedwidget-is-not-supposed-to-be-inherited/19313

---

## Post #1 by @keri (2021-08-23 11:22 UTC)

<p>Hi,</p>
<p>I wanted to set custom <code>qMRMLThreeDViewControllerWidget</code> to the <code>qMRMLThreeDWidget</code> . But <code>qMRMLThreeDWidgetPrivate</code> is declared and defined within <code>qMRMLThreeDWidget.cxx</code> (i.e. there is no <code>qMRMLThreeDWidget_p.h</code> file). Also there is no protected constructor for inherited classes that follows pimpl idea.</p>
<p>Was it hidden intensionally or is it some kind of a drawback?</p>
<p>By the way the similar class <code>qMRMLSliceWidget</code> has <code>qMRMLSliceWidget_p.h</code> header and Slicer Astro uses it to add custom button.</p>

---

## Post #2 by @lassoan (2021-08-23 14:14 UTC)

<p>Keeping certain implementation details private is essential for keeping enough degree of freedom for Slicer core developers to make changes without worrying that those changes may break extensions. Pluggable interfaces are available for many things, but implementing and maintaining these interfaces takes significant effort, so they only exist if there is a strong, confirmed need.</p>
<p>qMRMLThreeDWidget is a tiny class, that it is easier for developers to clone and modify rather than implement an API in Slicer core to inject a custom view controller widget or make it usable as a base class. You can also add/remove buttons dynamically at runtime with standard Qt API. But if you have any specific suggestion for changing the API - preferably without taking on significant development effort and maintenance commitment - then let us know.</p>

---
