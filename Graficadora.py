import rep
import graphviz
class GRAFICADORA():
    def __init__(self):
        pass
    def graficar(self, objMBR):
        salida="""
        digraph G {
        a1 [shape=none label=<
        <TABLE cellspacing="10" cellpadding="10" 
        style="rounded" bgcolor="red">
        <TR>
        <TD bgcolor="yellow">REPORTE MBR</TD>
        </TR>
        <TR>
        <TD bgcolor="yellow">mbr_tamano</TD>
        <TD bgcolor="yellow"> {objMBR.} </TD>
        </TR>
        <TR>
        <TD bgcolor="yellow">mbr_fecha_creacion</TD>
        <TD bgcolor="yellow">2020-12-12 02:22</TD>
        </TR>
        
        <TR>
        <TD bgcolor="yellow">mbr_disk_signature</TD>
        <TD bgcolor="yellow">74</TD>
        </TR>
        
        <TR>
        <TD bgcolor="purple">Particion</TD>
        
        </TR>
        
        </TABLE>>];
        }
        """
        graph = graphviz.Source(salida)
        graph.format = 'png'
        graph.render("output_file", view=True)