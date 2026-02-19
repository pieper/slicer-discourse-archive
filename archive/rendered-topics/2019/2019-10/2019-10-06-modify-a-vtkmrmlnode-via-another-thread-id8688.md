---
topic_id: 8688
title: "Modify A Vtkmrmlnode Via Another Thread"
date: 2019-10-06
url: https://discourse.slicer.org/t/8688
---

# Modify a vtkMRMLNode via another thread

**Topic ID**: 8688
**Date**: 2019-10-06
**URL**: https://discourse.slicer.org/t/modify-a-vtkmrmlnode-via-another-thread/8688

---

## Post #1 by @danial (2019-10-06 18:14 UTC)

<p>Operating system: macOS 10.14.6<br>
Slicer version: 4.10.2</p>
<p>I want to simulate respiratory motion on another thread via QTimer. I did it like this :</p>
<p><code>connect(processTimer, &amp;QTimer::timeout, [=]() {breathingProcess();});</code></p>
<pre><code>void qSlicerSimulationModuleWidget::breathingProcess()
{
    // if theres is no current animation (mutex is a kind of thread safe guard)
    if (mutex-&gt;tryLock())
    {

        int index = 0;

        generateFactor();

        // For each node in the movement data base
        for(std::vector&lt;std::pair&lt;vtkMRMLNode*, int&gt;&gt;::const_iterator itS = organType.begin(); itS != organType.end(); itS++)
        {
            vtkSmartPointer&lt;vtkPolyData&gt; input = vtkMRMLModelNode::SafeDownCast((*itS).first)-&gt;GetPolyData();

            vtkIdType numberOfPoints = input-&gt;GetNumberOfPoints();

            // According to the type of the organ, apply the right movement
            switch((*itS).second){
            case 0 :
                // Liver, Spleen, Pancreas
                BreathingSimulation::move_liver_like(input, numberOfPoints, factor, translation.x(),  translation.y(), translation.z(), translationFactor.x(), translationFactor.y(), translationFactor.z());
                break;
            case 4 :
                // Ribs
                BreathingSimulation::move_ribs(input, numberOfPoints, factor, translation.x(),  translation.y(), translation.z(), translationFactor.x(), translationFactor.y(), translationFactor.z());
                break;
            default:
                // Default
                // Do nothing
                break;
            }

            // Refresh display and view
            (*itS).first-&gt;Modified();
        }
        mutex-&gt;unlock();
    }
}
</code></pre>
<p>But it would not display the modifications in Viewer. Can you help me to modify nodes regularly, please ?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2019-10-06 18:33 UTC)

<p>You can compute the updated polydata on a background thread but you need to update the model node (by deep or shallow copy) from the main thread from a timer callback.</p>

---
