# Elastix registration error

**Topic ID**: 17335
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/elastix-registration-error/17335

---

## Post #1 by @Bence_Horvath (2021-04-26 16:05 UTC)

<p>Hi,<br>
I want to registrate  preoperative CT  with  postoperative CT , but Elastix always give me this error, when try to generate output:</p>
<p>Failed to load output transform from C:/Users/HORVIR~1/AppData/Local/Temp/Slicer/Elastix/20210426_161835_807\result-resample\deformationField.mhd<br>
Error: type object ‘MRMLCorePython.vtkMRMLTransformNode’ has no attribute ‘GetMovingNodeReferenceRole’</p>
<p>How can I solve this problem?</p>
<p>Best regards!<br>
Bence</p>

---

## Post #2 by @cpinter (2021-04-26 16:14 UTC)

<p>Szia Bence,</p>
<p>Which Slicer version do you use? If not the latest preview then please install that and try again (you seem to use Windows so Elastix should be fine for that - it has issues on Mac for several weeks now).</p>

---

## Post #3 by @Bence_Horvath (2021-04-26 16:23 UTC)

<p>Hi Csaba,</p>
<p>My Slicer version is 4.10.1, I uninstall and reinstall Elastix, but the problem is remain.<br>
So maybe I schould try Slicer version 4.11. ?</p>

---

## Post #4 by @cpinter (2021-04-26 16:25 UTC)

<p>4.10.1 is two and a half years old and we made a lot of improvements and fixes since then. I suggest using at least the latest stable, which is <a href="https://download.slicer.org/bitstream/1444239">4.11.20210226</a>. We do not fix bugs in old versions, so in any case if something is broken then we will only fix it if it persists in the latest version. Thanks!</p>

---

## Post #5 by @Bence_Horvath (2021-04-26 16:58 UTC)

<p>Okey, thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
