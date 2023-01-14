import PySimpleGUI as Sg
from Database import Database as Db

Sg.theme("DarkAmber")

# Struttura Finestra
Layout = [
    [Sg.T("Host:", 10), Sg.Combo(("192.168.0.37", "gomsil.ddns.net"), default_value="192.168.0.37", k="Host")],
    [Sg.T("Port:", 10), Sg.I("3306", k="Port")],
    [Sg.T("User:", 10), Sg.I("Gomsil", k="User")],
    [Sg.T("Password:", 10), Sg.I("Gomsil123", password_char="#", k="Pw")],
    [Sg.T("_" * 100)],
    [Sg.T("Tabella:", size=10), Sg.Combo(("Student", "StudentAddress"), k="Tab", enable_events=True,
                                         readonly=True, size=30, disabled=True)],
    [
        [Sg.Table([], ["Id", "Nome"], visible_column_map=[True, True], k="Table1", auto_size_columns=True, num_rows=10,
                  expand_x=True, justification="center", visible=False)],
        [Sg.Table([], ["Id", "Via", "Citta", "StudenteId"], visible_column_map=[True, True, True, True], k="Table2",
                  expand_x=True, auto_size_columns=True, num_rows=10, justification="center", visible=False)]
    ],
    [Sg.B("Connect", size=15, k="Connect"), Sg.Exit(s=15, k="Exit")],
    [Sg.StatusBar("          Application Started          ", k="Sb", justification="center")]
]

Window = Sg.Window("OneToOne", Layout)

# Main Loop Application
while True:
    Event, Values = Window.read()
    # Uscita Programma
    if Event in (Sg.WIN_CLOSED, "Exit"):
        break
    # Pulsante Connette al Database
    if Event == "Connect":
        Host = Values["Host"]
        Result = Db.Connette(Db, Host=Host, Port=Values["Port"],
                             User=Values["User"], Pw=Values["Pw"])
        if Result:
            Sg.Popup(f"Connected To Host: {Host}")
            Window["Sb"].update(f"Connesso a Database {Host}")
            Window["Tab"].update(disabled=False)
            Window["Connect"].update(disabled=True)
        else:
            Sg.PopupError("Errore Connessione Database", title="Errore")

    # Carica Dati da tabella
    if Event == "Tab":
        if Values["Tab"] == "Student":
            Values["Table1"] = Db.GetDatiTabella(Db, Values["Tab"])
            Window["Table1"].update(visible=True)
            Window["Table2"].update(visible=False)
            Window["Table1"].update(Values["Table1"])
        else:
            Values["Table2"] = Db.GetDatiTabella(Db, Values["Tab"])
            Window["Table1"].update(visible=False)
            Window["Table2"].update(visible=True)
            Window["Table2"].update(Values["Table2"])

Window.close()
