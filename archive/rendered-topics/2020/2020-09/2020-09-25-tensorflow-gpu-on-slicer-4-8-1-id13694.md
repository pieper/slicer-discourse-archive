# Tensorflow-gpu on Slicer 4.8.1

**Topic ID**: 13694
**Date**: 2020-09-25
**URL**: https://discourse.slicer.org/t/tensorflow-gpu-on-slicer-4-8-1/13694

---

## Post #1 by @luigi-palladino (2020-09-25 09:34 UTC)

<p>Hi,</p>
<p>is it possible to install tensorflow-gpu on slicer 4.8.1 on Windows 10?</p>
<p>Slicer 4.8.1 has python 2.7 as backend and according to <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/2">this discussion</a> it shouldn’t be possible:</p>
<blockquote>
<p>“On windows, it will currently work only for <em>pure</em> python wheels because the official package for python 2.7 are built with a compiler than the one used for the official wheels”.</p>
</blockquote>
<p>Is this true? Are there any workarounds known?</p>
<p>Thank you for your attention.</p>
<p>P.s.<br>
I was able to install other packages like Keras and other “pure python wheels”, but tensorflow doesn’t seem to be one of those.<br>
Changing Slicer version to nightly doesn’t seem to be a viable solution for me since I need some OpenIGTLink features which were not ported to Slicer 4.11 yet.</p>

---

## Post #2 by @jamesobutler (2020-09-25 11:43 UTC)

<p>I really would not suggest going down this method of trying to get tensorflow-gpu into Slicer 4.8.1. This will ultimately require you to build Slicer 4.8.1 from source and also tensorflow-GPU from source, but even then there is likely lacking support for a version that can be built with Visual Studio 2013 as would be required. I believe the latest tensorflow is also Python 3 only as most packages have dropped python 2 support since it went EOL finally on January 1st 2020. So even then you wouldn’t be able to use the current tensorflow in anything other than Slicer 4.11 which uses Python 3.</p>
<p>Instead your effort is best worthwhile changing your logic to use a different event if you are waiting for the ReceiveEvent for OpenIGTLinkIF to be restored.</p>
<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="13387">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtksliceropenigtlinkifmodulemrmlpython-vtkmrmligtl-has-no-attribute-receiveevent/13387/2">'vtkSlicerOpenIGTLinkIFModuleMRMLPython.vtkMRMLIGTL' has no attribute 'ReceiveEvent'</a></div>
<blockquote>
<p>Probably the events were not migrated with the rest of the functionality. I’ll let you know when I’ve re-added the events.</p>
</blockquote>
</aside>
<p>Slicer 4.11 preview uses Python 3 with modern compilers so there shouldn’t be any issue installing tensorflow-gpu. The OpenIGTLinkIF module is available within the <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="noopener nofollow ugc">SlicerOpenIGTLink</a> extension if you would like to check out the latest code.</p>

---

## Post #3 by @luigi-palladino (2020-09-25 13:03 UTC)

<p>I accept your suggestion. I’ll probably try to do as you said and try to use a different event while I wait that ReceiveEvent is migrated aswell.</p>
<p>Thank you very much for your answer!</p>

---

## Post #4 by @lassoan (2020-09-25 14:05 UTC)

<p>Adding the receive event should not be hard, it would be nice if you could implement it (you can ask advice from <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>).</p>

---
