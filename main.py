from notionAPI import main, helper
from googleAPI.rw_sheet import read_sheets, write_final_result


def updateRowsTrybeValues():
    SPREADSHEET_ID = "1W7N6_KSyrr6vyytuwr6pJ7w4YQCg-sSEO528Tzi4SI4"
    cels_to_read = "principal!A2:F2"
    base_row = "principal!A2"

    data_result = read_sheets(cels_to_read, SPREADSHEET_ID)
    print(data_result)

    update_row = [main.requestPages(helper.blocks, helper.headers)] 

    write_final_result(update_row, base_row, SPREADSHEET_ID)


updateRowsTrybeValues()
