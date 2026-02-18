# Crash after returning from hybernation

**Topic ID**: 12862
**Date**: 2020-08-05
**URL**: https://discourse.slicer.org/t/crash-after-returning-from-hybernation/12862

---

## Post #1 by @Alex_Vergara (2020-08-05 08:19 UTC)

<p>This happened to me in MacOS, Linux and Windows. After returning from hybernation Slicer crashes when making any operation. In MacOS it reports this</p>
<pre><code class="lang-auto">Process:               Slicer [1737]
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer
Identifier:            Slicer
Version:               ??? (4.11.0-2020-06-03)
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           Slicer [1737]
User ID:               501

Date/Time:             2020-08-05 10:14:44.294 +0200
OS Version:            Mac OS X 10.15.5 (19F101)
Report Version:        12
Bridge OS Version:     4.5 (17P5300)
Anonymous UUID:        091E1568-436C-6B92-129A-4DD230D034BF

Sleep/Wake UUID:       171BF89F-38DE-47B2-8D4E-F941C324DE4D

Time Awake Since Boot: 3700000 seconds
Time Since Wake:       3500000 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       EXC_I386_GPFLT
Exception Note:        EXC_CORPSE_NOTIFY

Termination Signal:    Segmentation fault: 11
Termination Reason:    Namespace SIGNAL, Code 0xb
Terminating Process:   exc handler [1737]
</code></pre>
<p>To reproduce Open Slicer, load some heavy scene (at least a 500MB mrb), do some operations, go to hybernation and wake up the computer. Then try to do some operation, Slicer will crash.</p>

---

## Post #2 by @pieper (2020-08-05 13:36 UTC)

<p>Interesting - I’ve never experienced this.  I often have slicer running when I shut the lid of a mac laptop and everything starts back up normally.  <a class="mention" href="/u/lassoan">@lassoan</a> do you see this on windows?  <a class="mention" href="/u/jcfr">@jcfr</a> do you see it on linux?</p>
<p>What Slicer versions have you seen this with?</p>

---

## Post #3 by @Alex_Vergara (2020-08-05 14:38 UTC)

<p>I am on MacOS 10.15<br>
Slicer nightly 2020-06-03</p>
<p>But also happened in Windows 10 and in Manjaro Linux.<br>
I usually leave the computer on during the night, and when I wake up this happens</p>

---

## Post #4 by @lassoan (2020-08-05 15:15 UTC)

<p>I work from a laptop all the time and never turn it off and I have never experienced this. However, I use default power options, which puts the computer into “sleep” and not hibernate. I don’t even see a hibernation option in power settings.</p>
<p>Since waking up from sleep is much faster, does not consume precious SSD space, and that is the default on modern laptops (at least on Windows), drivers does not get tested widely in hibernation mode. I would guess it is a graphics or network driver problem, maybe a bug in Qt or QWebEngine (Google Chromium).</p>
<p>I cannot investigate this, because I would not like to mess up power settings on my laptop by trying to force display of hibernation option (I would assume that hibernation option is not offered for a good reason).</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="3" data-topic="12862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I am on MacOS 10.15<br>
Slicer nightly 2020-06-03</p>
</blockquote>
</aside>
<p>You can try latest Slicer, which uses a more recent Qt version, to see if it makes a difference.</p>

---

## Post #5 by @muratmaga (2020-08-05 16:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since waking up from sleep is much faster, does not consume precious SSD space, and that is the default on modern laptops (at least on Windows), drivers does not get tested widely in hibernation mode. I would guess it is a graphics or network driver problem, maybe a bug in Qt or QWebEngine (Google Chromium).</p>
</blockquote>
</aside>
<p>I do use the hibernation on windows 10 (which I had to explicitly enable through command line, powercfg /h), because I would find my computer woke up from sleep from a background process (like virus check) and then used all the battery during travel. The point is though I never encountered this crash, after waking up from hibernation  and using it with large datasets…</p>

---

## Post #6 by @pieper (2020-08-05 18:13 UTC)

<p>As another datapoint, I suspended a docker instance of slicer and it resumed with no problems (debian image).</p>

---

## Post #7 by @Alex_Vergara (2020-08-05 19:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can try latest Slicer, which uses a more recent Qt version, to see if it makes a difference.</p>
</blockquote>
</aside>
<p>tried with current nightly on manjaro linux and seems to be resolved. I will try tomorrow with macos</p>

---

## Post #8 by @Alex_Vergara (2020-08-06 10:11 UTC)

<p>Tried in a Windows machine and seems to be solved, no more chashes.</p>
<p>Currently testing on MacOS.</p>

---

## Post #9 by @Alex_Vergara (2020-08-06 12:09 UTC)

<p>Tried on MacOS. Everything seems solved now. I will report if it happens again. Current version is being stable the whole day, no crashes so far.</p>
<p>BTW, my mac version is installed using brew so it is currently 2020-08-04</p>

---
