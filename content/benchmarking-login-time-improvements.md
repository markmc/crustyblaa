Title: Benchmarking Login Time Improvements
Date: 2005-12-11 11:25
Author: markmc
Tags: GNOME
Slug: benchmarking-login-time-improvements
Status: published

I finally got around to committing some [changes to
GConf](http://www.gnome.org/~markmc/code/gconf-merged-tree-split-translations.patch)
which [Lorenzo Colitti's analysis of GNOME startup
time](http://www.gnome.org/~lcolitti/gnome-startup/analysis/) showed
would make a considerable improvement to login time. More details
[here](http://mail.gnome.org/archives/desktop-devel-list/2005-December/msg00092.html).

The most frustrating part of this is just how difficult it is to get
decent, reproducible figures of login time to show the improvements.

I first tried using bootchart to reproduce the results as Lorenzo had
done. I hacked up a script to run gdm on a test machine, automatically
login as a test user and get a bootchart of the time between gdm
starting and the panel finishing loading the applets. I did a number of
runs for each of my test cases - unmodified GConf, unmerged tree;
unmodified GConf, merged tree; patched GConf, merged tree.

  --------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](http://www.gnome.org/~markmc/screenshots/bootchart-orig-small.png)](http://www.gnome.org/~markmc/screenshots/bootchart-orig.png)   [![](http://www.gnome.org/~markmc/screenshots/bootchart-merged-small.png)](http://www.gnome.org/~markmc/screenshots/bootchart-merged.png)   [![](http://www.gnome.org/~markmc/screenshots/bootchart-merged-split-small.png)](http://www.gnome.org/~markmc/screenshots/bootchart-merged-split.png)
  Unmodified                                                                                                                              Merged Tree                                                                                                                                 Merged Tree, Split Translations
  --------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------

You can see improvements, just as Lorenzo predicted, but annoyingly each
run of bootchart varied wildly from others, so you can't really be sure
exactly what difference you've made.

Next, I tried a much more low-tech approach. I wrote a
[script](http://www.gnome.org/~markmc/code/record-timestamp.sh.txt)to
record a timestamp in a text file in `/tmp` and ran that script from
xinitrc and from the panel (once it had finished loading applets). By
making the script reboot once it had recorded the second timestamp, and
configuring GDM to login automatically, I could walk away from the
machine and let it record a bunch of timings rather than sit there and
watch it reboot.

Disappointingly, these results varied quite a bit too. But, by
discarding obvious anomalies (note my ignorance of statistical methods)
and taking an average, I got:

-   Unmodified GConf - 14.382s
-   Unmodified GConf; merged tree - 13.978s
-   Patched GConf; merged tree - 11.086s

That shows a \~20% improvement in login time, which is certainly
promising.
