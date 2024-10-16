import wx
import requests
class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.Get_Update()
        self.basicGUI()

    def Get_Update(self):
        version_file="version.txt"
        repo_owner="Text-remist"
        repo_name="Tech_Support_App"
        update = True
        if update:
            YesNoBox = wx.MessageDialog(None, 'A new version exists!\nDo you wish to update?', 'Question',wx.YES_NO)
        if YesNoBox.ShowModal() == wx.ID_YES:
                  """Checks for an update by comparing the local version to the latest GitHub release version."""

        # Read the local version from version.txt
        try:
            with open(version_file, 'r') as file:
                local_version = file.read().strip()
        except FileNotFoundError:
            print(f"{version_file} not found.")
            return

        # Fetch the latest version from the GitHub repository
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
        response = requests.get(url)

        if response.status_code == 200:
            latest_version = response.json()["tag_name"]
        else:
            print(f"Error fetching latest version: {response.status_code}")
            return

        # Compare versions
        if local_version != latest_version:
            print(f"Update available! Latest version: {latest_version}, Your version: {local_version}")
        else:
            print("You are up-to-date!")
        
    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()

        editButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg...')

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
    
        nameBox = wx.TextEntryDialog(None,'what is your name?', 'Welcome', 'name')

        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()
            print(userName)
        YesNoBox = wx.MessageDialog(None, 'A new version exists!\nDo you wish to update?', 'Question',wx.YES_NO)
        YesNoAnswer = YesNoBox.ShowModal()
        YesNoBox.Destroy()
        print(YesNoAnswer)
        wx.TextCtrl(panel, pos=(10,10), size=(250,150))
        if YesNoAnswer == wx.ID_NO:
            userName = 'Loser!'
        self.SetTitle("Tech Support"+userName)
        self.Show(True)
        
    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)


    app.MainLoop()


main()
