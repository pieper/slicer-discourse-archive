# Volume rendering adjusting precisely

**Topic ID**: 45182
**Date**: 2025-11-21
**URL**: https://discourse.slicer.org/t/volume-rendering-adjusting-precisely/45182

---

## Post #1 by @michaelli (2025-11-21 14:26 UTC)

<p>In volume rendering, after selecting a preset, I can drag the slider to adjust the ‘shift’ value. But I want to know how to adjust the ‘shift’ precisely?</p>

---

## Post #2 by @cpinter (2025-11-21 14:52 UTC)

<p>The question is quite broad, but when I need to adjust it “precisely”, I tend to turn to one of the two following solutions:</p>
<ol>
<li>When simply the precision of moving the mouse is not enough and I want to take smaller steps: Click on the slider and use the left and right arrow keys</li>
<li>When you have changed the shift or the transfer functions and want to be able to return to that state: save the volume property node and load it when you need the same display again</li>
</ol>

---

## Post #3 by @michaelli (2025-11-21 15:16 UTC)

<p>Thank you for the reply. It seems that the left and right arrow keys sometimes do not work. Even when they are working, a one press may be too ‘big’. Is the 'arrow’ adjusting the display at the finest level?  I’m hoping I can input the ‘threshold’ value directly.</p>

---

## Post #4 by @cpinter (2025-11-21 15:25 UTC)

<p>Well they always work for me… But if it’s too coarse for you then that’s not the way anyway.</p>
<p>Unfortunately the display settings in volume rendering are quite inconvenient. What you can try to do is going to Advanced / Volume properties, and change the node positions manually.</p>
<p>Or, you can play with this python snippet:</p>
<pre><code class="lang-auto">volRenWidget = slicer.modules.volumerendering.widgetRepresentation()
volumePropertyNodeWidget = slicer.util.findChild(volRenWidget, 'VolumePropertyNodeWidget')

volumePropertyNodeWidget.moveAllPoints(1, 0, False)
</code></pre>
<p>After having your initial volume rendering set up, paste the first two lines in the console, then paste the third one. The amount with which the “shift” will happen in this case will be 1. Feel free to change the value, and/or call the function as many times you need (up then enter) to do the shift step by step.</p>

---

## Post #5 by @Deep_Learning (2025-11-24 14:48 UTC)

<p>If using CT, you might want to check your max and min HU.  Some scanners have wide ranges…  eg max=30000.   If this is the case, you can threshold to reasonable values. This wide range can make volume rendering and masking difficult.</p>

---
