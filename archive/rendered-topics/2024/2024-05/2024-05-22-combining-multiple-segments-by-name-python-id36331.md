# Combining multiple segments by name (python)

**Topic ID**: 36331
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/combining-multiple-segments-by-name-python/36331

---

## Post #1 by @rkraaijveld (2024-05-22 16:44 UTC)

<p>Hi!</p>
<p>Whenever I have my segmentations for several organs, such as Liver, Lungs, Kidney, I tend to split them into the connected components. I want to make an additional button in the Segment Editor where after splitting them into connected components, that I also am able to combine them.</p>
<p>For example, Lungs and Lungs_2 will become Lungs, Kidney and Kidney_2 will become Kidney etc.</p>
<p>This is what I’ve tried so far and it hasnt worked, can someone help out?</p>
<p>Below, organ_segments is simply:<br>
{Lungs: [“Lungs”, “Lungs_2”], Kidney: [“Kidney”, “Kidney_2”], Liver: [“Liver”]}</p>
<pre><code class="lang-auto">segmentation_node = self.editor.segmentationNode()

 self.editor.setActiveEffectByName("Logical operators")
 effect = self.editor.activeEffect()


 for organ in segmented_organs:
            main_segment = organ
            for segment in organ_segments[organ]:
                if segment != organ:
                    self.editor.setCurrentSegmentID(main_segment)
                    effect.setParameter("Operation", "UNION")
                    effect.setParameter("ModifierSegmentID", segment)
                    effect.self().onApply()
                    
                    print("combined:", segment, organ)
                    segmentation_node.RemoveSegment(segment)




</code></pre>

---

## Post #2 by @mikebind (2024-05-22 19:09 UTC)

<p>You may be running into the fact that the segmentID is not always the same as the segment name, depending on how it was created. This can be a bit confusing because the segmentID is just another string, and it often does coincide with the segment name. However, I think segmentIDs must always be unique within a segmentation, whereas segment names are allowed to be nonunique. Try modifying your code to explicitly get and use the segment IDs rather than relying on the assumption that the segment ID is the same as the segment name.  You can get the segment ID from the name using <code> segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(segment_name)</code><br>
For example, you could change the line getting the main segment id to read <code>main_segment_id = segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(organ)</code></p>

---

## Post #3 by @rkraaijveld (2024-05-23 07:07 UTC)

<p>Okay, thanks for the tips!</p>
<p>Maybe I’m missing something but when I add in your suggestion I seem to be getting a different error. This is the code:</p>
<pre><code class="lang-auto">for organ in segmented_organs:
            main_segment = segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(organ)
            
            for segment in organ_segments[organ]:
                if segment != organ:
                    segment_id = segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(segment)
                    
                    self.editor.setCurrentSegmentID(main_segment)
                    self.editor.setActiveEffectByName("Logical operators")
                    effect = self.editor.activeEffect()
                    effect.setParameter("ModifierSegmentID", segment_id)
                    effect.setParameter("Operation", "UNION")
                    effect.setParameter("BypassMasking", 1)
                    effect.self().onApply()
</code></pre>
<p>I still get the error: [Python] Operation UNION requires a selected modifier segment</p>
<p>Do you have any suggestions? Thanks in advance!</p>

---

## Post #4 by @mikebind (2024-05-23 15:23 UTC)

<p>Give this a try:</p>
<pre><code class="lang-auto">for organ in segmented_organs:
            main_segment_id = segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(organ)
            
            for segment in organ_segments[organ]:
                segment_id = segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(segment)
                if segment_id != main_segment_id:
                    self.editor.setCurrentSegmentID(main_segment_id)
                    self.editor.setActiveEffectByName("Logical operators")
                    effect = self.editor.activeEffect()
                    effect.setParameter("ModifierSegmentID", segment_id)
                    effect.setParameter("Operation", "UNION")
                    effect.setParameter("BypassMasking", 1)
                    effect.self().onApply()
</code></pre>
<p>It just finishes the process of using segment IDs instead of names.  Possibly, you were running into the error when the current segment and the modifier segment were the same.  If this doesn’t work, then the error is due to something else.</p>

---

## Post #5 by @rkraaijveld (2024-05-24 07:35 UTC)

<p>Perfect!! This works, thanks!!</p>

---

## Post #6 by @Hamburgerfinger (2025-07-13 01:55 UTC)

<p>I am using Slicer 5.4.0 and can’t get this to work…  I started creating a python function that looks like so:</p>
<p>def combine_segments(“segmentation_name”, [“first_segment”, “second_segment”, “third_segment”, …], “combined_segment_name”):<br>
code to combine the segments</p>
<p>Any help appreciated!</p>

---

## Post #7 by @cpinter (2025-07-28 13:47 UTC)

<p>I cannot really help with 5.4 specific issues, but if you explain how it does not work then I can probably make suggestions. Are you getting an error message in the console when running the script?</p>

---
