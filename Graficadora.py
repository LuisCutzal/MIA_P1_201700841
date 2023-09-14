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
        
    def graficarFDISK(self):
        salida ="""
        digraph D {
            subgraph cluster_0 {
                bgcolor="#68d9e2"
                node [style="rounded" style=filled];
                node_A [shape=record    label="MBR|Libre|{Extendida|{EBR|LOGICA|EBR|LOGICA}}|ParticionP|Libre"];
            }
        
        }
        """
        
        
        """
        digraph D {
    subgraph cluster_0 {
        bgcolor="#68d9e2"
        node [style="rounded" style=filled];
       
        node_A [shape=record    label="MBR|Libre|{Extendida|{EBR|LOGICA|EBR|LOGICA}}|ParticionP|Libre"];
    }
   
}

digraph D {
    subgraph cluster_0 {
        bgcolor="#68d9e2"
        node [style="rounded" style=filled];

        node_b [shape=record label="MBR:20|Libre:20|{Extendida|{EBR:20|LOGICA:20|EBR:20|LOGICA:20}}|ParticionP:20|Libre:20"];
    }
}
        
        
        """