from typing import List

class BaseRepository:
    def __init__(self, file_manager_instance: str):
        self.file_manager_instance = file_manager_instance

    def _load_by_filters(self, filters: List, data: List) -> List:
        print("Data: ", data)
        print("Filters: ", filters)
        result = []
        for item in data:
            for filter_data in filters:
                if filter_data[1] == item[filter_data[0]]:
                    result.append(item)

        print("Filter Result: ", result)

        return result
