# Context-Menu-Add-Items-App

## To work you need to run as administrator

![image](https://github.com/user-attachments/assets/2eb457c4-efb9-4d2c-868a-3adaa8c7d6e9)

### How to add
1 - Select where the new element will be added to
     Folder - by right-clicking on the folder
     For all files - by clicking on any file with extension
     Desktop - by clicking on any empty space
     Storage devices - by clicking on data storage devices
     Specific extension - DOES NOT WORK

2 - Enter the name of the item you want to see

3 - Top - to be at the top of the list
    Bottom - to be at the bottom of the list
    Empty - to be in the center of the list
    
4 - Your own command, for example - powershell.exe (runs powershell)

### How to delete
1 - win + r regedit

2 - type in the path string - if you add to 

                                            for all files: \HKEY_CLASSES_ROOT\*\shell

                                            folder: \HKEY_CLASSES_ROOT\Folder\shell
                                            
                                            desktop: \HKEY_CLASSES_ROOT\Directory\Background\shell
                                            
                                            drive: \HKEY_CLASSES_ROOT\Drive\shell
                                            
                                            
3 - Press del

4 - Done, you delete your element!
