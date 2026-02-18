# Sphere brush via script

**Topic ID**: 9066
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/sphere-brush-via-script/9066

---

## Post #1 by @Amine (2019-11-07 18:20 UTC)

<p>Hi, i can’t find the script to switch to sphere brush (or edit in 3d views as well),<br>
i tried this but it doesen’t seem to work:</p>
<blockquote>
<pre><code>    import EditorLib
    paramnode = EditorLib.EditUtil.EditUtil().getParameterNode()
    paramnode.SetParameter('PaintEffect,sphere', '1')
</code></pre>
</blockquote>
<p>Thanks for any inputs</p>

---

## Post #2 by @lassoan (2019-11-07 19:00 UTC)

<p>Please do not use the legacy Editor module but switch to Segment Editor module. Parameter names controlling paint effect are described <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.cxx#L1478-L1487">here</a>. Examples of scripting Segment Editor effects are available <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a>.</p>

---

## Post #3 by @Amine (2019-11-07 21:02 UTC)

<p>Thanks, that worked well, however i got another problem while using this to enable sphere brush; the checkbox on Segment Editor gets “stuck” and doesen’t work as a switch anymore:</p>
<blockquote>
<pre><code>editor = slicer.modules.segmenteditor.widgetRepresentation().self().editor
paint = editor.effectByName("Paint")
paint.setParameter("BrushSphere", 1)
</code></pre>
</blockquote>

---

## Post #4 by @lassoan (2019-11-07 21:05 UTC)

<p>As you can see in the code that I linked above, BrushSphere is a “common” parameter (so that the same setting can be used in paint and erase effects) and has to be set accordingly using <code>setCommonParameter</code>. Using <code>setParameter</code> would override the parameter value for a particular effect and so Segment Editor module GUI (that adjusts the common parameter value) would not have an effect anymore.</p>

---

## Post #5 by @Amine (2019-11-07 21:09 UTC)

<p>Thanks a lot, it works fine.</p>

---
