---
topic_id: 32008
title: "Resample Scalar Volume Automatization"
date: 2023-10-03
url: https://discourse.slicer.org/t/32008
---

# Resample Scalar Volume Automatization

**Topic ID**: 32008
**Date**: 2023-10-03
**URL**: https://discourse.slicer.org/t/resample-scalar-volume-automatization/32008

---

## Post #1 by @bserrano (2023-10-03 09:08 UTC)

<p>Hi all,</p>
<p>I am attempting to automate a volume resampling process using the <code>reslice</code> function. The issue I am encountering is that the resampling process takes a few seconds (approximately 20 seconds), and I need the code to wait until this process finishes. To address this, I have implemented the <code>waitUntilReslice</code> function. However, I seem to be encountering problems with the resampling status; it never changes to “Completed,” regardless of how long I wait. It consistently remains in the “Completing” state.</p>
<p>Following the resampling process, I also need to adjust the window level. However, I am encountering a “NoneType” error for the “reslicedVolumeNode.” Does anyone have any suggestions on how I can resolve this issue?</p>
<p>Code:</p>
<pre><code class="lang-auto">def waitUntilReslice(timeout, res, period=0.25):
  mustend = time.time() + timeout

  while time.time() &lt; mustend:
    if (res.GetStatusString() == 'Completed') or \
        (res.GetStatusString() == 'Completing'): # I want to use only "Completed"
        print(res.GetStatusString())
        return True
    time.sleep(period)
  return False

def reslice(volumeNode, resolution=0.25, name='resliced'):
    
    global res

    reslicedVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", name)
    parameters = {
        "outputPixelSpacing":"{:},{:},{:}".format(*[resolution]*3),
        "InputVolume":volumeNode.GetID(),
        "interpolationMode":'bspline',
        "referenceVolume": volumeNode.GetID(),
        "OutputVolume":reslicedVolumeNode.GetID()}
    
    res = slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)
    
    waitUntilReslice(60, res)
    
    # reslicedVolumeNode = slicer.util.getNode(name)
    
    if(not reslicedVolumeNode == None):
           reslicedVolumeNode.GetDisplayNode().SetAutoWindowLevel(0)
           reslicedVolumeNode.GetDisplayNode().SetWindowLevel(800,100)

    return reslicedVolumeNode
</code></pre>
<p>Thanks,</p>
<p>Belén</p>

---

## Post #2 by @pieper (2023-10-03 22:52 UTC)

<p>One option is to use the <code>runSync</code> option like in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">this example</a>.</p>
<p>Or you can observe the node for changes like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#running-cli-in-the-background">this one</a>.</p>
<p>It’s always best to avoid using sleep for things like this.  If you do need time-based processing, it’s better to use QTimer since it works with the Slicer event loop.</p>

---

## Post #3 by @bserrano (2023-10-06 08:36 UTC)

<p>Solved with runSync. Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @bserrano (2023-10-24 14:42 UTC)

<p>Hi,</p>
<p>I have a similar issue regarding the “wait” topic. I want the program to stop until the user presses some key.</p>
<p>Example:</p>
<pre><code class="lang-auto">...
# Ask the user to segment 
print("Now segment the teeth...")

# Wait until the user has segmented and continue the execution
while(key "y" not pressed):
     wait
</code></pre>
<p>Now what I’m doing is:</p>
<pre><code class="lang-auto"># Ask the user to segment 
input("Now segment the teeth and press key to continue...")
</code></pre>
<p>But this implies that the user has to go back to the python interactor and I want to avoid this.</p>
<p>I was thinking about using something with the below code. But still don’t know how to wait in the code.</p>
<pre><code class="lang-auto">import qt
import slicer

def moveForward():
    print("Continue pressed")
    continueVariable = True
        
shortcut1 = qt.QShortcut(slicer.util.mainWindow())
shortcut1.setKey(qt.QKeySequence("y"))
shortcut1.connect( 'activated()', moveForward)
</code></pre>
<p>How can I wait until a key is pressed?</p>

---
