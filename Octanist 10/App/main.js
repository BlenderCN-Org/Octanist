const { app, BrowserWindow, Menu, Tray } = require('electron')
const server = require('./server')

function createWindow() {
    // Start the server from module
    server.start()

    // Create the browser window.
    let win = new BrowserWindow({
        width: 480,
        height: 800,
        transparent: true,
        frame: false,
        resizable: false,
        alwaysOnTop: true
    })

    // Change the default minimize behaviour
    win.on('minimize', function (event) {
        event.preventDefault()
        win.hide()
    })

    // Create the system tray
    let tray = new Tray('/public/tray.ico')
    const contextMenu = Menu.buildFromTemplate([
        {
            label: 'Show App', click: function () {
                win.show()
            }
        },
        {
            label: 'Quit', click: function () {
                app.isQuiting = true
                app.quit()
            }
        }
    ])
    tray.setToolTip('Octanist 10')
    tray.setContextMenu(contextMenu)

    // Load the tray and the view
    win.tray = tray
    win.loadURL('http://localhost:5200')
}

app.on('ready', createWindow)