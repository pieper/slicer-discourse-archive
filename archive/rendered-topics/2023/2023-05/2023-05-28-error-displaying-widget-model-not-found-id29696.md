# Error displaying widget: model not found

**Topic ID**: 29696
**Date**: 2023-05-28
**URL**: https://discourse.slicer.org/t/error-displaying-widget-model-not-found/29696

---

## Post #1 by @morning_jade (2023-05-28 12:06 UTC)

<p>When I use jupyter to run code： slicernb. ViewInteractiveWidget()，Widget failed to load and reported an error<br>
<strong>Error displaying widget: model not found</strong><br>
and 3d slicer shows error</p>
<pre><code class="lang-auto">[I 2023-05-28 16:55:56.680 ServerApp] Connecting to kernel 24772f77-eeac-4d90-a1e0-75d06a4edda1.
ERROR: received bad message: No such comm target registered: jupyter.widget.control
Message type: comm_open
ERROR: received bad message: No such comm registered: 14c86747-6042-41dd-9429-b199dfe5a98a
Message type: comm_msg
</code></pre>

---

## Post #2 by @lassoan (2023-05-29 02:10 UTC)

<p>What Slicer version are you using? On what operating system?</p>

---

## Post #3 by @morning_jade (2023-05-29 07:32 UTC)

<p>5.2.2<br>
Windows<br>
and It’s normal when my ipykernel is Python 3</p>

---

## Post #4 by @ATAKAN_Isik (2023-05-29 16:50 UTC)

<p>Try disable anti-virus programs if u have any. Control environmental path and check python path. Maybe your jupyter libraries were not installed on your path same as comm targets of Slicer. If u had not added slicer/bin file path to environments please do and try.<br>
Keep us informed.<br>
Good Luck</p>

---

## Post #5 by @Juergen (2023-07-18 20:18 UTC)

<p>Hello,<br>
I just encountered the same problem. How did you resolve this problem?<br>
Thanks, Juergen</p>

---

## Post #6 by @just_zzzzzz (2023-08-01 20:59 UTC)

<p>I’m encountering the same problem. This happens when run the “01_Data_loading_and_display.ipynb” - " Dynamic views". Adding slicer/bin file path to environments doesn’t solve the problem. I’m using windows and slicer 5.2.2</p>

---

## Post #7 by @Juergen (2023-09-12 23:35 UTC)

<p>Hello, just trying to follow up. Any suggestions?</p>

---
