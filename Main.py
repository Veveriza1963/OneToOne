import PySimpleGUI as Sg
import Database as Db

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

Window = Sg.Window("OneToOne", Layout)


# Main Loop Application
while True:
    Event, Values = Window.read()
    # Uscita Programma
    if Event in (Sg.WIN_CLOSED, "-Exit-"):
        break
    # Pulsante Connette al Database
    if Event == "-Connect-":
        Host = Window["-Host-"].get()
        Result = Db.Database.Connette(Db.Database, Host=Host, Port=Window["-Port-"].get(),
                                      User=Window["-User-"].get(), Pw=Window["-Pw-"].get())
        if Result:
            Sg.Popup(f"Connected To Host: {Host}")
            Window["-Sb-"].update(f"Connesso a Database {Host}")
            Window["-Tab-"].update(disabled=False)
        else:
            Sg.PopupError("Errore Connessione Database", title="Errore")

    # Carica Dati da tabella
    if Event == "-Tab-":
        Rows = Db.Database.GetDatiTabella(Db.Database, Window["-Tab-"].get())
        print(Rows)

Window.close()
