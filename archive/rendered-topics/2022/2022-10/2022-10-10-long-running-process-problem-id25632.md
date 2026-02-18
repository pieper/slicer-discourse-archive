# Long running process problem

**Topic ID**: 25632
**Date**: 2022-10-10
**URL**: https://discourse.slicer.org/t/long-running-process-problem/25632

---

## Post #1 by @bzhu (2022-10-10 23:16 UTC)

<p>I have a set of code for imaging processing that takes quite a long while to run.</p>
<p>If I run the code in command-line with PythonSlicer, the code completes and generates a new image.</p>
<p>However, when I run the code inside my Slicer extension, Slicer has a spin busy cursor for a long while and then the whole Slicer studio quits.</p>
<p>Just wonder if the 3d Slicer has a built-in timeout with an adjustable parameter for the timeout.</p>
<p>Thanks,<br>
Bing Zhu<br>
UCLA</p>

---

## Post #2 by @pieper (2022-10-11 13:12 UTC)

<p>If you can reproduce this with a script you can share it will be easier for people to help.</p>

---

## Post #3 by @jay1987 (2022-10-13 07:14 UTC)

<p>i think you can use the extension [SlicerParallelProcessing] to put the complex computation in that,and the main process listen to the sub process when it finished,that won’t cause a spin busy cursor.<br>
but i encount a problem when i import qt in [SlicerParallelProcessing],the sub process stop with error , i dont’t know why <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #4 by @pieper (2022-10-13 14:25 UTC)

<aside class="quote no-group" data-username="jay1987" data-post="3" data-topic="25632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jay1987/48/16183_2.png" class="avatar"> jay1987:</div>
<blockquote>
<p>i import qt in [SlicerParallelProcessing],the sub process stop with error , i dont’t know why</p>
</blockquote>
</aside>
<p>ParallelProcessing uses <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227">PythonSlicer</a> by default so it can communicate via stdin/stdout of the subprocess.  if you have a use case that requires Qt, you could start <code>Slicer --no-main-window</code> instead, but you’d need to implement a different communication strategy since the main Slicer app doesn’t communicate via stdin/stdout (although I wish it did and perhaps we should implement that).  An option for communicating a helper Slicer background process would be to run with the WebServer in either the helper or the main Slicer and passing commands and data back and forth via http.</p>

---

## Post #5 by @jay1987 (2022-10-14 00:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="25632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>ParallelProcessing uses <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227" rel="noopener nofollow ugc">PythonSlicer</a> by default so it can communicate via stdin/stdout of the subprocess. if you have a use case that requires Qt, you could start <code>Slicer --no-main-window</code> instead, but you’d need to implement a different communication strategy since the main Slicer app doesn’t communicate via stdin/stdout (although I wish it did and perhaps we should implement that). An</p>
</blockquote>
</aside>
<p>thank you pieper,it helps me!</p>

---
