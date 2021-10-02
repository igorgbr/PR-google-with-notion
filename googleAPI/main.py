from rw_sheet import read_sheets, write_final_result

# SPREADSHEET_ID = "1W7N6_KSyrr6vyytuwr6pJ7w4YQCg-sSEO528Tzi4SI4"
# cels_to_read = "principal!A2:F2"
# base_row = "principal!A2"


def updateRowsTrybeValues(SPREADSHEET_ID, cels_to_read, base_row):
    data_result = read_sheets(cels_to_read, SPREADSHEET_ID)
    # print(data_result[0][0])

    notion_students = 100
    notion_colab = 0
    notion_conf = 0
    notion_comp = 0
    notion_transp = 0
    notion_people = 0

    update_row = [
        [
            int(data_result[0][0]) + notion_students
        ][  # Estudantes em primeiro lugar
            int(data_result[0][1]) + notion_colab
        ][  # Colaboração
            int(data_result[0][2]) + notion_conf
        ][  # Confiança Genuina
            int(data_result[0][3]) + notion_comp
        ][  # Comprometimento
            int(data_result[0][4]) + notion_transp
        ][  # Transparência
            int(data_result[0][5]) + notion_people
        ]  # Nosso Negócio é gente
    ]
    data_write = write_final_result(update_row, base_row, SPREADSHEET_ID)
