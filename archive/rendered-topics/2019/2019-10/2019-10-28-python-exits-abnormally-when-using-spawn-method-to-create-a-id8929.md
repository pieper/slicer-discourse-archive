---
topic_id: 8929
title: "Python Exits Abnormally When Using Spawn Method To Create A"
date: 2019-10-28
url: https://discourse.slicer.org/t/8929
---

# Python exits abnormally when using spawn method to create a new process in multiprocessing on Unix

**Topic ID**: 8929
**Date**: 2019-10-28
**URL**: https://discourse.slicer.org/t/python-exits-abnormally-when-using-spawn-method-to-create-a-new-process-in-multiprocessing-on-unix/8929

---

## Post #1 by @Guangshan_Chen (2019-10-28 19:54 UTC)

<p>On Unix, mutiprocessing works well with default creating new process method (fork). However, if I set the creating method as spawn,  python exits abnormally. I could not get the reason why python exits abnormally. Here is my simple testing code:</p>
<pre><code>def test_mp():
    num_processes = 3
    print("chengs++: mp start a new process with method: ", get_start_method())
    set_start_method('spawn', force=True)
    print("chengs++: mp start a new process with method after resetting to spawn: ", get_start_method())
    with Pool(num_processes) as pool:
        results = pool.starmap(
            doubler,
            zip(
                [2] * num_processes,
                [1] * num_processes,
            ),
        )
    print(results)

def doubler(number, r):
    result = number * 2 + r
    return result
</code></pre>
<p>If you have any clue, please let me know. Thanks in advance.</p>

---

## Post #2 by @lassoan (2019-10-28 21:26 UTC)

<p>You may need to use recent Slicer Preview Release for this to work. But there is a good chance that you can only use the default multiprocessing method because Slicer uses an embedded Python interpreter, which may manage threading differently than what multiprocessing expects.</p>
<p>There are many different multiprocessing options in Slicer - as they have been discussed on this forum before. Let us know if you don’t find those discussions or you have remaining questions.</p>

---

## Post #3 by @Guangshan_Chen (2019-10-29 15:14 UTC)

<p>Thanks, Lassoan.</p>
<p>I got latest preview release version. It did not work.</p>
<p>I search the forum. No issue with the spawn method in mutiprocessing.</p>

---
