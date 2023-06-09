from utilities import read_utils
from utilities.read_utils import get_sheet_as_list


test_mouseoverdata = get_sheet_as_list("../test_data/test_data_mouse_over.xlsx", "test_mouseover_product")

test_shopping_cart_data = get_sheet_as_list("../test_data/test_shopping_cart_data.xlsx", "test_shopping_cart")

test_filter_sort_data = read_utils.get_csv_as_list("../test_data/test_filters_sort.csv")