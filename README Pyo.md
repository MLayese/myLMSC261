# ReadMe File

## Problems
So with the installation of this one I found a few mishaps.

Getting pip was easy enough. It was 
```
sudo pip3 install -U wxPython==4.1.0
```
that gave me some issues. It didn't authorize my user for whatever reason However adding in an -H let me bypass this.

```
sudo -H pip3 install -U wxPython==4.1.0
```
When attempting to run 
```
brew install liblo libsndfile portaudio portmidi
```
The error message “Could Not Resolve HEAD to a Revision” popped up. Obviously, I was unable to run the .py files and had to resolve this issue. 

Looking up this error message on StackOverflow showed me that
```
git -C $(brew --repository homebrew/core) checkout master
```
would override the HEAD problem amd continue with the installation.

## I'm straight up not having a good time 
So after installing pip and having it work on Monday, I check again on Thursday and see that I can no longer run the files. attempting to just reinstall the pyo file gave me some issues - I quite literally couldn't. 
```
Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/pip-18.1.dist-info/INSTALLER'
Consider using the `--user` option or check the permissions.
```
To combat this issue I just used
```
 pip install --upgrade pip --user
```
After doing this I was still met with the same error message I got when trying to install --coreaudio (the email I sent you had that same issue)
I also tried the suggestion you gave to just run the pyo without the --coreaudio tag but that didn't work either. I still got the same 32 warnings and 1 error message. 
When rerunning the file again the following day (as in redownloading everything) it wouldn't let me download - the pip file wasn't executable since my account wasn't authorized(?)
Fed up, I decided to 
```
chmod -775
```
and see if I could open the files myself and make my own installation. This wasn't necessary. I guess I did something because then homebrew installed all the files I needed and my pyo files actually worked. Just to check I ran everything in IDLE.
Nice. My brain hurts