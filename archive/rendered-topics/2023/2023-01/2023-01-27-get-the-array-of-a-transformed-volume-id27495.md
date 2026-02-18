# Get the array of a transformed volume

**Topic ID**: 27495
**Date**: 2023-01-27
**URL**: https://discourse.slicer.org/t/get-the-array-of-a-transformed-volume/27495

---

## Post #1 by @rodrigo.vargas (2023-01-27 10:46 UTC)

<p>I’m trying to rotate a volume and then get the corresponding (rotated) array. I thought hardening and then using <code>util.arrayFromVolume</code> would do it, but it doesn’t (if I transform further, get again the array and compare, obtain the same result). My code is as follows:</p>
<pre><code class="lang-auto">def getTransformedVolume():
    cloned = cloneNode(volumeNode)
    cloned.SetAndObserveTransformNodeID(transformNode.GetID())
    cloned.HardenTransform()
    a = util.arrayFromVolume(cloned)
    mrmlScene.RemoveNode(cloned)
    return a

def cloneNode(node):
    itemIDToClone = shNode.GetItemByDataNode(node)
    clonedItemID = modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
    return shNode.GetItemDataNode(clonedItemID)
</code></pre>
<p>Here, <code>volumeNode</code> and <code>transformNode</code> are some global variables that I already have defined, and</p>
<pre><code class="lang-auto">shNode = vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(mrmlScene)
</code></pre>
<p>So, with that I go like this:</p>
<pre><code class="lang-auto">a = getTransformedVolume()
# modify the global transformNode
b = getTransformedVolume()
(a == b).all() # expect to get False, but it's actually True
</code></pre>
<p>How can I achieve this? Let me further note that I’m actually interested in the 2D array corresponding to a particular (transformed) slice, not actually the whole transformed volume, but was trying this approach because I couldn’t find a way to do that either. Thanks in advance for your support!</p>

---

## Post #2 by @pieper (2023-01-27 12:49 UTC)

<p>If you harden a linear transform it only changes the IJKToRAS matrix, so the pixels you get in the numpy array will be unchanged.  You’ll need to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Resampling">resample</a> the data through the transform to do this.  There are several ways to do this, but calling <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html">this CLI</a> might be the easiest, or there might be a convenience method I’m not thinking of at the moment.</p>

---

## Post #3 by @rodrigo.vargas (2023-01-27 15:30 UTC)

<p>OK. If I understand correctly, I should see that module under “all modules”, but I actually don’t have that sub-menu… I don’t have either one that, if I remember correctly, should be called “examples”, where I should be able to see the modules that the module wizard creates for me to code. What should I do to see those?</p>

---

## Post #4 by @pieper (2023-01-27 15:32 UTC)

<p>It sounds like you are using an older version of slicer.  We suggest updating to the most recent version and using the script repository and programming tutorials to get comfortable with the system to simplify the process of developing your own code.</p>

---

## Post #5 by @rodrigo.vargas (2023-01-27 15:33 UTC)

<p>I’m on 5.2.1, Ubuntu. Maybe I should reinstall, I’ll try later and let you know, thanks!</p>

---

## Post #6 by @rodrigo.vargas (2023-01-27 17:30 UTC)

<p>So, I tried version 5.3.0 and my UI looks identical. I realized though that I can use the module finder and I was able to resample the volume using the “Resample Scalar/Vector/DWI Volume” module that you suggested. I just looked at the code, but alas it’s C++ (not python). Any hint as to how I could invoke the module using python? Thanks again!</p>

---

## Post #7 by @lassoan (2023-01-28 17:57 UTC)

<p>You can use all Slicer modules in Python. Resampling module is a CLI module, you can find in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">Python FAQ how to run such module from Python</a>.</p>

---
