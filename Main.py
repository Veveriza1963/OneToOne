import PySimpleGUI as Sg
import mariadb_sqlbuilder as SqlBuild
from PySimpleGUI import Window

Sg.theme("DarkAmber")

# Struttura Finestra
Layout = [
    [Sg.T("Host:", 10), Sg.Combo(("192.168.0.37", "gomsil.ddns.net"), default_value="192.168.0.37", k="-Host-")],
    [Sg.T("Port:", 10), Sg.I("3306", k="-Port-")],
    [Sg.T("User:", 10), Sg.I("Gomsil", k="-User-")],
    [Sg.T("Password:", 10), Sg.I("Gomsil123", password_char="#", k="-Pw-")],
    [Sg.T("-" * 100)],
    [Sg.T("Tabella:", size=10), Sg.Combo(("Student", "StudentAddress"), k="-Tab-", enable_events=True,
                                         readonly=True, size=30, disabled=True)],
    [Sg.B("Connect", size=15, k="-Connect-")],
    [Sg.Exit(s=15, k="-Exit-")],
    [Sg.StatusBar("          Application Started          ", k="-Sb-", justification="center")]
]

Window: Window = Sg.Window("OneToOne", Layout)


# Connette al database
def Connect(Host, Port, User, Pw):
    Port1: int = int(Port)
    Connection = SqlBuild.Connect(Host, User, Pw, "OneToOne", Port1)
    if Connection is not None:
        Sg.Popup(f"Connected To Host: {Host}")
        Window["-Sb-"].update(f"Connesso a Database {Host}")
        Window["-Tab-"].update(disabled=False)
    else:
        Sg.PopupError("Errore Connessione Database", title="Errore")


# Visualizza Dati Tabella
def GetDatiTabella(Tabella):
    Rows = Connection.table(Tabella).select("*").fetchall()
    print(Rows)


# Main Loop Application
while True:
    Event, Values = Window.read()
    # Uscita Programma
    if Event in (Sg.WIN_CLOSED, "-Exit-"):
        break
    # Pulsante Connette al Database
    if Event == "-Connect-":
        Connect(Window["-Host-"].get(), Window["-Port-"].get(),
                Window["-User-"].get(), Window["-Pw-"].get())

    # Scelta Tabella
    if Event == "-Tab-":
        GetDatiTabella(Window["-Tab-"].get())

Window.close()
