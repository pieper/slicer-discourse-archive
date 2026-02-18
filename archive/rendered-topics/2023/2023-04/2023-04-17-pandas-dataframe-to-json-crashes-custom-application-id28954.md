# Pandas dataframe .to_json() crashes Custom Application

**Topic ID**: 28954
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/pandas-dataframe-to-json-crashes-custom-application/28954

---

## Post #1 by @brandus1 (2023-04-17 08:39 UTC)

<p>Hi,</p>
<p>I have a custom app built with SlicerCustomAppTemplate (slicer 5.2.2).</p>
<p>I compiled the application on ubuntu 20.04 (docker), and a weird thing is happening.</p>
<p>calling .to_json() from any pandas dataframe crashes the application with “exit abnormally”</p>
<p>a simple example like this will crash:</p>
<p>import pandas as pd<br>
import numpy as np</p>
<p>random_table = pd.DataFrame(np.random.rand(5, 4), columns=[‘A’, ‘B’, ‘C’, ‘D’])<br>
random_table.to_json()<br>
(of course after slicer.util.pip_install(‘pandas’) resolves successfully)</p>
<p>Note that this does not crash when being executed just with PythonSlicer, but only when the app is running (headless or not). This also does not happen on stable linux Slicer downloaded from the website.</p>
<p>Downgrading pandas to older versions does not solve the issue.</p>
<p>Not sure how to debug this. Will try a debug build, but I am not sure it will catch the error when slicer exits abnormally.</p>
<p>My workaround will be to push this piece of code to a python subprocess.<br>
But if anyone has a feeling on what it might be that would be great.</p>
<p>Cheers</p>

---

## Post #2 by @pieper (2023-04-17 16:01 UTC)

<p>My guess would be that you’ve got two versions of python packages mixed in your pythonpath or similar.  Maybe run your process with strace to see what it’s doing just before it crashes.</p>

---
