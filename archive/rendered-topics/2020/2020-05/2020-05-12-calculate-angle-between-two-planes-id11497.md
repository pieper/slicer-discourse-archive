---
topic_id: 11497
title: "Calculate Angle Between Two Planes"
date: 2020-05-12
url: https://discourse.slicer.org/t/11497
---

# Calculate angle between two planes

**Topic ID**: 11497
**Date**: 2020-05-12
**URL**: https://discourse.slicer.org/t/calculate-angle-between-two-planes/11497

---

## Post #1 by @syh91006 (2020-05-12 03:09 UTC)

<p>Operating system:  windows 10<br>
Slicer version:  version 4.11.0 revision 29053 built 2020-05-11<br>
Expected behavior: calculate angle between two planes<br>
Actual behavior:<br>
After I used extensions manager installing “AnglePlanesExtension”<br>
AnglePlanesExtension did not show up in modules, even after I restarted the 3d slicer</p>
<p>And this is show in my Python interactor<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\syh\AppData\Local\NA-MIC\Slicer 4.11.0-2020-04-10\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/syh/AppData/Roaming/NA-MIC/Extensions-28945/AnglePlanesExtension/lib/Slicer-4.11/qt-scripted-modules/AnglePlanes.py”, line 73<br>
print “-------Angle Planes Widget Setup-------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Angle Planes Widget Setup-------")?</p>
<p>what’s wrong ?   or Is there other way to calculate angle between two planes?</p>
<p>Thx a lot.</p>

---

## Post #2 by @lassoan (2020-05-12 03:29 UTC)

<p>Probably the AnglePlanesExtension has not been updated to work with latest Slicer version.</p>
<p>While that’s being fixed, you can measure angle between two planes by copy-pasting scripts into the Python console:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_markup_planes">measure angle between two markup planes</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes">measure angle between two slice planes</a></li>
</ul>

---

## Post #3 by @syh91006 (2020-05-12 04:03 UTC)

<p>thanks a lot!!  really helpful!</p>
<p>Is there any scripts can calculated angle between two markup lines?<br>
I know there is is an “angle” tool in “create and place”, but I would like to measure angle between two markup lines.  It’s slightly different. Thanks again.</p>

---

## Post #4 by @lassoan (2020-05-12 19:03 UTC)

<p>I’ve added one more example:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_markup_lines">measure angle between two markup lines</a></li>
</ul>

---

## Post #5 by @syh91006 (2020-05-14 01:47 UTC)

<p>Thank you very much!!</p>

---
