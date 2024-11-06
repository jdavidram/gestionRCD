def tableHTML(df):
    table = "<table>"
    table += "<thead>"
    for h in list(df):
        table += "<th>" + h + "</th>"
    table += "</thead>"
    table += "<tbody>"
    for r in range(0, len(df), 1):
        table += "<tr>"
        for d in list(df.iloc[r]):
            subList = d.split("\n")
            if len(subList) > 1:
                table += "<td>"
                table += "<ul>"
                for i in subList:
                    table += "<li>" + i.replace("* ", "") + "</li>"
                table += "</ul>"
                table += "</td>"
            else:
                table += "<td>" + d + "</td>"
        table += "</tr>"
    table += "</tbody>"
    table += "</table>"
    print(table)