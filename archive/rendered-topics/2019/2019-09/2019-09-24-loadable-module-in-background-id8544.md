# Loadable module in background

**Topic ID**: 8544
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/loadable-module-in-background/8544

---

## Post #1 by @fpsiddiqui91 (2019-09-24 12:16 UTC)

<p>Hello Developers,<br>
As you might have already noticed, I have been trying all the development options in Slicer.<br>
I am now working on using Loadable module for heavy computations while the remaining part of my code will be in scripted module.<br>
My question is, can we run the computations on loadable module in the background. I want that user keep on interacting with the slicer while heavy computations runs on the background. This is possible in CLI. But I want to use loadable module.</p>
<p>Is there anyway to do it?</p>

---

## Post #2 by @lassoan (2019-09-24 13:11 UTC)

<p>Yes, you can do computations in the background in a loadable module. You can use any threading APIs (C++11 multithreading, VTK’s vtkMultiThreader, Qt threads, etc.).</p>
<p>The only tricky part is synchronization with the main thread. You are only allowed to modify MRML nodes or invoke MRML events from the main thread.</p>

---

## Post #3 by @fpsiddiqui91 (2019-09-24 13:15 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>  for your response. Is there any example code for implementing this multithreading operation in Slicer?<br>
I just want that the mouse interaction should not be effected with these computations.</p>
<p>Thanks alot</p>

---

## Post #4 by @lassoan (2019-09-24 15:57 UTC)

<p><a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">OpenIGTLinkIF</a> module does this. It is not easy to use it as an example, as the module is quite complex, but maybe if you add a breakpoint where an image is received and step through in a debugger then you can get an idea how it works.</p>

---

## Post #5 by @fpsiddiqui91 (2019-09-24 16:07 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thank you for your response. Since my problem is quite simple I have tried pthread functions.<br>
it seems to work, but still I cannot interact with the slicer window while my module is doing the computation.<br>
its worth mentioning that, I haven’t added any MRML Node in my loadable  module. I am just wroking with vtkFloatArray.</p>
<pre><code>void *test2(void *ptr)
{

vtkFloatArray *a;
a=(vtkFloatArray *) ptr;



int c[2];

double Signal[49];
double test;

cout &lt;&lt; "loading signal values.. " &lt;&lt; std::endl;

int t=0;
for (int i=0;i&lt;96;i++)
{ for (int j=0;j&lt;128;j++)
{for (int k=0;k&lt;128;k++)
	{for (int l=0;l&lt;49;l++)
{t=i+(96*j)+((96*128)*k)+((96*128*128)*l);
Signal[l]=a-&gt;GetValue(t);
}

}}}

return NULL;
}
</code></pre>
<p>And I am calling this function with<br>
int err = pthread_create(&amp;(tid[2]), NULL, test2, (void*) &amp;a);</p>
<p>The code doesn’t mean anything, but I just want to run ‘test2’ pat of the code in other thread. (not in the main thread) so that my interaction wont get effected.</p>
<p>Thank you so much for your help</p>

---

## Post #6 by @lassoan (2019-09-24 16:18 UTC)

<p>Creating a thread should not block the main thread. I would not recommend pthreads, as it is ancient unix-specific API. You can use C++11 multithreading, VTK’s vtkMultiThreader, or Qt threads instead.</p>

---

## Post #7 by @fpsiddiqui91 (2019-09-24 16:21 UTC)

<p>Thank you, I will try with other multhreading APIs but I am afraid it would result the same.</p>
<p>As the threading seems to work but still my main thread gets blocked. I know it shouldn’t be the case.</p>
<p>Am I missing something else? or should it work?</p>
<p>Thank you again for your time and guidance.</p>

---

## Post #8 by @lassoan (2019-09-24 16:32 UTC)

<p>If you can send a link to your source code repository then I may be able to have a look.</p>

---

## Post #9 by @fpsiddiqui91 (2019-09-24 16:47 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your response, I am actually combining Scripted module and Loadable module. so my code is little messy. I can just add the important part here, so it might be easier for you:</p>
<p>The part of the code from my Scripted module (Python):</p>
<pre><code>def onCheckBootstrap(self):
modlog = slicer.vtkSlicerBootstrapping_loadableLogic()
aa = (np.random.randint(0, 100, size=(96, 128, 128, 49)))
a = numpy_support.numpy_to_vtk(num_array=aa.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
bb = (np.random.randint(0, 100, size=(49, 6)))
b = numpy_support.numpy_to_vtk(num_array=bb.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
c=modlog.Test(a,b)
print ("Back to python:")
print(c)
</code></pre>
<p>The part of the code from my Loadable module:</p>
<pre><code>void vtkSlicerBootstrapping_loadableLogic::Test(vtkFloatArray *a,vtkFloatArray *b)
{





 double Signal[49];
double test;

cout &lt;&lt; "loading signal values.. " &lt;&lt; std::endl;

char *message1 = "Thread 1";
pthread_t tid[2];

int err = pthread_create(&amp;(tid[2]), NULL, test2, (void*) &amp;a);
pthread_join( tid[2], NULL);

}

void *test2(void *ptr)
{

vtkFloatArray *a;
a=(vtkFloatArray *) ptr;



int c[2];

double Signal[49];
double test;

cout &lt;&lt; "loading signal values.. " &lt;&lt; std::endl;

int t=0;
for (int i=0;i&lt;96;i++)
{ for (int j=0;j&lt;128;j++)
 {for (int k=0;k&lt;128;k++)
	{for (int l=0;l&lt;49;l++)
{t=i+(96*j)+((96*128)*k)+((96*128*128)*l);
Signal[l]=a-&gt;GetValue(t);
}

}}}

return NULL;
}
</code></pre>
<p>I have added all the required parts of the code. Its working. The only problem is my main thread got blocked while running this loadable module.</p>
<p>Thank you so much for your time</p>

---

## Post #10 by @lassoan (2019-09-24 17:36 UTC)

<blockquote>
<p>The  <em>pthread_join</em> () function shall suspend execution of the calling thread until the target  <em>thread</em>  terminates</p>
</blockquote>
<p><em><a href="https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html" class="inline-onebox">pthread_join</a></em></p>
<p>So, you must not call <code>pthread_join</code>. You need to signal completion using alternative mechanisms. Polling a thread-safe queue object using a timer is simple and you can implement it using any of the threading/synchronization libraries. However, if you want to have minimal latency and synchronization overhead then probably you need to use proper synchronization objects.</p>

---
