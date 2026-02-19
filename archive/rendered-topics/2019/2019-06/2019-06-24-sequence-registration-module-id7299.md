---
topic_id: 7299
title: "Sequence Registration Module"
date: 2019-06-24
url: https://discourse.slicer.org/t/7299
---

# Sequence registration module

**Topic ID**: 7299
**Date**: 2019-06-24
**URL**: https://discourse.slicer.org/t/sequence-registration-module/7299

---

## Post #1 by @Jainey (2019-06-24 19:56 UTC)

<p>Has the sequence registration module been renamed or something? It doesn’t come up after installing the latest nightly in windows or Mac,<br>
It was usually under sequences; Other 3 categories are there (crop volume sequences, sequence browser and sequences ) but not sequence registration. I 've installed sequences and 4 D elastix.</p>
<p>Thanks a lot</p>

---

## Post #2 by @jamesobutler (2019-06-24 20:40 UTC)

<p>You should be able to see in the Python Interactor within Slicer that the SequenceRegistration module is failing to import (see <a href="http://slicer.cdash.org/testDetails.php?test=9575175&amp;build=1625725" rel="nofollow noopener">failing test</a>).  This is because the extension hasn’t been updated to work with Python3 which the Slicer nightly now uses.</p>
<p>You can try installing it using Slicer 4.10.2 which still uses Python2.</p>
<p>Or it would be welcomed if you could submit a PR to <a href="https://github.com/moselhy/SlicerSequenceRegistration" rel="nofollow noopener">SlicerSequenceRegistration</a> with updates that will make it Python 2/3 compatible.</p>

---

## Post #3 by @lassoan (2019-06-25 03:50 UTC)

<p>Thanks <a class="mention" href="/u/jainey">@Jainey</a> for reporting and <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for investigating. I’ve pushed a <a href="https://github.com/moselhy/SlicerSequenceRegistration/commit/e9ac5c24e30ecee6a0f8dfee472aa54ff11497cf" rel="nofollow noopener">fix</a>, please update SequenceRegistration tomorrow and let me know if you still experience problems.</p>

---

## Post #4 by @Jainey (2019-06-28 18:31 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. I will update this, hopefully this solves the problem<br>
Sorry Just tried updating still not working</p>

---

## Post #5 by @jamesobutler (2019-06-28 19:16 UTC)

<p>What error are you getting? Check Help-&gt;Report A Bug or look for any output in the python interactor.</p>

---

## Post #6 by @arvind112358 (2023-08-22 05:38 UTC)

<p>hello,<br>
I am trying to use sequence registration but it shows this error<br>
Error: Command ‘elastix’ died with &lt;Signals.SIGABRT: 6&gt;.</p>

---
