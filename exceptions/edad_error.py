class EdadError(Exception):
    
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__()