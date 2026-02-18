# Arduino PedalBoard

**Topic ID**: 22909
**Date**: 2022-04-11
**URL**: https://discourse.slicer.org/t/arduino-pedalboard/22909

---

## Post #1 by @PaoloZaffino (2022-04-11 15:03 UTC)

<p>Hi all,<br>
we are glad to announce that the <a href="https://github.com/pzaffino/SlicerArduinoController" rel="noopener nofollow ugc">SlicerArduinoController</a> extension now has a new module for controlling Slicer view via a dedicated pedalboard connected to Arduino.</p>
<p>For the moment, just a basic set of instructions are implemented.</p>
<p>Any comments/suggestions/contributions are more than welcomed!</p>
<p>Best,<br>
Paolo</p>

---

## Post #2 by @lassoan (2022-04-11 20:39 UTC)

<p>Sounds interesting, thanks for sharing. Could you attach an example video showing how it works?</p>

---

## Post #3 by @Christian_Simon (2022-04-12 20:11 UTC)

<p>Here you are :</p>
<div class="youtube-onebox lazy-video-container" data-video-id="8R6LfBqHNPY" data-video-title="SlicerArduino Demo - Slicer Project Week Dec 2020" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=8R6LfBqHNPY" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/8R6LfBqHNPY/maxresdefault.jpg" title="SlicerArduino Demo - Slicer Project Week Dec 2020" width="" height="">
  </a>
</div>


---

## Post #4 by @lassoan (2022-04-12 21:42 UTC)

<p>Thank you, this is a very informative video. Do you have anything that shows the pedal board in action?</p>

---

## Post #5 by @PaoloZaffino (2022-04-13 16:41 UTC)

<p>I’ll ask my student to record a video, no problem</p>

---

## Post #6 by @PaoloZaffino (2022-05-03 17:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> here the video, sorry for the delay</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F_WdKU6zyXg" data-video-title="3D Slicer Arduino PedalBoard" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F_WdKU6zyXg" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F_WdKU6zyXg/maxresdefault.jpg" title="3D Slicer Arduino PedalBoard" width="" height="">
  </a>
</div>


---

## Post #7 by @lassoan (2022-05-03 23:22 UTC)

<p>Very nice, thank you! What pedal hardware did you use (brand/model)?</p>

---

## Post #8 by @PaoloZaffino (2022-05-04 15:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> we just picked a (random) pedalboard up and we customized it for our purpose (we took advantage of the mechanical part already there).<br>
Whatever 3-buttons hardware can be used.</p>

---

## Post #9 by @lassoan (2022-05-04 18:50 UTC)

<p>We bought similar USB foot switches before and they were configurable to send keyboard shortcuts or mouse events when a button was pressed. Since <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts">any keyboard shortcut can be mapped to any Python command</a>, it might be simpler to use foot switches like this without modifications if the goal is to simply trigger software functions by the press of a pedal. Of course there could be more complex use cases for that is better if the arduino processes pedal signals. It would be nice to find and document those kind of more complex use cases.</p>

---

## Post #10 by @PaoloZaffino (2022-05-06 14:57 UTC)

<p>That’s definitely an option.<br>
Our idea was to catch the signal from Arduino board and use it for calling a slicer function that modifies the view.<br>
Ideally, we could call whatever function.</p>

---
