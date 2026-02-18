# Access to a loadable module from the python console

**Topic ID**: 1038
**Date**: 2017-09-11
**URL**: https://discourse.slicer.org/t/access-to-a-loadable-module-from-the-python-console/1038

---

## Post #1 by @laurapascal (2017-09-11 22:31 UTC)

<p>Hi everyone!</p>
<p>I am trying to create a scripted module using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences" rel="nofollow noopener">Sequences</a> extension. I was wondering if, from the python console, there is a way to use a loadable module in the same way than a CLI (<code>slicer.cli.run(slicer.modules.&lt;cli-module-name&gt;,parameters)</code>), or if there is a way to access the interface in order to specify the inputs and click on the buttons in the same way than a scripted module (<code>slicer.modules.&lt;scripted-module-name&gt;Widget</code>) ?</p>
<p>Any help will be appreciated! Thanks in advance!<br>
Laura</p>

---

## Post #2 by @lassoan (2017-09-11 23:19 UTC)

<p>All classes of Sequences extension are available in Python. Sequence registration module is a good example showing how to create and manipulate sequences: <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py">https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py</a></p>

---

## Post #3 by @dpgood (2017-09-26 21:52 UTC)

<p>Try this: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_access_a_scripted_module_from_python_scripts" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Python scripting - Slicer Wiki</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/2485d26919316b1d80aa60f5ca8e2cb5bc0275fe.jpg" width="45" height="45"></p>

---

## Post #4 by @laurapascal (2017-10-03 14:53 UTC)

<p>Thank you so much for your help. I managed to create a sequence and to run it by using the <em>vtkMRMLSequenceNode</em> and <em>vtkMRMLSequenceBrowserNode</em> classes ! I have unfortunately an issue about these particular classes, so I opened another topic <a href="https://discourse.slicer.org/t/modification-of-models-color-in-a-vtkmrmlsequencenode/1166">here</a>.</p>

---
