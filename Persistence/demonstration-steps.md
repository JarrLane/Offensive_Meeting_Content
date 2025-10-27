# Please follow this step by step if this is your first time trying something like this, these steps are 100% safe

1. Download lubuntu (just a lightweight version of ubuntu) from the website

2. Open Oracle VM VirtualBox Manager

3. Click "New"

4. Name it whatever you want 

5. For ISO, select the ISO you downloaded and hit next

6. For resources, you dont need to go crazy but give yourself more ram and CPU so you can actually run it smoothly

7. In the Virtual Hard Disk, have "Create a Virtual Hard Disk Now" selected, and give yourself 5~10 GB (should be fine)

8. Click "Finish" at the summary page

9. Start up the virtual machine

10. When you are in it will let you either try or install the VM, INSTALL IT OR THIS LAB WONT WORK

11. Once it is all set up, you need to somehow get the script on your VM, at the meeting I used a burner email, you can do that or you can create a shared folder (How to do that: https://github.com/seed-labs/seed-labs/blob/master/manuals/vm/seedvm-manual.md#appendix-c-creating-a-shared-folder)

12. When you have the script on your VM, make it executable, you can do this by either doing `chmod +x filename` or do it through the GUI by right clicking and going to properties

13. Run the script, you will see that you get HACKED!!! (It might take a bit to actually start going, it wont just happen right away)

14. Try turning off or restarting your machine

15. Log back in

16. Oh FUCK you are still HACKED!!!!

17. Open a terminal and type `crontab -e` to edit the list of cronjobs

18. Delete the entry that runs the malware!!!

19. Save and exit the file

20. You are safe now!!! (it may popup a few more times for whatever reason but it will stop)

Afterwards you can do whatever you want with the vm you made, if you just wanted to test this out and be done then you can delete it, otherwise if you want to try other things out you can keep it
