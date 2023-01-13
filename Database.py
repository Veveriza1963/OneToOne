import mariadb_sqlbuilder as SqlBuilder


class Database:
    def __int__(self):
        pass

    # Connette al Database
    @staticmethod
    def Connette(self, Host, User, Pw, Port):
        Port1 = int(Port)
        self.Connessione = SqlBuilder.Connect(Host, User, Pw, "OneToOne", Port1)
        if self.Connessione is not None:
            return True
        else:
            return False

    # Carica la Tabella
    @staticmethod
    def GetDatiTabella(self, Tabella):
        Rows = self.Connessione.table(Tabella).select("*").fetchall()
        return Rows