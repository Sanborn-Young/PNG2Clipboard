## Give It To Me Now

The binary is called PNG2Clipboard.exe and is in the dist folder.  Click on the folder and the program and download to use.

## Details
This is a quick and dirty utility mainly for Obsidian but should work on other .md files.  Because I'll most likely never touch this again, the executable is attached, and will not be put on a release.  If you download the binary, it should be completely self contained, and has no ability to config the file.

![ProgramIcon](./README_display/Icon.webp)


If you run the program, it will looks in %CurrentUser%\OneDrive\Pictures\Screenshots for latest png files, turns it into webp 1080 @ 20 and then transfer this to your clipboard.  You can then paste the string directly into Obsidian.

If not clear, you need to have your PC with a standard load and be using OneDrive.  If this doesn't fit, you'll need to download and compile the program again.  It also assumes you've done nothing to the Windows Snipping tool, which places a .png file into your Screenshot folder after every snip of the screen.

After running the program, you will get the following dialog box below.  When first run the program finds the newest .png file in your screenshot folder.  It turns this png file into a b64 data stream (ASCII UTF-8), pads it with the right front and end, so you paste it into your Obsidian note or any other note as an embedded graphic.

If you take another screenshot, you will need to hit the repeat button on the dialog box to process the new slide.

![ProgramIcon](./README_display/Dialog.webp)

Remember that the clipbox gets overwritten if you copy something else into the buffer, but you can always hit the refresh button to grab the latest screenshot shot out of the screenshot folder.

If you want more control but a slower process, look at PNG2MD on this same github.
