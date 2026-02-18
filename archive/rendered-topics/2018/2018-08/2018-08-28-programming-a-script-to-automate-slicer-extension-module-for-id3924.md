# Programming a script to automate Slicer Extension Module for DiceComputation (CLI)

**Topic ID**: 3924
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/programming-a-script-to-automate-slicer-extension-module-for-dicecomputation-cli/3924

---

## Post #1 by @phoenixyuwilkie (2018-08-28 13:41 UTC)

<p>Hello all,</p>
<p>I am currently trying to program a script that will automate thresholding of scalar volumes then compute the DSC values of these segmentations when compared with previously manually segmented ones. While the coding for Threshold worked seamlessly with CLI, I have been struggling to figure out the parameters for DiceComputation (the extension).</p>
<p>Documentation here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DiceComputation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DiceComputation</a></p>
<p>The script runs beautifully in Slicer from Command Line, but then gives me a NoneType object attribute error because the parameter name is clearly wrong and cannot associate with the value I give it in the code. I am convinced it is only a parameter naming problem as all of my other code works well.</p>
<p>When checking the documentation online, I couldn’t find any of the attribute names. Therefore, I have been mostly guessing them based on what I know from other CLI parameters in different modules. I have also tried looking for the original source code of DiceComputation both on GitHub as well as from my own computer after installing the module. However, while I had no luck for the former, I only found .so (compiled Shared Object files) on my computer in its directory.</p>
<p>If anyone knows what the parameters are or have worked in CLI for DiceComputation before, please let me know. All tips and tricks are warmly welcomed. I don’t know, but perhaps DiceComputation doesn’t have the capabilities for CLI?</p>
<p>Thank you,<br>
Phoenix</p>

---

## Post #2 by @Sam_Horvath (2018-08-28 14:00 UTC)

<p>The source code for the DiceComputation module is here: <a href="https://github.com/lchauvin/DiceComputation" rel="nofollow noopener">https://github.com/lchauvin/DiceComputation</a></p>
<p>This is a loadable module, not a CLI.  However, computing the Dice coefficient is implemented in the logic for the module, and so should be easily accessible through python.  See: <a href="https://discourse.slicer.org/t/help-with-accessing-module-logic-in-python-scripted-modules/409">Help with Accessing Module Logic in Python Scripted Modules</a></p>

---

## Post #3 by @phoenixyuwilkie (2018-08-28 14:03 UTC)

<p>Thank you! I will check this all out and hope it solves my problems.</p>

---

## Post #4 by @Michael_Hardisty (2018-08-28 14:09 UTC)

<p>Hi Phoenix,</p>
<p>Here is a function written for this purpose, to interact with the DiceComputation widget.</p>
<pre><code class="lang-auto">def calculateDiceCoefficient(self, inputVolume1, inputVolume2):
    dc = slicer.modules.dicecomputation.widgetRepresentation()
    dc.onLabelMapNumberChanged(2)
    # set label maps
    labelMaps = dc.findChild('ctkCollapsibleButton','LabelMapsFrame').findChildren('qSlicerDiceComputationLabelMapSelectorWidget')
    item1 = labelMaps[0].findChild('qMRMLNodeComboBox')
    item1.setCurrentNode(inputVolume1)
    item2 = labelMaps[1].findChild('qMRMLNodeComboBox')
    item2.setCurrentNode(inputVolume2)
    dc.computeDiceCoefficient()
    # get dsc
    outFrame = dc.findChild('ctkCollapsibleButton','OutputFrame')
    table = outFrame.findChild('QTableWidget','OutputResultsTable')
    dsc = float(table.item(0,1).text())

    return dsc

</code></pre>
<pre><code class="lang-auto">inputVolume1 and inputVolume2 are both label maps

</code></pre>
<pre><code class="lang-auto">Best,

</code></pre>
<pre><code class="lang-auto">Michael

</code></pre>

---

## Post #5 by @phoenixyuwilkie (2018-08-28 14:14 UTC)

<p>Thank you Michael.</p>
<p>I had tried using this in a previous iteration of the code before Threshold was working. I’ll try again.</p>
<p>Best,<br>
Phoenix</p>

---

## Post #6 by @lassoan (2018-08-28 15:13 UTC)

<p>Note that Dice metric is a very poor metric for comparing segmentations. The main issue that the value has no absolute meaning -  99% value may be unacceptably low and a 80% value may be perfectly good, depending on the shape of the compared segments. Instead, I would recommend to use Hausdorff distance as a metric. Both Dice and Hausdorff distance metrics are computed by Segment Comparison module (available in SlicerRT extension).</p>

---
