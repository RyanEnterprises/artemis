#! C:/Program Files/nodejs/node.exe
const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');
const os = require('os');
const { shell } = require('electron');
const openAboutWindow = require('about-window').default;

// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) {
  // eslint-disable-line global-require
  app.quit();
}

const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    icon: 'images/FullColorIcon.ico',
  });

  // and load the index.html of the app.
  mainWindow.loadFile(path.join(__dirname, 'index.html'));
};

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);
console.log("Ready");

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});



const menu = Menu.buildFromTemplate([
  {
    label: 'File',
    submenu: [
      {
        label: 'New',
        accelerator: 'CmdOrCtrl+N',
        click: () => {
          console.log('New File');
        }
      },
      {
        label: 'Open',
        accelerator: 'CmdOrCtrl+O',
        click: () => {
          console.log('Open File');
        }
      },
      {
        label: 'Save',
        accelerator: 'CmdOrCtrl+S',
        click: () => {
          console.log('Save File');
        }
      },
      {
        label: 'Save As',
        click: () => {
          console.log('Save As File');
        }
      },
      {
        label: 'Close',
        click: () => {
          console.log('Close File');
        }
      },
      {
        label: 'Quit',
        accelerator: 'CmdOrCtrl+Q',
        click: () => {
          app.quit();
        }
      }
    ]
  },
  {
    label: 'Edit',
    submenu: [
      {
        label: 'Cut',
        accelerator: 'CmdOrCtrl+X',
        click: () => {
          console.log('Cut');
        }
      },
      {
        label: 'Copy',
        accelerator: 'CmdOrCtrl+C',
        click: () => {
          console.log('Copy');
        }
      },
      {
        label: 'Paste',
        accelerator: 'CmdOrCtrl+V',
        click: () => {
          console.log('Paste');
        }
      },
      {
        label: 'Select All',
        accelerator: 'CmdOrCtrl+A',
        click: () => {
          console.log('Select All');
        }
      }
    ]
  },
  {
    label: 'View',
    submenu: [
      {
        label: 'Reload',
        accelerator: 'CmdOrCtrl+R',
        click: () => {
          BrowserWindow.getFocusedWindow().reload();
        }
      },
      {
        label: 'Toggle Developer Tools',
        accelerator: 'Alt+CmdOrCtrl+I',
        click: () => {
          BrowserWindow.getFocusedWindow().webContents.toggleDevTools();
        }
      },
      {
        label: 'Toggle Full Screen',
        accelerator: 'CmdOrCtrl+Shift+F',
        click: () => {
          BrowserWindow.getFocusedWindow().setFullScreen(!BrowserWindow.getFocusedWindow().isFullScreen());
        }
      }
    ]
  },
  {
    label: 'Window',
    submenu: [
      {
        label: 'Minimize',
        accelerator: 'CmdOrCtrl+M',
        click: () => {
          BrowserWindow.getFocusedWindow().minimize();
        }
      },
      {
        label: 'Close',
        accelerator: 'CmdOrCtrl+W',
        click: () => {
          BrowserWindow.getFocusedWindow().close();
        }
      },
      {
        label: 'Prank',
        accelerator: 'CmdOrCtrl+R',
        click: () => {
          shell.openExternal('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
        }
      }
    ]
  },
  {
    label: 'Help',
    submenu: [
      {
        label: 'Github',
        click: () => {
          shell.openExternal('https://github.com/RyanEnterprises/artemis');
        }
      },
      {
        label: 'About Artemis',
        click: () => {
          openAboutWindow({
            icon_path: path.join(__dirname, 'images/ArtemisLockupFullColor.svg'),
            copyright: 'Copyright © 2022 Ryan Enterprises',
            package_json_dir: path.join(__dirname, '../package.json'),
            use_version_info: [
              ['Artemis', '5.0.0'],
              ['node.js', '17.6.0'],
              ['electron', '18.0.1'],
              ['chromium', '100.0.4896.60'],
              ['vscode', '1.32.1'],
              ['electron-forge', '11.0.0'],
            ],})
        }
      }
    ]
  },
]);

app.applicationMenu = menu;














// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.

//const fileManagerButton = document.getElementById('fileManagerButton');
//fileManagerButton.addEventListener('click', () => {
  //shell.openItem(os.homedir());
//});

//const notification = {
  //title: 'Hello',
  //body: 'This is a notification',
//};

//const notificationButton = document.getElementById('notificationButton');

//notificationButton.addEventListener('click', () => {
  //new Notification(notification.title, notification);
  //notification.onclick = () => {
    //console.log('Notification clicked');
  //}
//});
