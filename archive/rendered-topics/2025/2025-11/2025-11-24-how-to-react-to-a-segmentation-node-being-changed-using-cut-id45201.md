# How to react to a segmentation node being changed using cut, erase, paint?

**Topic ID**: 45201
**Date**: 2025-11-24
**URL**: https://discourse.slicer.org/t/how-to-react-to-a-segmentation-node-being-changed-using-cut-erase-paint/45201

---

## Post #1 by @Victor_Wayne (2025-11-24 04:32 UTC)

<p>Hello,</p>
<p>How can I react to a segmentation node being changed using the cut, erase and paint capabilities of the segmentation extension? At first I tried to attach <code>slicer.vtkMRMLSegmentationNode.SegmentationChangedEvent</code> this event to the segmentation node and tried to react to it but whenever I changed the segment the control did not go inside my function to react to it. And after that I tried using <code>vtk.vtkSegmentation.SourceRepresentationModified</code>, event but this also so did not work. Is the problem is in my code and one of the above mentioned event is the correct one to use? Or is it totally a different event to react to?</p>
<p>Thank you for your help.</p>

---

## Post #2 by @pieper (2025-11-24 04:58 UTC)

<p>Looks like you need something like:</p>
<pre><code class="lang-auto">segmentationNode.GetSegmentation().AddObserver(slicer.vtkSegmentation.RepresentationModified, print)
</code></pre>

---

## Post #3 by @Victor_Wayne (2025-11-24 05:02 UTC)

<p>I just tried it. and I also tired <code>SourceRepresentationModified</code> too. Both of them did not work.</p>
<pre data-code-wrap="python"><code class="lang-python">            # --- Snip ----

            self.targetSegementationNode.GetSegmentation().AddObserver(
                slicer.vtkSegmentation.RepresentationModified,
                self.onSegmentModified
            )
            
            self.segmentBtn.setEnabled(False)
            self.cancelPreviewBtn.setEnabled(False)
            self.previewBtn.setEnabled(False)

            # Disable undo
            disableShortcut("Ctrl+z")
            
        except Exception as e:
            slicer.util.errorDisplay(f"Error - {e}")
            traceback.print_exc()

    def onSegmentModified(self, caller, event):
        """
        Callback for when the segmentation is modified (Paint/Erase/Cut).
        """
        print("Segment content changed (Erase/Paint detected)!")
</code></pre>
<p>When I used the cut tool it did not print.</p>

---

## Post #4 by @pieper (2025-11-24 05:09 UTC)

<p>Try something simple and it should work.  I just have one segmentation and when I use the code I pasted I get a print when I use the paint effect on the segmentation.  Try to debug in the python console before using the approach in more complex code so that you are confident you know a certain call will work.</p>

---

## Post #5 by @Victor_Wayne (2025-11-24 05:55 UTC)

<p>Thanks for the solution. It worked.</p>

---
