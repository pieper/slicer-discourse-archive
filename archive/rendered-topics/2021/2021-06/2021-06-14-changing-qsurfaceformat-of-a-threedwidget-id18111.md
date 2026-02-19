---
topic_id: 18111
title: "Changing Qsurfaceformat Of A Threedwidget"
date: 2021-06-14
url: https://discourse.slicer.org/t/18111
---

# Changing QSurfaceFormat of a ThreeDWidget

**Topic ID**: 18111
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/changing-qsurfaceformat-of-a-threedwidget/18111

---

## Post #1 by @MarineC (2021-06-14 12:55 UTC)

<p>Hello everyone,</p>
<p>I am trying to show a 3D view outside the view layout, to be able to activate the QuadBuffer stereo mode on Slicer 4.13 (with VTK9). I followed <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-3d-view-outside-the-view-layout" rel="noopener nofollow ugc">this example</a> for the widget but using C++.</p>
<p>First, I created a VTK app which used <a href="https://vtk.org/doc/nightly/html/classQVTKOpenGLStereoWidget.html" rel="noopener nofollow ugc">QVTKOpenGLStereoWidget</a>  and I had to change the surface of the widget like this:</p>
<pre><code class="lang-auto">QVTKOpenGLStereoWidget widget;
QSurfaceFormat format;
format.setStereo(true);
widget.setFormat(format);
</code></pre>
<p>Or like this : <code>QSurfaceFormat::setDefaultFormat(QVTKOpenGLStereoWidget::defaultFormat(1));</code></p>
<p>With the surface like this and some others parameters for the render window it works like a charm.</p>
<p>My problem is, now that I want to do it in Slicer, I must use the class threeDWidget. However, from what I understood, I cannot change the format of the ThreeDWidget (in the class <a href="http://apidocs.slicer.org/master/classqMRMLThreeDWidget.html#aa489037124728d003ccc34b1c4207517" rel="noopener nofollow ugc">qMRMLThreeDWidget</a>), so I would like to know if there is another way for me to use the format I need. Or if I can use a Stereo widget inside Slicer rather than the threeDWidget class, so I’ll have direct access to the surface as I seen above.</p>
<p>Thank you for your help !</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2021-09-07 19:08 UTC)

<p>Have you figure this out? Have you managed to make the zspace device work in Slicer?</p>

---
