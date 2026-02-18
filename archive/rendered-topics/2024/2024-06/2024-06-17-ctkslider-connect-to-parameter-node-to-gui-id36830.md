# Ctkslider connect to parameter node to GUI

**Topic ID**: 36830
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/ctkslider-connect-to-parameter-node-to-gui/36830

---

## Post #1 by @park (2024-06-17 08:14 UTC)

<p>Hi all,</p>
<p>I would like to connect ctksliderwidget to GUI using the parameter node.<br>
Could you find the error in my codes?</p>
<pre><code class="lang-auto">@parameterPack
class SliderRange:
    Minimum: float
    Maximum: float
    Value: float

@parameterNodeWrapper
class ModulesParameterNode:

    # GUIs
    frameSliderValue: SliderRange
    thicknessSliderValue: SliderRange  
    

self.mapping = {
    "frameSliderValue": self.widget.frameSlider,
    "thicknessSliderValue": self.widget.projectionSlider,
}


self._parameterNodeGuiTag = self._parameterNode.connectParametersToGui(self.mapping)
</code></pre>

---

## Post #2 by @pieper (2024-06-19 17:25 UTC)

<p>It could help if you provided this in the form of a complete example that can easily be tested.  I.e. the minimum reproducible example that illustrates the question.  (At least I think that would help - I haven’t use the parameter nodes so I don’t know the answer myself).</p>

---
