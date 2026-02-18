# Corner Annotations multiple texts

**Topic ID**: 18434
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/corner-annotations-multiple-texts/18434

---

## Post #1 by @seanchoi0519 (2021-06-30 15:01 UTC)

<p>Would there be any way for me to add 2 texts in the lower middle of the view? I know that the code for adding a line of text is:</p>
<pre><code>self.view = slicer.app.layoutManager().threeDWidget(0).threeDView()
self.view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.LowerEdge,'Text')
#I'd like to create another textbox at the exact same location
self.view.cornerAnnotation().GetTextProperty().SetColor(255,255,255)
self.view.forceRender()
</code></pre>
<p>I’m asking as I’d like to assign an animation that fades in 1 text while fading out another text.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-07-02 03:47 UTC)

<p>You can fade out the old text and <em>then</em> fade in the new text (using <code>view.cornerAnnotation().GetTextProperty().SetOpacity(...)</code>).</p>

---

## Post #3 by @seanchoi0519 (2021-07-02 07:56 UTC)

<p>Resolved. Thank you!</p>

---
