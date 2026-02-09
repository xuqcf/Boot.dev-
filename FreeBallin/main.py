from enum import Enum

CSVExportStatus = Enum(
    "CSVExportStatus", ["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
)


def get_csv_status(status, data):
    def pending(data):
        converted = list(
            map(
                lambda row: list(map(str, row)),
                data
            )
        )
        return converted
    
    def processing(data):
        rows = list(
            map(
                lambda row: ",".join(row),
                data
            )
        )

        table = "\n".join(rows)

        return table
    
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending...", pending(data))
        
        case CSVExportStatus.PROCESSING:
            return ("Processing...", processing(data))
        
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        
        case CSVExportStatus.FAILURE:
            converted = pending(data)
            table = processing(converted)
            return ("Unknown error, retrying...", table)
        
        case _:
            raise Exception("unknown export status")
