class ListTable(list):
    """ Overridden list class which takes a 2-dimensional list of 
        the form [[1,2,3],[4,5,6]], and renders an HTML Table in 
        IPython Notebook. """
    
    def _repr_html_(self):
        html = ["<center> <table>"]
        for row in self:
            html.append("<tr>")
            
            for col in row:
                html.append("<td>{0}</td>".format(col))
            
            html.append("</tr>")
        html.append("</table> </center>")
        return ''.join(html)

table = ListTable()
table.append([10*'&nbsp;'+'testcase', 'predicted', 'expected'])
table.append(['/usr/bin/wget:21598',1,1])
table.append(['/usr/bin/wget:21558',1,1])
table.append(['/usr/bin/wget:21600',1,1])
table.append(['/usr/bin/wget:21288',0,0])
table.append(['<b>/usr/bin/wget:21329','<b>1','<b>0'])
table.append(['/usr/bin/wget:21442',1,1])
table.append(['/usr/bin/wget:21295',0,0])
table.append(['/usr/bin/wget:21512',1,1])
table.append(['/usr/bin/wget:21515',1,1])
table.append(['/usr/bin/wget:21552',1,1])
table.append(['/usr/bin/wget:21584',1,1])
