---
topic_id: 9270
title: "Segmentation Via Web Browser"
date: 2019-11-22
url: https://discourse.slicer.org/t/9270
---

# Segmentation via web-browser

**Topic ID**: 9270
**Date**: 2019-11-22
**URL**: https://discourse.slicer.org/t/segmentation-via-web-browser/9270

---

## Post #1 by @alex (2019-11-22 15:31 UTC)

<p>Hi all,</p>
<p>I looking for a way to segment label masks via a web-based interface. I have seen a few entries from a prior project week in 2017 but no follow-up to that issue. I am sure that is an issue many groups face as we start using some DL algorithms to segment staff and need the end user to improve upon the machine’s work.  Does Slicer support such a way ?<br>
If not, any other suggestions on other open source applications are also welcome. Cornerstone has a brush tool that should almost be sufficient to run on something like OHIF viewer…?</p>
<p>Thanks in advance for any replies.</p>

---

## Post #2 by @lassoan (2019-11-22 15:55 UTC)

<p>There are <a href="https://github.com/pieper/SlicerDockers">docker containers</a> for Slicer that allows you to run Slicer in a web browser. See for example this demo: <a href="https://bit.ly/2XAtqbu">https://bit.ly/2XAtqbu</a> (click X11 session; I will keep this running for a while, but this is not a permanent service).</p>
<p>We would like to set up a demo server that can serve multiple users - see for example this topic: <a href="https://discourse.slicer.org/t/can-slicer3d-be-hosted-on-a-rendering-server/9256/4" class="inline-onebox">Can slicer3D be hosted on a rendering server?</a></p>
<p>Do you have funding or expertise to contribute towards this goal?</p>

---

## Post #3 by @pieper (2019-11-22 19:47 UTC)

<p>Also note that development of segmentation tools native to OHIF is under active development.  these will be interoperable with Slicer (so you can move segmentation files back and forth as needed).</p>

---

## Post #4 by @alex (2019-11-23 02:24 UTC)

<p>Hi Andras,<br>
Thanks for your quick response. This is super helpful. Your question about funding and expertise is very broad - so I guess my answers is shy maybe. That said, I am certainly very excited about this topic and happy help if I am of any value.</p>

---
