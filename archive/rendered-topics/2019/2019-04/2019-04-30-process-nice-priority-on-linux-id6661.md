# Process nice/priority on linux

**Topic ID**: 6661
**Date**: 2019-04-30
**URL**: https://discourse.slicer.org/t/process-nice-priority-on-linux/6661

---

## Post #1 by @gcsharp (2019-04-30 21:51 UTC)

<p>Hi, I just noticed that my Slicer sets itself to a nice value of 19 on linux.<br>
(I noticed this because I let a colleague run some jobs on my desktop.)<br>
What is going on?  Is there any way to run it at nice = 0?</p>

---

## Post #2 by @lassoan (2019-05-01 02:40 UTC)

<p>Setting background processing priority to low was added <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Base/GUI/vtkSlicerApplication.cxx?revision=1607&amp;view=markup&amp;pathrev=1607#l455" rel="nofollow noopener">13 years ago</a>, to make GUI more responsive during CLI execution. On Windows, only the processing thread priority is decreased, which is correct behavior. However, on Linux&amp;Mac <a href="https://linux.die.net/man/3/setpriority" rel="nofollow noopener">setpriority function</a> is used, which decreases priority of the entire process.</p>
<p>Could you try if replacing <code>setpriority</code> by <a href="http://man7.org/linux/man-pages/man3/pthread_getschedparam.3.html" rel="nofollow noopener"><code>pthread_setschedparam</code></a> works better? Or maybe process prioritization could be removed for Linux&amp;Mac.</p>
<p>What do you experience as a result of running at nice(19)?</p>

---

## Post #3 by @gcsharp (2019-05-01 15:38 UTC)

<p>Thank you Andras.  I was certainly curious about why this decision was made.</p>
<p>What I noticed was launch time.  With all cores busy at nice=0, application launch took several minutes.</p>
<p>If I understand your idea, it would be to nice the CLI threads only, and not the UI thread.  But I am not sure where this would go.  As per your link, I tried changing this in vtkSlicerApplicationLogic::ProcessingThreaderCallback, but it had no effect; the main Slicer thread still runs at nice 19.  (Below is my test code.)</p>
<pre><code>  int policy;
  struct sched_param priority;
  int ret;
  ret = pthread_getschedparam (pthread_self(), &amp;policy, &amp;priority);
  priority.sched_priority = 20;
  ret = pthread_setschedparam (pthread_self(), policy, &amp;priority);
  (void)ret; // unused variable
</code></pre>
<p>Anyway, might not be worth the effort, because multi-user computers are less common these days.</p>

---

## Post #4 by @lassoan (2019-05-01 18:09 UTC)

<p>Does the process priority remain default if you remove priority setting completely? (remove both <code>setpriority</code> calls from vtkSlicerApplicationLogic, I don’t think there is any other place where process priority is changed)</p>

---

## Post #5 by @gcsharp (2019-05-02 21:52 UTC)

<p>Curiously, it does not.  I did a quick grep through the Slicer code, and also the CTK app launcher code, and did not find any other obvious location that setpriority() or nice() is called.</p>
<p>As this is not a high priority for me, we may postpone this investigation.  But I’m happy to continue if any other user runs into a problem.</p>

---

## Post #6 by @aymeric.chataigner (2020-07-29 08:44 UTC)

<p>Hi,</p>
<p>I would also like to have the classic medium priority for SlicerAppReal.<br>
I have the expected behaviour if I set priority to 0 in vtkSlicerApplicationLogic::ProcessingThreaderCallback.</p>
<p>It seems there is a solution to decrease the priority of the processing thread on Linux:<br>
</p><aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/10876342/equivalent-of-setthreadpriority-on-linux-pthreads/10876787#10876787" target="_blank" rel="nofollow noopener">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/561300/alexandru-c" target="_blank" rel="nofollow noopener">
    <img alt="Alexandru C." src="https://www.gravatar.com/avatar/ff1a5de8ed4b4eb2d92123450890f5a8?s=128&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="60" height="60">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/10876342/equivalent-of-setthreadpriority-on-linux-pthreads/10876787#10876787" target="_blank" rel="nofollow noopener">Equivalent of SetThreadPriority on Linux (pthreads)</a>
</h4>

<div class="tags">
  <strong>c++, c, linux, winapi</strong>
</div>

<div class="date">
  
  answered by
  <a href="https://stackoverflow.com/users/561300/alexandru-c" target="_blank" rel="nofollow noopener">
    Alexandru C.
  </a>
  on <a href="https://stackoverflow.com/questions/10876342/equivalent-of-setthreadpriority-on-linux-pthreads/10876787#10876787" target="_blank" rel="nofollow noopener">05:46AM - 04 Jun 12 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Do you think it would be possible to use this code in vtkSlicerApplicationLogic::ProcessingThreaderCallback ?</p>
<p>Best regards</p>

---

## Post #7 by @lassoan (2020-07-29 13:05 UTC)

<p>Thank you for investigating this. Could you submit a pull request to <a href="https://github.com/slicer/slicer">https://github.com/slicer/slicer</a> with all the changes that fixes the priorities for you?</p>

---

## Post #8 by @hherhold (2020-07-29 13:37 UTC)

<p>Does this make a difference on modern multicore systems? I did some quick testing with renice-ing Slicer on macOS (even to -20) and I don’t see much difference in loading speeds for a large volume, for example.</p>

---

## Post #9 by @aymeric.chataigner (2020-08-06 10:43 UTC)

<p>Hi Andras,</p>
<p>Thanks for this quick reply.<br>
I tried to do a pull request using this code <a href="https://stackoverflow.com/a/10876787/1643726" rel="nofollow noopener">https://stackoverflow.com/a/10876787/1643726</a> but here is the issue:</p>
<p>This code runs… but it does not change the priority of the thread because the scheduling policy is SCHED_OTHER which does not allow to change the priority. We could change the scheduling policy before changing thread priority but it requires root privileges and it can be quite dangerous:  <a href="https://stackoverflow.com/a/3663250/1643726" rel="nofollow noopener">https://stackoverflow.com/a/3663250/1643726</a></p>
<p>So here is a pull request which just removes the code responsible of the VERY LOW priority:<br>
</p><aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5087" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5087" target="_blank" rel="nofollow noopener">DO NOT MERGE: remove the code responsible of VERY LOW priority of Sli…</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>achataigner:aymeric-chataigner/do-not-merge/set-slicerappreal-priority-to-normal</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-08-06" data-time="10:42:50" data-timezone="UTC">10:42AM - 06 Aug 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/achataigner" target="_blank" rel="nofollow noopener">
          <img alt="achataigner" src="https://avatars3.githubusercontent.com/u/3016648?v=4" class="onebox-avatar-inline" width="20" height="20">
          achataigner
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 0 additions and 24 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5087/files" target="_blank" rel="nofollow noopener">
          <span class="added">+0</span>
          <span class="removed">-24</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><strong>But it should not be necessary to merge this branch: until now I don’t have problems caused by the VERY LOW priority of SlicerAppReal, so we should keep it if it fixed the UI performances in the past…</strong></p>
<p>Best regards</p>

---
