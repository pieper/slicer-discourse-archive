---
topic_id: 37733
title: "How To Pickle Mrmlcorepython Vtkmrmlscene Object"
date: 2024-08-06
url: https://discourse.slicer.org/t/37733
---

# How to pickle 'MRMLCorePython.vtkMRMLScene' object

**Topic ID**: 37733
**Date**: 2024-08-06
**URL**: https://discourse.slicer.org/t/how-to-pickle-mrmlcorepython-vtkmrmlscene-object/37733

---

## Post #1 by @alientex (2024-08-06 14:07 UTC)

<p>Hello everyone,</p>
<p>Does anyone know how to pickle an arbitrary object type like <code>MRMLCorePython.vtkMRMLScene</code> in python?</p>
<p>I am trying to start a process from the main process by passing the function <code>SaveSceneToSlicerDataBundleDirectory</code> to the <code>multiprocessing.Process</code>:</p>
<pre><code class="lang-auto">from multiprocessing import Process
f = slicer.mrmlScene.SaveSceneToSlicerDataBundleDirectory
p = Process(target=f, args=("C:/Users/Tex/Desktop/TestScene",))
p.start()
</code></pre>
<p>But I am getting the following error:</p>
<pre><code class="lang-auto">TypeError: cannot pickle 'MRMLCorePython.vtkMRMLScene' object
</code></pre>
<p>I would appreciate any help.</p>
<p>Thank you.</p>

---

## Post #2 by @alientex (2024-08-08 04:46 UTC)

<p>Can anybody please help me solve this problem?</p>

---
